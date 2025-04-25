---
usedIn: "[[Neural network models]]"
enables: "[[Gradient descent]]"
computesWith: "[[Chain rule]]"
trainsBy: "[[Loss function]]"
implements: "[[Error propagation]]"
updates: "[[Weights]]"
---

# Backpropagation

Backpropagation (backward propagation of errors) is a fundamental algorithm for training artificial neural networks. First introduced by Rumelhart, Hinton, and Williams in their seminal 1986 Nature paper "Learning representations by back-propagating errors", it revolutionized deep learning by providing an efficient method to compute gradients.

## Definition

Backpropagation is a gradient estimation method that computes the gradient of a loss function with respect to each weight in the network by propagating errors backward from output to input layers using the chain rule of calculus.

## How It Works

1. **Forward Pass**: Input data flows through the network to produce an output
2. **Error Calculation**: Compare network output with desired output using a loss function
3. **Backward Pass**: Propagate error backward through layers, computing gradients
4. **Weight Update**: Adjust weights to minimize the error using gradient descent

## Mathematical Foundation

The algorithm applies the chain rule to efficiently compute partial derivatives:

∂L/∂w = ∂L/∂a × ∂a/∂z × ∂z/∂w

Where:
- L is the loss function
- a is the activation
- z is the weighted sum
- w is the weight

## Key Features

- **Efficiency**: Computes all gradients in one backward pass
- **Generality**: Works with various network architectures
- **Parallelization**: Can compute gradients for mini-batches simultaneously
- **Automatic Differentiation**: Foundation for modern deep learning frameworks

## Historical Significance

The 1986 paper by Rumelhart, Hinton, and Williams demonstrated that backpropagation could train multi-layer networks to learn internal representations, solving the credit assignment problem that had limited neural networks for decades.

## Applications

- Training deep neural networks
- Supervised learning tasks
- Optimization of complex models
- Feature learning
- Representation learning

## Challenges

- Vanishing gradients in deep networks
- Computational intensity for large networks
- Potential for getting stuck in local minima
- Requires differentiable activation functions

See also: [[Gradient descent]], [[Neural network models]], [[Deep learning]], [[Chain rule]], [[Loss function]]
