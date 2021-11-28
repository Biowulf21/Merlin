
#Subscriber Class
class Subscriber():

    def __init__(self, fname, lname, email, date, time, phoneNumber, status):
        self._firstName = fname 
        self._lastName = lname
        self._Email = email
        self._Date = date
        self._Time = time
        self._PhoneNumber = phoneNumber
        self._Status = status
    @property
    def getLastName(self):
        #print('Called last name getter')
        return self._lastName

    @property
    def getFirstName(self):
        return self._firstName

    @property
    def getDate(self):
        return self._Date
    
    @property
    def getTime(self):
        return self._Time
    @property
    def getStatus(self):
        return self._Status

    @property
    def getPhoneNumber(self):
        return self._PhoneNumber
    
    @property
    def getEmail(self):
        return self._Email
    