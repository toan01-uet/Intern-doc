import requests
from elasticNet_model import data
from sklearn.model_selection import train_test_split
import json
import numpy as np

np.random.seed(40)
# Split the data into training and test sets. (0.75, 0.25) split.
train, test = train_test_split(data)
 
  # The predicted column is "progression" which is a quantitative measure of disease progression one year after baseline
train_x = train.drop(["progression"], axis=1)
test_x = test.drop(["progression"], axis=1)
train_y = train[["progression"]]
test_y = test[["progression"]]
data_request = test_x.iloc[0]

input_example = [{
  "age": 5.1,
  "sex": 3.5,
  "bmi": 1.4,
  "bp": 0.2,
  "s1": 0.5,
  "s2": 0.5,
  "s3": 0.5,
  "s4": 0.5,
  "s5": 0.5,
  "s6": 0.5
}]
# data_json = json.dumps(data_request.tolist())

data_json = json.dumps(input_example)

print(data_json)

headers = {'Content-Type': 'application/json; format=pandas-records'}
request_uri = 'http://127.0.0.1:5000/invocations'

if __name__ == '__main__':
    try:
        response = requests.post(request_uri, data=data_json, headers=headers)
        print(response.content)
        print('done!!!')
    except Exception as ex:
        raise (ex)