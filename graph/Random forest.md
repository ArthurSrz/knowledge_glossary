---
foundationalPaper: "Random Forests (Breiman, 2001)"
keyPapers: ["Bagging Predictors (Breiman, 1996)", "Random Decision Forests (Ho, 1995)", "Shape Quantization and Recognition with Randomized Trees (Amit & Geman, 1997)"]
typeOf: "[[Ensemble learning method]]"
composedOf: "[[Decision trees]]"
uses: ["[[Bootstrap aggregating (bagging)]]", "[[Feature bagging]]"]
relatedTo: ["[[Bagging]]", "[[Ensemble methods]]", "[[Classification]]", "[[Regression]]"]
---

# Random Forest

Random Forests were developed by Leo Breiman in 2001, combining his earlier work on bagging with Ho's random subspace method.

## Original Definition

From Breiman (2001):
"Random forests are a combination of tree predictors such that each tree depends on the values of a random vector sampled independently and with the same distribution for all trees in the forest."

Key insight from the paper:
"The generalization error of a forest of tree classifiers depends on the strength of the individual trees in the forest and the correlation between them."

## Historical Development

1. **Bagging (Breiman, 1996)**: Introduced bootstrap aggregating to reduce variance
2. **Random Subspace Method (Ho, 1995)**: Proposed random feature selection
3. **Random Forests (Breiman, 2001)**: Combined both approaches with additional innovations

## Core Algorithm

As originally described:
1. For each tree in the forest:
   - Draw a bootstrap sample from the training data
   - At each node, randomly select m features from the p total features
   - Choose the best split among these m features
   - Grow the tree to maximum depth (no pruning)
2. Aggregate predictions by majority vote (classification) or averaging (regression)

## Key Innovations

From Breiman's paper:
1. **Random Feature Selection**: "At each node, a random selection of features is chosen and the best split on these features is used to split the node"
2. **No Pruning**: "Each tree is grown to the largest extent possible"
3. **Out-of-Bag Error**: "Using the out-of-bag samples to estimate the generalization error gives evidence to show that the out-of-bag estimate is as accurate as using a test set of the same size as the training set"

## Mathematical Foundation

Breiman proved that as the number of trees increases:
- The generalization error converges to a limit
- Random forests do not overfit as more trees are added
- The error rate depends on the correlation between trees and their individual strength

## Historical Significance

Random Forests represented a breakthrough because they:
- Combined simplicity with high accuracy
- Handled high-dimensional data effectively
- Provided variable importance measures
- Were remarkably resistant to overfitting
- Scaled well to large datasets

As Breiman noted: "Random forests are an effective tool in prediction. Because of the Law of Large Numbers they do not overfit."
