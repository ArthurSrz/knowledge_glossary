To avoid [[Data drift]] or [[Concept drift]]. 

We want to look at the Input data that goes into the data pipeline : 

* [[Data quality]] 
* Distribution of input data 
* Correlation of feature to targets
* Periodic manual audits. 

We want to check also data coming out of the pipeline : 
* check distribution post and pre-pipeline work. 

We want to check model output. 

We also want to monitor model performance by creating subgroups and checking consistency. 

We also want to make sure we still understand what the model is doing : 
* [[Local Interpretable Model-Agnostic Explanations (LIME)]]
* [[Shapley Additive Explanations (SHAP)]]
*



## Related concepts

- [[Monitor]] - The action of monitoring
- [[Concept drift]] - Monitoring changes in data
- [[Data drift]] - Data distribution shifts
- [[Model decay]] - Performance degradation over time
- [[Detection tool performance]] - Tracking tool efficiency
- [[Dashboard]] - Visualization of monitoring data
- [[ML System failures]] - Problems to detect
- [[Excessive latency]] - Performance issue to monitor
- [[Scheduled retraining]] - Response to monitoring
- [[Retraining]] - Model update process
- [[Fault tolerance]] - System resilience
