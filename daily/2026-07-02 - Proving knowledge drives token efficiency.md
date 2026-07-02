
Today we're up to prove that [[knowledge]] drives efficiency. No, let's narrow this down : I'm up to prove that [[knowledge]] layers help reduce [[token]] consumption **and saves users' time**. Why would I want to prove that ? 

First, because it is a common intuition that the more you know, the less you speak. Or, as we say in french about culture : 

> [!quote]
> La culture, c'est comme la confiture, moins tu en as, plus tu l'étales. (*Culture is like jam: the less you have, the more you spread it.*)

([[Token]] jam became quite expansive these days). Proving that [[knowledge]] layers help reduce [[token]] consumption then would confirm the popular saying and intuition. 

Second, trying to prove that is a way to challenge my hypothesis that [[knowledge]] helps reduce natural semantic dispersion of [[Large Language Model]]. For it is reasonable enough to assume that the sparser the [[output]] of a [[Large Language Model]] (semantically speaking) the more iterations are required to reach a certain [[outcome]]. And the more iterations, the more tokens you consume. (I reckon here my predicate is that us, humans, are all looking for semantic [[precision]] when we prompt a LLM, to debate)

Third, and most important I think, if [[knowledge]] does drive [[token]] efficiency, because it helps reach faster semantic deep and precise [[output]]s, that would confirm as [Alban Leveau-Vallier wrote](https://hyper.hypotheses.org/171) , that traveling inside a [[latent space]] is the right way to think about [[Generation]].


> [!summary] Interlude
> If we prove that [[knowledge]] drives [[token]] efficiency, it would echo the French saying that culture, like jam, gets spread thinner the less you have. The logic: without [[knowledge]] semantically sparse LLM outputs need more iterations, and thus more tokens, to reach [[precision]]. Confirming this would also support Alban Leveau-Vallier's view of [[generation]] as travel through a [[latent space]] where [[knowledge]] is like a map that shows a faster [[path]] toward destination

Now, let's get down to the hard part : designing a simple and good enough experiment (which is the same, cf [[Occam's rasor]]). 

## Experiment [[design]] 

The hardest part is often to agree on an *end state*, [[meaning]] here : when do we consider it is no longer necessary to consume tokens to reach the desirable goal ? From there, we can [[test]] different solutions (some with, some others without [[knowledge]] layers, different types of [[knowledge]] layers and so on). But to get there, we must first agree on what a final solution looks like. 

Funny enough here, I advocate that a final solution is **one that looks like so much an original human-made solution that we can no longer distinguish which is which**. The idea is not mine, it is Turing's one. In other words, I advocate a final solution a solution that passes the [[Turing test]]. 

So you know you should no longer consume [[token]] once the generated [[output]] looks like so much the original you can no longer distinguish which was produced and which was generated.

Rephrasing the objective of the experiment to [[design]] here : 

> Do [[knowledge]] layers help generated ouput pass the [[Turing test]] faster ? 

> [!summary] Interlude 
> Designing the experiment first requires agreeing on an end state, i.e the point at which consuming more tokens is no longer necessary to reach the goal. The proposed criterion, borrowed from Turing, is indistinguishability: the [[output]] is done once it resembles a human-made original so closely that you can't tell which is which. This reframes the whole question as: do [[knowledge]] layers help generated [[output]] pass the [[Turing test]] faster?

The simpler end state to agree on is a slide. Why a slide ? Because a slide is simple, and needs both semantic and visual [[precision]].

So I'll take a slide crafted by humans (below) and this will be our end state. 

![[good_visually.png]]

### How will I [[measure]] the quality of the generated [[output]] ? 

As I said, if the generated slide passes the Turing tests, then the end state was reached and we should stop consuming tokens. But Turing's [[test]] most certainly rely on subjectivity : some people will be confused, others will be wrong, others will spot AI intervention instantly. 

So we need more than a [[Turing test]]. We need metrics. I propose 3 [[metric]] : 

1. **Structure [[metric]]** : how many **structure elements** from the generated [[output]] match the original one ? 
2. **Content [[metric]]** : what is the [[distance]] between the [[token]] sequence generated and the original word sequence ? 
3. **Visual [[metric]]** : LLM as a judge [[metric]], where the [[model]] will say what are the [[differences]] between the generated and the original slide 

([[confusion matrix]] ?)

In the slide above we see : 
* 5 structure elements (1 title and 4 boxes)
* 10 word sequences 
* 1 visual [[design]] with a relatively small title, lots of space inside the slide and distinguishable color palette

> [!summary] Interlude
> The chosen end state is a human-made slide, since a slide is simple yet demands both semantic and visual [[precision]]. Because the [[Turing test]] alone is too subjective, quality is measured with three metrics: a structure [[metric]] (how many structural elements match the original), a content [[metric]] (the [[distance]] between generated and original word sequences), and a visual [[metric]] (an LLM-as-judge comparing the two slides). The reference slide has 5 structure elements (1 title, 4 boxes), 10 word sequences, and a distinct visual [[design]] featuring a small title, generous spacing, and a clear color palette.

All in all, the end state is reached once : 

* The generated content passed the [[Turing test]] 
* Perfect match of structure elements
* [[Distance]] between content is near 0 
* The LLM as a judge does not spot any visual difference

### How will I [[measure]] [[token]] consumption ? 

That's the easy part. I'll take 5 different harness (with their native LLM attached) : 
* [[Claude]] Cowork 
* Copilot in [[Power]] Point 
* 
