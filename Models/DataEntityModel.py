class DataEntityModel:

    # initiating object
    def __init__(self, domainName, domainAddress, userName, email, password, securityQuestion, securityAnswer):
        self._domainName = domainName
        self._domainAddress = domainAddress
        self._userName = userName
        self._email = email
        self._password = password
        self._securityQuestion = securityQuestion
        self._securityAnswer = securityAnswer

    # function to update the current data
    def updateData(self, newData):    
        self._domainName = newData.domainName
        self._domainAddress = newData.domainAddress
        self._userName = newData.userName
        self._email = newData.email
        self._password = newData.password
        self._securityQuestion = newData.securityQuestion
        self._securityAnswer = newData.securityAnswer
    
    # pack and return all variable data as one dictionday-entity
    def packEntity(self):
        entity = {
            'domainName': self._domainName,
            'domainAddress': self._domainAddress,
            'userName': self._userName,
            'email': self._email,
            'password': self._password,
            'securityQuestion': self._securityQuestion,
            'securityAnswer': self._securityAnswer
        }
        return entity