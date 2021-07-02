## reference: https://docs.databricks.com/_static/notebooks/mlflow/mlflow-quick-start-inference.html

import mlflow
import mlflow.sklearn

run_id1 = "83618d28a8824e808576553d5ccddf4c"
model_uri = "runs:/" + run_id1 + "/model"

## load a model previously logged to MLflow
model = mlflow.sklearn.load_model(model_uri=model_uri)
print("coefs of model: ",model.coef_)

# Import required libraries
from sklearn import datasets
import numpy as np
import pandas as pd
 
# Load diabetes datasets
diabetes = datasets.load_diabetes()
X = diabetes.data
y = diabetes.target
 
# Create pandas DataFrame for sklearn ElasticNet linear_model
Y = np.array([y]).transpose()
d = np.concatenate((X, Y), axis=1)
cols = ['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6', 'progression']
data = pd.DataFrame(d, columns=cols)

# Get a prediction for a row of the dataset
print("Predicted value",model.predict(data[0:1].drop(["progression"], axis=1)))
print("real value",data[0:1]["progression"])