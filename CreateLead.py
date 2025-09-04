import os
from fastapi import FastAPI
import requests
import json
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from typing import Optional, List
app = FastAPI()
URLBITRIX = os.environ['URLBITRIX']
EMOJI = os.environ['EMOJI']
SOURCE_ID = os.environ['SOURCE_ID']

class Item(BaseModel):
    fields: dict

class Fields(BaseModel):
    TITLE: str
    NAME: Optional[str] = None
    COMMENTS: Optional[str] = None
    OPENED: Optional[str] = None
    PHONE: Optional[List[int]] = None
    SOURCE_DESCRIPTION: Optional[str] = None
    UTM_SOURCE: Optional[str] = None
    UTM_CONTENT: Optional[int] = None
    UTM_TERM: Optional[int] = None

class Params(BaseModel):
    REGISTER_SONET_EVENT: Optional[str] = None

class RequestModel(BaseModel):
    fields: Fields
    params: Optional[Params] = None
    
@app.post("/testprocess/")
async def process(request: RequestModel):
    lead_data = {'fields':{
            'TITLE':request['NAME'],
            'NAME': request['NAME'],
            "STATUS_ID": "NEW",
            "SOURCE_ID": SOURCE_ID,
            "UTM_SOURCE":request['UTM_SOURCE'],
            "UTM_MEDIUM":request['UTM_MEDIUM'],
            "UTM_CAMPAIGN":request['UTM_CAMPAIGN'],
            "UTM_TERM":request['UTM_TERM'],
            "UTM_CONTENT":request['UTM_CONTENT'],
            "PHONE": [{ "VALUE": request['PHONE'][0]["VALUE"],"VALUE_TYPE": "OTHER","TYPE_ID": "PHONE"}],
            'COMMENTS': request['COMMENTS']
        
        }}
    response = requests.post(str(f'{URLBITRIX}/crm.lead.add.json'), json=lead_data)
    print(response)
    answ = json.loads(response.text)
    return {"data": answ['result']}



@app.post("/addlead/crm.lead.add.json")
def read_post_root(item: Item):
    lead_data = {'fields':{
            'TITLE':item.fields['TITLE'],
            'NAME': item.fields['NAME'],
            "STATUS_ID": "NEW",
            "SOURCE_ID": SOURCE_ID,
            #"UTM_SOURCE":item.fields['UTM_SOURCE'],
            #"UTM_MEDIUM":item.fields['UTM_MEDIUM'],
            #"UTM_CAMPAIGN":item.fields['UTM_CAMPAIGN'],
            #"UTM_TERM":item.fields['UTM_TERM'],
            #"UTM_CONTENT":item.fields['UTM_CONTENT'],
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
            #"UTM_SOURCE":item.UTM_SOURCE,
            #"UTM_MEDIUM":item.UTM_MEDIUM,
            #"UTM_CAMPAIGN":item.UTM_CAMPAIGN,
            #"UTM_TERM":item.UTM_TERM,
            #"UTM_CONTENT":item.UTM_CONTENT,
            "PHONE": [{ "VALUE": item.PHONE,"VALUE_TYPE": "OTHER","TYPE_ID": "PHONE"}],
            'COMMENTS': item.COMMENT
        }}
    print(f'send data ={lead_data}')
    response = requests.post(str(f'{URLBITRIX}/crm.lead.add.json'), json=lead_data)
    print(response)
    answ = json.loads(response.text)
    return {"data": answ['result']}







