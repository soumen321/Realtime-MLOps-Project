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


 store the model -> .pkl file in S3 bucket


 ### Create kubernetes cluster (Demo purpose use kind)

 kind create cluster --name=churn-model-cluster

 ## Install Kserve

 Use for:

  - Model deploying
  - Model Serving
  - Model Inferance

 Install Cert Manager

 kubectl apply -f https://github.com/cert-manager/cert-manager/releases/latest/download/cert-manager.yaml

 Install KServe CRDs

 kubectl create namespace kserve

 for powershell

 helm install kserve-crd oci://ghcr.io/kserve/charts/kserve-crd `
  --version v0.16.0 `
  -n kserve `
  --wait

for linux  

helm install kserve-crd oci://ghcr.io/kserve/charts/kserve-crd \
  --version v0.16.0 \
  -n kserve \
  --wait

kubectl get crds  

Install KServe controller

for windows:

helm install kserve oci://ghcr.io/kserve/charts/kserve --version v0.16.0 -n kserve --set kserve.controller.deploymentMode=RawDeployment --wait

for linux:

helm install kserve oci://ghcr.io/kserve/charts/kserve \
  --version v0.16.0 \
  -n kserve \
  --set kserve.controller.deploymentMode=RawDeployment \
  --wait

kubectl get pods -n kserve  



### Create Inference file

Unable to access model from s3 because s3 not public

For that we create a service account, from there we access the s3 bucket using aws creadentials

How to do -> in service account add secrect which has aws cred

kubectl create namespace ml

create service account

files in k8s folder

service acc file:

kubectl apply -f .\k8s\serviceaccount.yml

kubectl get sa -n ml

inference file:

kubectl apply -f .\k8s\inference.yml

kubectl get pods -n ml -w

kubectl get svc -n ml

kubectl port-forward svc/churn-predictor-predictor 7001:80 --address 0.0.0.0 -n ml


POwershell

Invoke-RestMethod -Method Post -Uri "http://localhost:7001/v1/models/churn-predictor:predict" `
>>   -ContentType "application/json" `
>>   -Body '{
>>     "instances": [
>>       [45, 24, 79.99, 1920.00, 3]
>>     ]
>>   }'

predictions
-----------
{1}  


Create a CI file in workflows using github action

Using ARGOCD we deploy inference.yml

Goto Ardo CD doc

kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

Though I have use kind cluster, so i port-forward ArgoCD then i get access argocd user interphase

kubectl get svc -n argocd

kubectl port-forward svc/argocd-server  7003:80 --address 0.0.0.0 -n argocd

for usename and password

kubectl get secrets -n argocd
kubectl edit secrets/argocd-initial-admin-secret -n argocd

echo <> | base64 --decode

admin / <password>

kubectl get secret -n ml

 kubectl edit secret s3-secret -n ml 










