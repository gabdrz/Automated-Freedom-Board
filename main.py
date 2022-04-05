from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import pandas as pd
import instagram as ig
import photoshop as ps

SCOPE = ["https://spreadsheets.google.com/feeds"]
SECRETS_FILE = "missed-connections.json"
SPREADSHEET = "(ORG) Missed Connections (Responses).xls"
  
# Initializing a GoogleAuth Object
gauth = GoogleAuth()
  
# client_secrets.json file is verified
# and it automatically handles authentication
gauth.LocalWebserverAuth()
  
# GoogleDrive Instance is created using
# authenticated GoogleAuth instance
drive = GoogleDrive(gauth)
  
# Initialize GoogleDriveFile instance with file id
file_obj = drive.CreateFile({'id': '1rtcZwv9wBoxJokbiTW65BmlRvqSp_vkQFLG8IG4hNcE'})
file_obj.GetContentFile(SPREADSHEET,
                mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
dataframe = pd.read_excel(SPREADSHEET)
dataset = dataframe.to_numpy()

ps.makePNG(dataset)
ig.upload(len(dataset))

