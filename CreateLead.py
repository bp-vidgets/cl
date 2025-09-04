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

class Fields(BaseModel):
    TITLE: str
    NAME: Optional[str] = None
    COMMENTS: Optional[str] = None
    PHONE: Optional[List[dict]] = None
    SOURCE_DESCRIPTION: Optional[str] = None
    UTM_SOURCE: Optional[str|int] = None
    UTM_CAMPAIGN: Optional[str|int] = None
    UTM_MEDIUM: Optional[str|int] = None
    UTM_CONTENT: Optional[str|int] = None
    UTM_TERM: Optional[str|int] = None

class RequestModel(BaseModel):
    fields: Fields


@app.post("/addlead2/crm.lead.add.json")
def read_post_root(item: RequestModel):
    tmpphone= item.fields.PHONE[0]["VALUE"]
    lead_data = {'fields':{
            'TITLE':item.fields.TITLE,
            'NAME': item.fields.NAME,
            "STATUS_ID": "NEW",
            "SOURCE_ID": SOURCE_ID,
            "UTM_SOURCE":item.fields.UTM_SOURCE,
            "UTM_MEDIUM":item.fields.UTM_MEDIUM,
            "UTM_CAMPAIGN":item.fields.UTM_CAMPAIGN,
            "UTM_TERM":item.fields.UTM_TERM,
            "UTM_CONTENT":item.fields.UTM_CONTENT,
            "PHONE": [{ "VALUE": item.fields.PHONE[0]["VALUE"],"VALUE_TYPE": "OTHER","TYPE_ID": "PHONE"}],
            'COMMENTS': item.fields.COMMENTS
    }}
        
@app.post("/addlead/crm.lead.add.json")
def read_post_root(item: RequestModel):
    lead_data = {'fields':{
            'TITLE':item.fields.TITLE,
            'NAME': item.fields.NAME,
            "STATUS_ID": "NEW",
            "SOURCE_ID": SOURCE_ID,
            "UTM_SOURCE":item.fields.UTM_SOURCE,
            "UTM_MEDIUM":item.fields.UTM_MEDIUM,
            "UTM_CAMPAIGN":item.fields.UTM_CAMPAIGN,
            "UTM_TERM":item.fields.UTM_TERM,
            "UTM_CONTENT":item.fields.UTM_CONTENT,
            "PHONE": [{ "VALUE": item.fields.PHONE[0]["VALUE"],"VALUE_TYPE": "OTHER","TYPE_ID": "PHONE"}],
            'COMMENTS': item.fields.COMMENTS
    }}
    
    response = requests.post(str(f'{URLBITRIX}/crm.lead.add.json'), json=lead_data)
    print(response)
    answ = json.loads(response.text)
    return {"data": answ['result']}

@app.get("/addlead/")
def read_get_root(item: RequestModel):
    lead_data = {'fields':{
            'TITLE':item.fields.TITLE,
            'NAME': item.fields.NAME,
            "STATUS_ID": "NEW",
            "SOURCE_ID": SOURCE_ID,
            "UTM_SOURCE":item.fields.UTM_SOURCE,
            "UTM_MEDIUM":item.fields.UTM_MEDIUM,
            "UTM_CAMPAIGN":item.fields.UTM_CAMPAIGN,
            "UTM_TERM":item.fields.UTM_TERM,
            "UTM_CONTENT":item.fields.UTM_CONTENT,
            "PHONE": [{ "VALUE": item.fields.PHONE[0]["VALUE"],"VALUE_TYPE": "OTHER","TYPE_ID": "PHONE"}],
            'COMMENTS': item.fields.COMMENTS
    }}
    print(f'send data ={lead_data}')
    response = requests.post(str(f'{URLBITRIX}/crm.lead.add.json'), json=lead_data)
    print(response)
    answ = json.loads(response.text)
    return {"data": answ['result']}















