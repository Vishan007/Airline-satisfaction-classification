Airline Satisfaction Binary Classification using Random Forest
This repository contains a machine learning model for binary classification of airline satisfaction using Random Forest algorithm. The model is built to predict whether a customer is satisfied or dissatisfied with their airline experience based on various features such as gender, age, type of travel, etc.

Dataset
The dataset used for this model is the Airline Passenger Satisfaction dataset, which can be found on Kaggle here. The dataset consists of 129,880 records with 24 features including both categorical and numerical data.

Model
The model is built using Python programming language with the following libraries:

pandas for data manipulation
numpy for numerical operations
sklearn for machine learning algorithms
matplotlib and seaborn for data visualization
The dataset is preprocessed to handle missing values, encode categorical data, and scale numerical features. The preprocessed dataset is then split into training and testing sets with a 75:25 ratio. The Random Forest algorithm is applied to the training data with 100 trees and the default hyperparameters of the RandomForestClassifier function from sklearn.ensemble.

The model achieved an accuracy score of 0.95 on the test set, indicating a high level of accuracy in predicting customer satisfaction.

Usage
To use this model, clone or download this repository and run the airline_satisfaction.ipynb notebook file using Jupyter Notebook or Jupyter Lab. The notebook contains the code for preprocessing the dataset, building and training the Random Forest model, and evaluating the model on the test set.

Conclusion
The Random Forest model built in this repository can accurately predict whether a customer is satisfied or dissatisfied with their airline experience with an accuracy of 95%. This model can be used by airlines to analyze customer satisfaction and improve their services accordingly.
Due to feature selection and feature extraction techniques we have lost almost 1% of accuracy.The accuracy of models if all the features are selected is as follows.
1)RandomForest accuracy - 96.17920215581541%
2)SVM classifier accuracy - 95.35152302584091
3)ANN accuracy - 95.5488186324046%
