#Google Sheets API imports
from google.oauth2 import service_account
from oauth2client.service_account import ServiceAccountCredentials
import gspread
from pprint import pprint



SCOPES = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
SERVICE_ACCOUNT_FILE = 'cyb.json'

CREDS = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_FILE, SCOPES)

CYB_SPREADSHEET = "12XZR1ngkdj76rN2FidtCQ6bXl8K0ZKPuTIvJYyvgviU"

client = gspread.authorize(CREDS)
sheet = client.open('CYB').sheet1
data = sheet.get_all_records()


#FIXME: No way to edit status of subscriber in google sheets

def WriteStatus(query):
    newStatus = "Notified"
    column = sheet.col_values(8)
    searchUpdateStatus(query)
    #print(column)


def searchUpdateStatus(query):
    #Searches for the cell based on ID number and finds its specific row
    findName = sheet.find(query).row
    #print(f"cell position is {findName}")
    #Searches for the 
    print(f"before value is {sheet.cell(findName, 8).value}")
    sheet.update_cell(findName, 8, 'Notified')
    print(f"after value is {sheet.cell(findName, 8).value}")


def SearchID(query):
    
    #Searches for the right email in the XU mail column
    col = sheet.col_values(2)
    rownum = col.index(query) + 1 
    row = sheet.row_values(rownum)
    #print(row)
    #name = row[2]
    #date = row[4]
    #time = row[5]
    #emailaddress = row[1]
    return row

def SearchLastName(query):
    col = sheet.col_values(4)
    rownum = col.index(query) +1
    row = sheet.row_values(rownum)
    print(row)
    return row

    
    

def getRow(row_number):
    print('In Get Row')
    row = sheet.row_values(row_number)
    print(row)
