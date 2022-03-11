FastAPI_Nowcast

Implemented FastAPI for prediction of weather data using Nowcast

Install uvicorn using:

$ pip install uvicorn

Download the model files from

https://drive.google.com/drive/folders/1r9XM9P-iZUNtacBSoq-XdnlnlYL8X8dS?usp=sharing

Run the api.py file from CLI using:

uvicorn api:app --reload

Go to local host server "/docs" to give the input. You can give the input as:

json under /fin
text box input under /location
Once you execute, the model predictions (12 images) will be obtained as merged output.

Alternatively, You can run the Client.py notebook which invokes the api and displays the predictions (12 images corresponding to the next hour's weather pattern)
