import os
from fastapi import FastAPI
import requests
import json
from pydantic import BaseModel
app = FastAPI()
URLBITRIX = os.environ['URLBITRIX']
EMOJI = os.environ['EMOJI']
SOURCE_ID = os.environ['SOURCE_ID']

class Item(BaseModel):
    fields: dict
  
@app.post("/addlead/crm.lead.add.json")
def read_post_root(item: Item):
    lead_data = {'fields':{
            'TITLE':item.fields['TITLE'],
            'NAME': item.fields['NAME'],
            "STATUS_ID": "NEW",
            "SOURCE_ID": SOURCE_ID,
            "UTM_SOURCE":item.fields['UTM_SOURCE'],
            #"UTM_MEDIUM":item.fields['UTM_MEDIUM'],
            #"UTM_CAMPAIGN":item.fields['UTM_CAMPAIGN'],
            "UTM_TERM":item.fields['UTM_TERM'],
            "UTM_CONTENT":item.fields['UTM_CONTENT'],
            "PHONE": [{ "VALUE": item.fields['PHONE'][0]["VALUE"],"VALUE_TYPE": "OTHER","TYPE_ID": "PHONE"}],
            'COMMENTS': item.fields['COMMENTS']
        
        }}
    response = requests.post(str(f'{URLBITRIX}/crm.lead.add.json'), json=lead_data)
    print(response)
    answ = json.loads(response.text)
    return {"data": answ['result']}

@app.get("/addlead/")
def read_get_root(item: Item):
    lead_data = {'fields':{
            'TITLE':str(EMOJI + item.NAME),
            'NAME': item.NAME,
            "STATUS_ID": "NEW",
            "SOURCE_ID": SOURCE_ID,
            "UTM_SOURCE":item.UTM_SOURCE,
            "UTM_MEDIUM":item.UTM_MEDIUM,
            "UTM_CAMPAIGN":item.UTM_CAMPAIGN,
            "UTM_TERM":item.UTM_TERM,
            "UTM_CONTENT":item.UTM_CONTENT,
            "PHONE": [{ "VALUE": item.PHONE,"VALUE_TYPE": "OTHER","TYPE_ID": "PHONE"}],
            'COMMENTS': item.COMMENT
        }}
    print(f'send data ={lead_data}')
    response = requests.post(str(f'{URLBITRIX}/crm.lead.add.json'), json=lead_data)
    print(response)
    answ = json.loads(response.text)
    return {"data": answ['result']}


