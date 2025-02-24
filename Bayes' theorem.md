
## Statement of theorem


Bayes' theorem is stated mathematically as the following equation:[[17]](#cite_note-18)

![{\displaystyle P(A\vert B)={\frac {P(B\vert A)P(A)}{P(B)}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/4211e3e7c3482573cdfbc0653d48a6279104c899)

where ![{\displaystyle A}](https://wikimedia.org/api/rest_v1/media/math/render/svg/7daff47fa58cdfd29dc333def748ff5fa4c923e3) and ![{\displaystyle B}](https://wikimedia.org/api/rest_v1/media/math/render/svg/47136aad860d145f75f3eed3022df827cee94d7a) are [events](https://en.wikipedia.org/wiki/Event_\(probability_theory\) "Event (probability theory)") and ![{\displaystyle P(B)\neq 0}](https://wikimedia.org/api/rest_v1/media/math/render/svg/4696c4543d63622a09c29cbb00c0fea4e0b8d7b7).

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Bayes_theorem_visual_proof.svg/170px-Bayes_theorem_visual_proof.svg.png)](https://en.wikipedia.org/wiki/File:Bayes_theorem_visual_proof.svg)

Visual proof of Bayes' theorem

Bayes' theorem may be derived from the definition of [conditional probability](https://en.wikipedia.org/wiki/Conditional_probability "Conditional probability"):

![{\displaystyle P(A\vert B)={\frac {P(A\cap B)}{P(B)}},{\text{ if }}P(B)\neq 0,}](https://wikimedia.org/api/rest_v1/media/math/render/svg/8933ae615029cbf453fd2908335dc816b7a66df9)

where ![{\displaystyle P(A\cap B)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f22276bc48d131dadc7e4dacbf38cee3ed05d536) is the probability of both A and B being true. Similarly,

![{\displaystyle P(B\vert A)={\frac {P(A\cap B)}{P(A)}},{\text{ if }}P(A)\neq 0.}](https://wikimedia.org/api/rest_v1/media/math/render/svg/e46e9d1e9656e662594c1c41cc1d170ae5208f58)

Solving for ![{\displaystyle P(A\cap B)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f22276bc48d131dadc7e4dacbf38cee3ed05d536) and substituting into the above expression for ![{\displaystyle P(A\vert B)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/8114af1733b7f0ad6aa718629a01264569d689ee) yields Bayes' theorem:

![{\displaystyle P(A\vert B)={\frac {P(B\vert A)P(A)}{P(B)}},{\text{ if }}P(B)\neq 0.}](https://wikimedia.org/api/rest_v1/media/math/render/svg/6158075cb0aa165f426e663093f2a1351e447b3c)

#### For continuous random variables

[[edit](https://en.wikipedia.org/w/index.php?title=Bayes%27_theorem&action=edit&section=5 "Edit section: For continuous random variables")]

For two continuous [random variables](https://en.wikipedia.org/wiki/Random_variable "Random variable") _X_ and _Y_, Bayes' theorem may be analogously derived from the definition of [conditional density](https://en.wikipedia.org/wiki/Conditional_density "Conditional density"):

![{\displaystyle f_{X\vert Y=y}(x)={\frac {f_{X,Y}(x,y)}{f_{Y}(y)}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/5987d81d13006ceb511dbf041471c1fefd3d5ff1)

![{\displaystyle f_{Y\vert X=x}(y)={\frac {f_{X,Y}(x,y)}{f_{X}(x)}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/b51980b44e3ad658c94f2a131f56630d8d753c23)

Therefore,

![{\displaystyle f_{X\vert Y=y}(x)={\frac {f_{Y\vert X=x}(y)f_{X}(x)}{f_{Y}(y)}}.}](https://wikimedia.org/api/rest_v1/media/math/render/svg/854fd5ed4411c1b9ba2b9ddaad3780ca1b934aab)

Let ![{\displaystyle P_{Y}^{x}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/d92eb885c1778b36fe0ea7654f5fa17aacfa7d9d) be the conditional distribution of ![{\displaystyle Y}](https://wikimedia.org/api/rest_v1/media/math/render/svg/961d67d6b454b4df2301ac571808a3538b3a6d3f) given ![{\displaystyle X=x}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0661396d873679039ffe8e908a39f02402d4912d) and let ![{\displaystyle P_{X}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/8348dd8ce7e6f7f4778ee01fa5bdc7b828afd98c) be the distribution of ![{\displaystyle X}](https://wikimedia.org/api/rest_v1/media/math/render/svg/68baa052181f707c662844a465bfeeb135e82bab). The joint distribution is then ![{\displaystyle P_{X,Y}(dx,dy)=P_{Y}^{x}(dy)P_{X}(dx)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/ec7fe44cedd3314ca245dfd53a2c11e3ed1c9aca). The conditional distribution ![{\displaystyle P_{X}^{y}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/40ad7fcb2df4aacda6af4df410c7e2259292cc7c) of ![{\displaystyle X}](https://wikimedia.org/api/rest_v1/media/math/render/svg/68baa052181f707c662844a465bfeeb135e82bab) given ![{\displaystyle Y=y}](https://wikimedia.org/api/rest_v1/media/math/render/svg/678864c5e9a7ce08acfc22d0d7f726d2cade5b45) is then determined by

![{\displaystyle P_{X}^{y}(A)=E(1_{A}(X)|Y=y)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/ac77ab2aa324d8ef6653f6e5ff984e1fc0304fbb)

Existence and uniqueness of the needed [conditional expectation](https://en.wikipedia.org/wiki/Conditional_expectation "Conditional expectation") is a consequence of the [Radon–Nikodym theorem](https://en.wikipedia.org/wiki/Radon%E2%80%93Nikodym_theorem "Radon–Nikodym theorem"). This was formulated by [Kolmogorov](https://en.wikipedia.org/wiki/Andrey_Kolmogorov "Andrey Kolmogorov") in 1933. Kolmogorov underlines the importance of conditional probability, writing, "I wish to call attention to ... the theory of conditional probabilities and conditional expectations".[[18]](#cite_note-19) Bayes' theorem determines the posterior distribution from the prior distribution. Uniqueness requires continuity assumptions.[[19]](#cite_note-20) Bayes' theorem can be generalized to include improper prior distributions such as the uniform distribution on the real line.[[20]](#cite_note-21) Modern [Markov chain Monte Carlo](https://en.wikipedia.org/wiki/Markov_chain_Monte_Carlo "Markov chain Monte Carlo") methods have boosted the importance of Bayes' theorem, including in cases with improper priors.[[21]](#cite_note-22)

### Recreational mathematics

Bayes' rule and computing [conditional probabilities](https://en.wikipedia.org/wiki/Conditional_probability "Conditional probability") provide a method to solve a number of popular puzzles, such as the [Three Prisoners problem](https://en.wikipedia.org/wiki/Three_Prisoners_problem "Three Prisoners problem"), the [Monty Hall problem](https://en.wikipedia.org/wiki/Monty_Hall_problem "Monty Hall problem"), the [Two Child problem](https://en.wikipedia.org/wiki/Boy_or_Girl_paradox "Boy or Girl paradox"), and the [Two Envelopes problem](https://en.wikipedia.org/wiki/Two_envelopes_problem "Two envelopes problem").

Suppose, a particular test for whether someone has been using cannabis is 90% [sensitive](https://en.wikipedia.org/wiki/Sensitivity_\(tests\) "Sensitivity (tests)"), meaning the [true positive rate](https://en.wikipedia.org/wiki/True_positive_rate "True positive rate") (TPR) = 0.90. Therefore, it leads to 90% true positive results (correct identification of drug use) for cannabis users.

The test is also 80% [specific](https://en.wikipedia.org/wiki/Specificity_\(tests\) "Specificity (tests)"), meaning [true negative rate](https://en.wikipedia.org/wiki/True_negative_rate "True negative rate") (TNR) = 0.80. Therefore, the test correctly identifies 80% of non-use for non-users, but also generates 20% false positives, or [false positive rate](https://en.wikipedia.org/wiki/False_positive_rate "False positive rate") (FPR) = 0.20, for non-users.

Assuming 0.05 [prevalence](https://en.wikipedia.org/wiki/Prevalence "Prevalence"), meaning 5% of people use cannabis, what is the [probability](https://en.wikipedia.org/wiki/Probability "Probability") that a random person who tests positive is really a cannabis user?

The [Positive predictive value](https://en.wikipedia.org/wiki/Positive_predictive_value "Positive predictive value") (PPV) of a test is the proportion of persons who are actually positive out of all those testing positive, and can be calculated from a sample as:

PPV = True positive / Tested positive

If sensitivity, specificity, and prevalence are known, PPV can be calculated using Bayes' theorem. Let ![{\displaystyle P({\text{User}}\vert {\text{Positive}})}](https://wikimedia.org/api/rest_v1/media/math/render/svg/d138c95f551ed76cc90c8a0592cd42768ec972b7) mean "the probability that someone is a cannabis user given that they test positive", which is what PPV means. We can write:

![{\displaystyle {\begin{aligned}P({\text{User}}\vert {\text{Positive}})&={\frac {P({\text{Positive}}\vert {\text{User}})P({\text{User}})}{P({\text{Positive}})}}\\&={\frac {P({\text{Positive}}\vert {\text{User}})P({\text{User}})}{P({\text{Positive}}\vert {\text{User}})P({\text{User}})+P({\text{Positive}}\vert {\text{Non-user}})P({\text{Non-user}})}}\\[8pt]&={\frac {0.90\times 0.05}{0.90\times 0.05+0.20\times 0.95}}={\frac {0.045}{0.045+0.19}}\approx 19\%\end{aligned}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/c26c47487bf7b0fc56304c7123c3890a2b3e0f15)


The denominator ![{\displaystyle P({\text{Positive}})=P({\text{Positive}}\vert {\text{User}})P({\text{User}})+P({\text{Positive}}\vert {\text{Non-user}})P({\text{Non-user}})}](https://wikimedia.org/api/rest_v1/media/math/render/svg/bd7a281e27f176df4cbf947aa5d334e056b42392) is a direct application of the [Law of Total Probability](https://en.wikipedia.org/wiki/Law_of_Total_Probability "Law of Total Probability"). In this case, it says that the probability that someone tests positive is the probability that a user tests positive times the probability of being a user, plus the probability that a non-user tests positive, times the probability of being a non-user. This is true because the classifications user and non-user form a [partition of a set](https://en.wikipedia.org/wiki/Partition_of_a_set "Partition of a set"), namely the set of people who take the drug test. This combined with the definition of [conditional probability](https://en.wikipedia.org/wiki/Conditional_probability "Conditional probability") results in the above statement.

In other words, if someone tests positive, the probability that they are a cannabis user is only 19%—because in this group, only 5% of people are users, and most positives are false positives coming from the remaining 95%.

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Bayes-rule3.png/220px-Bayes-rule3.png)](https://en.wikipedia.org/wiki/File:Bayes-rule3.png)

Using a frequency box to show ![{\displaystyle P({\text{User}}\vert {\text{Positive}})}](https://wikimedia.org/api/rest_v1/media/math/render/svg/d138c95f551ed76cc90c8a0592cd42768ec972b7) visually by comparison of shaded areas. Note how small the pink area of true positives is compared to the blue area of false positives.

If 1,000 people were tested:

- 950 are non-users and 190 of them give false positive (0.20 × 950)
- 50 of them are users and 45 of them give true positive (0.90 × 50)

The 1,000 people thus have 235 positive tests, of which only 45 are genuine, about 19%.

#### Sensitivity or specificity

[[edit](https://en.wikipedia.org/w/index.php?title=Bayes%27_theorem&action=edit&section=10 "Edit section: Sensitivity or specificity")]

The importance of [specificity](https://en.wikipedia.org/wiki/Specificity_\(tests\) "Specificity (tests)") can be seen by showing that even if sensitivity is raised to 100% and specificity remains at 80%, the probability that someone who tests positive is a cannabis user rises only from 19% to 21%, but if the sensitivity is held at 90% and the specificity is increased to 95%, the probability rises to 49%.

|Test<br><br>Actual|Positive|Negative||Total|
|---|---|---|---|---|
|User|**45**|5|50|
|Non-user|190|760|950|
||   |   |   |   |
|Total|**235**|765|1000|
|90% sensitive, 80% specific, PPV=45/235 ≈ 19%|   |   |   |   |

|Test<br><br>Actual|Positive|Negative||Total|
|---|---|---|---|---|
|User|**50**|0|50|
|Non-user|190|760|950|
||   |   |   |   |
|Total|**240**|760|1000|
|100% sensitive, 80% specific, PPV=50/240 ≈ 21%|   |   |   |   |

|Test<br><br>Actual|Positive|Negative||Total|
|---|---|---|---|---|
|User|**45**|5|50|
|Non-user|47|903|950|
||   |   |   |   |
|Total|**92**|908|1000|
|90% sensitive, 95% specific, PPV=45/92 ≈ 49%|   |   |   |   |

If all patients with pancreatic cancer have a certain symptom, it does not follow that anyone who has that symptom has a 100% chance of getting pancreatic cancer. Assuming the incidence rate of pancreatic cancer is 1/100000, while 10/99999 healthy individuals have the same symptoms worldwide, the probability of having pancreatic cancer given the symptoms is 9.1%, and the other 90.9% could be "false positives" (that is, falsely said to have cancer; "positive" is a confusing term when, as here, the test gives bad news).

Based on incidence rate, the following table presents the corresponding numbers per 100,000 people.

|Symptom<br><br>Cancer|Yes|No||Total|
|---|---|---|---|---|
|Yes|1|0|1|
|No|10|99989|99999|
||   |   |   |   |
|Total|11|99989|100000|

Which can then be used to calculate the probability of having cancer when you have the symptoms:

![{\displaystyle {\begin{aligned}P({\text{Cancer}}|{\text{Symptoms}})&={\frac {P({\text{Symptoms}}|{\text{Cancer}})P({\text{Cancer}})}{P({\text{Symptoms}})}}\\&={\frac {P({\text{Symptoms}}|{\text{Cancer}})P({\text{Cancer}})}{P({\text{Symptoms}}|{\text{Cancer}})P({\text{Cancer}})+P({\text{Symptoms}}|{\text{Non-Cancer}})P({\text{Non-Cancer}})}}\\[8pt]&={\frac {1\times 0.00001}{1\times 0.00001+(10/99999)\times 0.99999}}={\frac {1}{11}}\approx 9.1\%\end{aligned}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/d78d8f2bcc4f4b701033a5b1f1c2bf6c050970f6)

### Defective item rate

[[edit](https://en.wikipedia.org/w/index.php?title=Bayes%27_theorem&action=edit&section=12 "Edit section: Defective item rate")]

|Condition<br><br>Machine|Defective|Flawless||Total|
|---|---|---|---|---|
|A|10|190|200|
|B|9|291|300|
|C|**5**|495|500|
||   |   |   |   |
|Total|**24**|976|1000|

A factory produces items using three machines—A, B, and C—which account for 20%, 30%, and 50% of its output, respectively. Of the items produced by machine A, 5% are defective, while 3% of B's items and 1% of C's are defective. If a randomly selected item is defective, what is the probability it was produced by machine C?

Once again, the answer can be reached without using the formula by applying the conditions to a hypothetical number of cases. For example, if the factory produces 1,000 items, 200 will be produced by A, 300 by B, and 500 by C. Machine A will produce 5% × 200 = 10 defective items, B 3% × 300 = 9, and C 1% × 500 = 5, for a total of 24. Thus 24/1000 (2.4%) of the total output will be defective and the likelihood that a randomly selected defective item was produced by machine C is 5/24 (~20.83%).

This problem can also be solved using Bayes' theorem: Let _Xi_ denote the event that a randomly chosen item was made by the _i_ th machine (for _i_ = A,B,C). Let _Y_ denote the event that a randomly chosen item is defective. Then, we are given the following information:

![{\displaystyle P(X_{A})=0.2,\quad P(X_{B})=0.3,\quad P(X_{C})=0.5.}](https://wikimedia.org/api/rest_v1/media/math/render/svg/e7b055f1700a12db75d72221ca43686e19b623f8)

If the item was made by the first machine, then the probability that it is defective is 0.05; that is, _P_(_Y_ | _X_A) = 0.05. Overall, we have

![{\displaystyle P(Y|X_{A})=0.05,\quad P(Y|X_{B})=0.03,\quad P(Y|X_{C})=0.01.}](https://wikimedia.org/api/rest_v1/media/math/render/svg/42e390b71af825f5f34b8001e6f1e5a1cfc305c7)

To answer the original question, we first find _P_(Y). That can be done in the following way:

![{\displaystyle P(Y)=\sum _{i}P(Y|X_{i})P(X_{i})=(0.05)(0.2)+(0.03)(0.3)+(0.01)(0.5)=0.024.}](https://wikimedia.org/api/rest_v1/media/math/render/svg/2ba5ec579a63c77e821a4fa42dcc4be5519eac05)

Hence, 2.4% of the total output is defective.

We are given that _Y_ has occurred and we want to calculate the conditional probability of _X_C. By Bayes' theorem,

![{\displaystyle P(X_{C}|Y)={\frac {P(Y|X_{C})P(X_{C})}{P(Y)}}={\frac {0.01\cdot 0.50}{0.024}}={\frac {5}{24}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/04d3d5182f6344e07323113d18c47afb33b227c1)

Given that the item is defective, the probability that it was made by machine C is 5/24. C produces half of the total output but a much smaller fraction of the defective items. Hence the knowledge that the item selected was defective enables us to replace the prior probability _P_(_X_C) = 1/2 by the smaller posterior probability _P_(XC | _Y_) = 5/24.

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Bayes_theorem_assassin.svg/220px-Bayes_theorem_assassin.svg.png)](https://en.wikipedia.org/wiki/File:Bayes_theorem_assassin.svg)

A geometric visualization of Bayes' theorem using astronauts, from the online game _[Among Us](https://en.wikipedia.org/wiki/Among_Us "Among Us")_, who may be suspicious (with eyebrows) and may be assassins (with daggers)

The interpretation of Bayes' rule depends on the [interpretation of probability](https://en.wikipedia.org/wiki/Probability_interpretations "Probability interpretations") ascribed to the terms. The two predominant interpretations are described below.

### Bayesian interpretation

[[edit](https://en.wikipedia.org/w/index.php?title=Bayes%27_theorem&action=edit&section=14 "Edit section: Bayesian interpretation")]

In the [Bayesian (or epistemological) interpretation](https://en.wikipedia.org/wiki/Bayesian_probability "Bayesian probability"), probability measures a "degree of belief". Bayes' theorem links the degree of belief in a proposition before and after accounting for evidence. For example, suppose it is believed with 50% certainty that a coin is twice as likely to land heads than tails. If the coin is flipped a number of times and the outcomes observed, that degree of belief will probably rise or fall, but might remain the same, depending on the results. For proposition _A_ and evidence _B_,

- _P_ (_A_), the _prior_, is the initial degree of belief in _A_.
- _P_ (_A_ | _B_), the _posterior_, is the degree of belief after incorporating news that _B_ is true.
- the quotient ⁠_P_(_B_ | _A_)/_P_(_B_)⁠ represents the support _B_ provides for _A_.

For more on the application of Bayes' theorem under the Bayesian interpretation of probability, see [Bayesian inference](https://en.wikipedia.org/wiki/Bayesian_inference "Bayesian inference").

### Frequentist interpretation

[[edit](https://en.wikipedia.org/w/index.php?title=Bayes%27_theorem&action=edit&section=15 "Edit section: Frequentist interpretation")]

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Bayes_theorem_tree_diagrams.svg/220px-Bayes_theorem_tree_diagrams.svg.png)](https://en.wikipedia.org/wiki/File:Bayes_theorem_tree_diagrams.svg)

Illustration of frequentist interpretation with [tree diagrams](https://en.wikipedia.org/wiki/Tree_diagram_\(probability_theory\) "Tree diagram (probability theory)")

In the [frequentist interpretation](https://en.wikipedia.org/wiki/Frequentist_interpretation_of_probability "Frequentist interpretation of probability"), probability measures a "proportion of outcomes". For example, suppose an experiment is performed many times. _P_(_A_) is the proportion of outcomes with property _A_ (the prior) and _P_(_B_) is the proportion with property _B_. _P_(_B_ | _A_) is the proportion of outcomes with property _B_ _out of_ outcomes with property _A_, and _P_(_A_ | _B_) is the proportion of those with _A_ _out of_ those with _B_ (the posterior).

The role of Bayes' theorem can be shown with tree diagrams. The two diagrams partition the same outcomes by _A_ and _B_ in opposite orders, to obtain the inverse probabilities. Bayes' theorem links the different partitionings.

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Bayes_theorem_simple_example_tree.svg/220px-Bayes_theorem_simple_example_tree.svg.png)](https://en.wikipedia.org/wiki/File:Bayes_theorem_simple_example_tree.svg)

Tree diagram illustrating the beetle example. _R, C, P_ and ![{\displaystyle {\overline {P}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/d5e1bed5bc42d4e46dd9e5c7d2fc327927b87169) are the events rare, common, pattern and no pattern. Percentages in parentheses are calculated. Three independent values are given, so it is possible to calculate the inverse tree.

An [entomologist](https://en.wikipedia.org/wiki/Entomology "Entomology") spots what might, due to the pattern on its back, be a rare [subspecies](https://en.wikipedia.org/wiki/Subspecies "Subspecies") of [beetle](https://en.wikipedia.org/wiki/Beetle "Beetle"). A full 98% of the members of the rare subspecies have the pattern, so _P_(Pattern | Rare) = 98%. Only 5% of members of the common subspecies have the pattern. The rare subspecies is 0.1% of the total population. How likely is the beetle having the pattern to be rare: what is _P_(Rare | Pattern)?

From the extended form of Bayes' theorem (since any beetle is either rare or common),

![{\displaystyle {\begin{aligned}P({\text{Rare}}\vert {\text{Pattern}})&={\frac {P({\text{Pattern}}\vert {\text{Rare}})\,P({\text{Rare}})}{P({\text{Pattern}})}}\\[8pt]&={\tfrac {P({\text{Pattern}}\vert {\text{Rare}})\,P({\text{Rare}})}{P({\text{Pattern}}\vert {\text{Rare}})\,P({\text{Rare}})+P({\text{Pattern}}\vert {\text{Common}})\,P({\text{Common}})}}\\[8pt]&={\frac {0.98\times 0.001}{0.98\times 0.001+0.05\times 0.999}}\\[8pt]&\approx 1.9\%\end{aligned}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/db5dde505d680ed31c343105203efc38506e9132)

For events _A_ and _B_, provided that _P_(_B_) ≠ 0,

![{\displaystyle P(A|B)={\frac {P(B|A)P(A)}{P(B)}}.}](https://wikimedia.org/api/rest_v1/media/math/render/svg/c1a7279a1639d92d751e0f2d3aa54e62a2ddb1e8)

In many applications, for instance in [Bayesian inference](https://en.wikipedia.org/wiki/Bayesian_inference "Bayesian inference"), the event _B_ is fixed in the discussion and we wish to consider the effect of its having been observed on our belief in various possible events _A_. In such situations the denominator of the last expression, the probability of the given evidence _B_, is fixed; what we want to vary is _A_. Bayes' theorem shows that the posterior probabilities are [proportional](https://en.wikipedia.org/wiki/Proportionality_\(mathematics\) "Proportionality (mathematics)") to the numerator, so the last equation becomes:

![{\displaystyle P(A|B)\propto P(A)\cdot P(B|A).}](https://wikimedia.org/api/rest_v1/media/math/render/svg/6112b2ccd1d0e2bc37aa571dc3e56c74370113c9)

In words, the posterior is proportional to the prior times the likelihood.[[22]](#cite_note-23)

If events _A_1, _A_2, ..., are mutually exclusive and exhaustive, i.e., one of them is certain to occur but no two can occur together, we can determine the proportionality constant by using the fact that their probabilities must add up to one. For instance, for a given event _A_, the event _A_ itself and its complement ¬_A_ are exclusive and exhaustive. Denoting the constant of proportionality by _c_, we have:

![{\displaystyle P(A|B)=c\cdot P(A)\cdot P(B|A){\text{ and }}P(\neg A|B)=c\cdot P(\neg A)\cdot P(B|\neg A).}](https://wikimedia.org/api/rest_v1/media/math/render/svg/8a9b95f96a54c659184fa1ea54b4e4aef672812e)

Adding these two formulas we deduce that:

![{\displaystyle 1=c\cdot (P(B|A)\cdot P(A)+P(B|\neg A)\cdot P(\neg A)),}](https://wikimedia.org/api/rest_v1/media/math/render/svg/50e3aa1e5f83ee4b581bf9b67b419a0a64d73616)

or

![{\displaystyle c={\frac {1}{P(B|A)\cdot P(A)+P(B|\neg A)\cdot P(\neg A)}}={\frac {1}{P(B)}}.}](https://wikimedia.org/api/rest_v1/media/math/render/svg/8cbd0a1115070eb4ca6494a243939bbad9034128)

|   |   |   |   |
|---|---|---|---|
[Contingency table](https://en.wikipedia.org/wiki/Contingency_table "Contingency table")
|Background<br><br>Proposition|B|⁠![{\displaystyle \lnot B}](https://wikimedia.org/api/rest_v1/media/math/render/svg/36cc283f1ab46e0de7fdd0b252f224350f060d02)⁠  <br>(not B)|Total|
|A|![{\displaystyle P(B\|A)\cdot P(A)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/9b4e0c15322ef6cc00d575d1fe35391e0eb03ab8)  <br>![{\displaystyle =P(A\|B)\cdot P(B)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/8408b14de2cdeb0cc2be15010c52767e06471486)|![{\displaystyle P(\neg B\|A)\cdot P(A)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/964a2b792e4a994d982fe5bddbb9f6f9e00ee23b)  <br>![{\displaystyle =P(A\|\neg B)\cdot P(\neg B)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/7af897a1678a28a475f74136f3e499f9f730a61d)|⁠![{\displaystyle P(A)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/4f264d19e21604793c6dc54f8044df454db82744)⁠|
|⁠![{\displaystyle \neg A}](https://wikimedia.org/api/rest_v1/media/math/render/svg/195aae731102b36b14a902a091d04ac5c6a5af49)⁠  <br>(not A)|![{\displaystyle P(B\|\neg A)\cdot P(\neg A)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/fbcf18f47f4e10f4a89a9713df0e86a11afdf59f)  <br>![{\displaystyle =P(\neg A\|B)\cdot P(B)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/5d645f93a4568a96ff81d552d5bc203370504916)|![{\displaystyle P(\neg B\|\neg A)\cdot P(\neg A)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/71cbb7258d0164ec355d039a9305b966413e3249)  <br>![{\displaystyle =P(\neg A\|\neg B)\cdot P(\neg B)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f0b67145527e6ca2a782a6f101b3a2afb0d64d84)|![{\displaystyle P(\neg A)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/959e9a80221def318e57d5c2cf71d8e31a6ef4c7)=  <br>![{\displaystyle 1-P(A)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/7c2b4077e696025374a6f7f7df4e96cb869b3bac)|
||   |   |   |   |
|Total|⁠![{\displaystyle P(B)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/e593d180a26fd68657ea50368dbfe1a661e652aa)⁠|![{\displaystyle P(\neg B)=1-P(B)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/ea0c3dc4eae0a4b8033eecdee98bb56a472640ba)|1|

Another form of Bayes' theorem for two competing statements or hypotheses is:

![{\displaystyle P(A|B)={\frac {P(B|A)P(A)}{P(B|A)P(A)+P(B|\neg A)P(\neg A)}}.}](https://wikimedia.org/api/rest_v1/media/math/render/svg/b63653680275c0e1a910a0671dfd094eb2c84222)

For an epistemological interpretation:

For proposition _A_ and evidence or background _B_,[[23]](#cite_note-24)

Often, for some [partition](https://en.wikipedia.org/wiki/Partition_of_a_set "Partition of a set") {_Aj_} of the [sample space](https://en.wikipedia.org/wiki/Sample_space "Sample space"), the [event space](https://en.wikipedia.org/wiki/Sample_space "Sample space") is given in terms of _P_(_Aj_) and _P_(_B_ | _Aj_). It is then useful to compute _P_(_B_) using the [law of total probability](https://en.wikipedia.org/wiki/Law_of_total_probability "Law of total probability"):

![{\displaystyle P(B)=\sum _{j}P(B\cap A_{j}),}](https://wikimedia.org/api/rest_v1/media/math/render/svg/d702d6bad9585c5b7cdd0984cacc3acc5c045266)

Or (using the multiplication rule for conditional probability),[[24]](#cite_note-25)

![{\displaystyle P(B)={\sum _{j}P(B|A_{j})P(A_{j})},}](https://wikimedia.org/api/rest_v1/media/math/render/svg/ac1f267991ef5384500f98dc2e48834bfe324679)

![{\displaystyle \Rightarrow P(A_{i}|B)={\frac {P(B|A_{i})P(A_{i})}{\sum \limits _{j}P(B|A_{j})P(A_{j})}}\cdot }](https://wikimedia.org/api/rest_v1/media/math/render/svg/d81a43df2b685ee4142ca9d04ea59c53f79c70fa)

In the special case where _A_ is a [binary variable](https://en.wikipedia.org/wiki/Binary_variable "Binary variable"):

![{\displaystyle P(A|B)={\frac {P(B|A)P(A)}{P(B|A)P(A)+P(B|\neg A)P(\neg A)}}\cdot }](https://wikimedia.org/api/rest_v1/media/math/render/svg/70d6ae9cb8f7cc22d5af309fbea8bf964f6f9808)

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Bayes_continuous_diagram.svg/220px-Bayes_continuous_diagram.svg.png)](https://en.wikipedia.org/wiki/File:Bayes_continuous_diagram.svg)

Bayes' theorem applied to an event space generated by continuous random variables _X_ and _Y_ with known probability distributions. There exists an instance of Bayes' theorem for each point in the [domain](https://en.wikipedia.org/wiki/Domain_of_a_function "Domain of a function"). In practice, these instances might be parametrized by writing the specified probability densities as a [function](https://en.wikipedia.org/wiki/Function_\(Mathematics\) "Function (Mathematics)") of _x_ and _y_.

Consider a [sample space](https://en.wikipedia.org/wiki/Sample_space "Sample space") Ω generated by two [random variables](https://en.wikipedia.org/wiki/Random_variables "Random variables") _X_ and _Y_ with known probability distributions. In principle, Bayes' theorem applies to the events _A_ = {_X_ = _x_} and _B_ = {_Y_ = _y_}.

![{\displaystyle P(X{=}x|Y{=}y)={\frac {P(Y{=}y|X{=}x)P(X{=}x)}{P(Y{=}y)}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/e652899b1dd693a7c06e4979a349e8bb3b1f4ccd)

Terms become 0 at points where either variable has finite [probability density](https://en.wikipedia.org/wiki/Probability_density_function "Probability density function"). To remain useful, Bayes' theorem can be formulated in terms of the relevant densities (see [Derivation](#Derivation)).

If _X_ is continuous and _Y_ is discrete,

![{\displaystyle f_{X|Y{=}y}(x)={\frac {P(Y{=}y|X{=}x)f_{X}(x)}{P(Y{=}y)}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/ca682ab193f9d885b94fc553ec658500f583ff0f)

where each ![{\displaystyle f}](https://wikimedia.org/api/rest_v1/media/math/render/svg/132e57acb643253e7810ee9702d9581f159a1c61) is a density function.

If _X_ is discrete and _Y_ is continuous,

![{\displaystyle P(X{=}x|Y{=}y)={\frac {f_{Y|X{=}x}(y)P(X{=}x)}{f_{Y}(y)}}.}](https://wikimedia.org/api/rest_v1/media/math/render/svg/6a3e9038dc8ae23ef5e5a047d4ec834438e4d7db)

If both _X_ and _Y_ are continuous,

![{\displaystyle f_{X|Y{=}y}(x)={\frac {f_{Y|X{=}x}(y)f_{X}(x)}{f_{Y}(y)}}.}](https://wikimedia.org/api/rest_v1/media/math/render/svg/6121b5d3fd660871d0c9966009251060c01b1ca2)

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Continuous_event_space_specification.svg/220px-Continuous_event_space_specification.svg.png)](https://en.wikipedia.org/wiki/File:Continuous_event_space_specification.svg)

A way to conceptualize event spaces generated by continuous random variables X and Y

A continuous event space is often conceptualized in terms of the numerator terms. It is then useful to eliminate the denominator using the [law of total probability](https://en.wikipedia.org/wiki/Law_of_total_probability "Law of total probability"). For _fY_(_y_), this becomes an integral:

![{\displaystyle f_{Y}(y)=\int _{-\infty }^{\infty }f_{Y|X=\xi }(y)f_{X}(\xi )\,d\xi .}](https://wikimedia.org/api/rest_v1/media/math/render/svg/c054f6c7a58284fe7509507695566db2147c1eca)

### Bayes' rule in odds form

[[edit](https://en.wikipedia.org/w/index.php?title=Bayes%27_theorem&action=edit&section=25 "Edit section: Bayes' rule in odds form")]

Bayes' theorem in [odds form](https://en.wikipedia.org/wiki/Odds "Odds") is:

![{\displaystyle O(A_{1}:A_{2}\vert B)=O(A_{1}:A_{2})\cdot \Lambda (A_{1}:A_{2}\vert B)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/43003aaaecc7b5e8082f6ca9ec5f46b11ccf8131)

where

![{\displaystyle \Lambda (A_{1}:A_{2}\vert B)={\frac {P(B\vert A_{1})}{P(B\vert A_{2})}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f5346e50e43b6fd120f3b595996197fa9b19a4f2)

is called the [Bayes factor](https://en.wikipedia.org/wiki/Bayes_factor "Bayes factor") or [likelihood ratio](https://en.wikipedia.org/wiki/Likelihood_ratio "Likelihood ratio"). The odds between two events is simply the ratio of the probabilities of the two events. Thus:

![{\displaystyle O(A_{1}:A_{2})={\frac {P(A_{1})}{P(A_{2})}},}](https://wikimedia.org/api/rest_v1/media/math/render/svg/27ec7e34df4a353c90415b2d81b55cedc965f4fb)

![{\displaystyle O(A_{1}:A_{2}\vert B)={\frac {P(A_{1}\vert B)}{P(A_{2}\vert B)}},}](https://wikimedia.org/api/rest_v1/media/math/render/svg/094e27ab031562eff2831bdff1e8d4a8ef0881d3)

Thus the rule says that the posterior odds are the prior odds times the [Bayes factor](https://en.wikipedia.org/wiki/Bayes_factor "Bayes factor"); in other words, the posterior is proportional to the prior times the likelihood.

In the special case that ![{\displaystyle A_{1}=A}](https://wikimedia.org/api/rest_v1/media/math/render/svg/952b7ec04f00578d251108fc0f2005054668b154) and ![{\displaystyle A_{2}=\neg A}](https://wikimedia.org/api/rest_v1/media/math/render/svg/9bd2c70de71ad3232ce643decf074f278f294074), one writes ![{\displaystyle O(A)=O(A:\neg A)=P(A)/(1-P(A))}](https://wikimedia.org/api/rest_v1/media/math/render/svg/48966571814a086428e263dab9c8e188c498ee8f), and uses a similar abbreviation for the Bayes factor and for the conditional odds. The odds on ![{\displaystyle A}](https://wikimedia.org/api/rest_v1/media/math/render/svg/7daff47fa58cdfd29dc333def748ff5fa4c923e3) is by definition the odds for and against ![{\displaystyle A}](https://wikimedia.org/api/rest_v1/media/math/render/svg/7daff47fa58cdfd29dc333def748ff5fa4c923e3). Bayes' rule can then be written in the abbreviated form

![{\displaystyle O(A\vert B)=O(A)\cdot \Lambda (A\vert B),}](https://wikimedia.org/api/rest_v1/media/math/render/svg/98415b6ab1886d37e1677eb5407a944e76fe96bc)

or, in words, the posterior odds on ![{\displaystyle A}](https://wikimedia.org/api/rest_v1/media/math/render/svg/7daff47fa58cdfd29dc333def748ff5fa4c923e3) equals the prior odds on ![{\displaystyle A}](https://wikimedia.org/api/rest_v1/media/math/render/svg/7daff47fa58cdfd29dc333def748ff5fa4c923e3) times the likelihood ratio for ![{\displaystyle A}](https://wikimedia.org/api/rest_v1/media/math/render/svg/7daff47fa58cdfd29dc333def748ff5fa4c923e3) given information ![{\displaystyle B}](https://wikimedia.org/api/rest_v1/media/math/render/svg/47136aad860d145f75f3eed3022df827cee94d7a). In short, **posterior odds equals prior odds times likelihood ratio**.

For example, if a medical test has a [sensitivity](https://en.wikipedia.org/wiki/Sensitivity_and_specificity "Sensitivity and specificity") of 90% and a [specificity](https://en.wikipedia.org/wiki/Sensitivity_and_specificity "Sensitivity and specificity") of 91%, then the positive Bayes factor is ![{\displaystyle \Lambda _{+}=P({\text{True Positive}})/P({\text{False Positive}})=90\%/(100\%-91\%)=10}](https://wikimedia.org/api/rest_v1/media/math/render/svg/57341fd6fa26582dd99dbe2cfc938c91d38d52e8). Now, if the [prevalence](https://en.wikipedia.org/wiki/Prevalence "Prevalence") of this disease is 9.09%, and if we take that as the prior probability, then the prior odds is about 1:10. So after receiving a positive test result, the posterior odds of having the disease becomes 1:1, which means that the posterior probability of having the disease is 50%. If a second test is performed in serial testing, and that also turns out to be positive, then the posterior odds of having the disease becomes 10:1, which means a posterior probability of about 90.91%. The negative Bayes factor can be calculated to be 91%/(100%-90%)=9.1, so if the second test turns out to be negative, then the posterior odds of having the disease is 1:9.1, which means a posterior probability of about 9.9%.

The example above can also be understood with more solid numbers: assume the patient taking the test is from a group of 1,000 people, 91 of whom have the disease (prevalence of 9.1%). If all 1,000 take the test, 82 of those with the disease will get a true positive result (sensitivity of 90.1%), 9 of those with the disease will get a false negative result ([false negative rate](https://en.wikipedia.org/wiki/False_positives_and_false_negatives "False positives and false negatives") of 9.9%), 827 of those without the disease will get a true negative result (specificity of 91.0%), and 82 of those without the disease will get a false positive result (false positive rate of 9.0%). Before taking any test, the patient's odds for having the disease is 91:909. After receiving a positive result, the patient's odds for having the disease is

![{\displaystyle {\frac {91}{909}}\times {\frac {90.1\%}{9.0\%}}={\frac {91\times 90.1\%}{909\times 9.0\%}}=1:1}](https://wikimedia.org/api/rest_v1/media/math/render/svg/4d61f98e3125378d18093cedd117646fd8adb757)

which is consistent with the fact that there are 82 true positives and 82 false positives in the group of 1,000.

## Correspondence to other mathematical frameworks

[[edit](https://en.wikipedia.org/w/index.php?title=Bayes%27_theorem&action=edit&section=26 "Edit section: Correspondence to other mathematical frameworks")]

### Propositional logic

[[edit](https://en.wikipedia.org/w/index.php?title=Bayes%27_theorem&action=edit&section=27 "Edit section: Propositional logic")]

Where the [conditional probability](https://en.wikipedia.org/wiki/Conditional_probability "Conditional probability") ![{\displaystyle P(A\vert B)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/8114af1733b7f0ad6aa718629a01264569d689ee) is [defined](https://en.wikipedia.org/wiki/Conditional_probability#Conditioning_on_an_event_of_probability_zero "Conditional probability"), it can be seen to capture the implication ![{\displaystyle B\to A}](https://wikimedia.org/api/rest_v1/media/math/render/svg/9ef7d663f25816b2edf065af9a473eebebeea56a). The probabilistic calculus then mirrors or even generalizes various logical inference rules. Beyond, for example, assigning binary truth values, here one assigns probability values to statements. The assertion ![{\displaystyle B\to A}](https://wikimedia.org/api/rest_v1/media/math/render/svg/9ef7d663f25816b2edf065af9a473eebebeea56a) is captured by the assertion ![{\displaystyle P(A\vert B)=1}](https://wikimedia.org/api/rest_v1/media/math/render/svg/80b22f968be7e9548336c43dcc130483f8108786), i.e. that the conditional probability take the extremal probability value ![{\displaystyle 1}](https://wikimedia.org/api/rest_v1/media/math/render/svg/92d98b82a3778f043108d4e20960a9193df57cbf). Likewise, the assertion of a negation of an implication is captured by the assignment of ![{\displaystyle 0}](https://wikimedia.org/api/rest_v1/media/math/render/svg/2aae8864a3c1fec9585261791a809ddec1489950).[[1]](#cite_note-Jøsang-1) So, for example, if ![{\displaystyle P(A)=1}](https://wikimedia.org/api/rest_v1/media/math/render/svg/5daf997bb6fe750f4568a2d8766e0b65fdb5bfd5), then (if it is defined) ![{\displaystyle P(A\vert B)=1}](https://wikimedia.org/api/rest_v1/media/math/render/svg/80b22f968be7e9548336c43dcc130483f8108786), which entails ![{\displaystyle A\to (B\to A)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/ba8692a5036a11936ef451eadfda6c4039a56249), the [implication introduction](https://en.wikipedia.org/wiki/Implication_introduction "Implication introduction") in logic.

Similarly, as the product of two probabilities equaling ![{\displaystyle 1}](https://wikimedia.org/api/rest_v1/media/math/render/svg/92d98b82a3778f043108d4e20960a9193df57cbf) necessitates that both factors are also ![{\displaystyle 1}](https://wikimedia.org/api/rest_v1/media/math/render/svg/92d98b82a3778f043108d4e20960a9193df57cbf), one finds that Bayes' theorem

![{\displaystyle P(A)\,P(B\vert A)=P(B)\,P(A\vert B)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/4311cb4a7c968aedf80357db3ac98e0276e16062)

entails ![{\displaystyle {\big (}A\land (A\to B){\big )}\leftrightarrow {\big (}B\land (B\to A){\big )}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/817b4567d9f8f3c65e4371f72fe72bc7cef30000), which now also includes [modus ponens](https://en.wikipedia.org/wiki/Modus_ponens "Modus ponens").

For positive values ![{\displaystyle P(A)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/4f264d19e21604793c6dc54f8044df454db82744), if it equals ![{\displaystyle P(B)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/e593d180a26fd68657ea50368dbfe1a661e652aa), then the two conditional probabilities are equal as well, and vice versa. Note that this mirrors the generally valid ![{\displaystyle (A\leftrightarrow B)\leftrightarrow {\big (}(A\to B)\leftrightarrow (B\to A){\big )}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/a431e2a1f46a0ce75c66445209940608b7ead4e7).

On the other hand, reasoning about either of the probabilities equalling ![{\displaystyle 0}](https://wikimedia.org/api/rest_v1/media/math/render/svg/2aae8864a3c1fec9585261791a809ddec1489950) [classically](https://en.wikipedia.org/wiki/Classical_logic "Classical logic") entails the following contrapositive form of the above: ![{\displaystyle {\big (}\neg B\lor \neg (B\to A){\big )}\leftrightarrow {\big (}\neg A\lor \neg (A\to B){\big )}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/cc0e378f03f07f33ba2baa6f85122b7944bf3884).

Bayes' theorem with negated ![{\displaystyle A}](https://wikimedia.org/api/rest_v1/media/math/render/svg/7daff47fa58cdfd29dc333def748ff5fa4c923e3) gives

![{\displaystyle P(B\vert \neg A){\big (}1-P(A){\big )}={\big (}1-P(A\vert B){\big )}P(B)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/4d357102383f64fdef966126e24ba98196cc83dd).

Ruling out the extremal case ![{\displaystyle P(\neg A)=0}](https://wikimedia.org/api/rest_v1/media/math/render/svg/ce47692aae3b7e926813e617ad589b411c8b6f96) (i.e. ![{\displaystyle P(A)=1}](https://wikimedia.org/api/rest_v1/media/math/render/svg/5daf997bb6fe750f4568a2d8766e0b65fdb5bfd5)), one has ![{\displaystyle P(B\vert \neg A)=P(B)\cdot {\tfrac {1-P(A\vert B)}{1-P(A)}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0f56815eb3e08d3e6ddcea47d88736724c40cca5) and in particular

![{\displaystyle P(\neg B\vert \neg A)=1-P(B)\cdot {\frac {1-P(A\vert B)}{1-P(A)}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/51ad529f74367186259168b3598dff02b3d66b5e).

Ruling out also the extremal case ![{\displaystyle P(B)=0}](https://wikimedia.org/api/rest_v1/media/math/render/svg/973532626488736dc14f2ab2add7c09c7b2132ed), one finds they attain the maximum ![{\displaystyle 1}](https://wikimedia.org/api/rest_v1/media/math/render/svg/92d98b82a3778f043108d4e20960a9193df57cbf) simultaneously:

![{\displaystyle P(A\vert B)=1\ \leftrightarrow \ P(\neg B\vert \neg A)=1}](https://wikimedia.org/api/rest_v1/media/math/render/svg/810781d5a4b274fb818f6f44c559d5c469232986)

which (at least when having ruled out [explosive](https://en.wikipedia.org/wiki/Principle_of_explosion "Principle of explosion") antecedents) captures the classical [contraposition](https://en.wikipedia.org/wiki/Contraposition "Contraposition") principle

![{\displaystyle (B\to A)\leftrightarrow (\neg A\to \neg B)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/6f24244d0511a695c78c271934bbf28e3d412414).

Bayes' theorem represents a special case of deriving inverted conditional opinions in [subjective logic](https://en.wikipedia.org/wiki/Subjective_logic "Subjective logic") expressed as:

![{\displaystyle (\omega _{A{\tilde {|}}B}^{S},\omega _{A{\tilde {|}}\lnot B}^{S})=(\omega _{B\vert A}^{S},\omega _{B\vert \lnot A}^{S}){\widetilde {\phi }}a_{A},}](https://wikimedia.org/api/rest_v1/media/math/render/svg/85d582409b20764cfad50fdbab3349aee67cf890)

where ![{\displaystyle {\widetilde {\phi }}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0a0956a6f78314ab8cad802bf8a25d96bdd6260d) denotes the operator for inverting conditional opinions. The argument ![{\displaystyle (\omega _{B\vert A}^{S},\omega _{B\vert \lnot A}^{S})}](https://wikimedia.org/api/rest_v1/media/math/render/svg/edce44ee61014b511a6eefb9e61e73b01562ffb7) denotes a pair of binomial conditional opinions given by source ![{\displaystyle S}](https://wikimedia.org/api/rest_v1/media/math/render/svg/4611d85173cd3b508e67077d4a1252c9c05abca2), and the argument ![{\displaystyle a_{A}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/187a574b62266ad7c236172391d575b150e69bc9) denotes the [prior probability](https://en.wikipedia.org/wiki/Prior_probability "Prior probability") (aka. the [base rate](https://en.wikipedia.org/wiki/Base_rate "Base rate")) of ![{\displaystyle A}](https://wikimedia.org/api/rest_v1/media/math/render/svg/7daff47fa58cdfd29dc333def748ff5fa4c923e3). The pair of derivative inverted conditional opinions is denoted ![{\displaystyle (\omega _{A{\tilde {|}}B}^{S},\omega _{A{\tilde {|}}\lnot B}^{S})}](https://wikimedia.org/api/rest_v1/media/math/render/svg/23590c528bb5f51d2d3b3267d6198fc9759e8780). The conditional opinion ![{\displaystyle \omega _{A\vert B}^{S}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/96b57edc1f26887da5a1420b7a6e3b148cf2a84b) generalizes the probabilistic conditional ![{\displaystyle P(A\vert B)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/8114af1733b7f0ad6aa718629a01264569d689ee), i.e. in addition to assigning a probability the source ![{\displaystyle S}](https://wikimedia.org/api/rest_v1/media/math/render/svg/4611d85173cd3b508e67077d4a1252c9c05abca2) can assign any subjective opinion to the conditional statement ![{\displaystyle (A\vert B)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/116d0c4ede70511eef9e6b0f557ebf89182c7b0f). A binomial subjective opinion ![{\displaystyle \omega _{A}^{S}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/5a3c6ccbb0089282a6eb5949c02d39e3b321d4fc) is the belief in the truth of statement ![{\displaystyle A}](https://wikimedia.org/api/rest_v1/media/math/render/svg/7daff47fa58cdfd29dc333def748ff5fa4c923e3) with degrees of epistemic uncertainty, as expressed by source ![{\displaystyle S}](https://wikimedia.org/api/rest_v1/media/math/render/svg/4611d85173cd3b508e67077d4a1252c9c05abca2). Every subjective opinion has a corresponding projected probability ![{\displaystyle P(\omega _{A}^{S})}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0ad4c1b2a77a99ffde3fd53d5cddcb041ff1fc12). The application of Bayes' theorem to projected probabilities of opinions is a [homomorphism](https://en.wikipedia.org/wiki/Homomorphism "Homomorphism"), meaning that Bayes' theorem can be expressed in terms of projected probabilities of opinions:

![{\displaystyle P(\omega _{A{\tilde {|}}B}^{S})={\frac {P(\omega _{B\vert A}^{S})a(A)}{P(\omega _{B\vert A}^{S})a(A)+P(\omega _{B\vert \lnot A}^{S})a(\lnot A)}}.}](https://wikimedia.org/api/rest_v1/media/math/render/svg/8762fce6aeba91868706061d9c2fbf982bde770e)

Hence, the subjective Bayes' theorem represents a generalization of Bayes' theorem.[[25]](#cite_note-26)

### Bayes theorem for 3 events

[[edit](https://en.wikipedia.org/w/index.php?title=Bayes%27_theorem&action=edit&section=30 "Edit section: Bayes theorem for 3 events")]

A version of Bayes' theorem for 3 events[[26]](#cite_note-koller09-27) results from the addition of a third event ![{\displaystyle C}](https://wikimedia.org/api/rest_v1/media/math/render/svg/4fc55753007cd3c18576f7933f6f089196732029), with ![{\displaystyle P(C)>0,}](https://wikimedia.org/api/rest_v1/media/math/render/svg/3e89c245de57bfca0bce8aec5df7e5e0187c1359) on which all probabilities are conditioned:

![{\displaystyle P(A\vert B\cap C)={\frac {P(B\vert A\cap C)\,P(A\vert C)}{P(B\vert C)}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/7fe5ef441f64d47a36cefb8d534fec2bddd6be8f)

Using the [chain rule](https://en.wikipedia.org/wiki/Chain_rule_\(probability\) "Chain rule (probability)")

![{\displaystyle P(A\cap B\cap C)=P(A\vert B\cap C)\,P(B\vert C)\,P(C)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/03539e57f581052c9cca4cd3e055b87f394264dd)

And, on the other hand

![{\displaystyle P(A\cap B\cap C)=P(B\cap A\cap C)=P(B\vert A\cap C)\,P(A\vert C)\,P(C)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/a2a8c5b795d0388159a0924854246669649f6e0b)

The desired result is obtained by identifying both expressions and solving for ![{\displaystyle P(A\vert B\cap C)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/b0d7bc266b2e4791165a5ef3b0931ee7b542e268).

In genetics, Bayes' rule can be used to estimate the probability that someone has a specific genotype. Many people seek to assess their chances of being affected by a genetic disease or their likelihood of being a carrier for a recessive gene of interest. A Bayesian analysis can be done based on family history or [genetic testing](https://en.wikipedia.org/wiki/Genetic_testing "Genetic testing") to predict whether someone will develop a disease or pass one on to their children. Genetic testing and prediction is common among couples who plan to have children but are concerned that they may both be carriers for a disease, especially in communities with low genetic variance.[[27]](#cite_note-28)

### Using pedigree to calculate probabilities

[[edit](https://en.wikipedia.org/w/index.php?title=Bayes%27_theorem&action=edit&section=33 "Edit section: Using pedigree to calculate probabilities")]

|Hypothesis|Hypothesis 1: Patient is a carrier|Hypothesis 2: Patient is not a carrier|
|---|---|---|
|Prior Probability|1/2|1/2|
|Conditional Probability that all four offspring will be unaffected|(1/2) ⋅ (1/2) ⋅ (1/2) ⋅ (1/2) = 1/16|About 1|
|Joint Probability|(1/2) ⋅ (1/16) = 1/32|(1/2) ⋅ 1 = 1/2|
|Posterior Probability|(1/32) / (1/32 + 1/2) = 1/17|(1/2) / (1/32 + 1/2) = 16/17|

Example of a Bayesian analysis table for a female's risk for a disease based on the knowledge that the disease is present in her siblings but not in her parents or any of her four children. Based solely on the status of the subject's siblings and parents, she is equally likely to be a carrier as to be a non-carrier (this likelihood is denoted by the Prior Hypothesis). The probability that the subject's four sons would all be unaffected is 1/16 (1⁄2⋅1⁄2⋅1⁄2⋅1⁄2) if she is a carrier and about 1 if she is a non-carrier (this is the Conditional Probability). The Joint Probability reconciles these two predictions by multiplying them together. The last line (the Posterior Probability) is calculated by dividing the Joint Probability for each hypothesis by the sum of both joint probabilities.[[28]](#cite_note-Ogino_et_al_2004-29)

### Using genetic test results

[[edit](https://en.wikipedia.org/w/index.php?title=Bayes%27_theorem&action=edit&section=34 "Edit section: Using genetic test results")]

Parental genetic testing can detect around 90% of known disease alleles in parents that can lead to carrier or affected status in their children. Cystic fibrosis is a heritable disease caused by an autosomal recessive mutation on the CFTR gene,[[29]](#cite_note-30) located on the q arm of chromosome 7.[[30]](#cite_note-31)

Here is a Bayesian analysis of a female patient with a family history of cystic fibrosis (CF) who has tested negative for CF, demonstrating how the method was used to determine her risk of having a child born with CF: because the patient is unaffected, she is either homozygous for the wild-type allele, or heterozygous. To establish prior probabilities, a Punnett square is used, based on the knowledge that neither parent was affected by the disease but both could have been carriers:

|Mother<br><br>Father|W<br><br>Homozygous for the wild-  <br>type allele (a non-carrier)|M<br><br>Heterozygous  <br>(a CF carrier)|
|---|---|---|
|W<br><br>Homozygous for the wild-  <br>type allele (a non-carrier)|WW|MW|
|M<br><br>Heterozygous (a CF carrier)|MW|MM<br><br>(affected by cystic fibrosis)|

Given that the patient is unaffected, there are only three possibilities. Within these three, there are two scenarios in which the patient carries the mutant allele. Thus the prior probabilities are 2⁄3 and 1⁄3.

Next, the patient undergoes genetic testing and tests negative for cystic fibrosis. This test has a 90% detection rate, so the conditional probabilities of a negative test are 1/10 and 1. Finally, the joint and posterior probabilities are calculated as before.

|Hypothesis|Hypothesis 1: Patient is a carrier|Hypothesis 2: Patient is not a carrier|
|---|---|---|
|Prior Probability|2/3|1/3|
|Conditional Probability of a negative test|1/10|1|
|Joint Probability|1/15|1/3|
|Posterior Probability|1/6|5/6|

After carrying out the same analysis on the patient's male partner (with a negative test result), the chance that their child is affected is the product of the parents' respective posterior probabilities for being carriers times the chance that two carriers will produce an affected offspring (1⁄4).

### Genetic testing done in parallel with other risk factor identification

[[edit](https://en.wikipedia.org/w/index.php?title=Bayes%27_theorem&action=edit&section=35 "Edit section: Genetic testing done in parallel with other risk factor identification")]

Bayesian analysis can be done using phenotypic information associated with a genetic condition. When combined with genetic testing, this analysis becomes much more complicated. Cystic fibrosis, for example, can be identified in a fetus with an ultrasound looking for an echogenic bowel, one that appears brighter than normal on a scan. This is not a foolproof test, as an echogenic bowel can be present in a perfectly healthy fetus. Parental genetic testing is very influential in this case, where a phenotypic facet can be overly influential in probability calculation. In the case of a fetus with an echogenic bowel, with a mother who has been tested and is known to be a CF carrier, the posterior probability that the fetus has the disease is very high (0.64). But once the father has tested negative for CF, the posterior probability drops significantly (to 0.16).[[28]](#cite_note-Ogino_et_al_2004-29)

Risk factor calculation is a powerful tool in genetic counseling and reproductive planning but cannot be treated as the only important factor. As above, incomplete testing can yield falsely high probability of carrier status, and testing can be financially inaccessible or unfeasible when a parent is not present.

- [Bayesian epistemology](https://en.wikipedia.org/wiki/Bayesian_epistemology "Bayesian epistemology")
- [Inductive probability](https://en.wikipedia.org/wiki/Inductive_probability "Inductive probability")
- [Quantum Bayesianism](https://en.wikipedia.org/wiki/Quantum_Bayesianism "Quantum Bayesianism")
- _[Why Most Published Research Findings Are False](https://en.wikipedia.org/wiki/Why_Most_Published_Research_Findings_Are_False "Why Most Published Research Findings Are False")_, a 2005 essay in [metascience](https://en.wikipedia.org/wiki/Metascience "Metascience") by John Ioannidis
- [Regular conditional probability](https://en.wikipedia.org/wiki/Regular_conditional_probability "Regular conditional probability")
- [Bayesian persuasion](https://en.wikipedia.org/wiki/Bayesian_persuasion "Bayesian persuasion")

1. **[^](#cite_ref-8 "Jump up")** Laplace refined Bayes's theorem over a period of decades:
    
    - Laplace announced his independent discovery of Bayes' theorem in: Laplace (1774) "Mémoire sur la probabilité des causes par les événements", "Mémoires de l'Académie royale des Sciences de MI (Savants étrangers)", **4**: 621–656. Reprinted in: Laplace, "Oeuvres complètes" (Paris, France: Gauthier-Villars et fils, 1841), vol. 8, pp. 27–65. Available on-line at: [Gallica](http://gallica.bnf.fr/ark:/12148/bpt6k77596b/f32.image). Bayes' theorem appears on p. 29.
    - Laplace presented a refinement of Bayes' theorem in: Laplace (read: 1783 / published: 1785) "Mémoire sur les approximations des formules qui sont fonctions de très grands nombres", "Mémoires de l'Académie royale des Sciences de Paris", 423–467. Reprinted in: Laplace, "Oeuvres complètes" (Paris, France: Gauthier-Villars et fils, 1844), vol. 10, pp. 295–338. Available on-line at: [Gallica](http://gallica.bnf.fr/ark:/12148/bpt6k775981/f218.image.langEN). Bayes' theorem is stated on page 301.
    - See also: Laplace, "Essai philosophique sur les probabilités" (Paris, France: Mme. Ve. Courcier [Madame veuve (i.e., widow) Courcier], 1814), [page 10](https://books.google.com/books?id=rDUJAAAAIAAJ&pg=PA10). English translation: Pierre Simon, Marquis de Laplace with F. W. Truscott and F. L. Emory, trans., "A Philosophical Essay on Probabilities" (New York, New York: John Wiley & Sons, 1902), [p. 15](https://google.com/books?id=WxoPAAAAIAAJ&pg=PA15#v=onepage).
    

1. ^ [Jump up to: _**a**_](#cite_ref-Jøsang_1-0) [_**b**_](#cite_ref-Jøsang_1-1) Audun Jøsang, 2016, _Subjective Logic; A formalism for Reasoning Under Uncertainty._ Springer, Cham, [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-3-319-42337-1](https://en.wikipedia.org/wiki/Special:BookSources/978-3-319-42337-1 "Special:BookSources/978-3-319-42337-1")
2. **[^](#cite_ref-Liberty's_Apostle_2-0 "Jump up")** Frame, Paul (2015). [_Liberty's Apostle_](https://www.uwp.co.uk/book/libertys-apostle-richard-price-his-life-and-times/). Wales: University of Wales Press. p. 44. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-1783162161](https://en.wikipedia.org/wiki/Special:BookSources/978-1783162161 "Special:BookSources/978-1783162161"). Retrieved 23 February 2021.
3. **[^](#cite_ref-3 "Jump up")** Allen, Richard (1999). [_David Hartley on Human Nature_](https://books.google.com/books?id=NCu6HhGlAB8C&pg=PA243). SUNY Press. pp. 243–244. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0791494516](https://en.wikipedia.org/wiki/Special:BookSources/978-0791494516 "Special:BookSources/978-0791494516"). Retrieved 16 June 2013.
4. **[^](#cite_ref-Price1763_4-0 "Jump up")** Bayes, Thomas & Price, Richard (1763). ["An Essay towards solving a Problem in the Doctrine of Chance. By the late Rev. Mr. Bayes, communicated by Mr. Price, in a letter to John Canton, A.M.F.R.S."](https://doi.org/10.1098%2Frstl.1763.0053) _Philosophical Transactions of the Royal Society of London_. **53**: 370–418. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1098/rstl.1763.0053](https://doi.org/10.1098%2Frstl.1763.0053).
5. **[^](#cite_ref-Holland46_5-0 "Jump up")** Holland, pp. 46–7.
6. **[^](#cite_ref-6 "Jump up")** Price, Richard (1991). [_Price: Political Writings_](https://books.google.com/books?id=xdH-gjy2vzUC&pg=PR23). Cambridge University Press. p. xxiii. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0521409698](https://en.wikipedia.org/wiki/Special:BookSources/978-0521409698 "Special:BookSources/978-0521409698"). Retrieved 16 June 2013.
7. **[^](#cite_ref-EB1911_7-0 "Jump up")** [Mitchell 1911](#CITEREFMitchell1911), p. 314.
8. **[^](#cite_ref-9 "Jump up")** Daston, Lorraine (1988). [_Classical Probability in the Enlightenment_](https://books.google.com/books?id=oq8XNbKyUewC&pg=PA268). Princeton Univ Press. p. 268. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [0691084971](https://en.wikipedia.org/wiki/Special:BookSources/0691084971 "Special:BookSources/0691084971").
9. **[^](#cite_ref-10 "Jump up")** Stigler, Stephen M. (1986). ["Inverse Probability"](https://books.google.com/books?id=M7yvkERHIIMC&pg=PA99). _The History of Statistics: The Measurement of Uncertainty Before 1900_. Harvard University Press. pp. 99–138. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0674403413](https://en.wikipedia.org/wiki/Special:BookSources/978-0674403413 "Special:BookSources/978-0674403413").
10. **[^](#cite_ref-Jeffreys1973_11-0 "Jump up")** [Jeffreys, Harold](https://en.wikipedia.org/wiki/Harold_Jeffreys "Harold Jeffreys") (1973). [_Scientific Inference_](https://archive.org/details/scientificinfere0000jeff) (3rd ed.). [Cambridge University Press](https://en.wikipedia.org/wiki/Cambridge_University_Press "Cambridge University Press"). p. [31](https://archive.org/details/scientificinfere0000jeff/page/31). [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0521180788](https://en.wikipedia.org/wiki/Special:BookSources/978-0521180788 "Special:BookSources/978-0521180788").
11. **[^](#cite_ref-12 "Jump up")** Stigler, Stephen M. (1983). "Who Discovered Bayes' Theorem?". _The American Statistician_. **37** (4): 290–296. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1080/00031305.1983.10483122](https://doi.org/10.1080%2F00031305.1983.10483122).
12. **[^](#cite_ref-Stats,_Data_and_Models_13-0 "Jump up")** de Vaux, Richard; Velleman, Paul; Bock, David (2016). _Stats, Data and Models_ (4th ed.). Pearson. pp. 380–381. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0321986498](https://en.wikipedia.org/wiki/Special:BookSources/978-0321986498 "Special:BookSources/978-0321986498").
13. **[^](#cite_ref-14 "Jump up")** Edwards, A. W. F. (1986). "Is the Reference in Hartley (1749) to Bayesian Inference?". _The American Statistician_. **40** (2): 109–110. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1080/00031305.1986.10475370](https://doi.org/10.1080%2F00031305.1986.10475370).
14. **[^](#cite_ref-15 "Jump up")** Hooper, Martyn (2013). ["Richard Price, Bayes' theorem, and God"](https://doi.org/10.1111%2Fj.1740-9713.2013.00638.x). _Significance_. **10** (1): 36–39. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1111/j.1740-9713.2013.00638.x](https://doi.org/10.1111%2Fj.1740-9713.2013.00638.x). [S2CID](https://en.wikipedia.org/wiki/S2CID_\(identifier\) "S2CID (identifier)") [153704746](https://api.semanticscholar.org/CorpusID:153704746).
15. ^ [Jump up to: _**a**_](#cite_ref-mcgrayne2011theory_16-0) [_**b**_](#cite_ref-mcgrayne2011theory_16-1) McGrayne, S. B. (2011). [_The Theory That Would Not Die: How Bayes' Rule Cracked the Enigma Code, Hunted Down Russian Submarines & Emerged Triumphant from Two Centuries of Controversy_](https://archive.org/details/theorythatwouldn0000mcgr). [Yale University Press](https://en.wikipedia.org/wiki/Yale_University_Press "Yale University Press"). [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0300188226](https://en.wikipedia.org/wiki/Special:BookSources/978-0300188226 "Special:BookSources/978-0300188226").
16. **[^](#cite_ref-17 "Jump up")** Bruss, F. Thomas (2014). "250 years of "An essay towards solving a problem in the doctrine of chances" communicated by Price to the Royal Society". _Jahresbericht der deutschen Mathematiker-Vereinigung_. **115** (3): 129–133.
17. **[^](#cite_ref-18 "Jump up")** Stuart, A.; Ord, K. (1994), _Kendall's Advanced Theory of Statistics: Volume I – Distribution Theory_, [Edward Arnold](https://en.wikipedia.org/wiki/Edward_Arnold_\(publisher\) "Edward Arnold (publisher)"), §8.7
18. **[^](#cite_ref-19 "Jump up")** Kolmogorov, A.N. (1933) [1956]. _Foundations of the Theory of Probability_. Chelsea Publishing Company.
19. **[^](#cite_ref-20 "Jump up")** Tjur, Tue (1980). [_Probability based on Radon measures_](http://archive.org/details/probabilitybased0000tjur). New York: Wiley. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-471-27824-5](https://en.wikipedia.org/wiki/Special:BookSources/978-0-471-27824-5 "Special:BookSources/978-0-471-27824-5").
20. **[^](#cite_ref-21 "Jump up")** Taraldsen, Gunnar; Tufto, Jarle; Lindqvist, Bo H. (2021-07-24). ["Improper priors and improper posteriors"](https://doi.org/10.1111%2Fsjos.12550). _Scandinavian Journal of Statistics_. **49** (3): 969–991. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1111/sjos.12550](https://doi.org/10.1111%2Fsjos.12550). [hdl](https://en.wikipedia.org/wiki/Hdl_\(identifier\) "Hdl (identifier)"):[11250/2984409](https://hdl.handle.net/11250%2F2984409). [ISSN](https://en.wikipedia.org/wiki/ISSN_\(identifier\) "ISSN (identifier)") [0303-6898](https://search.worldcat.org/issn/0303-6898). [S2CID](https://en.wikipedia.org/wiki/S2CID_\(identifier\) "S2CID (identifier)") [237736986](https://api.semanticscholar.org/CorpusID:237736986).
21. **[^](#cite_ref-22 "Jump up")** Robert, Christian P.; Casella, George (2004). [_Monte Carlo Statistical Methods_](http://worldcat.org/oclc/1159112760). Springer. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-1475741452](https://en.wikipedia.org/wiki/Special:BookSources/978-1475741452 "Special:BookSources/978-1475741452"). [OCLC](https://en.wikipedia.org/wiki/OCLC_\(identifier\) "OCLC (identifier)") [1159112760](https://search.worldcat.org/oclc/1159112760).
22. **[^](#cite_ref-23 "Jump up")** Lee, Peter M. (2012). ["Chapter 1"](http://www-users.york.ac.uk/~pml1/bayes/book.htm). _Bayesian Statistics_. [Wiley](https://en.wikipedia.org/wiki/John_Wiley_%26_Sons "John Wiley & Sons"). [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-1-1183-3257-3](https://en.wikipedia.org/wiki/Special:BookSources/978-1-1183-3257-3 "Special:BookSources/978-1-1183-3257-3").
23. **[^](#cite_ref-24 "Jump up")** ["Bayes' Theorem: Introduction"](https://web.archive.org/web/20040821012342/http://www.trinity.edu/cbrown/bayesweb/). _Trinity University_. Archived from [the original](http://www.trinity.edu/cbrown/bayesweb/) on 21 August 2004. Retrieved 5 August 2014.
24. **[^](#cite_ref-25 "Jump up")** ["Bayes Theorem - Formula, Statement, Proof | Bayes Rule"](https://www.cuemath.com/data/bayes-theorem/). _Cuemath_. Retrieved 2023-10-20.
25. **[^](#cite_ref-26 "Jump up")** Audun Jøsang, 2016, _[Generalising Bayes' Theorem in Subjective Logic](http://folk.uio.no/josang/papers/Josang2016-MFI.pdf)._ IEEE International Conference on Multisensor Fusion and Integration for Intelligent Systems (MFI 2016), Baden-Baden, September 2016
26. **[^](#cite_ref-koller09_27-0 "Jump up")** [Koller, D.](https://en.wikipedia.org/wiki/Daphne_Koller "Daphne Koller"); [Friedman, N.](https://en.wikipedia.org/wiki/Nir_Friedman "Nir Friedman") (2009). [_Probabilistic Graphical Models_](https://web.archive.org/web/20140427083249/http://pgm.stanford.edu/). Massachusetts: MIT Press. p. 1208. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-262-01319-2](https://en.wikipedia.org/wiki/Special:BookSources/978-0-262-01319-2 "Special:BookSources/978-0-262-01319-2"). Archived from [the original](http://pgm.stanford.edu/) on 2014-04-27.
27. **[^](#cite_ref-28 "Jump up")** Kraft, Stephanie A; Duenas, Devan; Wilfond, Benjamin S; [Goddard, Katrina AB](https://en.wikipedia.org/wiki/Katrina_A._B._Goddard "Katrina A. B. Goddard") (24 September 2018). ["The evolving landscape of expanded carrier screening: challenges and opportunities"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6752283). _[Genetics in Medicine](https://en.wikipedia.org/wiki/Genetics_in_Medicine "Genetics in Medicine")_. **21** (4): 790–797. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1038/s41436-018-0273-4](https://doi.org/10.1038%2Fs41436-018-0273-4). [PMC](https://en.wikipedia.org/wiki/PMC_\(identifier\) "PMC (identifier)") [6752283](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6752283). [PMID](https://en.wikipedia.org/wiki/PMID_\(identifier\) "PMID (identifier)") [30245516](https://pubmed.ncbi.nlm.nih.gov/30245516).
28. ^ [Jump up to: _**a**_](#cite_ref-Ogino_et_al_2004_29-0) [_**b**_](#cite_ref-Ogino_et_al_2004_29-1) Ogino, Shuji; Wilson, Robert B; Gold, Bert; Hawley, Pamela; Grody, Wayne W (October 2004). ["Bayesian analysis for cystic fibrosis risks in prenatal and carrier screening"](https://doi.org/10.1097%2F01.GIM.0000139511.83336.8F). _Genetics in Medicine_. **6** (5): 439–449. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1097/01.GIM.0000139511.83336.8F](https://doi.org/10.1097%2F01.GIM.0000139511.83336.8F). [PMID](https://en.wikipedia.org/wiki/PMID_\(identifier\) "PMID (identifier)") [15371910](https://pubmed.ncbi.nlm.nih.gov/15371910).
29. **[^](#cite_ref-30 "Jump up")** "Types of CFTR Mutations". Cystic Fibrosis Foundation, www.cff.org/What-is-CF/Genetics/Types-of-CFTR-Mutations/.
30. **[^](#cite_ref-31 "Jump up")** "CFTR Gene – Genetics Home Reference". U.S. National Library of Medicine, National Institutes of Health, ghr.nlm.nih.gov/gene/CFTR#location.

-  ![](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Wikisource-logo.svg/12px-Wikisource-logo.svg.png)This article incorporates text from a publication now in the [public domain](https://en.wikipedia.org/wiki/Public_domain "Public domain"): Mitchell, John Malcolm (1911). "[Price, Richard](https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Price,_Richard "s:1911 Encyclopædia Britannica/Price, Richard")". In [Chisholm, Hugh](https://en.wikipedia.org/wiki/Hugh_Chisholm "Hugh Chisholm") (ed.). _[Encyclopædia Britannica](https://en.wikipedia.org/wiki/Encyclop%C3%A6dia_Britannica_Eleventh_Edition "Encyclopædia Britannica Eleventh Edition")_. Vol. 22 (11th ed.). Cambridge University Press. pp. 314–315.

- Bolstad, William M.; Curran, James M. (2017). "Logic, Probability, and Uncertainty". _Introduction to Bayesian Statistics_ (3rd ed.). New York: Wiley. pp. 59–82. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-1-118-09156-2](https://en.wikipedia.org/wiki/Special:BookSources/978-1-118-09156-2 "Special:BookSources/978-1-118-09156-2").
- Lee, Peter M. (2012). _Bayesian Statistics: An Introduction_ (4th ed.). Wiley. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-1-118-33257-3](https://en.wikipedia.org/wiki/Special:BookSources/978-1-118-33257-3 "Special:BookSources/978-1-118-33257-3").
- Schmitt, Samuel A. (1969). "Accumulating Evidence". _Measuring Uncertainty : An Elementary Introduction to Bayesian Statistics_. Reading: Addison-Wesley. pp. 61–99. [OCLC](https://en.wikipedia.org/wiki/OCLC_\(identifier\) "OCLC (identifier)") [5013](https://search.worldcat.org/oclc/5013).
- Stigler, Stephen M. (August 1986). ["Laplace's 1774 Memoir on Inverse Probability"](https://doi.org/10.1214%2Fss%2F1177013620). _Statistical Science_. **1** (3): 359–363. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1214/ss/1177013620](https://doi.org/10.1214%2Fss%2F1177013620).

- ["The Bayesian Trap"](https://www.youtube.com/watch?v=R13BD8qKeTg). _[Veritasium](https://en.wikipedia.org/wiki/Veritasium "Veritasium")_. April 5, 2017 – via [YouTube](https://en.wikipedia.org/wiki/YouTube "YouTube").