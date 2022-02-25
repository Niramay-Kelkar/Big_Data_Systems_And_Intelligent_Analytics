# Big_Data_Systems_And_Intelligent_Analytics
Assignments and Projects for Big Data Systems and Intelligent Analytics

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

This repo also contains a design document that focuses on deployment of the Nowcast Intelligent System in an Insurance Provider senario.


