# REST APIs & the requests Library

# This module provides the implementation of the API endpoints for the application. It defines the routes and the logic for handling incoming requests and returning appropriate responses.
# REST API stands for Representational State Transfer Application Programming Interface.
# API stands for Application Programming Interface. It’s a set of rules that allows one piece of software to interact with another. An API defines how requests should be made, what data formats to use, and what responses to expect.
# In plain English: a REST API is a way for one program to ask another program for information or to do something, without needing to know how the other program works inside. On the web, most REST APIs work over the internet using HTTP — the same system your browser uses to load websites. You send a request to a URL, and the API sends back data (usually in JSON format).

# Your Python Program  →  (HTTP Request)  →  API Server  →  Database
# Your Python Program  ←  (JSON Response) ←  API Server





# HTTP Methods 
# HTTP is the language computers use to talk over the internet. Every request has a "method" — a word that describes what action you want to do. There are four main ones:
# •	GET    → Read/fetch data  (like opening a webpage)
# •	POST   → Send new data    (like submitting a form)
# •	PUT    → Replace data     (like re-uploading a profile)
# •	DELETE → Remove data      (like deleting your account)

# Method	    Simple Meaning	        Example Use	                                  Sends Data?
# GET	        Get information from the server	Fetch BTC price, get weather	            No
# POST	    Send new information to the server	Login, create account, place order	  Yes
# PUT	        Replace existing information	Update full profile	                       Yes
# PATCH	    Update part of existing info	Change just email address	               Yes
# DELETE	    Remove information	Delete a post, close account	                        No

# Status Codes 
# When you make a request to an API, it responds with a status code — a three-digit number that tells you what happened. 

# there are 5 groups of status codes:
# 1xx	Informational (rarely used)
# 2xx	Success (everything went well)
# 3xx	Redirection (the resource has moved)
# 4xx	Client Error (you did something wrong)
# 5xx	Server Error (the server messed up)

# Status Code	Description
# 200 OK	The request was successful, and the server is returning the requested data.
# 201 Created	Your POST worked and created something new on the server.
# 404 Not Found	The requested resource was not found.
# 400 Bad Request	Your request is broken — missing a field, wrong format, etc.
# 401 Unauthorized	You did not send an API key, or the key is wrong or expired.
# 403 Forbidden	You are logged in but not allowed to do that action.
# 404 Not Found	That URL or resource does not exist. Check your spelling.
# 429 Too Many	You sent too many requests. The API is telling you to slow down.
# 500 Internal Server Error	The server encountered an error while processing the request.

# Requests and Responses
# Requests is a popular Python library for making HTTP requests. It allows you to send HTTP requests using Python and handle the responses easily. You can use it to interact with APIs, scrape websites, or automate any task that involves making HTTP requests.

# REQUEST has 4 parts:
# •	1. Method + URL  (what you want to do + where to go)
# •	2. Headers       (metadata — who you are, your API key, what format you want)
# •	3. Parameters    (filters — added to the URL after a ?)
# •	4. Body          (data you are sending — only for POST/PUT/PATCH)


# Response has 3 main parts:
# •	Status Code (what happened)
# •	Headers     (metadata about the response)
# •	Body          (the actual data — usually JSON)


# import requests

# response = requests.get("https://api.github.com/users/nodexxplorer")
 
# # Step 2: Check — did it work?
# print(response.status_code)    # should print 200
 
# # Step 3: Get the data (converts JSON text into a Python dict)
# data = response.json()
 
# # Step 4: Use the data like any Python dict
# print(data["name"])           # Linus Torvalds
# print(data["public_repos"])   # number of his public repos
# print(data["followers"])      # how many people follow him
# print(data["created_at"])    # when he joined GitHub
# print(data["html_url"])     # link to his GitHub profile
# print(data["avatar_url"])   # link to his profile picture
# print(data["bio"])        # his bio/description
# print(data["location"])   # where he’s located
# print(data["company"])    # his company/organization
# # print(data["collaborators"]) # list of his collaborators (if available )



# pip install requests

import requests

# # WITH params dict — cleaner, safer, requests handles encoding
# url    = "https://api.openweathermap.org/data/2.5/weather"
# params = {
#     "q":     input("Enter city name: ").strip(),
#     "units": "metric",
#     "appid": "f14d1f442a0a9828f07416116a0f4f6e",
# }
 
# response = requests.get(url, params=params, timeout=10)
 
# # Print the full URL requests built (useful for debugging)
# print(response.status_code)
 
# if response.status_code == 200:
#     data   = response.json()
#     city   = data["name"]
#     temp   = data["main"]["temp"]
#     humid  = data["main"]["humidity"]
#     desc   = data["weather"][0]["description"]
#     wind   = data["wind"]["speed"]
#     # uv     = data["weather"][0]["uvi"]
#     print(f"City:      {city}")
#     print(f"Temp:      {temp}°C")
#     print(f"Humidity:  {humid}%")
#     print(f"Condition: {desc}")
#     print(f"Wind Speed: {wind} m/s")
#     # print(f"UV Index:  {uv}")

# else:
#     print(f"Error: {response.status_code}")

# handling errors the right way is important — you don’t want your program to crash just because the API is down or you made a typo in the city name. Always check the status code before trying to use the data, and consider adding try/except blocks to catch exceptions that may occur during the request.



# def get_github_user(username):
#     try:
#         url = f"https://api.github.com/users/{username}"
#         response = requests.get(url, timeout=10)
#         response.raise_for_status()  # Raises an HTTPError if the status code is 4xx or 5xx
#         return response.json()
#     except requests.RequestException as e:
#         if e.response.status_code == 404:
#             print(f"User '{username}' not found on GitHub.")
#         elif e.response.status_code == 401:
#             print("Unauthorized access. Check your API key.")
#         elif e.response.status_code == 403:
#             print("Forbidden. You don't have permission to access this resource.")
#         elif e.response.status_code == 429:
#             print("Too many requests. Please slow down.")
#         else:
#             print(f"An error occurred: {e}")
    
#     except requests.Timeout:
#         print("The request timed out. Please try again later.") 

#     except requests.ConnectionError:
#         print("A connection error occurred. Please check your internet connection and try again.")

# user = get_github_user(input("Enter GitHub username: ").strip())
# if user:
#     print(f"Name: {user['name']}")
#     print(f"Public Repos: {user['public_repos']}")
#     print(f"Followers: {user['followers']}")
#     print(f"Joined GitHub: {user['created_at']}")



 
def get_exchange_rates(base="USD"):
    """Get live exchange rates for a base currency."""
    url    = "https://open.er-api.com/v6/latest/" + base
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    data = r.json()
    return data["rates"]
rates = get_exchange_rates("USD")
 
currencies = ["NGN", "GHS", "KES", "ZAR", "EUR", "GBP"]
print("Exchange Rates (1 USD = ?):")
for currency in currencies:
    if currency in rates:
        print(f"  {currency}: {rates[currency]:,.2f}")


 






























