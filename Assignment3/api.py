from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
import os
import zipfile
import io
import tensorflow as tf
from random import randint
import numpy as np
import matplotlib.pyplot as plt
from nowcast_reader import read_data


app = FastAPI()
'''
@app.get("/")
async def root():
    return {"message": "Hello World"}'''
'''
@app.get("/location/{location_name}")
def analyze_location(location_name: str , year : int , month :int, day : int):
    return {"location_name" : location_name, "Year" : year, "Month" : month, "Day":day}'''

from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    location: str
    year: Optional[int] = None
    month: Optional[int] = None
    day: Optional[int] = None

app = FastAPI()

@app.put("/location/")
async def create_item(item: Item):
  items = item.dict()
  locs = items["location"]
  filep = os.path.join(this_file_path,"files/fin.jpg")
  if os.path.exists(filep):
    return FileResponse(filep , media_type="image/jpeg", filename= "myfin.jpg")
  return {"error:file not found"}
    #return {"location_name": item_id, **item.dict()}

@app.get("/fin", responses= {200: {"Desc" : "Prediction for next one hour", "content" : {"image/jpg": {"example": "No pred available"}}}})
def fin():
    filep = os.path.join(this_file_path,"files/fin.jpg")
    if os.path.exists(filep):
      return FileResponse(filep , media_type="image/jpeg", filename= "myfin.jpg")
    return {"error:file not found"}


model = "./mse_model.h5"
mse_model = tf.keras.models.load_model(model,compile=False,custom_objects={"tf":tf})

x_test, y_test = read_data('./nowcast_testing.h5', end=50)


storm_loc = 'Miami'

loc = randint(10,19)

y_preds=[]

norm = {'scale':47.54,'shift':33.44}
hmf_colors = np.array( [
    [82,82,82], 
    [252,141,89],
    [255,255,191],
    [145,191,219]
])/255

def prediction(location_name, year, month, day):
  #loc = get_id(location_name, year, month, day)
  loc = loc
  y_pred = mse_model.predict(x_test)
  if isinstance(y_pred,(list,)):
    y_pred=y_pred[0]
  y_preds.append(y_pred+norm['scale']+norm['shift'])

  res = imgsave(loc , y_preds)
  return res

def imgsave(id,y_preds):
  y_preds=np.asarray(y_preds)
  y_preds=y_preds[0]
  #print(y_preds[id])
  #print(type(y_preds))
  filepath = "./images/"
  #return filepath 
  
  for i in range(0,12):
    #print(y_preds[id])
    y_data= y_preds[id,:,:,i]
    filepath = "./images/"
    plt.imsave(f"./images{i}.jpg", y_data)
  return filepath




def zipfiles(filenames):
    zip_filename = "archive.zip"

    s = io.BytesIO()
    zf = zipfile.ZipFile(s, "w")

    for fpath in filenames:
        # Calculate path for file in zip
        fdir, fname = os.path.split(fpath)

        # Add file, at correct path
        zf.write(fpath, fname)

    # Must close zip for all contents to be written
    zf.close()

    # Grab ZIP file from in-memory, make response with correct MIME-type
    resp = Response(s.getvalue(), media_type="application/x-zip-compressed", headers={
        'Content-Disposition': f'attachment;filename={zip_filename}'
    })

    return resp




@app.get("/get_pred/{location_name}")
def get_pred(location_name: str , year : int , month :int, day : int):
    p = prediction(location_name, year, month, day)
    return {"location_name" : location_name, "Year" : year, "Month" : month, "Day":day}

# An endpoint to serve images for documentation
@app.get("/fin", responses= {200: {"Desc" : "Prediction for next one hour", "content" : {"image/jpg": {"example": "No pred available"}}}})
def fin():
    filep = os.path.join(this_file_path,"files/fin.jpg")
    if os.path.exists(filep):
      return FileResponse(filep , media_type="image/jpeg", filename= "myfin.jpg")
    return {"error:file not found"}


this_file_path = "/Users/akankshatelagamsetty/Desktop/BDIS"

import sys
from PIL import Image

images1 = [Image.open(x) for x in ['images0.jpg', 'images1.jpg', 'images2.jpg', 'images3.jpg', 'images4.jpg', 'images5.jpg']]
images2 = [Image.open(y) for y in ['images6.jpg', 'images7.jpg', 'images8.jpg', 'images9.jpg', 'images10.jpg', 'images11.jpg']]

widths, heights = zip(*(i.size for i in images1))
widths2, heights2 = zip(*(i.size for i in images2))

total_width = sum(widths)
max_height = max(heights)

total_width2 = sum(widths2)
max_height2 = max(heights2)


new_im1 = Image.new('RGB', (total_width, max_height))
new_im2 = Image.new('RGB', (total_width2, max_height2))
new_im = Image.new('RGB', (total_width, 2*max_height)) #since double

x_offset = 0
for im1 in images1:
  new_im1.paste(im1, (x_offset,0))
  x_offset += im1.size[0]

x_offset2 = 0
for im2 in images2:
  new_im2.paste(im2, (x_offset2,0))
  x_offset2 += im2.size[0]

new_im1.save('test1.jpg')
new_im2.save('test2.jpg')


imgs = [Image.open(x) for x in ['test1.jpg', 'test2.jpg']]
new_pos=0
for im in imgs:
        new_im.paste(im, (0, new_pos))
        new_pos += im.size[1] #position for the next image
new_im.save('files/fin.jpg') #change the filename if you want

# An endpoint to serve images for documentation
@app.get("/fin", responses= {200: {"Desc" : "Prediction for next one hour", "content" : {"image/jpg": {"example": "No pred available"}}}})
def fin():
    filep = os.path.join(this_file_path,"files/fin.jpg")
    if os.path.exists(filep):
      return FileResponse(filep , media_type="image/jpeg", filename= "myfin.jpg")
    return {"error:file not found"}


#JSON 
'''
[

  {
    _id: '{{objectId()}}',
    location_name: "boston",
    timestamp: [
     
      {
          "Year": 2022,
          "Month": 2,
          "Day": 12
      }
    ]
    
    }
  
]
'''
