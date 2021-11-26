from google.oauth2 import service_account
from oauth2client.service_account import ServiceAccountCredentials
import gspread
from pprint import pprint

import sendMail

from pyasn1.type.univ import Null

SCOPES = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
SERVICE_ACCOUNT_FILE = 'cyb.json'

CREDS = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_FILE, SCOPES)

CYB_SPREADSHEET = "12XZR1ngkdj76rN2FidtCQ6bXl8K0ZKPuTIvJYyvgviU"

client = gspread.authorize(CREDS)
sheet = client.open('CYB').sheet1
data = sheet.get_all_records()


def main():
    value = input('Enter an email:')
    SearchUser(value)


def getRow(row_number):
    print('In Get Row')
    row = sheet.row_values(row_number)
    print(row)

def SearchUser(query):
   
    #Searches for the right email in the XU mail column
    #cellfind = sheet.find(query, in_column=2)
    #getRow(cellfind)
    col = sheet.col_values(2)
    rownum = col.index(query) + 1
    row = sheet.row_values(rownum)
    name = row[2]
    date = row[4]
    time = row[5]
    emailaddress = row[1]
    sendMail.advisory(name, date, time, emailaddress)


if __name__ == "__main__":
  main()


