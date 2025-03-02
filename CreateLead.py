import os
from fastapi import FastAPI
import requests
import json
app = FastAPI()
URLBITRIX = os.environ['URLBITRIX']
EMOJI = os.environ['EMOJI']
SOURCE_ID = os.environ['SOURCE_ID']
WMIDFIELD = os.environ['WMIDFIELD'] #WMID USER FIELD
TS_ID = os.environ['TS_ID'] #TRACKING_SOURCE_ID
ASSIGNED_BY_ID = os.environ['ASSIGNED_BY_ID']
@app.post("/addlead/")
def read_root(Name:str,
              Phone: str,
              WMID: int| None = None,COMMENT: str| None = None,
              UTM_SOURCE: str| None = None,UTM_MEDIUM:str| None = None,UTM_CAMPAIGN:str| None = None,UTM_CONTENT:str| None = None,UTM_TERM:str| None = None
              ):
    lead_data = {'fields':{
            'TITLE':str(EMOJI + NAME),
            'NAME': NAME,
            "STATUS_ID": "NEW",
            "ASSIGNED_BY_ID ":ASSIGNED_BY_ID,
            "SOURCE_ID": SOURCE_ID,
            "PHONE": [{ "VALUE": PHONE,"VALUE_TYPE": "OTHER","TYPE_ID": "PHONE"}],
            'UTM_SOURCE': UTM_SOURCE,
            'UTM_MEDIUM':UTM_MEDIUM,
            'UTM_CAMPAIGN':UTM_CAMPAIGN,
            'UTM_CONTENT':UTM_CONTENT,
            'UTM_TERM':UTM_TERM,
            'COMMENTS':COMMENT,
            WMIDFIELD: WMID  
        }}
    response = requests.post(str(f'{URLBITRIX}/crm.lead.add.json'), json=lead_data)
    print(response)
    answ = json.loads(response.text)
    return {"data": answ['result']}
