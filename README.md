### Customer Churn Model

DVC + KServe + Kubernetes + Github Action + ArgoCD   

Real Time Usecase : (Telecom Industry)  



management -> DataSet -> Data -> dataset

*** Common step for m/c learning

create virtual env

python -m venv .venv
.venv\Scripts\activate

### install requirements
python -m pip install -r requirements.txt

## For testing purpose generate data
python generate_data.py

## For traing
 python train.py

 ## for api
 python api.py


 ### for powershell

 Invoke-RestMethod -Uri http://localhost:8000/predict `
  -Method POST `
  -Headers @{ "Content-Type" = "application/json" } `
  -Body '{
    "age": 45,
    "tenure_months": 24,
    "monthly_charges": 79.99,
    "total_charges": 1920.00,
    "num_support_calls": 3
  }'

  REsponse :

  churn churn_probability
----- -----------------
    1              0.52

 ### DVC
python -m pip install dvc

python -m pip install dvc-s3

dvc init 
create .dvc folder

AWS account create S3 bucket
AWS configure

### Add remote bucket in s3

dvc remote add -d s3remote s3://aws-bedrock-blogs-bucket-220781

add csv file to remote storage

dvc add .\data\churn_data.csv
dvc push

ls data

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----          2/1/2026   9:32 PM             17 .gitignore
-a----          2/1/2026   9:32 PM          51314 churn_data.csv
-a----          2/1/2026   9:32 PM            100 churn_data.csv.dvc









