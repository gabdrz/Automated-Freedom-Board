import gspread
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
import pandas as pd

ID = "1rtcZwv9wBoxJokbiTW65BmlRvqSp_vkQFLG8IG4hNcE"
form_id = '1OeBHrYdl3Zdwwo7eAE5pB2RxdHuw5HEJWoFfFYxr6ZM'
range_ = 'A2:C110'

credentials_path = "credentials.json"
scope = ["https://www.googleapis.com/auth/spreadsheets", 
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scope)
client = gspread.authorize(credentials)
service = build('forms', 'v1', credentials=credentials)

try:
    # Call the 'list' method on the responses resource to retrieve all response IDs
    service.spreadsheets().values().batchClear(spreadsheetId=spreadsheet_id, body={}).execute()
    
    print(f"Responses cleared for form with ID '{form_id}'.")
    
except HttpError as error:
    print(f"An error occurred: {error}")

# sheet = client.open_by_key(ID).sheet1

# values = sheet.get_all_values()
# df = pd.DataFrame(values[1:], columns=values[0])


# cell_list = sheet.range(range_)

# for cell in cell_list:
#     cell.value = ""
# sheet.update_cells(cell_list)
