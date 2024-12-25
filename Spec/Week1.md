# Week 1: Collaborative Filtering Recommendations

## Objective
Build a collaborative filtering recommendation system using Amazon Review Data. The system will provide personalized product recommendations based on user-item interactions.


## Tasks

These are the tasks you should complete in this week:

### 1. **Data Preparation**
- Download the [Amazon Review Data (5-core subset)](https://nijianmo.github.io/amazon/#subsets).
- Preprocess the data:
  - Filter out irrelevant columns.
  - Handle missing or inconsistent values.
  - Create a user-item interaction matrix.

### 2. **Collaborative Filtering Implementation**
- Implement **user-based collaborative filtering**:
  - Compute user-user similarities using cosine similarity.
  - Generate recommendations based on similar users’ preferences.
- Evaluate using metrics like RMSE (for predicted ratings) or Precision@K (for ranking).

### 3. **Visualizations**
- Visualize the user-item interaction matrix.
- Display example recommendations for a sample user.



## Bonus
Do these if time permits:
- Add **item-based collaborative filtering** for comparison.
- Explore hyperparameter tuning for similarity thresholds.
- If time permits, implement a simple evaluation dashboard.




## Learning Goals
- Understand the concept of collaborative filtering.
- Learn to preprocess and analyze user-item interaction data.
- Familiarize yourself with evaluation metrics for recommendation systems.



## Resources
- Dataset: [Amazon Review Data (5-core subset)](https://nijianmo.github.io/amazon/index.html)
- Tools:
  - Python, pandas, NumPy, scikit-learn
  - Visualization libraries: Matplotlib, Seaborn
- Tutorials and References:
  - Collaborative filtering tutorials 
  - Documentation for `sklearn.metrics.pairwise.cosine_similarity`.
  

