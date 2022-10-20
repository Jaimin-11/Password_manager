from Models.UserDataModel import UserDataModel


class App:

    # global class variables
    _filepath = "./TMP_DATA.csv"    # file path of main data(which can be changed/set from settings)
    _userDataOBJ = UserDataModel(_filepath)   # initializing _userDataOBJ object with providing file path

    def __init__(self):
        pass

# Function to take inputs for new data and packing it as a dictionary
    def newDataInput(self):
        domainName = input("domainName: ")
        domainAddress = input("domainAddress: ")
        userName = input("userName: ")
        email = input("email: ")
        password = input("password: ")
        securityQuestion = input("securityQuestion: ")
        securityAnswer = input("securityAnswer: ")

        # adding new entry to main DataDictionary object
        return [domainName, domainAddress, userName, email, password, securityQuestion, securityAnswer]

    # method to run the main application
    def run(self):
        # running main menu
        while (1):
            print("#---Password manager---# (version-0.1)")
            print("<------Main menu------>")
            print("Enter 'E' or 'e' as an input to exit the program")
            print("1. Show \t2. New entry")
            # variable to store user selected action through menu
            # obviously taken as string, to make all condition-handling smooth
            act = str(input("Enter option: "))
            if act == "e" or act == "E":
                exit(1)
            if act == "1":
                self._userDataOBJ.showAllaData()
            if act == "2":
                self._userDataOBJ.newEntry(*self.newDataInput())