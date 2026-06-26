# Probability

## Definition

Probability is a mathematical framework for quantifying uncertainty, formally axiomatized by Andrey Kolmogorov in 1933 as a measure on a σ-algebra of events.

## Historical Development

1. **Classical Probability**: Early work by Pascal, Fermat, and Laplace
2. **Frequentist Approach**: Von Mises and the frequency interpretation
3. **Axiomatic Foundation (1933)**: Kolmogorov published "Grundbegriffe der Wahrscheinlichkeitsrechnung" (Foundations of the Theory of Probability)

## Kolmogorov's Axioms (1933)

Given a sample space Ω and an event space F, a probability measure P must satisfy:

1. **Non-negativity**: P(A) ≥ 0 for any event A
2. **Normalization**: P(Ω) = 1
3. **Countable Additivity**: For any countable sequence of disjoint events A₁, A₂, ...,
   P(⋃ᵢ Aᵢ) = ∑ᵢ P(Aᵢ)

## Key Concepts from Kolmogorov

1. **Probability Space**: The triple (Ω, F, P) where:
   - Ω is the sample space
   - F is a σ-algebra of events
   - P is a probability measure

2. **Random Variables**: Measurable functions from Ω to a measurable space

3. **Independence**: Events A and B are independent if P(A ∩ B) = P(A)P(B)

4. **Conditional Probability**: P(A|B) = P(A ∩ B) / P(B) for P(B) > 0

## Fundamental Properties

Derived from the axioms:
- P(∅) = 0
- P(Aᶜ) = 1 - P(A) (complement rule)
- If A ⊆ B, then P(A) ≤ P(B) (monotonicity)
- P(A ∪ B) = P(A) + P(B) - P(A ∩ B) (inclusion-exclusion)

## Interpretations of Probability

1. **Classical**: Equally likely outcomes
2. **Frequentist**: Long-run frequency of events
3. **Subjective/Bayesian**: Degree of belief
4. **Propensity**: Physical tendency to produce outcomes

## Applications

- Statistics and inference
- Physics and quantum mechanics
- Finance and risk assessment
- Machine learning and AI
- Information theory
- Genetics and biology

## Scientific Impact

Kolmogorov's work:
- Unified probability theory on rigorous mathematical foundations
- Enabled development of modern statistics
- Formed basis for stochastic processes
- Essential for quantum mechanics formulation
- Foundation for information theory

## Extensions and Developments

1. **Stochastic Processes**: Time-dependent random phenomena
2. **Measure Theory**: Generalization of probability
3. **Martingales**: Mathematical model of fair games
4. **Ergodic Theory**: Statistical properties of dynamical systems

## Related Concepts
- [[Measure theory]]
- [[Statistics]]
- [[Random variables]]
- [[Stochastic processes]]
- [[Information theory]]

## References

Kolmogorov, A.N. (1933). Grundbegriffe der Wahrscheinlichkeitsrechnung. Berlin: Springer. 
English translation: Foundations of the Theory of Probability (1956). New York: Chelsea Publishing.