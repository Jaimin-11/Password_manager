from Models.DataEntityModel import DataEntityModel


class UserDataModel:

    _DATALIST = []
    
    # user basic information
    _userName = "Jaimin"    # user name
    _userEmail = "ds"   # user email

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.retrieveMainData()

    # Sign up function
    def signpUp(self):
        pass

    def signIn(self, ):
        pass

    # retrieve from database
    def retrieveMainData(self):
         with open(self.file_path, "r") as filehandle:
            filecontent = filehandle.readlines()

            for line in filecontent:
                # using * to unpack and pass list/tuple values- use ** incase of dictionary
                self._DATALIST.append(DataEntityModel(*line.strip().split(",")))

    def newEntry(self, domainName: str, domainAddress: str, userName: str, email: str, password: str, securityQuestion: str, securityAnswer: str):
        self._DATALIST.append(DataEntityModel(domainName, domainAddress, userName, email, password, securityQuestion, securityAnswer))
        return

    # method to sync current data to stored data at database(update database with latest data)
    def sync(self):
        pass

    def showAllaData(self):
        if len(self._DATALIST)==0:
            print("No records to show. Add new record via 'New entry' option...")
            return
        i=1
        for d in self._DATALIST:
            print(f"Data record-{i}")
            i+=1
            tmp = d.packEntity()
            for key in tmp:
                print(f"   {key}: {tmp[key]}")
            print(end="\n")