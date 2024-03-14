from datetime import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build
import pdfplumber

CAL_ID = "<add your calendar id here>@group.calendar.google.com"
PDF_FILE = "path/to/your/file.pdf"
CREDENTIALS_FILE = "path/to/your/credentials.json"
TIMEZONE = "America/Fortaleza"

SCOPES = ["https://www.googleapis.com/auth/calendar"]

def get_calendar_service():
  credentials = service_account.Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPES)
  service = build("calendar", "v3", credentials=credentials)
  return service

def get_events(file):
  events = []
  with pdfplumber.open(file) as pdf:
    for page in pdf.pages:
      for row in page.extract_table():
        # Check if columns match with your PDF and change if need. In my case I have the following format:
        if row[3] and row[3] != "EVENTOS":
          d = dict()
          d["start"] = row[1]
          d["end"] = row[1]
          d["event"] = row[3]
          events.append(d)
  return events

def main():
  service = get_calendar_service()
  for event in get_events(PDF_FILE):
    id = f"{event['event']}"
    found = service.events().list(calendarId=CAL_ID, iCalUID=id, showDeleted=True).execute().get("items")
    
    start_date = datetime.strptime(f"{event['start']}", "%d/%m/%Y").strftime("%Y-%m-%d")
    end_date = datetime.strptime(f"{event['end']}", "%d/%m/%Y").strftime("%Y-%m-%d")
    
    if found:
      service.events().update(
        calendarId=CAL_ID,
        eventId=found[0]["id"],
        body={
          "summary": f"{event['event']}",
          "description": f"{event['event']}",
          "start": {"date": f"{start_date}", "timeZone": TIMEZONE},
          "end": {"date": f"{end_date}", "timeZone": TIMEZONE}
        }
      ).execute()
      print(f"{event['start']} - {event['end']} | {event['event']}", "updated")
    else:
      service.events().insert(calendarId=CAL_ID,
        body={
          "summary": event['event'],
          "description": event['event'],
          "start": {"date": start_date, "timeZone": TIMEZONE},
          "end": {"date": end_date, "timeZone": TIMEZONE},
          "iCalUID": event['event']
        }
      ).execute()
      print(f"{event['start']} - {event['end']} | {event['event']}", "created")

def clear_events(): # BE CAREFUL, IT DELETES ALL EVENTS
  service = get_calendar_service()
  for event in service.events().list(calendarId=CAL_ID).execute().get("items"):
    service.events().delete(calendarId=CAL_ID, eventId=event["id"]).execute()
    print({event['id']}, "deleted")

#clear_events() # BE CAREFUL, IT DELETES ALL EVENTS
main()
