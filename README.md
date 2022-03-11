# Big_Data_Systems_And_Intelligent_Analytics

Assignments and Projects for Big Data Systems and Intelligent Analytics
# Assignment 2
This repo consists of stepd to generate Nowcast and Synrad testing data nad use it to test the two models:
1. Synrad
2. Nowcast

Create a python environment(Python 3.6 or 3.7) that supports tensorflow v2.1 and the other requirements specified.
To download the models, set your path to assignment folder and:
cd models/
python download_models.py

Download sevir data:
Using boto3

To make test dataset:
python make_nowcast_dataset.py --sevir_data sevir --sevir_catalog CATALOG.csv --output_location interim

Once, you have the require data, you can run the Synrad and Nowcast notebooks present in notebooks/.

Refer the master branch for the implementation of Nowcasting.

This repo also contains a design document that focuses on deployment of the Nowcast Intelligent System in an Insurance Provider senario.



# Assignment 3
# FastAPI_Nowcast
Implemented FastAPI for prediction of weather data using Nowcast


## Install uvicorn using:
$ pip install uvicorn

## Download the model files from 
https://drive.google.com/drive/folders/1r9XM9P-iZUNtacBSoq-XdnlnlYL8X8dS?usp=sharing


## Run the api.py file from CLI using:
uvicorn api:app --reload

Go to local host server "/docs" to give the input.
You can give the input as:
1. json under /fin
2. text box input under /location

Once you execute, the model predictions (12 images) will be obtained as merged output.

Alternatively,
You can run the Client.py notebook which invokes the api and displays the predictions (12 images corresponding to the next hour's weather pattern)

