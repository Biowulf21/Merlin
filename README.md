## Software Written By
## James Jilhaney - CYB 2022 Computer Systems Officer

# 🧙 Merlin 🧙
Merlin was designed to help the Crusader Yearbook to send formatted bulk emails to subscribers.

## Table of Contents
1. [Features](#Features)
1. [Dependencies](#Dependencies)
1. [Installation](#Installation)
1. [Usage](#Usage)
   1. [Bulk Emails](#Bulk)
   1. [Individual Emails](#Individual)
1.  [Customizing the Email Body](#Customizing the Email Body)
1. [FAQs](#FAQS)

## Features
- Send emails to individual subscribers
- Bulk send emails to multiple subscribers
- Custom emails based on user information
- Template System for Email Subject and Body
- Formatted emails through the use of markdown files
- Collaborate with teammates using the Google Sheets dependency file
- Real-time notification status change
## Dependencies
1. [SMTPEmail](https://docs.python.org/3/library/smtplib.html) - `pip3 install smtplib`
1. [Google Drive and Google Sheets API](https://www.youtube.com/watch?v=cnPlKLEGR7E&t=4s)
1. [Markdown](https://pypi.org/project/Markdown/) - `pip3 install markdown`
1. [PyQt5](https://pypi.org/project/PyQt5/) - `pip3 install PyQt5`
1. [OAuth2Client](https://pypi.org/project/oauth2client/) - `pip3 install google.oauth2`
1. [Gspread](https://pypi.org/project/gspread/) - `pip3 install gspread`  
## Installation
1. Clone the repository by typing: ``` git clone https://github.com/Biowulf21/Merlin.git```.
1. After typing cloning the repository, make sure to add the directory of the repository to your $PYTHONPATH environment variable by typing:
```export PYTHONPATH=/path/of/directory:${PYTHONPATH}```.
1. Make sure all dependencies are installed on your system.  
## Usage
### Bulk  
1. Change the email body by going into __Settings > Change Template > Email Body/Email Subject__ and change the contents there to change the content of either the email body or subject. Alternatively, you can go ahead and open the `compose.md` and `emailSubject.txt` files to change the body and subject respectively.   __Note:__ The email body should be written in markdown. For more information on how to use markdown, check out this [link](https://www.markdownguide.org/cheat-sheet/).
1. Input all necessary information in Google Sheet dependency file.
1. Copy the content of the __email column__ in the Google Sheet.
1. Press the __*Send Bulk Email*__ button.
1. Errors will be shown and sending will stop if the Merlin encounters errors, example, if the Google API detects too much usage (more on this on the [FAQs](#FAQ).
1. Check the progress by checking the progress bar indicator.
1. Merlin will prompt you if the sending is complete.
---
### Individual  
1. Change the email body by going into __Settings > Change Template > Email Body/Email Subject__ and change the contents there to change the content of either the email body or subject. Alternatively, you can go ahead and open the `compose.md` and `emailSubject.txt` files to change the body and subject respectively.   __Note:__ The email body should be written in markdown. For more information on how to use markdown, check out this [link](https://www.markdownguide.org/cheat-sheet/).
1. Input all necessary information in Google Sheet dependency file.
1. Search for the Subscriber by searching for the subscriber's last name or XU ID by inputting the information into the appropriate search box and pressing `Submit`.
1. If the user is in the Google Sheet Dependency File, Merlin will show all information relating to the subscriber.
1. Press the `Select Student` button to confirm the current student as the receipient.
1. Press the `Send Email` button to send the email to the subscriber.
1. . Errors will be shown and sending will stop if the Merlin encounters errors. Example, if the subscriber isn't found on the Google Sheet file, Merlin will throw an error.
---
### Customizing the Email Body
Customizing the email body by using information on the Merlin Google Sheet file is very easy. As of the moment, Merlin customizes the __NAME__, __DATE__, and __LINK__ columns from the Google sheet.
1. Every instance of the words above (__NAME__, __DATE__, __LINK__) will be replaced by the respective information from the Google Sheet file.
1. You can customize these words by changing these codeblocks:
    - ![ReplaceTemplate](https://user-images.githubusercontent.com/77718539/153858165-9bf1328d-d4fc-49e4-831d-9cffda6c6d88.png) - Line 108 of `Merlin.py` file.
    - ![image](https://user-images.githubusercontent.com/77718539/153858329-88310d84-fa65-48fc-ad77-721cf35360ca.png) - Line 159 of `Merlin.py` file.

## FAQ
1. __Q: How many emails can Merlin send bulk emails to?__  
__A:__ Merlin can send as many emails as needed as long as all information from the Google Sheet file is correct. Do keep in mind that Google API calls (Google Drive and Google Sheets) are limited and may cause errors if too many emails are being sent emails at once.
