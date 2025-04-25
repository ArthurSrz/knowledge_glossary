---
includes: "[[Neural network models]]"
uses: "[[Algorithm]]"
trainedWith: "[[Training data set]]"
evaluatedBy: "[[Evaluation metrics]]"
deployedIn: "[[ML system]]"
---

# ML Models

Machine Learning models are mathematical representations that learn patterns from data to make predictions or decisions without being explicitly programmed. They form the core of any machine learning system, transforming inputs into desired outputs based on learned patterns.

## Categories of ML Models

### By Learning Type
1. **Supervised Learning Models**
   - Classification models (predict categories)
   - Regression models (predict continuous values)
   - Examples: [[Linear regression models]], [[Decision tree]], [[Support Vector Machine]]

2. **Unsupervised Learning Models**
   - Clustering models (group similar data)
   - Dimensionality reduction models (reduce feature space)
   - Examples: [[K-Means Clustering]], [[Principal Component Analysis]]

3. **Reinforcement Learning Models**
   - Policy-based models
   - Value-based models
   - Actor-critic models

### By Architecture
1. **Traditional ML Models**
   - Linear models
   - Tree-based models
   - Instance-based models
   - Bayesian models

2. **Deep Learning Models**
   - [[Neural network models]]
   - [[Convolutional neural networks]]
   - [[Transformers]]
   - [[Autoencoder]]

## Model Selection Criteria

1. **Problem Complexity**: Match model complexity to problem requirements
2. **Data Availability**: Consider volume and quality of training data
3. **Interpretability**: Balance between accuracy and explainability
4. **Computational Resources**: Consider training and inference costs
5. **Deployment Requirements**: Real-time vs batch processing needs

## Model Lifecycle

1. **Development**: Creating and training the model
2. **Validation**: Testing model performance
3. **Deployment**: Integrating into production systems
4. **Monitoring**: Tracking model performance over time
5. **Maintenance**: Updating and retraining as needed

## Challenges

- **Overfitting**: Models memorizing rather than generalizing
- **Underfitting**: Models too simple to capture patterns
- **Concept drift**: Changing data distributions over time
- **Model bias**: Systemic errors in predictions
- **Scalability**: Handling increasing data volumes

See also: [[Model selection]], [[Model tuning]], [[Model evaluation]], [[Model deployment]]
