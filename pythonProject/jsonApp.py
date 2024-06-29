import json
import os
class User:
    def __init__(self,username,password,email):
        self.username = username
        self.password=password
        self.email =email


class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}
        self.loadUsers()

    def loadUsers(self):
        if os.path.exists("users.json"):
            with open("users.json", "r", encoding="utf-8") as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    newUser = User(user["username"], user["password"], user["email"])
                    self.users.append(newUser)
                print(self.users)
    def register(self,user:User):
        self.users.append(user)
        self.saveToFile()
        print("User Created!!")
    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print("Logged In")
                break
    def logout(self):
        self.IsloggedIn = False
        self.currentUser = {}
        print("Logged Out")

    def identity(self):
        if self. isLoggedIn :
            print(f"Username : {self.currentUser.username}")
        else:
            print("You are not logged in")

    def saveToFile(self):
        list = []
        for user in self.users:
            list.append(json.dumps(user.__dict__))

        with open("users.json","w")as file:
            json.dump(list, file)


repo = UserRepository()


while True:
    print("Menu".center(50,"*"))
    choice = input("1-Register\n2-Login\n3-Logout\n4-Identity\n5-Exit\n")
    if choice == "5":
        break
    else:
        if choice == "1":
            username = input("Username: ")
            password = input("Password: ")
            email = input("E-mail: ")

            user = User(username,password,email)
            repo.register(user)
        elif choice == "2":
            if not repo.isLoggedIn:
                username = input("Username: ")
                password = input("Password: ")
                repo.login(username, password)
            else:
                print("You already logged in")
        elif choice == "3":
            repo.logout()
        elif choice == "4":
            repo.identity()
        else:
            print("Invalid Choice!!")