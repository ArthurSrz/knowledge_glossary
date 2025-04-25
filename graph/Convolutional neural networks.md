---
foundationalPaper: "Gradient-Based Learning Applied to Document Recognition (LeCun et al., 1998)"
keyPapers: ["Neocognitron: A Self-organizing Neural Network Model (Fukushima, 1980)", "Backpropagation Applied to Handwritten Zip Code Recognition (LeCun et al., 1989)"]
typeOf: "[[Neural network models]]"
usedIn: ["[[Computer vision]]", "[[Image classification]]", "[[Object detection]]"]
consistsOf: ["[[Convolutional layers]]", "[[Pooling layers]]", "[[Fully connected layers]]"]
inspiredBy: ["[[Visual cortex]]", "[[Receptive fields]]"]
---

# Convolutional Neural Networks (CNNs)

Convolutional Neural Networks were first introduced by Kunihiko Fukushima in 1980 with the Neocognitron, but gained widespread recognition through Yann LeCun's work in the late 1980s and 1990s.

## Original Definition

From LeCun et al. (1998) in "Gradient-Based Learning Applied to Document Recognition":
"Convolutional Networks are designed to recognize visual patterns directly from pixel images with minimal preprocessing. They can recognize patterns with extreme variability (such as handwritten characters), and with robustness to distortions and simple geometric transformations."

## Historical Development

1. **Neocognitron (Fukushima, 1980)**: First introduced the key concepts of local receptive fields and hierarchical feature extraction, inspired by Hubel and Wiesel's discoveries about the visual cortex.

2. **LeNet (LeCun et al., 1989)**: First practical implementation using backpropagation for training, demonstrating success on handwritten digit recognition.

3. **LeNet-5 (LeCun et al., 1998)**: The architecture that established the standard CNN structure with alternating convolutional and pooling layers.

## Key Principles

As defined in the original papers:
- **Local Connectivity**: Neurons connect only to a local region of the input
- **Shared Weights**: The same filter is applied across the entire input
- **Spatial Hierarchies**: Features are built from simple to complex through layers
- **Translation Invariance**: Recognition is robust to position changes

From LeCun et al.: "The network extracts features at all locations on the input, and combines them to form higher-order features. The architecture ensures some degree of shift, scale, and distortion invariance."

## Architecture Components

1. **Convolutional layers**: Apply learnable filters to extract features
2. **Pooling layers**: Reduce spatial dimensions and provide invariance
3. **Fully connected layers**: Perform classification based on extracted features

The foundational insight was that by constraining the network architecture to reflect the structure of visual data, CNNs could learn more efficiently and effectively than fully connected networks.
