# import json
# import requests
# import datetime

# def get_wishlist_from_url(userid):
#       response = requests.get(f"https://store.steampowered.com/wishlist/profiles/{userid}/wishlistdata/?p=0")
#       steam_wishlist = response.json()
#       print(f"{'Game id' : <10} : {'Game name' : ^50} : {'release date' : <15}")
#       for key in steam_wishlist:
#             if steam_wishlist[key]['release_string'] == "Coming soon":
#                   print(f"{key : <10} : {steam_wishlist[key]['name'] : ^50} : {steam_wishlist[key]['release_string'] : <15}")
#             else:
#                   release_date = datetime.datetime.fromtimestamp(int(steam_wishlist[key]['release_date'])).strftime('%Y-%m-%d')
#                   print(f"{key : <10} : {steam_wishlist[key]['name'] : ^50} : {release_date : <15}")
#             # if steam_wishlist[key]['release_string'] == "coming soon":
#                   # print(f"{key : <10} : {steam_wishlist[key]['name'] : ^50} : {steam_wishlist[key]['release_string'] : <15}")
#             # else:
#                   # release_date = datetime.datetime.fromtimestamp(int(steam_wishlist[key]['release_date'])).strftime('%Y-%m-%d')
#                   # print(f"{key : <10} : {steam_wishlist[key]['name'] : ^50} : {release_date : <15}")


# id = input()
# get_wishlist_from_url(id)

# def get_wishlist_from_file(filename):
#       with open(f"{filename}", "rt", encoding="utf-8") as input_json:
#             steam_wishlist = json.load(input_json)
#       print(f"{'Game id' : <10} : {'Game name' : ^50} : {'release date' : <15}")
#       for key in steam_wishlist:
#             print(f"{key : <10} : {steam_wishlist[key]['name'] : ^50} : {steam_wishlist[key]['release_string'] : <15}")

# given_filename = input()
# get_wishlist_from_file(given_filename)

# user_input = int(input())
# date = datetime.datetime.fromtimestamp(user_input).strftime('%Y-%m-%d')
# print(date)

# def menu(options):
#     while True:
#         print("Please select an option:")
        
#         for i, option in enumerate(options, start=1):
#             print(f"{i}. {option}")
        
#         try:
#             choice = int(input("Enter the number of your choice: "))
            
#             if 1 <= choice <= len(options):
#                 return options[choice - 1]
#             else:
#                 print("Invalid choice. Please try again.")
                
#         except ValueError:
#             print("Invalid input. Please enter a number.")

# # Define your options as a list of strings
# options = ["Option 1", "Option 2", "Option 3", "Option 4"]

# # Call the menu function with the options list
# selected_option = menu(options)

# print(f"You have selected: {selected_option}")