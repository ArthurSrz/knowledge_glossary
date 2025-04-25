---
foundationalPaper: "A Method of Solving a System of Linear Equations through Optimization (Cauchy, 1847)"
keyPapers: ["An Overview of Gradient Descent Optimization Algorithms (Ruder, 2016)", "Adam: A Method for Stochastic Optimization (Kingma & Ba, 2014)", "On the Convergence of Adam and Beyond (Reddi et al., 2018)"]
examples: ["[[Gradient descent]]", "[[Stochastic gradient descent]]", "[[Adam]]", "[[RMSprop]]", "[[AdaGrad]]"]
optimizes: "[[Loss function]]"
updates: "[[Model parameters]]"
uses: ["[[Gradient]]", "[[Learning rate]]", "[[Momentum]]"]
---

# Optimizer Algorithm

Optimizer algorithms evolved from classical optimization theory to specialized methods for training neural networks.

## Historical Origins

From Cauchy (1847) on steepest descent:
"Pour trouver le minimum d'une fonction, il faut se déplacer dans la direction opposée au gradient."
("To find the minimum of a function, one must move in the direction opposite to the gradient.")

Modern definition (Goodfellow et al., 2016):
"An optimization algorithm determines how the learning algorithm will update the model parameters to minimize the loss function."

## Evolution of Optimizers

### 1. Gradient Descent (1847)
Cauchy's method:
θₜ₊₁ = θₜ - η∇f(θₜ)

### 2. Stochastic Gradient Descent (1951)
Robbins & Monro:
θₜ₊₁ = θₜ - ηₜ∇f(θₜ; xᵢ, yᵢ)

### 3. Momentum (1964)
Polyak:
vₜ = γvₜ₋₁ + η∇f(θₜ)
θₜ₊₁ = θₜ - vₜ

### 4. Adaptive Methods (2011+)
- AdaGrad (Duchi et al., 2011)
- RMSprop (Hinton, 2012)
- Adam (Kingma & Ba, 2014)

## Key Components

1. **Gradient Computation**: ∇f(θ)
2. **Learning Rate**: η
3. **Update Rule**: θₜ₊₁ = θₜ + Δθ
4. **Adaptive Mechanisms**: Per-parameter learning rates
5. **Momentum Terms**: Acceleration in consistent directions

## Modern Optimizers

### Adam (Kingma & Ba, 2014)
"Adam can be seen as a combination of RMSprop and momentum":
mₜ = β₁mₜ₋₁ + (1-β₁)gₜ
vₜ = β₂vₜ₋₁ + (1-β₂)gₜ²
m̂ₜ = mₜ/(1-β₁ᵗ)
v̂ₜ = vₜ/(1-β₂ᵗ)
θₜ₊₁ = θₜ - η·m̂ₜ/√(v̂ₜ + ε)

### RMSprop (Hinton, 2012)
vₜ = βvₜ₋₁ + (1-β)gₜ²
θₜ₊₁ = θₜ - η·gₜ/√(vₜ + ε)

## Design Principles

From Ruder (2016):
1. **Adaptive Learning Rates**: Adjust per parameter
2. **Momentum**: Accelerate in consistent directions
3. **Second-Order Information**: Approximate Hessian
4. **Noise Reduction**: Handle stochastic gradients
5. **Convergence Guarantees**: Theoretical properties

## Challenges and Solutions

### Convergence Issues
- Non-convex optimization
- Saddle points
- Local minima

### Solutions
- Momentum to escape saddle points
- Adaptive rates for different scales
- Warm-up and decay schedules
- Gradient clipping for stability

## Historical Significance

Optimizer evolution shows:
- Progress from theory to practice
- Importance of empirical validation
- Balance between simplicity and effectiveness
- Adaptation to deep learning challenges

As Ruder noted: "The choice of optimization algorithm can make the difference between getting state-of-the-art results in hours or days, or not converging at all."

## Modern Developments

- AdamW (decoupled weight decay)
- RAdam (rectified Adam)
- LAMB (layer-wise adaptive moments)
- Sharpness-aware minimization (SAM)
- Optimizers for large language models
