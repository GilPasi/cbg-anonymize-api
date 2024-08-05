


docker build --platform linux/amd64 -t genaiproj_anonymize_pii_lambda:latest .
### Testing: ###
    docker run --platform linux/amd64 -p 9000:8080 genaiproj_anonymize_pii_lambda:latest
second terminale:
    curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
get CONTAINER ID:
    docker ps
    docker kill <CONTAINER ID>
### ___ ###

aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin 696714140038.dkr.ecr.eu-central-1.amazonaws.com
aws ecr create-repository --repository-name genaiproj_anonymize_pii_lambda --region eu-central-1 --image-scanning-configuration scanOnPush=true --image-tag-mutability MUTABLE

docker tag genaiproj_anonymize_pii_lambda:latest 696714140038.dkr.ecr.eu-central-1.amazonaws.com/genaiproj_anonymize_pii_lambda:latest
docker push 696714140038.dkr.ecr.eu-central-1.amazonaws.com/genaiproj_anonymize_pii_lambda:latest
uri: 696714140038.dkr.ecr.eu-central-1.amazonaws.com/genaiproj_anonymize_pii_lambda

aws lambda create-function \
  --function-name genaiproj_AnonymizePii \
  --package-type Image \
  --code ImageUri=696714140038.dkr.ecr.eu-central-1.amazonaws.com/genaiproj_anonymize_pii_lambda:latest \
  --role arn:aws:iam::696714140038:role/genaiproj_LambdaPresidioRole \
   --region eu-central-1


aws lambda invoke --region eu-central-1 --function-name genaiproj_AnonymizePii response.json



####

aws lambda delete-function --function-name genaiproj_AnonymizePii --region eu-central-1

aws ecr delete-repository --repository-name genaiproj_anonymize_pii_lambda --region eu-central-1 --force
