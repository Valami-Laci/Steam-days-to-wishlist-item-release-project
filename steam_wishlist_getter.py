import json
import requests
import datetime
import sys
import os


# https://store.steampowered.com/wishlist/profiles/<userid>/wishlistdata/?p=0 - wishlist
# http://api.steampowered.com/ISteamApps/GetAppList/v0002/ - list of all game ids
# http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=XXXXXXXXXXXXXXXXX&steamid=76561197960434622&format=json - list of owned games

def gameid_to_name(gameid):
     """Finds the name of the game based on the game id"""
     with open (f"steam_list_of_apps.json", "rt", encoding = "utf-8") as input_json:
          steam_list_of_apps = json.load(input_json)
          for i in steam_list_of_apps['applist']['apps']:
               if i['appid'] == gameid:
                    return i['name']


class SteamUser:
    def __init__(self, username, userid, user_api_key = None):
        self.username = username
        self.userid = userid
        self.user_api_key = user_api_key

    def check_user_data(self):
        print(f"The current user is: \n"
              f"Username: {self.username}\n"
              f"userid: {self.userid}\n"
              f"api key: {self.user_api_key}\n")
        
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

    def check_owned_games(self):
        response = requests.get(f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={self.user_api_key}&steamid={self.userid}&format=json")
        owned_games = response.json()
        for i in owned_games['response']['games']:
          print(f"{i['appid']}: {gameid_to_name(i['appid'])} : {i['playtime_forever'] / 60:.2f}H")


dictionary_of_users = {}

def save_user(steam_user):
     if os.path.exists("steam_users.json"):
          with open (f"steam_users.json", "at", encoding = "utf-8") as output_json:
               json.dump(steam_user, output_json)
     
     else:
          with open (f"steam_users.json", "wt", encoding = "utf-8") as output_json:
               json.dump(steam_user, output_json)

def load_user():
     with open (f"steam_users.json", "rt", encoding = "utf-8") as input_json:
          dictionary_of_users = json.load(input_json)
          
     for key, value in dictionary_of_users.items():
          print(f"Userid: {key}, name : {value[0]}, api key : {value[1]}")
     print(f"Please choose the Userid you wish to load")
     user_id_choice = input("Your choice:")  
     if user_id_choice in dictionary_of_users:
          user_chosen_profile = (user_id_choice, dictionary_of_users[user_id_choice][0], dictionary_of_users[user_id_choice][1])        
          return user_chosen_profile
     else:
          print(f"No user with the following id was found: {user_id_choice}")
          user_selection_menu()

def delete_user():
     with open(f"steam_users.json", "rt", encoding = "utf-8") as input_json:
          dictionary_of_users = json.load(input_json)
     for key, value in dictionary_of_users.items():
          print(f"Userid: {key}, name : {value[0]}, api key : {value[1]}")
     
     print(f"Please choose the Userid you wish to delete")
     user_id_choice = input("Your choice:")
     if user_id_choice in dictionary_of_users:
          print(f"User {dictionary_of_users[user_id_choice][0]} is deleted from the profile list.")
          del dictionary_of_users[user_id_choice]

          if dictionary_of_users == {}:
               os.remove("steam_users.json")
          
          else:
               with open (f"steam_users.json", "wt", encoding = "utf-8") as output_json:
                    json.dump(dictionary_of_users, output_json)

     else:
          print(f"No user with the following id was found: {user_id_choice}")

def user_selection_menu():
     while True:
          print("\nPlease choose from the actions below:\n"
                    "1. enter user\n"
                    "2. load in user\n"
                    "3. delete user\n"
                    "4. Exit\n")
          
          user_choice = input("Your decision:")
          if user_choice == "1":
               input_username = input("Please enter the username: ")
               input_userid = input("Please enter the userid: ")
               input_user_api = input("Please enter your API key (optional): ")
               steam_user = SteamUser(input_username, input_userid, input_user_api)
               dictionary_of_users[steam_user.userid] = [steam_user.username, steam_user.user_api_key]
               user_action_menu(steam_user)

          elif user_choice == "2":
               user_id, user_name, user_api = load_user()
               steam_user = SteamUser(user_name, user_id, user_api)
               user_action_menu(steam_user)

          elif user_choice == "3":
               delete_user()
          
          elif user_choice == "4":
               sys.exit()

          else:
               print("Unacceptable command")

def user_action_menu(steam_user):
     while True:
          print(f"\n{steam_user.username} please choose from the actions below:\n"
               f"1. Check user data\n"
               f"2. Check wishlist\n"
               f"3. Check owned games\n"
               f"4. Save user\n"
               f"5. Change user\n"
               f"6. Exit")

          user_action = input("Your decision:")
          if user_action == "1":
               steam_user.check_user_data()
          
          elif user_action == "2":
               steam_user.check_wishlist()

          elif user_action == "3":
               steam_user.check_owned_games()
          
          elif user_action == "4":
               save_user(dictionary_of_users)

          elif user_action == "5":
               user_selection_menu()
               break
          
          elif user_action == "6":
               sys.exit()

          else:
               print("Unacceptable command")



print("Welcome to the Steam wishlist database\n")
user_selection_menu()