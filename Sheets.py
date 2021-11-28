#Google Sheets API imports
from google.oauth2 import service_account
from oauth2client.service_account import ServiceAccountCredentials
import gspread
from pprint import pprint

import sendMail


SCOPES = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
SERVICE_ACCOUNT_FILE = 'cyb.json'

CREDS = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_FILE, SCOPES)

CYB_SPREADSHEET = "12XZR1ngkdj76rN2FidtCQ6bXl8K0ZKPuTIvJYyvgviU"

client = gspread.authorize(CREDS)
sheet = client.open('CYB').sheet1
data = sheet.get_all_records()

#Position of columns inside the google sheets
MAIL = 2
LASTNAME = 4
DATE = 5
TIME = 6
STATUS = 7

def SearchID(query):
    
        #Searches for the right email in the XU mail column
        #cellfind = sheet.find(query, in_column=2)
        #getRow(cellfind)
        col = sheet.col_values(MAIL)
        rownum = col.index(query) + 1 
        row = sheet.row_values(rownum)
        print(row)
        #name = row[2]
        #date = row[4]
        #time = row[5]
        #emailaddress = row[1]
        #sendMail.advisory(name, date, time, emailaddress)

def SearchLastName(query):
    col = sheet.col_values(LASTNAME)
    rownum = col.index(query) +1
    row = sheet.row_values(rownum)
    print(row)

    
    

def getRow(row_number):
    print('In Get Row')
    row = sheet.row_values(row_number)
    print(row)
