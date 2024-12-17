# Automated Freedom Board

## Overview
The Automated Freedom Board is a bot that creates an anonymous message board on Instagram. It automates the process of collecting anonymous submissions through Google Forms, processing them through Photoshop, and publishing them to Instagram. This creates a platform where people can share thoughts and messages anonymously while maintaining a consistent visual style.

## Features
- Automated message collection through Google Forms
- Profanity filtering for content moderation
- Custom image generation using Photoshop templates
- Automated Instagram posting (single photos and albums)
- Automatic cleanup of processed submissions

## Prerequisites
- Python 3.7+
- Adobe Photoshop
- Google Cloud account
- Instagram account
- Required Python packages (see Installation section)

## Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/Automated-Freedom-Board.git
cd Automated-Freedom-Board
```

2. Install required Python packages
```bash
pip install gspread oauth2client pandas numpy better_profanity instagrapi pywin32
```

3. Set up Google Cloud Project
   1. Go to [Google Cloud Console](https://console.cloud.google.com)
   2. Create a new project
      - Click "Select a Project" → "New Project"
      - Enter your project name (e.g., "Automated Freedom Board")
   3. Enable required APIs
      - Navigate to "APIs & Services" → "Enable APIs and Services"
      - Search for and enable:
        - Google Sheets API
        - Google Drive API
        - Google Forms API
   4. Create service account credentials
      - Go to "APIs & Services" → "Credentials"
      - Click "CREATE CREDENTIALS" → "Service Account"
      - Fill in service account details and select "Owner" role
      - Generate and download JSON key
      - Rename the downloaded file to `credentials.json`

4. Configure Google Forms
   1. Create a new Google Form
   2. Set up form responses to save to a Google Sheet
      - Click "Responses" tab → "Create Spreadsheet"
   3. Copy the Spreadsheet ID from the URL:
      - Format: `https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/edit`

5. Project Configuration
   1. Place your `credentials.json` in the project root directory
   2. Update `main.py` with your Spreadsheet ID
   3. Update `instagram.py` with your Instagram credentials

## Usage

1. Prepare your Photoshop template
   - Create a PSD file named `template.psd`
   - Include text layers named "Message" and "Timestamp"
   - Save in the project root directory

2. Run the bot
```bash
python main.py
```

The bot will:
1. Check for new submissions in the Google Sheet
2. Filter out inappropriate content
3. Generate images using the Photoshop template
4. Upload images to Instagram
5. Clean up processed submissions

## File Structure
- `main.py` - Main script coordinating all operations
- `filter.py` - Content moderation functionality
- `instagram.py` - Instagram upload handling
- `photoshop.py` - Image generation using Photoshop
- `credentials.json` - Google Cloud service account credentials
- `template.psd` - Photoshop template for message images

## Troubleshooting
1. If Google APIs fail:
   - Verify credentials.json is correctly placed
   - Check if APIs are enabled in Google Cloud Console
   - Ensure service account has appropriate permissions

2. If Photoshop automation fails:
   - Verify Photoshop is installed and accessible
   - Check template.psd exists and has correct layer names
   - Ensure you're running on Windows (COM API requirement)

3. If Instagram upload fails:
   - Verify credentials are correct
   - Check internet connection
   - Ensure images folder exists and is writable

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
[Add your chosen license here]

## Disclaimer
This project is for educational purposes only. Be sure to comply with Instagram's terms of service and community guidelines when using this bot.