# Classification

## Definition

Classification is the process of identifying to which of a set of categories (sub-populations) a new observation belongs, based on a training set of data containing observations whose category membership is known.

## Historical Development

1. **Landmark Paper (1936)**: R.A. Fisher published "The Use of Multiple Measurements in Taxonomic Problems" in Annals of Eugenics, introducing discriminant analysis

2. **Iris Dataset (1936)**: Fisher used his now-famous iris dataset to demonstrate classification methods

3. **Linear Discriminant Analysis**: Fisher established the mathematical foundation for classification problems

## Key Concepts from Fisher (1936)

1. **Discriminant Function**: A linear combination of features that maximally separates classes
2. **Multiple Measurements**: Using several features to improve classification accuracy
3. **Taxonomic Problems**: Originally applied to biological species classification
4. **Maximum Likelihood**: Basis for determining class membership

## Fisher's Original Framework

According to Fisher:
- Classification uses multiple measurements to maximize separation between groups
- The discriminant function is the linear compound that maximizes the ratio of between-class to within-class variance
- Probabilities of misclassification can be computed

## Types of Classification

1. **Binary Classification**: Two classes
2. **Multiclass Classification**: More than two classes
3. **Multilabel Classification**: Multiple labels per instance
4. **Hierarchical Classification**: Classes organized in a hierarchy

## Modern Classification Methods

1. **Linear Models**: 
   - Linear Discriminant Analysis (LDA)
   - Logistic Regression
   
2. **Non-linear Models**:
   - Decision Trees
   - Support Vector Machines
   - Neural Networks
   
3. **Ensemble Methods**:
   - Random Forests
   - Gradient Boosting

## Key Metrics

1. **Accuracy**: Proportion of correct predictions
2. **Precision**: True positives / (True positives + False positives)
3. **Recall**: True positives / (True positives + False negatives)
4. **F1 Score**: Harmonic mean of precision and recall

## Scientific Impact

Fisher's work:
- Created the foundation for statistical classification
- Introduced discriminant analysis
- Established pattern recognition as a field
- Influenced machine learning development

## Applications

- Medical diagnosis
- Image recognition
- Spam detection
- Credit scoring
- Species identification
- Sentiment analysis

## Related Concepts
- [[Discriminant analysis]]
- [[Pattern recognition]]
- [[Machine learning]]
- [[Supervised learning]]
- [[Statistical learning]]

## References

Fisher, R.A. (1936). The use of multiple measurements in taxonomic problems. Annals of Eugenics, 7(2), 179-188.