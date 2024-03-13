# PDF Scraper

## Overview
A tool that scrap a specific pdf format table and update google calendars.

## Google pre-configuration

1. Create Google Cloud Platform account.
2. Enable Google Calendar API on Google Cloud Platform.
   
    Please move to “APIs & Services” > “Dashboard”.

    ![image](https://github.com/caiofrota/pdf-scraper/assets/9461960/b61f1a03-ed4e-4fc3-b9ff-e8b22d1e9e63)
  
    Please move to “ENABLE APIS AND SERVICES”.
  
    ![image](https://github.com/caiofrota/pdf-scraper/assets/9461960/bf08fbf3-a573-4f01-989e-ed93bf812857)

    Please type “Google Calendar API” in the search window and select “Google Calendar API”, and then enable Google Calendar API by clicking “ENABLE” button.

    ![image](https://github.com/caiofrota/pdf-scraper/assets/9461960/c462c006-5c55-450f-9f2d-3c491a76f77e)


3. Create Service Account on Google Cloud Platform. Service Account is for non-human users.

    Please move to “APIs & Services” > “Service Accounts”.

    ![image](https://github.com/caiofrota/pdf-scraper/assets/9461960/f0e28c6c-27a6-4ae8-9207-4c1cc6742339)

    And then please click “CREATE SERVICE ACCOUNT”.

    ![image](https://github.com/caiofrota/pdf-scraper/assets/9461960/ad8f6f40-c0e9-456b-b49c-3ad59810c187)

    Please input service account name and click “CREATE” button.

    ![image](https://github.com/caiofrota/pdf-scraper/assets/9461960/6afe705f-bb8e-4af3-ad95-2901acdc284a)
   
    Other things are optional. So, I’ll skip inputting them because this time is just test. Please click “CONTINUE” and “DONE” buttons.

    ![image](https://github.com/caiofrota/pdf-scraper/assets/9461960/2eb02142-9f16-4808-b319-08fa21b2b809)

6. Generate Service Account key.
   
    Please select “Actions” > “Manage keys” at Service Account page.
    
    ![image](https://github.com/caiofrota/pdf-scraper/assets/9461960/290ea921-3fe4-4eae-932d-3b89628c4829)
    
    Please click “ADD KEY” > “Create new key”.
    
    ![image](https://github.com/caiofrota/pdf-scraper/assets/9461960/0579e9ec-5e55-42fc-a37f-ba4df64b6d03)

    Please click “CREATE” button with “JSON” key type. After that, you can see a dialog box for save and please save and keep your key. The key will be used by Python script.

    ![image](https://github.com/caiofrota/pdf-scraper/assets/9461960/00d47657-c88c-42e6-902f-94d9d532e930)

7. Add Service Account to Google Calendar’s share member.

    Please copy Service Account email addoress.
    After that, Please open Google Calendar and move to “Settings and sharing”.

    ![image](https://github.com/caiofrota/pdf-scraper/assets/9461960/cc49ee3a-fb8d-4c6a-8a16-0301aa25789a)

    Please click “Add people” button at “Share with specific people”.

    ![image](https://github.com/caiofrota/pdf-scraper/assets/9461960/fe4e4d7d-2b31-461c-bb85-ac94eb6cf6f8)

    Please input your Service Account email address and click “Send” button.

    ![image](https://github.com/caiofrota/pdf-scraper/assets/9461960/da55d9ff-4129-4444-9289-40902b1a508e)

## Installation

This example uses Python 3.10.12 and pip 22.0.2

1. Install required libs
   
    ```pip install google-api-python-client google-auth pdfplumber```

2. Change the constants PDF_FILE, CREDENTIALS_FILE and CAL_ID.

   PDF_FILE is your PDF to be scraped
   
   CREDENTIALS_FILE is the file downloaded in the step 5 of the google pre-configuration

   CAL_ID is the Google Calendar Id you can get on calendar “Settings and sharing”
      
4. python3 scraper.py
5. See the magic!

## Example of PDF

![image](https://github.com/caiofrota/pdf-scraper/assets/9461960/c6b40d9f-74dc-4525-a5fa-aff31d66a55b)

## Contributing
Contributions are welcome! If you have ideas for improvements, bug fixes, or new features, please feel free to submit an issue or pull request.

## License
PDF Scraper is released under MIT License. Feel free to use, modify, and distribute the application as per the license terms.

## Disclaimer
This tool is intended for personal use. Users are responsible for adhering to the terms of service of the websites they scrape.
