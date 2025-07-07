"""
HopRAG Streamlit App - Knowledge-Intensive AI with Multi-Hop Reasoning
Implementation based on HopRAG paper: https://arxiv.org/abs/2502.12442
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from typing import List, Dict, Any, Optional, Tuple
import json
import os
from pathlib import Path
import networkx as nx
import numpy as np
from dataclasses import dataclass
import logging
from sentence_transformers import SentenceTransformer
import re
from collections import defaultdict, deque
import time

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class HopPath:
    """Represents a multi-hop reasoning path"""
    entities: List[str]
    relations: List[str]
    evidence: List[str]
    confidence: float
    hop_count: int
    reasoning_chain: str

@dataclass
class HopRAGResult:
    """Result from HopRAG query"""
    answer: str
    confidence: float
    hop_paths: List[HopPath]
    supporting_evidence: List[str]
    reasoning_explanation: str
    research_abstract: str
    reasoning_paper: str
    query_metadata: Dict[str, Any]

class KnowledgeGraphLoader:
    """Loads knowledge graph from markdown files"""
    
    def __init__(self, graph_path: str):
        self.graph_path = Path(graph_path)
        self.graph = nx.Graph()
        self.concept_content = {}
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        
    def load_graph(self) -> nx.Graph:
        """Load knowledge graph from markdown files"""
        st.info("Loading knowledge graph from markdown files...")
        
        # Load all markdown files
        markdown_files = list(self.graph_path.glob("*.md"))
        progress_bar = st.progress(0)
        
        for i, file_path in enumerate(markdown_files):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                concept_name = file_path.stem
                self.concept_content[concept_name] = content
                
                # Add node to graph
                self.graph.add_node(concept_name, content=content)
                
                # Extract relationships from content
                self._extract_relationships(concept_name, content)
                
                progress_bar.progress((i + 1) / len(markdown_files))
                
            except Exception as e:
                logger.error(f"Error loading {file_path}: {e}")
        
        st.success(f"Loaded {len(self.graph.nodes)} concepts and {len(self.graph.edges)} relationships")
        return self.graph
    
    def _extract_relationships(self, concept_name: str, content: str):
        """Extract relationships from markdown content"""
        # Look for markdown links to other concepts
        links = re.findall(r'\[\[([^\]]+)\]\]', content)
        
        for link in links:
            if link in self.concept_content:
                self.graph.add_edge(concept_name, link, relation="RELATED_TO")
        
        # Look for explicit relationships in content
        relation_patterns = [
            (r'is a type of (.+)', "IS_A"),
            (r'is related to (.+)', "RELATED_TO"),
            (r'depends on (.+)', "DEPENDS_ON"),
            (r'uses (.+)', "USES"),
            (r'implements (.+)', "IMPLEMENTS"),
        ]
        
        for pattern, relation_type in relation_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            for match in matches:
                # Clean up the match
                target = match.strip().rstrip('.,;:')
                if target in self.concept_content:
                    self.graph.add_edge(concept_name, target, relation=relation_type)

class HopRAGEngine:
    """Core HopRAG reasoning engine"""
    
    def __init__(self, knowledge_graph: nx.Graph, concept_content: Dict[str, str]):
        self.graph = knowledge_graph
        self.concept_content = concept_content
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        self.max_hops = 5  # Increased for deeper exploration
        self.top_k_paths = 15  # More paths for better diversity
        
    def query(self, question: str, max_hops: int = 3, top_k: int = 5, stream_callback=None) -> HopRAGResult:
        """Process query using HopRAG methodology with streaming updates"""
        
        if stream_callback:
            stream_callback("🔍 **Step 1: Entity Recognition and Linking**", "info")
        
        # Step 1: Entity Recognition and Linking
        start_entities = self._extract_entities(question)
        if stream_callback:
            stream_callback(f"Found {len(start_entities)} starting entities: {', '.join(start_entities[:3])}{'...' if len(start_entities) > 3 else ''}", "success")
        
        if stream_callback:
            stream_callback("🕸️ **Step 2: Multi-hop Path Discovery**", "info")
        
        # Step 2: Multi-hop Path Discovery
        hop_paths = self._discover_hop_paths(start_entities, question, max_hops, stream_callback)
        
        if stream_callback:
            stream_callback("📚 **Step 3: Evidence Aggregation**", "info")
        
        # Step 3: Evidence Aggregation
        evidence = self._aggregate_evidence(hop_paths)
        if stream_callback:
            stream_callback(f"Aggregated evidence from {len(evidence)} sources", "success")
        
        if stream_callback:
            stream_callback("💡 **Step 4: Answer Generation**", "info")
        
        # Step 4: Answer Generation
        answer, confidence = self._generate_answer(question, hop_paths, evidence)
        if stream_callback:
            stream_callback(f"Generated answer with {confidence:.1%} confidence", "success")
        
        if stream_callback:
            stream_callback("📄 **Step 5: Research Abstract Generation**", "info")
        
        # Step 5: Generate Research Abstract
        abstract = self._generate_research_abstract(question, hop_paths, evidence)
        if stream_callback:
            stream_callback("Research abstract generated", "success")
            stream_callback(f"**Abstract Preview:** {abstract[:150]}...", "abstract")
        
        if stream_callback:
            stream_callback("📱 **Step 6: LinkedIn Post Generation**", "info")
        
        # Step 6: Generate Reasoning Paper (LinkedIn format) with streaming
        reasoning_paper = self._generate_reasoning_paper_streaming(question, hop_paths, stream_callback)
        if stream_callback:
            stream_callback("LinkedIn post completed!", "success")
        
        # Step 7: Reasoning Explanation
        reasoning = self._generate_reasoning_explanation(question, hop_paths)
        
        return HopRAGResult(
            answer=answer,
            confidence=confidence,
            hop_paths=hop_paths[:top_k],
            supporting_evidence=evidence,
            reasoning_explanation=reasoning,
            research_abstract=abstract,
            reasoning_paper=reasoning_paper,
            query_metadata={
                "start_entities": start_entities,
                "total_paths_explored": len(hop_paths),
                "max_hops_used": max_hops,
                "graph_coverage": len(set().union(*[path.entities for path in hop_paths])) / len(self.graph.nodes)
            }
        )
    
    def _extract_entities(self, question: str) -> List[str]:
        """Extract relevant entities from question"""
        question_embedding = self.embedding_model.encode(question)
        
        # Find most similar concepts
        similarities = []
        for concept, content in self.concept_content.items():
            concept_embedding = self.embedding_model.encode(concept + " " + content[:500])
            similarity = np.dot(question_embedding, concept_embedding) / (
                np.linalg.norm(question_embedding) * np.linalg.norm(concept_embedding)
            )
            similarities.append((concept, similarity))
        
        # Sort by similarity and take top entities
        similarities.sort(key=lambda x: x[1], reverse=True)
        return [concept for concept, _ in similarities[:5]]
    
    def _discover_hop_paths(self, start_entities: List[str], question: str, max_hops: int, stream_callback=None) -> List[HopPath]:
        """Discover multi-hop reasoning paths with enhanced depth and quality"""
        question_embedding = self.embedding_model.encode(question)
        all_paths = []
        
        for i, start_entity in enumerate(start_entities):
            if start_entity not in self.graph.nodes:
                continue
            
            if stream_callback:
                stream_callback(f"🌱 Exploring from entity: **{start_entity}** ({i+1}/{len(start_entities)})", "path")
                
            # Enhanced DFS with path quality tracking
            paths_from_entity = self._deep_path_search(
                start_entity, question_embedding, max_hops, set(), [], stream_callback
            )
            all_paths.extend(paths_from_entity)
            
            if stream_callback:
                stream_callback(f"Found {len(paths_from_entity)} paths from {start_entity}", "path")
        
        if stream_callback:
            stream_callback(f"🔍 **Path Analysis:** Discovered {len(all_paths)} total paths", "info")
        
        # Advanced path filtering and scoring
        quality_paths = self._filter_and_score_paths(all_paths, question_embedding)
        
        if stream_callback:
            stream_callback(f"🎯 **Quality Filter:** {len(quality_paths)} high-quality paths retained", "success")
        
        # Ensure path diversity
        diverse_paths = self._ensure_path_diversity(quality_paths)
        
        if stream_callback:
            stream_callback(f"🌟 **Final Selection:** {len(diverse_paths[:self.top_k_paths])} diverse paths selected", "success")
        
        return diverse_paths[:self.top_k_paths]
    
    def _deep_path_search(self, current_node: str, question_embedding: np.ndarray, 
                         max_hops: int, visited_in_path: set, current_path: List[str], stream_callback=None) -> List[HopPath]:
        """Deep recursive path search with better exploration"""
        paths = []
        
        # Add current node to path
        new_path = current_path + [current_node]
        new_visited = visited_in_path.copy()
        new_visited.add(current_node)
        
        # Generate path at current depth if meaningful (2+ hops)
        if len(new_path) >= 2:
            path_obj = self._create_path_object(new_path, question_embedding)
            if path_obj.confidence > 0.1:  # Quality threshold
                paths.append(path_obj)
                if stream_callback and len(new_path) >= 3:  # Report significant paths
                    path_str = ' → '.join(new_path)
                    stream_callback(f"🔗 **Path Found:** {path_str} (conf: {path_obj.confidence:.2f})", "path")
        
        # Continue exploration if within hop limit
        if len(new_path) < max_hops + 1:
            # Get neighbors sorted by relevance
            neighbors = self._get_sorted_neighbors(current_node, question_embedding)
            
            for neighbor, neighbor_score in neighbors[:8]:  # Top 8 neighbors per node
                if neighbor not in new_visited:
                    # Recursive exploration
                    sub_paths = self._deep_path_search(
                        neighbor, question_embedding, max_hops, new_visited, new_path, stream_callback
                    )
                    paths.extend(sub_paths)
        
        return paths
    
    def _get_sorted_neighbors(self, node: str, question_embedding: np.ndarray) -> List[tuple]:
        """Get neighbors sorted by relevance to question"""
        neighbors = []
        
        for neighbor in self.graph.neighbors(node):
            if neighbor in self.concept_content:
                # Calculate neighbor relevance
                neighbor_text = neighbor + " " + self.concept_content[neighbor][:300]
                neighbor_embedding = self.embedding_model.encode(neighbor_text)
                
                similarity = np.dot(question_embedding, neighbor_embedding) / (
                    np.linalg.norm(question_embedding) * np.linalg.norm(neighbor_embedding)
                )
                
                neighbors.append((neighbor, similarity))
        
        # Sort by relevance
        neighbors.sort(key=lambda x: x[1], reverse=True)
        return neighbors
    
    def _create_path_object(self, path: List[str], question_embedding: np.ndarray) -> HopPath:
        """Create HopPath object with enhanced scoring"""
        # Generate evidence
        evidence = [self.concept_content.get(node, "") for node in path]
        
        # Extract relations
        relations = []
        for i in range(len(path) - 1):
            if self.graph.has_edge(path[i], path[i+1]):
                edge_data = self.graph.get_edge_data(path[i], path[i+1])
                relation = edge_data.get('relation', 'RELATED_TO')
            else:
                relation = 'CONNECTED_TO'
            relations.append(relation)
        
        # Enhanced confidence calculation
        confidence = self._calculate_path_confidence(path, evidence, question_embedding)
        
        # Create reasoning chain
        reasoning_chain = self._create_reasoning_chain(path, relations)
        
        return HopPath(
            entities=path.copy(),
            relations=relations,
            evidence=evidence,
            confidence=confidence,
            hop_count=len(path) - 1,
            reasoning_chain=reasoning_chain
        )
    
    def _calculate_path_confidence(self, path: List[str], evidence: List[str], 
                                  question_embedding: np.ndarray) -> float:
        """Calculate enhanced path confidence score"""
        # Semantic similarity component
        path_text = " ".join(path) + " " + " ".join(evidence)
        path_embedding = self.embedding_model.encode(path_text[:1000])
        
        semantic_sim = np.dot(question_embedding, path_embedding) / (
            np.linalg.norm(question_embedding) * np.linalg.norm(path_embedding)
        )
        
        # Path length bonus (longer paths can be more informative)
        length_bonus = min(len(path) / 5.0, 1.0)  # Bonus up to 5 hops
        
        # Evidence quality bonus
        evidence_quality = sum(1 for e in evidence if len(e.strip()) > 50) / len(evidence)
        
        # Node connectivity bonus (well-connected nodes are often important)
        connectivity_bonus = np.mean([
            min(self.graph.degree(node) / 10.0, 1.0) for node in path 
            if node in self.graph.nodes
        ])
        
        # Combined confidence score
        confidence = (
            semantic_sim * 0.5 +
            length_bonus * 0.2 +
            evidence_quality * 0.2 +
            connectivity_bonus * 0.1
        )
        
        return min(confidence, 1.0)
    
    def _filter_and_score_paths(self, paths: List[HopPath], question_embedding: np.ndarray) -> List[HopPath]:
        """Filter and enhance scoring of paths"""
        quality_paths = []
        
        for path in paths:
            # Quality filters
            if (path.confidence > 0.15 and  # Minimum confidence
                len(path.entities) >= 2 and  # At least 2 entities
                len(path.entities) <= 6 and  # Not too long
                len(set(path.entities)) == len(path.entities)):  # No cycles
                
                quality_paths.append(path)
        
        # Sort by confidence
        quality_paths.sort(key=lambda x: x.confidence, reverse=True)
        
        return quality_paths
    
    def _ensure_path_diversity(self, paths: List[HopPath]) -> List[HopPath]:
        """Ensure diversity in reasoning paths"""
        if not paths:
            return paths
            
        diverse_paths = [paths[0]]  # Always include the best path
        
        for path in paths[1:]:
            # Check if path is sufficiently different from existing ones
            is_diverse = True
            for existing_path in diverse_paths:
                # Calculate entity overlap
                overlap = len(set(path.entities) & set(existing_path.entities))
                overlap_ratio = overlap / max(len(path.entities), len(existing_path.entities))
                
                if overlap_ratio > 0.7:  # Too similar
                    is_diverse = False
                    break
            
            if is_diverse:
                diverse_paths.append(path)
                
            # Stop when we have enough diverse paths
            if len(diverse_paths) >= self.top_k_paths * 2:
                break
        
        return diverse_paths
    
    def _create_reasoning_chain(self, path: List[str], relations: List[str]) -> str:
        """Create human-readable reasoning chain"""
        if len(path) < 2:
            return path[0] if path else ""
        
        chain_parts = []
        for i in range(len(path) - 1):
            chain_parts.append(f"{path[i]} → {relations[i]} → {path[i+1]}")
        
        return " | ".join(chain_parts)
    
    def _aggregate_evidence(self, hop_paths: List[HopPath]) -> List[str]:
        """Aggregate evidence from multiple paths"""
        evidence_map = defaultdict(float)
        
        for path in hop_paths:
            for entity, evidence_text in zip(path.entities, path.evidence):
                # Weight evidence by path confidence
                evidence_map[evidence_text] += path.confidence
        
        # Sort by aggregated confidence
        sorted_evidence = sorted(evidence_map.items(), key=lambda x: x[1], reverse=True)
        return [evidence for evidence, _ in sorted_evidence[:10]]
    
    def _generate_answer(self, question: str, hop_paths: List[HopPath], evidence: List[str]) -> Tuple[str, float]:
        """Generate answer using retrieved evidence"""
        # Simple extractive approach - in practice, use a generative model
        
        # Combine top evidence
        combined_evidence = "\n".join(evidence[:3])
        
        # Extract relevant sentences
        sentences = re.split(r'[.!?]+', combined_evidence)
        question_embedding = self.embedding_model.encode(question)
        
        sentence_scores = []
        for sentence in sentences:
            if len(sentence.strip()) > 20:
                sentence_embedding = self.embedding_model.encode(sentence)
                score = np.dot(question_embedding, sentence_embedding) / (
                    np.linalg.norm(question_embedding) * np.linalg.norm(sentence_embedding)
                )
                sentence_scores.append((sentence.strip(), score))
        
        # Sort and take top sentences
        sentence_scores.sort(key=lambda x: x[1], reverse=True)
        
        answer_sentences = [sent for sent, _ in sentence_scores[:3]]
        answer = " ".join(answer_sentences)
        
        # Calculate confidence based on path quality
        avg_path_confidence = np.mean([path.confidence for path in hop_paths[:3]]) if hop_paths else 0.0
        
        return answer, avg_path_confidence
    
    def _generate_reasoning_explanation(self, question: str, hop_paths: List[HopPath]) -> str:
        """Generate explanation of reasoning process"""
        explanation_parts = [
            f"To answer '{question}', I explored {len(hop_paths)} reasoning paths:",
            ""
        ]
        
        for i, path in enumerate(hop_paths[:3]):
            explanation_parts.append(f"Path {i+1} ({path.hop_count} hops, confidence: {path.confidence:.3f}):")
            explanation_parts.append(f"  {path.reasoning_chain}")
            explanation_parts.append("")
        
        return "\n".join(explanation_parts)
    
    def _generate_research_abstract(self, question: str, hop_paths: List[HopPath], evidence: List[str]) -> str:
        """Generate research paper abstract from discovered paths and evidence"""
        
        # Extract key concepts and themes
        all_entities = set()
        all_relations = set()
        for path in hop_paths[:5]:
            all_entities.update(path.entities)
            all_relations.update(path.relations)
        
        # Calculate research metrics
        avg_confidence = sum(p.confidence for p in hop_paths) / len(hop_paths) if hop_paths else 0
        max_depth = max(p.hop_count for p in hop_paths) if hop_paths else 0
        
        abstract_parts = [
            f"**Abstract**",
            "",
            f"**Background:** This study investigates the research question: '{question}' through systematic multi-hop reasoning analysis across a knowledge graph containing interconnected concepts.",
            "",
            f"**Methods:** We employed a graph-based reasoning approach to discover {len(hop_paths)} distinct reasoning paths, exploring up to {max_depth} conceptual hops. Our methodology combines semantic similarity analysis with path quality assessment, achieving an average confidence score of {avg_confidence:.1%}.",
            "",
            f"**Key Findings:** The analysis identified {len(all_entities)} primary concepts connected through {len(all_relations)} relationship types. Major conceptual themes include: {', '.join(sorted(list(all_entities))[:8])}. Evidence synthesis reveals complex interdependencies between ethical considerations, technical implementations, and practical applications.",
            "",
            f"**Conclusions:** Multi-hop reasoning analysis demonstrates that {question.lower()} involves intricate relationships across {len(all_entities)} conceptual domains. The findings suggest that effective understanding requires consideration of both direct and indirect conceptual connections, with implications for practitioners and researchers in the field.",
            "",
            f"**Keywords:** {', '.join(sorted(list(all_entities))[:10])}",
            "",
            f"**Methodology Validation:** Confidence range: {min(p.confidence for p in hop_paths):.1%} - {max(p.confidence for p in hop_paths):.1%} | Evidence sources: {len(evidence)} | Graph coverage: {len(all_entities)} concepts"
        ]
        
        return "\n".join(abstract_parts)
    
    def _generate_reasoning_paper(self, question: str, hop_paths: List[HopPath]) -> str:
        """Generate story-driven LinkedIn post using new narrative patterns"""
        
        # Extract rich insights from content
        content_insights = self._extract_content_insights(hop_paths[:3], question)
        
        # Use the new story-driven generator
        linkedin_generator = LinkedInPostGenerator()
        return linkedin_generator.generate_post(question, hop_paths, content_insights)
    
    def _generate_reasoning_paper_streaming(self, question: str, hop_paths: List[HopPath], stream_callback=None) -> str:
        """Generate story-driven LinkedIn post with streaming updates"""
        
        # Extract insights first
        content_insights = self._extract_content_insights(hop_paths[:3], question)
        
        if stream_callback:
            stream_callback("🎯 **Generating Story-Driven LinkedIn Post:**", "linkedin_header")
            stream_callback("🎭 **Selecting narrative pattern...**", "linkedin_progress")
        
        # Generate the full post using new system
        linkedin_generator = LinkedInPostGenerator()
        final_post = linkedin_generator.generate_post(question, hop_paths, content_insights)
        
        # Show incremental building by revealing sections
        import time
        post_lines = final_post.split('\n')
        
        # Show hook first
        hook_lines = []
        for line in post_lines:
            hook_lines.append(line)
            if line.strip() == "" and len(hook_lines) > 2:  # Found first empty line after content
                break
                
        if stream_callback:
            stream_callback("🎪 **Hook generated...**", "linkedin_progress")
            stream_callback("\n".join(hook_lines), "linkedin_update")
            time.sleep(0.5)
        
        # Show progressive reveal
        midpoint = len(post_lines) // 2
        if stream_callback:
            stream_callback("📝 **Building narrative...**", "linkedin_progress")
            stream_callback("\n".join(post_lines[:midpoint]), "linkedin_update")
            time.sleep(0.5)
        
        if stream_callback:
            stream_callback("🎯 **Adding conclusion...**", "linkedin_progress")
            stream_callback(final_post, "linkedin_update")
            time.sleep(0.3)
        
        # Final reveal
        if stream_callback:
            stream_callback(final_post, "linkedin_final")
        
        return final_post
    
    def _extract_content_insights(self, hop_paths: List[HopPath], question: str) -> List[Dict[str, str]]:
        """Extract meaningful insights from actual node content"""
        insights = []
        question_embedding = self.embedding_model.encode(question)
        
        for path in hop_paths:
            # Analyze the relationship and content for this path
            path_insight = self._analyze_path_content(path, question_embedding)
            if path_insight:
                insights.append(path_insight)
        
        # Remove duplicates and keep most relevant
        unique_insights = []
        seen_concepts = set()
        
        for insight in insights:
            concept_key = insight['concept'].lower()
            if concept_key not in seen_concepts:
                unique_insights.append(insight)
                seen_concepts.add(concept_key)
                
        return unique_insights[:3]  # Top 3 unique insights
    
    def _analyze_path_content(self, path: HopPath, question_embedding: np.ndarray) -> Dict[str, str]:
        """Analyze a single path to extract meaningful content insights with story elements"""
        
        # Focus on the most important entities in the path (usually the first 2-3)
        key_entities = path.entities[:3]
        
        for i, entity in enumerate(key_entities):
            content = self.concept_content.get(entity, "")
            if not content.strip():
                continue
                
            # Extract key information from content
            insight = self._extract_key_insight_from_content(entity, content, question_embedding)
            if insight:
                # Create a meaningful title based on the path relationship
                if i < len(path.relations):
                    relation = path.relations[i]
                    next_entity = key_entities[i+1] if i+1 < len(key_entities) else None
                    title = self._create_insight_title(entity, relation, next_entity)
                else:
                    title = f"Understanding {entity}"
                
                # Extract story elements from content
                story_elements = self._extract_story_elements_from_content(entity, content)
                
                result = {
                    'concept': entity,
                    'title': title,
                    'explanation': insight['explanation'],
                    'example': insight.get('example', ''),
                    'content': content
                }
                
                # Add story elements
                result.update(story_elements)
                
                return result
        
        return None
    
    def _extract_story_elements_from_content(self, entity: str, content: str) -> Dict[str, str]:
        """Extract specific story elements from content for narrative building"""
        elements = {}
        
        import re
        
        # Look for numbers and statistics for data-driven stories
        numbers = re.findall(r'(\d+(?:\.\d+)?%)', content)
        if numbers:
            elements['percentage'] = numbers[0]
            
        # Look for examples that can become case studies
        if 'example' in content.lower():
            examples = re.findall(r'[Ee]xamples? include ([^.]+)', content)
            if examples:
                elements['case_study'] = examples[0]
                
        # Look for problems/failures mentioned
        problem_keywords = ['fail', 'error', 'mistake', 'wrong', 'issue', 'problem', 'challenge']
        for keyword in problem_keywords:
            if keyword in content.lower():
                elements['has_failure_element'] = True
                break
                
        # Look for controversial or contrarian statements
        contrarian_keywords = ['however', 'but', 'contrary', 'opposite', 'although', 'despite']
        for keyword in contrarian_keywords:
            if keyword in content.lower():
                elements['has_contrarian_element'] = True
                break
                
        # Extract specific domain insights for different concepts
        if 'bias' in entity.lower():
            elements['domain_insight'] = 'AI bias affects real hiring decisions'
            elements['secret'] = 'Most bias comes from training data, not algorithms'
            elements['lesson'] = 'Test on diverse groups before deploying'
            elements['counterintuitive_point'] = 'Removing bias doesn\'t guarantee fairness'
            
        elif 'ethics' in entity.lower():
            elements['domain_insight'] = 'Ethical AI is often ignored until it\'s too late'
            elements['secret'] = 'Ethics reviews slow down projects, but prevent disasters'
            elements['lesson'] = 'Build ethics into the process from day one'
            
        elif 'quality' in entity.lower():
            elements['domain_insight'] = 'Data quality matters more than algorithm complexity'
            elements['secret'] = 'Garbage in, garbage out - still true in 2024'
            elements['lesson'] = 'Spend 80% of time on data, 20% on models'
            elements['counterintuitive_point'] = 'Less data, better curated beats more data every time'
            
        elif 'privacy' in entity.lower():
            elements['domain_insight'] = 'Privacy-first design actually improves model performance'
            elements['secret'] = 'Most privacy breaches happen in data storage, not algorithms'
            elements['lesson'] = 'Design for privacy from the start, not as an afterthought'
            
        return elements
    
    def _extract_key_insight_from_content(self, entity: str, content: str, question_embedding: np.ndarray) -> Dict[str, str]:
        """Extract the most relevant insight from content based on the question"""
        
        # Split content into sentences and find most relevant ones
        sentences = [s.strip() for s in content.split('.') if len(s.strip()) > 20]
        if not sentences:
            return None
        
        # Score sentences by relevance to question
        sentence_scores = []
        for sentence in sentences:
            if len(sentence) > 10:
                sentence_embedding = self.embedding_model.encode(sentence)
                similarity = np.dot(question_embedding, sentence_embedding) / (
                    np.linalg.norm(question_embedding) * np.linalg.norm(sentence_embedding)
                )
                sentence_scores.append((sentence, similarity))
        
        # Sort by relevance
        sentence_scores.sort(key=lambda x: x[1], reverse=True)
        
        if not sentence_scores:
            return None
        
        # Get the most relevant sentence as explanation
        best_sentence = sentence_scores[0][0]
        
        # Look for examples or practical applications in remaining sentences
        example = ""
        for sentence, _ in sentence_scores[1:3]:
            if any(keyword in sentence.lower() for keyword in ['example', 'such as', 'like', 'including', 'for instance']):
                example = sentence
                break
        
        # Create more engaging explanation
        explanation = self._create_engaging_explanation(best_sentence, entity)
        
        return {
            'explanation': explanation,
            'example': self._make_content_linkedin_friendly(example) if example else ""
        }
    
    def _create_insight_title(self, entity: str, relation: str, next_entity: str = None) -> str:
        """Create meaningful insight titles based on relationships"""
        
        relation_titles = {
            'ADDRESSES': f"How {entity} tackles {next_entity}" if next_entity else f"Addressing {entity}",
            'PROMOTES': f"Why {entity} drives {next_entity}" if next_entity else f"Promoting {entity}",
            'ENCOMPASSES': f"How {entity} includes {next_entity}" if next_entity else f"Understanding {entity}",
            'CONFLICTS_WITH': f"Why {entity} challenges {next_entity}" if next_entity else f"Challenges with {entity}",
            'DEPENDS_ON': f"Why {entity} needs {next_entity}" if next_entity else f"Dependencies of {entity}",
            'REQUIRES': f"What {entity} demands" if next_entity else f"Requirements for {entity}",
            'ENFORCED_BY': f"How {next_entity} enforces {entity}" if next_entity else f"Enforcement of {entity}",
            'ENABLES': f"How {entity} empowers {next_entity}" if next_entity else f"Enabling {entity}",
            'IMPACTS': f"How {entity} affects {next_entity}" if next_entity else f"Impact of {entity}"
        }
        
        return relation_titles.get(relation, f"Understanding {entity}")
    
    def _make_content_linkedin_friendly(self, text: str) -> str:
        """Make content more LinkedIn-friendly while preserving meaning"""
        if not text:
            return ""
            
        # Clean up the text
        text = text.strip()
        if text.endswith('.'):
            text = text[:-1]
        
        # Make it more conversational and engaging
        replacements = {
            'artificial intelligence': 'AI',
            'machine learning': 'ML',
            'deep learning': 'DL',
            'natural language processing': 'NLP',
            'it is important': 'it\'s crucial',
            'it is essential': 'it\'s vital',
            'organizations': 'companies',
            'individuals': 'people',
            'implementation': 'rollout',
            'utilization': 'use',
            'optimization': 'improvement',
            'must ensure': 'need to make sure',
            'should implement': 'should definitely use',
            'requires consideration': 'needs careful thought',
            'systematic prejudices': 'built-in biases',
            'algorithmic decision-making': 'AI decisions',
            'encompasses': 'covers',
            'encompasses moral principles': 'is all about doing the right thing'
        }
        
        for old, new in replacements.items():
            text = text.replace(old, new)
        
        return text
    
    def _create_engaging_explanation(self, sentence: str, entity: str) -> str:
        """Transform a sentence into a more engaging LinkedIn explanation"""
        
        # Make it more conversational and story-driven
        explanation = self._make_content_linkedin_friendly(sentence)
        
        # Add engaging prefixes based on content type
        if 'bias' in entity.lower():
            prefixes = [
                "Here's the reality:",
                "This is where it gets tricky:",
                "The hard truth?",
                "What most people miss:"
            ]
        elif 'ethics' in entity.lower():
            prefixes = [
                "The bottom line:",
                "Here's what matters:",
                "The key insight:",
                "This is crucial:"
            ]
        elif 'quality' in entity.lower():
            prefixes = [
                "Here's the thing:",
                "The data shows:",
                "What I've learned:",
                "The reality check:"
            ]
        else:
            prefixes = [
                "Here's what's important:",
                "The key insight:",
                "What you need to know:",
                "The bottom line:"
            ]
        
        import random
        prefix = random.choice(prefixes)
        
        return f"{prefix} {explanation}"
    
    def _generate_content_aware_takeaways(self, content_insights: List[Dict], hop_paths: List[HopPath]) -> List[str]:
        """Generate takeaways based on actual content analysis"""
        takeaways = []
        
        for insight in content_insights:
            concept = insight['concept']
            content = insight.get('content', '')
            
            # Extract actionable advice from content
            actionable = self._extract_actionable_advice(concept, content)
            if actionable:
                takeaways.append(actionable)
        
        # Add generic advice if we don't have enough specific ones
        if len(takeaways) < 2:
            takeaways.extend([
                "Question your data before trusting your results",
                "Start small, iterate fast, scale smart"
            ])
        
        return takeaways[:3]
    
    def _extract_actionable_advice(self, concept: str, content: str) -> str:
        """Extract actionable advice from content"""
        
        # Look for actionable patterns in content
        actionable_patterns = [
            (r'should (.+?)[\.\,]', 'Start {}'),
            (r'must (.+?)[\.\,]', 'Always {}'),
            (r'important to (.+?)[\.\,]', 'Focus on {}'),
            (r'ensure (.+?)[\.\,]', 'Make sure you {}'),
            (r'avoid (.+?)[\.\,]', 'Never {}'),
            (r'consider (.+?)[\.\,]', 'Think about {}'),
            (r'implement (.+?)[\.\,]', 'Try {}'),
            (r'requires (.+?)[\.\,]', 'Don\'t forget to {}')
        ]
        
        import re
        for pattern, template in actionable_patterns:
            match = re.search(pattern, content.lower())
            if match:
                advice = match.group(1).strip()
                clean_advice = self._make_content_linkedin_friendly(advice)
                return template.format(clean_advice)
        
        # Enhanced concept-specific advice with more personality
        concept_advice = {
            'bias': 'Test your models on diverse datasets - it\'s a game changer',
            'ethics': 'Build ethics reviews into your workflow from day one',
            'privacy': 'Think privacy-first, not privacy-later',
            'quality': 'Spend 80% of your time on data quality - trust me on this',
            'fairness': 'Audit your models regularly - fairness isn\'t a one-time thing',
            'transparency': 'Make your models explainable to everyone, not just data scientists',
            'governance': 'Document everything - future you will thank you',
            'ai': 'Focus on solving real problems, not just using cool tech',
            'data': 'Question your data before trusting your results'
        }
        
        for key, advice in concept_advice.items():
            if key.lower() in concept.lower():
                return advice
        
        return None
    
    def _generate_dynamic_hashtags(self, content_insights: List[Dict]) -> str:
        """Generate hashtags based on actual content"""
        
        # Extract key terms from insights
        all_text = " ".join([insight.get('content', '') for insight in content_insights])
        
        # Common data science hashtags
        base_tags = ["#DataScience", "#AI", "#MachineLearning"]
        
        # Content-specific hashtags
        content_tags = []
        hashtag_mapping = {
            'ethics': '#AIEthics',
            'bias': '#ResponsibleAI',
            'privacy': '#DataPrivacy', 
            'governance': '#DataGovernance',
            'fairness': '#AlgorithmicFairness',
            'transparency': '#ExplainableAI',
            'regulation': '#AIRegulation',
            'compliance': '#DataCompliance',
            'security': '#DataSecurity',
            'quality': '#DataQuality'
        }
        
        for keyword, hashtag in hashtag_mapping.items():
            if keyword in all_text.lower():
                content_tags.append(hashtag)
        
        # Combine and limit to 8 hashtags
        all_tags = base_tags + content_tags[:5]
        return " ".join(all_tags)
    
    def _create_linkedin_hook(self, question: str, key_concepts: List[str]) -> str:
        """Create engaging LinkedIn hook based on question and concepts"""
        
        import random
        
        # More engaging hook patterns with storytelling
        storytelling_hooks = [
            f"Last week, a colleague asked me: '{question}'\n\n🤯 My answer surprised them.",
            f"I've been asked '{question}' dozens of times.\n\n📈 Here's what the data actually shows:",
            f"'{question}'\n\n🔥 This question comes up in every data team meeting I attend.",
            f"Hot take: Most people get '{question.lower()}' completely wrong.\n\n🎯 Let me explain why:",
            f"Three years ago, I thought I knew everything about {key_concepts[0].lower() if key_concepts else 'data'}.\n\n😅 I was so wrong."
        ]
        
        # Problem-focused hooks
        problem_hooks = [
            f"95% of data teams struggle with this:\n\n'{question}'\n\n💡 But there's a better way:",
            f"You're probably making this mistake:\n\n{question.lower().replace('how can', 'not knowing how to').replace('what are', 'ignoring').replace('why do', 'not understanding why')}\n\n🚀 Here's how to fix it:",
            f"The biggest misconception about {key_concepts[0].lower() if key_concepts else 'data'}?\n\n❌ {question}\n\n✅ Let me show you the reality:"
        ]
        
        # Choose hook style based on question type and add variety
        if "how" in question.lower():
            hooks = storytelling_hooks + problem_hooks
        elif "what" in question.lower():
            hooks = problem_hooks + storytelling_hooks
        elif "why" in question.lower():
            hooks = storytelling_hooks
        else:
            hooks = storytelling_hooks + problem_hooks
        
        return random.choice(hooks)
    
    def _make_linkedin_friendly(self, text: str) -> str:
        """Make text more LinkedIn-friendly and engaging"""
        # Remove overly technical jargon and make more accessible
        text = text.replace("artificial intelligence", "AI")
        text = text.replace("machine learning", "ML")
        text = text.replace("algorithms", "models")
        
        # Add conversational tone
        if text.endswith('.'):
            text = text[:-1]
        
        # Make it more engaging
        if "important" in text.lower():
            text = text.replace("important", "crucial")
        if "requires" in text.lower():
            text = text.replace("requires", "needs")
        
        return text
    
    def _generate_actionable_takeaways(self, hop_paths: List[HopPath]) -> List[str]:
        """Generate actionable takeaways for LinkedIn audience"""
        
        takeaways = []
        
        # Extract key themes and create actionable advice
        all_entities = []
        for path in hop_paths:
            all_entities.extend(path.entities)
        
        # Common data concepts and their actionable advice
        concept_advice = {
            "bias": "Always test your models on diverse datasets before deployment",
            "ethics": "Build ethical review into your data science workflow",
            "privacy": "Implement privacy-by-design in your data projects",
            "quality": "Spend 80% of your time on data cleaning - it's worth it",
            "fairness": "Regularly audit your models for fairness across different groups",
            "performance": "Track model performance over time, not just at deployment",
            "governance": "Document your data sources and transformations",
            "machine learning": "Start with simple models before going complex",
            "ai": "Focus on solving real problems, not just using cool tech",
            "data": "Always question your data before trusting your results"
        }
        
        # Generate relevant takeaways
        for entity in all_entities[:5]:  # Top 5 entities
            entity_lower = entity.lower()
            for concept, advice in concept_advice.items():
                if concept in entity_lower:
                    takeaways.append(advice)
                    break
        
        # Add generic valuable advice if no specific matches
        if not takeaways:
            takeaways = [
                "Always validate your assumptions with data",
                "Document your process for future reference",
                "Question your data before trusting your results"
            ]
        
        return takeaways[:3]  # Keep it concise

class NarrativePattern:
    """Base class for LinkedIn post narrative patterns"""
    
    def __init__(self, pattern_name: str):
        self.pattern_name = pattern_name
        
    def generate_hook(self, question: str, key_insights: List[Dict], story_elements: Dict) -> str:
        """Generate engaging hook for this narrative pattern"""
        raise NotImplementedError
        
    def generate_body(self, insights: List[Dict], story_elements: Dict) -> List[str]:
        """Generate main content body"""
        raise NotImplementedError
        
    def generate_conclusion(self, insights: List[Dict], story_elements: Dict) -> List[str]:
        """Generate conclusion and call to action"""
        raise NotImplementedError

class ContrariianPattern(NarrativePattern):
    """Pattern for contrarian/myth-busting posts"""
    
    def __init__(self):
        super().__init__("contrarian")
        
    def generate_hook(self, question: str, key_insights: List[Dict], story_elements: Dict) -> str:
        import random
        
        # Extract myth to bust
        default_insight = "Most AI failures aren't technical"
        default_view = "Your models aren't biased because of bad data"
        default_finding = "The best models use less data, not more."
        
        myth_hooks = [
            f"Everyone believes {story_elements.get('common_belief', 'data quality is just cleaning')}.\n\nThey're wrong.",
            f"Hot take: {story_elements.get('controversial_insight', default_insight)}",
            f"Unpopular opinion: {story_elements.get('contrarian_view', default_view)}",
            f"I see this mistake everywhere:\n\n\"{story_elements.get('common_mistake', 'We need more data')}\"\n\nHere's why that's backwards:",
            f"After analyzing {story_elements.get('data_point', '500+')} projects, I discovered something shocking:\n\n{story_elements.get('surprising_finding', default_finding)}"
        ]
        
        return random.choice(myth_hooks)
        
    def generate_body(self, insights: List[Dict], story_elements: Dict) -> List[str]:
        body_parts = []
        
        # Build the argument
        if story_elements.get('evidence'):
            body_parts.append(f"Here's the data:")
            body_parts.append("")
            for evidence in story_elements['evidence'][:2]:
                body_parts.append(f"📊 {evidence}")
            body_parts.append("")
        
        # Reveal the truth
        if insights:
            body_parts.append("The reality?")
            body_parts.append("")
            for i, insight in enumerate(insights[:2]):
                if insight.get('counterintuitive_point'):
                    body_parts.append(f"{i+1}. {insight['counterintuitive_point']}")
                elif insight.get('explanation'):
                    body_parts.append(f"{i+1}. {insight['explanation']}")
            body_parts.append("")
            
        # Add specific example
        if story_elements.get('specific_example'):
            body_parts.append(f"Example: {story_elements['specific_example']}")
            body_parts.append("")
            
        return body_parts
        
    def generate_conclusion(self, insights: List[Dict], story_elements: Dict) -> List[str]:
        conclusion = []
        
        if story_elements.get('lesson_learned'):
            conclusion.extend([
                "The lesson?",
                "",
                story_elements['lesson_learned'],
                ""
            ])
            
        # Provocative question
        questions = [
            "What's the biggest misconception in your field?",
            "Have you seen this mistake in your organization?",
            "What other \"best practices\" need questioning?",
            "Where else are we getting it backwards?"
        ]
        
        import random
        conclusion.append(random.choice(questions))
        
        return conclusion

class FailureStoryPattern(NarrativePattern):
    """Pattern for personal failure/learning stories"""
    
    def __init__(self):
        super().__init__("failure_story")
        
    def generate_hook(self, question: str, key_insights: List[Dict], story_elements: Dict) -> str:
        import random
        
        # Fix f-string backslash issue
        default_belief = "more data always meant better models"
        default_failure = "discriminated against women"
        
        failure_hooks = [
            f"I made a ${story_elements.get('cost', '50k')} mistake.\n\nBecause I didn't understand {story_elements.get('key_concept', 'bias in AI')}.",
            f"My model failed spectacularly in production.\n\nHere's what went wrong:",
            f"3 years ago, I thought {story_elements.get('wrong_belief', default_belief)}.\n\nI was so wrong it cost us {story_elements.get('consequence', 'months of work')}.",
            f"I used to ignore {story_elements.get('ignored_factor', 'data quality')}.\n\nBig mistake.",
            f"This is embarrassing to admit:\n\nI once deployed a model that {story_elements.get('failure_mode', default_failure)}.\n\nHere's how it happened:"
        ]
        
        return random.choice(failure_hooks)
        
    def generate_body(self, insights: List[Dict], story_elements: Dict) -> List[str]:
        body_parts = []
        
        # Tell the story
        if story_elements.get('what_happened'):
            body_parts.extend([
                "What happened:",
                "",
                story_elements['what_happened'],
                ""
            ])
            
        # The insight/lesson
        body_parts.append("What I learned:")
        body_parts.append("")
        
        for i, insight in enumerate(insights[:2]):
            if insight.get('lesson'):
                body_parts.append(f"• {insight['lesson']}")
            elif insight.get('explanation'):
                body_parts.append(f"• {insight['explanation']}")
                
        body_parts.append("")
        
        # How to avoid it
        if story_elements.get('prevention'):
            body_parts.extend([
                "How to avoid this:",
                "",
                story_elements['prevention'],
                ""
            ])
            
        return body_parts
        
    def generate_conclusion(self, insights: List[Dict], story_elements: Dict) -> List[str]:
        conclusion = []
        
        if story_elements.get('broader_lesson'):
            conclusion.extend([
                f"The bigger lesson: {story_elements['broader_lesson']}",
                ""
            ])
            
        conclusion.append("What's your biggest data science mistake? (I bet I can top it 😅)")
        
        return conclusion

class InsiderSecretsPattern(NarrativePattern):
    """Pattern for industry insider secrets"""
    
    def __init__(self):
        super().__init__("insider_secrets")
        
    def generate_hook(self, question: str, key_insights: List[Dict], story_elements: Dict) -> str:
        import random
        
        # Fix f-string backslash issues
        default_reality = "You'll spend 80% of your time on data, not algorithms"
        default_view = "The best data scientists aren't the ones with the fanciest models"
        
        secret_hooks = [
            f"After {story_elements.get('years_experience', '5')} years in data science, here's what nobody tells you:",
            f"Industry secret:\n\n{story_elements.get('hidden_truth', 'Most ML models in production are embarrassingly simple')}",
            f"What they don't teach you in data science courses:\n\n{story_elements.get('reality_check', default_reality)}",
            f"Behind the scenes at {story_elements.get('company_type', 'tech companies')}:\n\n{story_elements.get('insider_view', default_view)}",
            f"Recruiter told me this would never work in an interview.\n\nNow it's how we solve {story_elements.get('solved_problem', 'bias detection')} at scale."
        ]
        
        return random.choice(secret_hooks)
        
    def generate_body(self, insights: List[Dict], story_elements: Dict) -> List[str]:
        body_parts = []
        
        # Reveal the secrets
        body_parts.append("Here's what's really happening:")
        body_parts.append("")
        
        for i, insight in enumerate(insights[:3]):
            if insight.get('secret'):
                body_parts.append(f"{i+1}. {insight['secret']}")
            elif insight.get('explanation'):
                body_parts.append(f"{i+1}. {insight['explanation']}")
                
        body_parts.append("")
        
        # Add context
        if story_elements.get('why_hidden'):
            body_parts.extend([
                f"Why don't people talk about this? {story_elements['why_hidden']}",
                ""
            ])
            
        return body_parts
        
    def generate_conclusion(self, insights: List[Dict], story_elements: Dict) -> List[str]:
        conclusion = [
            "What other industry secrets should we be sharing?",
            "",
            "(Follow for more behind-the-scenes insights)"
        ]
        
        return conclusion

class RevealingQuestionPattern(NarrativePattern):
    """Pattern for provocative questions that reveal insights"""
    
    def __init__(self):
        super().__init__("revealing_question")
        
    def generate_hook(self, question: str, key_insights: List[Dict], story_elements: Dict) -> str:
        import random
        
        question_hooks = [
            f"Why do {story_elements.get('percentage', '90%')} of {story_elements.get('subject', 'AI projects')} fail?\n\nIt's not what you think.",
            f"Quick question: {story_elements.get('thought_provoking_q', 'How many of your models actually create business value?')}\n\nBe honest.",
            f"Serious question:\n\nWhen was the last time you questioned {story_elements.get('questioned_thing', 'your training data')}?",
            f"Pop quiz: What's the #1 reason {story_elements.get('failure_subject', 'machine learning projects')} fail?\n\n(Hint: It's not the algorithm)",
            f"Challenge: Name one time {story_elements.get('challenge_scenario', 'more data made your model worse')}.\n\nI'll wait."
        ]
        
        return random.choice(question_hooks)
        
    def generate_body(self, insights: List[Dict], story_elements: Dict) -> List[str]:
        body_parts = []
        
        # Answer the question
        body_parts.append("Here's the real answer:")
        body_parts.append("")
        
        if story_elements.get('surprising_answer'):
            body_parts.append(story_elements['surprising_answer'])
            body_parts.append("")
            
        # Break it down
        body_parts.append("Let me break this down:")
        body_parts.append("")
        
        for i, insight in enumerate(insights[:2]):
            if insight.get('breakdown_point'):
                body_parts.append(f"→ {insight['breakdown_point']}")
            elif insight.get('explanation'):
                body_parts.append(f"→ {insight['explanation']}")
                
        body_parts.append("")
        
        return body_parts
        
    def generate_conclusion(self, insights: List[Dict], story_elements: Dict) -> List[str]:
        import random
        
        follow_up_questions = [
            "What question should I ask next?",
            "What's your answer to this?",
            "Am I missing something here?",
            "What would you add to this?"
        ]
        
        return [random.choice(follow_up_questions)]

class LinkedInPostGenerator:
    """New story-driven LinkedIn post generator"""
    
    def __init__(self):
        self.patterns = [
            ContrariianPattern(),
            FailureStoryPattern(), 
            InsiderSecretsPattern(),
            RevealingQuestionPattern()
        ]
        
    def generate_post(self, question: str, hop_paths: List[HopPath], content_insights: List[Dict]) -> str:
        """Generate a story-driven LinkedIn post"""
        
        # Extract story elements from content
        story_elements = self._extract_story_elements(content_insights, hop_paths)
        
        # Choose narrative pattern based on content
        pattern = self._select_pattern(story_elements, content_insights)
        
        # Generate post sections
        hook = pattern.generate_hook(question, content_insights, story_elements)
        body = pattern.generate_body(content_insights, story_elements)
        conclusion = pattern.generate_conclusion(content_insights, story_elements)
        
        # Assemble post
        post_parts = [hook, ""]
        post_parts.extend(body)
        post_parts.extend(conclusion)
        
        # Add minimal hashtags
        hashtags = self._generate_minimal_hashtags(content_insights)
        post_parts.extend(["", hashtags])
        
        return "\n".join(post_parts)
        
    def _extract_story_elements(self, content_insights: List[Dict], hop_paths: List[HopPath]) -> Dict:
        """Extract story elements from content for narrative building"""
        elements = {}
        
        # Look for conflicting concepts for contrarian stories
        if len(content_insights) >= 2:
            concept1 = content_insights[0].get('concept', '')
            concept2 = content_insights[1].get('concept', '')
            
            if 'bias' in concept1.lower() and 'fairness' in concept2.lower():
                elements['common_belief'] = 'fairness just means removing bias'
                elements['controversial_insight'] = 'Fairness and bias removal are actually different problems'
                elements['counterintuitive_point'] = 'You can remove bias and still be unfair'
                
            elif 'ethics' in concept1.lower() and 'performance' in concept2.lower():
                elements['common_belief'] = 'ethical AI means slower AI'
                elements['controversial_insight'] = 'The most ethical models often perform better'
                
            elif 'quality' in concept1.lower():
                elements['common_mistake'] = 'We need more data'
                elements['surprising_finding'] = 'Better curation beats bigger datasets every time'
                
        # Extract specific numbers and examples
        for insight in content_insights:
            content = insight.get('content', '')
            
            # Look for percentages, numbers
            import re
            numbers = re.findall(r'(\d+(?:\.\d+)?%?)', content)
            if numbers:
                elements['data_point'] = numbers[0]
                
            # Look for specific examples
            if 'example' in content.lower():
                examples = re.findall(r'[Ee]xamples? include ([^.]+)', content)
                if examples:
                    elements['specific_example'] = examples[0]
                    
        # Generate failure scenarios based on concepts
        key_concepts = [insight.get('concept', '') for insight in content_insights]
        if 'bias' in str(key_concepts).lower():
            elements['failure_mode'] = 'showed bias against certain groups'
            elements['cost'] = '100k'
            elements['what_happened'] = 'We launched without proper bias testing. The model systematically rejected qualified candidates from underrepresented groups.'
            elements['prevention'] = 'Always test on diverse datasets and audit for fairness before deployment'
            
        elif 'quality' in str(key_concepts).lower():
            elements['failure_mode'] = 'failed due to data quality issues'
            elements['cost'] = '6 months'
            elements['what_happened'] = 'Our model looked great in testing but failed in production because training data was cleaner than real-world data.'
            
        # Industry secrets based on concepts
        if 'ethics' in str(key_concepts).lower():
            elements['hidden_truth'] = 'Most "ethical AI" initiatives are just PR'
            elements['years_experience'] = '7'
            elements['why_hidden'] = 'Companies don\'t want to admit how little they actually invest in real ethics'
            
        return elements
        
    def _select_pattern(self, story_elements: Dict, content_insights: List[Dict]) -> NarrativePattern:
        """Select the best narrative pattern for the content"""
        import random
        
        # Bias toward contrarian for controversial topics
        if story_elements.get('controversial_insight'):
            return self.patterns[0]  # ContrariianPattern
            
        # Use failure stories for bias/ethics content
        concepts = ' '.join([insight.get('concept', '') for insight in content_insights]).lower()
        if 'bias' in concepts or 'ethics' in concepts:
            if random.random() < 0.6:  # 60% chance
                return self.patterns[1]  # FailureStoryPattern
                
        # Default to random selection
        return random.choice(self.patterns)
        
    def _generate_minimal_hashtags(self, content_insights: List[Dict]) -> str:
        """Generate minimal, relevant hashtags"""
        concepts = [insight.get('concept', '') for insight in content_insights]
        
        # Keep it simple and relevant
        hashtags = ['#DataScience']
        
        concept_map = {
            'bias': '#AIBias', 
            'ethics': '#AIEthics',
            'fairness': '#ResponsibleAI',
            'quality': '#DataQuality',
            'privacy': '#DataPrivacy'
        }
        
        for concept in concepts:
            for key, tag in concept_map.items():
                if key in concept.lower() and tag not in hashtags:
                    hashtags.append(tag)
                    break
                    
        return ' '.join(hashtags[:3])  # Max 3 hashtags

class HopRAGStreamlitApp:
    """Streamlit application for HopRAG"""
    
    def __init__(self):
        self.kg_loader = None
        self.hoprag_engine = None
        self.graph = None
        
    def run(self):
        """Run the Streamlit application"""
        st.set_page_config(
            page_title="HopRAG - Knowledge-Intensive AI",
            page_icon="🔗",
            layout="wide"
        )
        
        st.title("🔗 HopRAG - Knowledge-Intensive AI")
        st.markdown("Multi-hop reasoning over your knowledge graph for enhanced AI capabilities")
        
        # Initialize system
        if not self.hoprag_engine:
            self._initialize_system()
        
        # Main interface
        self._render_interface()
    
    def _initialize_system(self):
        """Initialize the HopRAG system"""
        st.header("🚀 System Initialization")
        
        with st.spinner("Loading knowledge graph..."):
            try:
                # Load knowledge graph
                self.kg_loader = KnowledgeGraphLoader("/Users/arthursarazin/Documents/knowledge_glossary/graph")
                self.graph = self.kg_loader.load_graph()
                
                # Initialize HopRAG engine
                self.hoprag_engine = HopRAGEngine(self.graph, self.kg_loader.concept_content)
                
                st.success("✅ HopRAG system initialized successfully!")
                
            except Exception as e:
                st.error(f"❌ Error initializing system: {e}")
                st.stop()
    
    def _render_interface(self):
        """Render the main interface"""
        
        # Sidebar configuration
        with st.sidebar:
            st.header("🔧 Configuration")
            
            max_hops = st.slider("Maximum hops", 1, 8, 5)
            top_k_paths = st.slider("Top K paths", 1, 30, 10)
            show_reasoning = st.checkbox("Show reasoning paths", value=True)
            show_reasoning_paper = st.checkbox("Show LinkedIn post", value=True)
            show_graph_viz = st.checkbox("Show graph visualization", value=True)
            
            st.header("📊 System Stats")
            if self.graph:
                st.metric("Total Concepts", len(self.graph.nodes))
                st.metric("Total Relationships", len(self.graph.edges))
                st.metric("Graph Density", f"{nx.density(self.graph):.4f}")
            
            st.header("💡 Example Queries")
            examples = [
                "What is the relationship between bias and fairness in AI?",
                "How do privacy concerns affect machine learning deployment?",
                "What are the key components of responsible AI development?",
                "How does data governance impact AI model performance?",
                "What ethical considerations are important for AI systems?"
            ]
            
            for example in examples:
                if st.button(f"📝 {example[:30]}...", key=f"ex_{hash(example)}"):
                    st.session_state.current_query = example
        
        # Main query interface
        st.header("🔍 Query Interface")
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            query = st.text_area(
                "Enter your knowledge-intensive question:",
                value=st.session_state.get('current_query', ''),
                height=100,
                placeholder="Ask a complex question that requires multi-hop reasoning..."
            )
            
            if st.button("🚀 Execute HopRAG Query", type="primary"):
                if query and self.hoprag_engine:
                    self._process_query(query, max_hops, top_k_paths, show_reasoning, show_reasoning_paper, show_graph_viz)
                else:
                    st.warning("Please enter a query first")
        
        with col2:
            st.markdown("### 🎯 Query Tips")
            st.markdown("""
            - Ask complex questions requiring multiple reasoning steps
            - Use domain-specific terms from your knowledge graph
            - Questions about relationships work well
            - Try asking "how" and "why" questions
            """)
    
    def _process_query(self, query: str, max_hops: int, top_k: int, show_reasoning: bool, show_reasoning_paper: bool, show_viz: bool):
        """Process a HopRAG query with streaming display and real-time path visualization"""
        
        start_time = time.time()
        
        # Create streaming containers
        st.header("🔄 Real-Time Processing")
        
        # Main progress container
        progress_container = st.container()
        with progress_container:
            st.markdown("### 🚀 Processing Steps")
            
        # Create placeholders for streaming updates
        status_placeholder = st.empty()
        progress_placeholder = st.empty()
        path_placeholder = st.empty()
        abstract_placeholder = st.empty()
        linkedin_header_placeholder = st.empty()
        linkedin_post_placeholder = st.empty()
        linkedin_progress_placeholder = st.empty()
        
        # Real-time path visualization placeholder
        if show_viz:
            st.markdown("### 🕸️ **Real-Time Path Discovery**")
            realtime_viz_placeholder = st.empty()
            self.discovered_paths = []  # Track paths as they're discovered
        
        # Stream update function
        def stream_update(message: str, msg_type: str = "info"):
            if msg_type == "info":
                status_placeholder.info(message)
            elif msg_type == "success":
                status_placeholder.success(message)
            elif msg_type == "path":
                with path_placeholder.container():
                    st.markdown(f"**Path Discovery:** {message}")
                    
                # Update real-time visualization for significant paths
                if show_viz and "Path Found:" in message:
                    self._update_realtime_visualization(message, realtime_viz_placeholder)
                    
            elif msg_type == "abstract":
                with abstract_placeholder.container():
                    st.markdown(f"**Research Progress:** {message}")
            elif msg_type == "linkedin_header":
                with linkedin_header_placeholder.container():
                    st.markdown(f"### {message}")
            elif msg_type == "linkedin_update":
                with linkedin_post_placeholder.container():
                    st.markdown("```")
                    st.markdown(message)
                    st.markdown("```")
            elif msg_type == "linkedin_progress":
                with linkedin_progress_placeholder.container():
                    st.markdown(f"*{message}*")
            elif msg_type == "linkedin_final":
                with linkedin_post_placeholder.container():
                    st.success("📱 **Final LinkedIn Post:**")
                    st.markdown("---")
                    st.markdown(message)
                    st.markdown("---")
            
            # Add small delay for visual effect
            time.sleep(0.1)
        
        try:
            # Process query with streaming
            result = self.hoprag_engine.query(
                query, 
                max_hops=max_hops, 
                top_k=top_k, 
                stream_callback=stream_update
            )
            
            processing_time = time.time() - start_time
            
            # Clear streaming placeholders
            status_placeholder.empty()
            path_placeholder.empty()
            linkedin_progress_placeholder.empty()
            
            # Show completion
            st.success(f"✅ Processing completed in {processing_time:.2f} seconds!")
            
            # Display final results
            self._display_results(result, processing_time, show_reasoning, show_reasoning_paper, show_viz)
            
        except Exception as e:
            st.error(f"❌ Error processing query: {e}")
    
    def _display_results(self, result: HopRAGResult, processing_time: float, show_reasoning: bool, show_reasoning_paper: bool, show_viz: bool):
        """Display query results"""
        
        # Main answer
        st.header("📋 HopRAG Answer")
        st.markdown(f"**Query processed in {processing_time:.2f} seconds**")
        
        # Answer with confidence
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(result.answer)
        with col2:
            st.metric("Confidence", f"{result.confidence:.1%}")
        
        # Metadata
        st.header("📊 Query Metadata")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Start Entities", len(result.query_metadata.get('start_entities', [])))
        with col2:
            st.metric("Paths Explored", result.query_metadata.get('total_paths_explored', 0))
        with col3:
            st.metric("Max Hops Used", result.query_metadata.get('max_hops_used', 0))
        with col4:
            st.metric("Graph Coverage", f"{result.query_metadata.get('graph_coverage', 0):.1%}")
        
        # Reasoning paths
        if show_reasoning and result.hop_paths:
            st.header("🔍 Multi-Hop Reasoning Paths")
            
            for i, path in enumerate(result.hop_paths):
                with st.expander(f"Path {i+1}: {path.hop_count} hops (confidence: {path.confidence:.3f})"):
                    st.markdown(f"**Reasoning Chain:**")
                    st.text(path.reasoning_chain)
                    
                    st.markdown(f"**Entities:** {' → '.join(path.entities)}")
                    st.markdown(f"**Relations:** {' → '.join(path.relations)}")
                    
                    # Show evidence
                    st.markdown("**Supporting Evidence:**")
                    for j, evidence in enumerate(path.evidence):
                        if evidence.strip():
                            st.markdown(f"*Entity {j+1}:* {evidence[:200]}...")
        
        # Research Abstract
        if result.research_abstract:
            st.header("📄 Research Abstract")
            with st.expander("View Full Research Abstract", expanded=True):
                st.markdown(result.research_abstract)
        
        # Final Results Section
        st.header("🎯 Final Results")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            # LinkedIn post
            if show_reasoning_paper and result.reasoning_paper:
                st.subheader("📱 LinkedIn Post")
                with st.container():
                    st.markdown("---")
                    st.markdown(result.reasoning_paper)
                    st.markdown("---")
                    
                    # Copy button simulation
                    st.caption("💡 Copy this post to share your insights on LinkedIn!")
        
        with col2:
            # Graph visualization
            if show_viz and result.hop_paths:
                st.subheader("🕸️ Reasoning Graph")
                self._create_hop_visualization(result.hop_paths)
                st.caption(f"Visualization of {len(result.hop_paths)} reasoning paths")
        
        # Reasoning explanation
        if result.reasoning_explanation:
            st.header("💭 Reasoning Explanation")
            st.text(result.reasoning_explanation)
        
        # Supporting evidence
        if result.supporting_evidence:
            st.header("📚 Supporting Evidence")
            for i, evidence in enumerate(result.supporting_evidence[:5]):
                with st.expander(f"Evidence {i+1}"):
                    st.markdown(evidence[:500] + "..." if len(evidence) > 500 else evidence)
    
    def _create_hop_visualization(self, hop_paths: List[HopPath]):
        """Create enhanced interactive visualization of reasoning paths"""
        
        if not hop_paths:
            st.info("No reasoning paths to visualize")
            return
        
        # Show path selection controls
        col1, col2, col3 = st.columns([2, 2, 1])
        
        with col1:
            max_paths = st.slider("Number of paths to show", 1, min(len(hop_paths), 8), min(3, len(hop_paths)))
        
        with col2:
            layout_type = st.selectbox("Graph Layout", 
                ["Spring", "Circular", "Random", "Shell"], 
                index=0)
        
        with col3:
            show_confidence = st.checkbox("Show confidence", value=True)
        
        # Collect nodes and edges from selected paths
        selected_paths = hop_paths[:max_paths]
        all_nodes = {}  # Store node info
        all_edges = []
        node_frequencies = {}  # Count how many paths use each node
        
        for path_idx, path in enumerate(selected_paths):
            for node in path.entities:
                if node not in all_nodes:
                    all_nodes[node] = {
                        'name': node,
                        'paths': [],
                        'content': self.concept_content.get(node, "No content available")[:200] + "..."
                    }
                    node_frequencies[node] = 0
                all_nodes[node]['paths'].append(path_idx)
                node_frequencies[node] += 1
            
            for i in range(len(path.entities) - 1):
                all_edges.append({
                    'source': path.entities[i],
                    'target': path.entities[i+1],
                    'relation': path.relations[i],
                    'path_idx': path_idx,
                    'confidence': path.confidence,
                    'hop_position': i
                })
        
        # Create NetworkX graph for layout
        G = nx.Graph()
        for edge in all_edges:
            G.add_edge(edge['source'], edge['target'])
        
        # Apply selected layout
        if layout_type == "Spring":
            pos = nx.spring_layout(G, k=3, iterations=100, seed=42)
        elif layout_type == "Circular":
            pos = nx.circular_layout(G)
        elif layout_type == "Random":
            pos = nx.random_layout(G, seed=42)
        else:  # Shell
            pos = nx.shell_layout(G)
        
        # Create Plotly figure
        fig = go.Figure()
        
        # Define colors for different paths
        path_colors = [
            '#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', 
            '#FECA57', '#FF9FF3', '#54A0FF', '#5F27CD'
        ]
        
        # Add edges with enhanced styling
        for path_idx in range(max_paths):
            path_edges = [e for e in all_edges if e['path_idx'] == path_idx]
            path = selected_paths[path_idx]
            
            edge_x = []
            edge_y = []
            edge_info = []
            
            for edge in path_edges:
                if edge['source'] in pos and edge['target'] in pos:
                    x0, y0 = pos[edge['source']]
                    x1, y1 = pos[edge['target']]
                    edge_x.extend([x0, x1, None])
                    edge_y.extend([y0, y1, None])
                    edge_info.append(f"Path {path_idx + 1}: {edge['source']} → {edge['target']}<br>"
                                   f"Relation: {edge['relation']}<br>"
                                   f"Confidence: {edge['confidence']:.3f}")
            
            # Line width based on confidence
            line_width = 2 + (path.confidence * 4)  # 2-6 pixel width
            
            edge_trace = go.Scatter(
                x=edge_x, y=edge_y,
                line=dict(
                    width=line_width, 
                    color=path_colors[path_idx % len(path_colors)]
                ),
                mode='lines',
                name=f'Path {path_idx + 1} (conf: {path.confidence:.3f})',
                showlegend=True,
                hoverinfo='skip'
            )
            
            fig.add_trace(edge_trace)
        
        # Add nodes with enhanced information
        node_x = []
        node_y = []
        node_text = []
        node_info = []
        node_colors = []
        node_sizes = []
        
        for node_name, node_data in all_nodes.items():
            if node_name in pos:
                x, y = pos[node_name]
                node_x.append(x)
                node_y.append(y)
                
                # Display name (truncated if too long)
                display_name = node_name if len(node_name) <= 12 else node_name[:12] + "..."
                node_text.append(display_name)
                
                # Enhanced hover information
                paths_text = ", ".join([f"Path {i+1}" for i in node_data['paths']])
                frequency = node_frequencies[node_name]
                
                hover_text = (f"<b>{node_name}</b><br>"
                            f"Used in: {paths_text}<br>"
                            f"Frequency: {frequency} path(s)<br>"
                            f"Content: {node_data['content']}<br>"
                            f"Click for more details")
                node_info.append(hover_text)
                
                # Color based on frequency (more used nodes are redder)
                if show_confidence:
                    color_intensity = min(frequency / max_paths, 1.0)
                    node_colors.append(f'rgba(255, {int(100 + 155 * (1-color_intensity))}, {int(100 + 155 * (1-color_intensity))}, 0.8)')
                else:
                    node_colors.append('rgba(135, 206, 235, 0.8)')  # Light blue
                
                # Size based on frequency
                base_size = 20
                size_bonus = frequency * 8
                node_sizes.append(base_size + size_bonus)
        
        node_trace = go.Scatter(
            x=node_x, y=node_y,
            mode='markers+text',
            hoverinfo='text',
            text=node_text,
            textposition="middle center",
            hovertext=node_info,
            marker=dict(
                size=node_sizes,
                color=node_colors,
                line=dict(width=2, color='rgba(50, 50, 50, 0.8)'),
                sizemode='diameter'
            ),
            textfont=dict(size=10, color='black'),
            showlegend=False,
            name="Concepts"
        )
        
        fig.add_trace(node_trace)
        
        # Enhanced layout
        fig.update_layout(
            title=dict(
                text=f"Multi-Hop Reasoning Paths Visualization ({max_paths} paths)",
                font=dict(size=16)
            ),
            showlegend=True,
            hovermode='closest',
            margin=dict(b=20, l=5, r=5, t=60),
            font=dict(size=12),
            plot_bgcolor='rgba(248, 248, 255, 0.8)',
            paper_bgcolor='white',
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            ),
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            height=600,
            annotations=[dict(
                text="Hover over nodes and edges for details • Different colors represent different reasoning paths",
                showarrow=False,
                xref="paper", yref="paper",
                x=0.5, y=-0.02,
                xanchor='center',
                yanchor='top',
                font=dict(size=11, color='gray')
            )]
        )
        
        # Display the interactive plot
        st.plotly_chart(fig, use_container_width=True)
        
        # Add detailed path information below the graph
        self._display_path_details(selected_paths, show_confidence)
    
    def _display_path_details(self, hop_paths: List[HopPath], show_confidence: bool):
        """Display detailed information about reasoning paths"""
        
        st.subheader("🔍 Path Analysis")
        
        # Create tabs for different views
        tab1, tab2, tab3 = st.tabs(["📊 Path Comparison", "📈 Statistics", "🔗 Path Details"])
        
        with tab1:
            # Path comparison table
            if len(hop_paths) > 1:
                comparison_data = []
                for i, path in enumerate(hop_paths):
                    comparison_data.append({
                        'Path': f'Path {i+1}',
                        'Hops': path.hop_count,
                        'Confidence': f'{path.confidence:.3f}',
                        'Start': path.entities[0],
                        'End': path.entities[-1],
                        'Key Concepts': ' → '.join(path.entities)
                    })
                
                df = pd.DataFrame(comparison_data)
                st.dataframe(df, use_container_width=True)
            else:
                st.info("Add more paths to compare")
        
        with tab2:
            # Statistics about the paths
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                avg_hops = sum(p.hop_count for p in hop_paths) / len(hop_paths)
                st.metric("Average Hops", f"{avg_hops:.1f}")
            
            with col2:
                avg_confidence = sum(p.confidence for p in hop_paths) / len(hop_paths)
                st.metric("Average Confidence", f"{avg_confidence:.3f}")
            
            with col3:
                unique_concepts = len(set().union(*[p.entities for p in hop_paths]))
                st.metric("Unique Concepts", unique_concepts)
            
            with col4:
                total_connections = sum(p.hop_count for p in hop_paths)
                st.metric("Total Connections", total_connections)
            
            # Confidence distribution chart
            if show_confidence and len(hop_paths) > 1:
                st.subheader("Confidence Distribution")
                conf_data = pd.DataFrame({
                    'Path': [f'Path {i+1}' for i in range(len(hop_paths))],
                    'Confidence': [p.confidence for p in hop_paths]
                })
                
                bar_fig = px.bar(conf_data, x='Path', y='Confidence', 
                               title="Path Confidence Scores",
                               color='Confidence',
                               color_continuous_scale='RdYlBu_r')
                st.plotly_chart(bar_fig, use_container_width=True)
        
        with tab3:
            # Detailed path information
            path_selector = st.selectbox(
                "Select path for details:", 
                options=range(len(hop_paths)),
                format_func=lambda x: f"Path {x+1} (conf: {hop_paths[x].confidence:.3f})"
            )
            
            selected_path = hop_paths[path_selector]
            
            st.markdown(f"### Path {path_selector + 1} Details")
            
            col1, col2 = st.columns([1, 1])
            
            with col1:
                st.markdown("**Path Information:**")
                st.markdown(f"- **Hops:** {selected_path.hop_count}")
                st.markdown(f"- **Confidence:** {selected_path.confidence:.4f}")
                st.markdown(f"- **Reasoning Chain:**")
                st.code(selected_path.reasoning_chain, language=None)
            
            with col2:
                st.markdown("**Concept Progression:**")
                for i, (entity, relation) in enumerate(zip(selected_path.entities, selected_path.relations + ['END'])):
                    if relation != 'END':
                        st.markdown(f"{i+1}. **{entity}** `{relation}` →")
                    else:
                        st.markdown(f"{i+1}. **{entity}**")
            
            # Evidence details
            st.markdown("**Supporting Evidence:**")
            for i, evidence in enumerate(selected_path.evidence):
                if evidence.strip():
                    with st.expander(f"Evidence from {selected_path.entities[i]}"):
                        st.markdown(evidence[:300] + "..." if len(evidence) > 300 else evidence)
    
    def _update_realtime_visualization(self, path_message: str, viz_placeholder):
        """Update real-time visualization during path discovery"""
        
        # Extract path information from the message
        # Expected format: "🔗 **Path Found:** Entity1 → Entity2 → Entity3 (conf: 0.75)"
        import re
        
        # Parse the path string
        path_match = re.search(r'Path Found:\*\* (.+?) \(conf: ([\d\.]+)\)', path_message)
        if not path_match:
            # Try alternative pattern without formatting
            path_match = re.search(r'(.+?) \(conf: ([\d\.]+)\)', path_message)
            if not path_match:
                return
            
        path_str = path_match.group(1)
        confidence = float(path_match.group(2))
        entities = [e.strip() for e in path_str.split('→')]
        
        # Create a simple HopPath object for visualization
        from dataclasses import dataclass
        simple_path = HopPath(
            entities=entities,
            relations=['CONNECTED'] * (len(entities) - 1),
            evidence=[''] * len(entities),
            confidence=confidence,
            hop_count=len(entities) - 1,
            reasoning_chain=path_str
        )
        
        # Add to discovered paths
        self.discovered_paths.append(simple_path)
        
        # Create a simplified real-time graph visualization
        with viz_placeholder.container():
            st.markdown(f"**Paths Discovered: {len(self.discovered_paths)}**")
            
            # Always show the graph visualization with all paths
            # For performance, limit to most recent paths if too many
            max_paths_to_show = min(len(self.discovered_paths), 12)  # Show up to 12 paths
            paths_to_visualize = self.discovered_paths[-max_paths_to_show:]
            
            # Show metrics
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Paths", len(self.discovered_paths))
            with col2:
                st.metric("Showing", len(paths_to_visualize))
            with col3:
                avg_conf = sum(p.confidence for p in self.discovered_paths) / len(self.discovered_paths)
                st.metric("Avg Confidence", f"{avg_conf:.2f}")
            
            # Always show the graph with discovered paths
            self._create_lightweight_path_graph(paths_to_visualize)
    
    def _create_lightweight_path_graph(self, paths: List[HopPath]):
        """Create a lightweight graph for real-time updates with enhanced visualization"""
        
        if not paths:
            return
        
        # Create simplified NetworkX graph
        G = nx.Graph()
        all_edges = []
        node_frequencies = {}
        
        # Add paths to graph and count node frequencies
        for path_idx, path in enumerate(paths):
            for node in path.entities:
                node_frequencies[node] = node_frequencies.get(node, 0) + 1
                
            for i in range(len(path.entities) - 1):
                G.add_edge(path.entities[i], path.entities[i+1])
                all_edges.append({
                    'source': path.entities[i],
                    'target': path.entities[i+1],
                    'path_idx': path_idx,
                    'confidence': path.confidence
                })
        
        # Simple spring layout with better parameters
        pos = nx.spring_layout(G, k=1.5, iterations=100, seed=42)
        
        # Create lightweight Plotly figure
        fig = go.Figure()
        
        # Define colors for different paths
        path_colors = [
            '#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', 
            '#FECA57', '#FF9FF3', '#54A0FF', '#5F27CD',
            '#FD79A8', '#00B894', '#E17055', '#74B9FF'
        ]
        
        # Add edges grouped by path with different colors
        for path_idx in range(len(paths)):
            path_edges = [e for e in all_edges if e['path_idx'] == path_idx]
            path_color = path_colors[path_idx % len(path_colors)]
            
            edge_x, edge_y = [], []
            for edge in path_edges:
                if edge['source'] in pos and edge['target'] in pos:
                    x0, y0 = pos[edge['source']]
                    x1, y1 = pos[edge['target']]
                    edge_x.extend([x0, x1, None])
                    edge_y.extend([y0, y1, None])
            
            if edge_x:  # Only add if there are edges
                # Line width based on confidence
                line_width = 2 + (paths[path_idx].confidence * 3)  # 2-5 pixel width
                
                edge_trace = go.Scatter(
                    x=edge_x, y=edge_y,
                    line=dict(width=line_width, color=path_color),
                    hoverinfo='none',
                    mode='lines',
                    showlegend=True,
                    name=f'Path {path_idx + 1} (conf: {paths[path_idx].confidence:.2f})',
                    opacity=0.7
                )
                fig.add_trace(edge_trace)
        
        # Add nodes with enhanced styling
        node_x = [pos[node][0] for node in G.nodes()]
        node_y = [pos[node][1] for node in G.nodes()]
        node_text = [node[:12] + "..." if len(node) > 12 else node for node in G.nodes()]
        
        # Node sizes based on frequency (how many paths use this node)
        max_frequency = max(node_frequencies.values()) if node_frequencies else 1
        node_sizes = []
        node_colors = []
        node_info = []
        
        for node in G.nodes():
            frequency = node_frequencies.get(node, 1)
            # Size: 15-35 pixels based on frequency
            size = 15 + (frequency / max_frequency) * 20
            node_sizes.append(size)
            
            # Color intensity based on frequency
            intensity = frequency / max_frequency
            node_colors.append(f'rgba(100, 150, 255, {0.6 + intensity * 0.4})')
            
            # Hover info
            paths_using_node = [i+1 for i, path in enumerate(paths) if node in path.entities]
            node_info.append(f"{node}<br>Used in {frequency} path(s)<br>Paths: {', '.join(map(str, paths_using_node))}")
        
        node_trace = go.Scatter(
            x=node_x, y=node_y,
            mode='markers+text',
            hoverinfo='text',
            text=node_text,
            textposition="middle center",
            hovertext=node_info,
            marker=dict(
                size=node_sizes,
                color=node_colors,
                line=dict(width=2, color='rgba(50, 50, 50, 0.8)'),
                sizemode='diameter'
            ),
            textfont=dict(size=8, color='black'),
            showlegend=False,
            name="Concepts"
        )
        fig.add_trace(node_trace)
        
        # Enhanced layout for real-time view
        fig.update_layout(
            showlegend=True,
            hovermode='closest',
            margin=dict(b=20, l=5, r=5, t=50),
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            height=400,  # Slightly larger for better visibility
            plot_bgcolor='rgba(248, 248, 255, 0.3)',
            paper_bgcolor='white',
            legend=dict(
                orientation="v",
                yanchor="top",
                y=1,
                xanchor="left",
                x=1.02,
                font=dict(size=9)
            )
        )
        
        # Display with unique key to force updates
        st.plotly_chart(fig, use_container_width=True, key=f"realtime_{len(paths)}_{len(self.discovered_paths)}")

def main():
    """Main application entry point"""
    app = HopRAGStreamlitApp()
    app.run()

if __name__ == "__main__":
    main()