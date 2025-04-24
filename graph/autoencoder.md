---
subclass of:
  - "[[Artificial neural network]]"
facet of:
  - "[[deep learning]]"
  - "[[unsupervised learning]]"
---
![Autoencoder Thumbnail](https://upload.wikimedia.org/wikipedia/commons/3/37/Autoencoder_schema.png)
[Autoencoder](https://en.wikipedia.org/wiki/Autoencoder)

An autoencoder is a type of artificial neural network used to learn efficient codings of unlabeled data (unsupervised learning). An autoencoder learns two functions: an encoding function that transforms the input data, and a decoding function that recreates the input data from the encoded representation. The autoencoder learns an efficient representation (encoding) for a set of data, typically for dimensionality reduction, to generate lower-dimensional embeddings for subsequent use by other machine learning algorithms.

Variants exist which aim to make the learned representations assume useful properties. Examples are regularized autoencoders (sparse, denoising and contractive autoencoders), which are effective in learning representations for subsequent classification tasks, and variational autoencoders, which can be used as generative models. Autoencoders are applied to many problems, including facial recognition, feature detection, anomaly detection, and learning the meaning of words. In terms of data synthesis, autoencoders can also be used to randomly generate new data that is similar to the input (training) data.