from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
import gspread
import pandas as pd
import numpy as np
import instagram as ig
import photoshop as ps
import filter

SPREADSHEET = "(ORG) Missed Connections (Responses).xls"
ID = "1rtcZwv9wBoxJokbiTW65BmlRvqSp_vkQFLG8IG4hNcE"
form_id = '1OeBHrYdl3Zdwwo7eAE5pB2RxdHuw5HEJWoFfFYxr6ZM'
range_ = 'A2:C110'

print("Automated Freedom Board v1.0")
  
credentials_path = "credentials.json"
scope = ["https://www.googleapis.com/auth/spreadsheets", 
         'https://www.googleapis.com/auth/drive',
         'https://www.googleapis.com/auth/forms']

credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scope)
client = gspread.authorize(credentials)
service = build('forms', 'v1', credentials=credentials)

sheet = client.open_by_key(ID).sheet1

values = sheet.get_all_values()
df = pd.DataFrame(values[1:], columns=values[0])

dataset = df.to_numpy()

if not np.any(dataset):
    print("Google Sheets File is Empty")

else: 
    filtered = filter.cleanData(dataset)

    ps.makePNG(filtered)
    ig.upload(len(filtered))

    cell_list = sheet.range(range_)

    for cell in cell_list:
        cell.value = ""
    sheet.update_cells(cell_list)

    try:
        response = service.forms().responses().list(formId=form_id).execute()
        for r in response['responses']:
            service.forms().responses().delete(formId=form_id, responseId=r['responseId']).execute()
        
    except HttpError as error:
        print(f"An error occurred: {error}")