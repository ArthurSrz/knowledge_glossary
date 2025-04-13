---
instanceof: "[[ML System failures 1]]"
---

One of ML System failures. Happens when the patterns that the model learned no longer apply. 

Example : in fraud detection, the purchase of one-way tickets was a potential sign of fraud, but with COVID, the pattern no longer applied. 

From Wikipedia, the free encyclopedia

In [predictive analytics](https://en.wikipedia.org/wiki/Predictive_analytics "Predictive analytics"), [data science](https://en.wikipedia.org/wiki/Data_science "Data science"), [machine learning](https://en.wikipedia.org/wiki/Machine_learning "Machine learning") and related fields, **concept drift** or **drift** is an evolution of data that invalidates the [data model](https://en.wikipedia.org/wiki/Data_model "Data model"). It happens when the statistical properties of the target variable, which the model is trying to predict, change over time in unforeseen ways. This causes problems because the predictions become less accurate as time passes. **Drift detection** and **drift adaptation** are of paramount importance in the fields that involve dynamically changing data and data models.

## Predictive model decay



In machine learning and [predictive analytics](https://en.wikipedia.org/wiki/Predictive_analytics "Predictive analytics") this drift phenomenon is called concept drift. In machine learning, a common element of a data model are the statistical properties, such as [probability distribution](https://en.wikipedia.org/wiki/Probability_distribution "Probability distribution") of the actual data. If they deviate from the statistical properties of the [training data set](https://en.wikipedia.org/wiki/Training_data_set "Training data set"), then the learned predictions may become invalid, if the drift is not addressed.

## Data configuration decay


Another important area is [software engineering](https://en.wikipedia.org/wiki/Software_engineering "Software engineering"), where three types of data drift affecting [data fidelity](https://en.wikipedia.org/wiki/Data_fidelity "Data fidelity") may be recognized. Changes in the software environment ("infrastructure drift") may invalidate software infrastructure configuration. "Structural drift" happens when the data [schema](https://en.wikipedia.org/wiki/Database_schema "Database schema") changes, which may invalidate databases. "Semantic drift" is changes in the meaning of data while the structure does not change. In many cases this may happen in complicated applications when many independent developers introduce changes without proper awareness of the effects of their changes in other areas of the software system.

For many application systems, the nature of data on which they operate are subject to changes for various reasons, e.g., due to changes in business model, system updates, or switching the platform on which the system operates.

In the case of [cloud computing](https://en.wikipedia.org/wiki/Cloud_computing "Cloud computing"), infrastructure drift that may affect the applications running on cloud may be caused by the updates of cloud software.

There are several types of detrimental effects of data drift on data fidelity. Data corrosion is passing the drifted data into the system undetected. Data loss happens when valid data are ignored due to non-conformance with the applied schema. Squandering is the phenomenon when new data fields are introduced upstream the data processing pipeline, but somewhere downstream there data fields are absent.

"Data drift" may refer to the phenomenon when database records fail to match the real-world data due to the changes in the latter over time. This is a common problem with databases involving people, such as customers, employees, citizens, residents, etc. Human data drift may be caused by unrecorded changes in personal data, such as place of residence or name, as well as due to errors during data input.

"Data drift" may also refer to inconsistency of data elements between several replicas of a database. The reasons can be difficult to identify. A simple drift detection is to run [checksum](https://en.wikipedia.org/wiki/Checksum "Checksum") regularly. However the remedy may be not so easy.

The behavior of the customers in an [online shop](https://en.wikipedia.org/wiki/Online_shop "Online shop") may change over time. For example, if weekly merchandise sales are to be predicted, and a [predictive model](https://en.wikipedia.org/wiki/Predictive_modelling "Predictive modelling") has been developed that works satisfactorily. The model may use inputs such as the amount of money spent on [advertising](https://en.wikipedia.org/wiki/Advertising "Advertising"), [promotions](https://en.wikipedia.org/wiki/Promotion_\(marketing\) "Promotion (marketing)") being run, and other metrics that may affect sales. The model is likely to become less and less accurate over time – this is concept drift. In the merchandise sales application, one reason for concept drift may be seasonality, which means that shopping behavior changes seasonally. Perhaps there will be higher sales in the winter holiday season than during the summer, for example. Concept drift generally occurs when the covariates that comprise the data set begin to explain the variation of your target set less accurately — there may be some [confounding](https://en.wikipedia.org/wiki/Confounding "Confounding") variables that have emerged, and that one simply cannot account for, which renders the model accuracy to progressively decrease with time. Generally, it is advised to perform health checks as part of the post-production analysis and to re-train the model with new assumptions upon signs of concept drift.

To prevent deterioration in [prediction](https://en.wikipedia.org/wiki/Prediction "Prediction") accuracy because of concept drift, _reactive_ and _tracking_ solutions can be adopted. Reactive solutions retrain the model in reaction to a triggering mechanism, such as a change-detection test, to explicitly detect concept drift as a change in the statistics of the data-generating process. When concept drift is detected, the current model is no longer up-to-date and must be replaced by a new one to restore prediction accuracy. A shortcoming of reactive approaches is that performance may decay until the change is detected. Tracking solutions seek to track the changes in the concept by continually updating the model. Methods for achieving this include [online machine learning](https://en.wikipedia.org/wiki/Online_machine_learning "Online machine learning"), frequent retraining on the most recently observed samples, and maintaining an ensemble of classifiers where one new classifier is trained on the most recent batch of examples and replaces the oldest classifier in the ensemble.

Contextual information, when available, can be used to better explain the causes of the concept drift: for instance, in the sales prediction application, concept drift might be compensated by adding information about the season to the model. By providing information about the time of the year, the rate of deterioration of your model is likely to decrease, but concept drift is unlikely to be eliminated altogether. This is because actual shopping behavior does not follow any static, [finite model](https://en.wikipedia.org/wiki/Finite_model "Finite model"). New factors may arise at any time that influence shopping behavior, the influence of the known factors or their interactions may change.

Concept drift cannot be avoided for complex phenomena that are not governed by fixed [laws of nature](https://en.wikipedia.org/wiki/Physical_law "Physical law"). All processes that arise from human activity, such as [socioeconomic](https://en.wikipedia.org/wiki/Socioeconomic "Socioeconomic") processes, and [biological processes](https://en.wikipedia.org/wiki/Biological_processes "Biological processes") are likely to experience concept drift. Therefore, periodic retraining, also known as refreshing, of any model is necessary.

- [Data stream mining](https://en.wikipedia.org/wiki/Data_stream_mining "Data stream mining")
- [Data mining](https://en.wikipedia.org/wiki/Data_mining "Data mining")
- [Snyk](https://en.wikipedia.org/wiki/Snyk "Snyk"), a company whose portfolio includes drift detection in software applications



