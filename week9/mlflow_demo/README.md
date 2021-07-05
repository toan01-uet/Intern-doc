# MLflow demo
## 0. Reference
- [MLflow docs](https://mlflow.org/docs/latest/index.html)
- [Isaac4real MLflow Experiment](https://github.com/Isaac4real/MLflow_Experiment/tree/master/Part4-%20MLflow%20Registry_locally)
- [Databricks mlflow quickstart](https://docs.databricks.com/_static/notebooks/mlflow/mlflow-quick-start-training.html)
## 1. Mlflow tracking
- data, code: [Databricks mlflow quickstart](https://docs.databricks.com/_static/notebooks/mlflow/mlflow-quick-start-training.html)
- run experiment:
    ```ps
    python elasticNet_model.py [alpha] [l1_ratio]
    ```
    - view experiment in mlflow ui:
    ```ps
    mlflow ui
    ```
## 2. Mlflow projects
- In mlflow ui, if you run ml tracking, mlflow will generate ```MlModel```, ```conda.yaml```, ```model.pkl```, ```requirement.txt``` file.

    ![gen file](week9/img/mlflow_project_model.png)

- To build Mlflow projects, you can copy them(```conda.yaml```, ```MlModel```).
- Example to run experiment (direct to mlflow_demo):
    ```ps
    mlflow run -P alpha=0.01 MLflow_Project
    ```
- You can also run project from github URI (```mlflow_demo``` directory):
    ```ps
    mlflow run [OPTIONS] URI_github
    ```
## 3. Mlflow models
- Use  ```infer_signature()``` to auto format inputs, output of model.

    ![signature](week9/img/signature_mlflow_model.png)


    ![example](week9/img/signature_model.png)


## 4. Mlflow registry (in local)
[Reference](https://github.com/Isaac4real/MLflow_Experiment/tree/master/Part4-%20MLflow%20Registry_locally)
- Step 1: Train and Track the model:
    1.  run cmd
    ```ps 
    python run_MNSITmodel.py 
    ```
    2. launch 
    ```
    mlflow ui --backend-store-uri sqlite:///mlruns.db
    ```
    3. Got to http://127.0.0.1:5000
    4. Pick the best model, register with Model Registry as Fashion_MNISTmodel
    5. Choose second best model and create version 2 in the Model Registry
        - Transition the best model into Production
        - Transition the second best model into Staging
Use MLflow ui to registry model - tracked model (use ```sqlite db``` to store param,..)
- Step 2: Deploy and make predictions:
    1. ```from mlflow_demo``` directory run:
        ```ps
        deploy_model.sh
        ```
        This launches a gunicorn server serving at the localhost 127.0.0.1:5000. Now you can score locally on the deployed produciton model as a REST point.
    2. From another terminal send a POST request with our JSON payload
        ```ps
        python make_prediction.py
        ```
---
**NOTE**

Rename the registry model name, link in ```deploy.sh```

---