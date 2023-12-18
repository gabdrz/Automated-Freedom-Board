# Automated-Freedom-Board
1. Create a Google Cloud App
    - Go to this link https://console.cloud.google.com/getting-started?pli=1
    - Click "Select a Project" then "New Project"
    - Input your project information (i.e. "Automated Freedom Board")
    - Press the Navigation Menu button on the top left hand side and go to APIs & Services
    - Select your project, then click "Enable APIs and Services"
    - Search up the following APIs and add it to the app: 
        * Google Sheets API
        * Google Drive API
        * Google Forms API
    - Go back to the previous menu and go to credentials
    - Click "CREATE CREDENTIALS", then generate a service account
    - Configure the service account name, and ID
    - Select the owner role
    - On the APIs & Services Dashboard, click the email under service accounts
    - Navigate to Keys and download a JSON key
        - Rename the json file to credentials
2. Make a Google Forms form
    - Make sure that the responses' destination is to a Google Sheets file
    - Get the Google Sheets ID in the link 
        - i.e. https://docs.google.com/spreadsheets/d/$ID_HERE/edit?resourcekey#gid=1646859737
3. Clone the repo locally, then replace credentials.json with your credentials.json
    - Replace the ID in main.py to your Google Sheet ID
    - Replace the username and password in instagram.py with your account's information
4. Run the code
