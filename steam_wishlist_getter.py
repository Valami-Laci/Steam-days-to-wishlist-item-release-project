import json
import requests
import datetime


# https://store.steampowered.com/wishlist/profiles/<userid>/wishlistdata/?p=0
class SteamUser:
    def __init__(self, username, userid):
        self.username = username
        self.userid = userid

    def check_user_data(self):
        print(f"The current user is: \n"
              f"Username: {self.username}, userid: {self.userid}")
        
    def check_wishlist(self):
        response = requests.get(f"https://store.steampowered.com/wishlist/profiles/{self.userid}/wishlistdata/?p=0")
        steam_wishlist = response.json()
        print(f"{'Game id' : <10} : {'Game name' : ^50} : {'release date' : <15}")
        for key in steam_wishlist:
                if steam_wishlist[key]['release_string'] == "Coming soon":
                    print(f"{key : <10} : {steam_wishlist[key]['name'] : ^50} : {steam_wishlist[key]['release_string'] : <15}")
                else:
                    release_date = datetime.datetime.fromtimestamp(int(steam_wishlist[key]['release_date'])).strftime('%Y-%m-%d')
                    print(f"{key : <10} : {steam_wishlist[key]['name'] : ^50} : {release_date : <15}")



dictionary_of_users = {}
print("Welcome to the Steam wishlist database\n")
while True:
    print("Please choose from the actions below:\n"
          "1. Check users in the database\n"
          "2. Add a new user to the database\n"
          "3. Remove a user from the database\n"
          "4. Check a user's wishlist\n"
          "5. Exit\n")
    user_choice = input("Your decision:")
    if user_choice == "1":
         for key, value in dictionary_of_users.items():
             print(f"userid: {key}, username: {value}")

    elif user_choice == "2":
         input_username = input("Please enter the username: ")
         input_userid = input("Please enter the userid: ")
         new_steam_user = SteamUser(input_username, input_userid)
         dictionary_of_users[input_userid] = new_steam_user.username

    elif user_choice == "3":
         break
    
    elif user_choice == "4":
         break
    
    elif user_choice == "5":
         break
    
    else:
         print("Unacceptable command")


