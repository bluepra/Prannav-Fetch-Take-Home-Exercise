# Prannav-Fetch-Take-Home-Exercise

Welcome to the Fetch Take Home Backend Exercise. All work done by Prannav Arora.

## How to run
1. Clone the repo locally: ```git clone https://github.com/bluepra/Prannav-Fetch-Take-Home-Exercise.git```
2. Navigate to the repo folder
3. Create a docker image using the Dockerfile: ```docker build --tag fetch-python-docker-image .```
4. Run a docker container in detached mode: ```docker run -d -p 5000:5000 fetch-python-docker-image```
5. Make POST ```/receipts/process``` or GET ```/receipts/{id}/points``` requests using Postman
6. To close the container: ```docker stop {container_name}```

## How to run tests
1. Follow steps 1-4 from How to run section above
5. Run: ```python test_requests.py```
6. You do not need the container running to run ```python test_receipt_processing.py```
   
Thank you and appreciate any and all feedback!
