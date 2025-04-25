---
foundationalPaper: "Quantization Noise (Bennett, 1948)"
keyPapers: ["BinaryConnect: Training Deep Neural Networks with Binary Weights (Courbariaux et al., 2015)", "Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference (Jacob et al., 2018)", "Deep Compression: Compressing Deep Neural Networks with Pruning, Trained Quantization and Huffman Coding (Han et al., 2016)"]
applies_to: ["[[Neural network models]]", "[[Deep learning]]", "[[Edge AI]]"]
enables: ["[[Model compression]]", "[[Efficient inference]]", "[[Mobile deployment]]"]
techniques: ["[[Post-training quantization]]", "[[Quantization-aware training]]", "[[Mixed precision]]"]
---

# Quantization

Quantization in machine learning adapts the signal processing concept to reduce the numerical precision of model parameters and computations.

## Original Definition

From Bennett (1948) on signal quantization:
"The quantization process consists of replacing a continuous range of values by a finite set of discrete values... The quantization error is the difference between the actual signal and its quantized approximation."

In neural networks (Jacob et al., 2018):
"Quantization refers to techniques for performing computations and storing tensors at lower bitwidths than floating point precision."

## Historical Development

1. **Signal Processing Era (1948)**: Bennett's quantization theory
2. **Digital Systems (1960s)**: Fixed-point arithmetic
3. **Neural Network Compression (2015+)**: Binary and low-precision networks
4. **Production Deployment (2018+)**: Standardized quantization methods

## Types of Quantization

### Post-training Quantization
From Jacob et al. (2018):
"Quantize weights and activations of a pre-trained floating-point model without requiring retraining."

### Quantization-aware Training
From Courbariaux et al. (2015):
"Train the network with quantization in the forward pass, but use full precision gradients in the backward pass."

## Mathematical Formulation

Uniform quantization:
Q(x) = round(x/s) × s

Where:
- x is the original value
- s is the scale factor
- Q(x) is the quantized value

For mapping to integers:
q = round(x/s) + z

Where z is the zero-point for asymmetric quantization.

## Quantization Schemes

### Weight Quantization
- Float32 → Int8/Int4/Binary
- Symmetric or asymmetric
- Per-tensor or per-channel

### Activation Quantization
- Dynamic range consideration
- Calibration requirements
- Runtime quantization

## Key Insights

From Han et al. (2016):
"Deep neural networks have significant redundancy and can be compressed by 10-50x through quantization without significant loss in accuracy."

From Jacob et al. (2018):
"8-bit quantization offers a good balance between model size reduction, inference speedup, and accuracy preservation."

## Benefits and Trade-offs

### Benefits
1. **Size Reduction**: 4x for FP32→INT8
2. **Speed Improvement**: Faster integer arithmetic
3. **Power Efficiency**: Lower memory bandwidth
4. **Hardware Compatibility**: Integer-only accelerators

### Trade-offs
1. **Accuracy Loss**: Quantization noise
2. **Implementation Complexity**: Calibration requirements
3. **Training Challenges**: Gradient quantization issues

## Modern Applications

1. **Mobile Deployment**: TensorFlow Lite, PyTorch Mobile
2. **Edge Devices**: IoT, embedded systems
3. **Cloud Inference**: Throughput optimization
4. **Model Serving**: Reduced memory footprint

## Quantization Techniques

### Binary Neural Networks (BNNs)
Weights and activations constrained to {-1, +1}

### Ternary Networks
Weights in {-1, 0, +1}

### Mixed Precision
Different bitwidths for different layers

## Historical Significance

Quantization enabled:
- Deployment of deep learning on edge devices
- Efficient inference in production
- Democratization of AI applications
- Hardware-software co-design advances

As Jacob et al. noted: "Quantization is becoming a standard tool for deploying neural networks on platforms with limited computational resources."
