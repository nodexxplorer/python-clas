import asyncio, aiohttp


# Synchronous and Asynchronous Code 

# Synchronous code runs in a single sequence, one operation at a time. Each task must complete before the next one starts. This can lead to delays if a task takes a long time, as everything else has to wait.

# Asynchronous code allows multiple operations to run concurrently. Instead of waiting for one task to finish before starting the next, asynchronous code can start a task and move on to other tasks while waiting for the first one to complete. This is especially useful for I/O-bound tasks like network requests, where waiting for a response can take time.

# In code: sync programs wait (do nothing) while a network request travels across the internet and comes back. Async programs use that waiting time to do other work — serving other users, making other requests, etc. there are many ways to write async code in Python, but the most common is using the asyncio library along with async/await syntax. This allows you to define asynchronous functions that can be paused and resumed, enabling efficient multitasking.


# import requests, time
 
# coins = ["bitcoin","ethereum","solana","cardano","dogecoin"]
# URL   = "https://api.coingecko.com/api/v3/simple/price"
 
# # ── SYNCHRONOUS: one at a time ──
# start = time.time()
 
# for coin in coins:
#     params   = {"ids": coin, "vs_currencies": "usd"}
#     response = requests.get(URL, params=params, timeout=10)
#     price    = response.json()[coin]["usd"]
#     print(f"  {coin}: ${price:,.2f}")
 
# elapsed = time.time() - start
# print(f"Sync took: {elapsed:.2f}s")



# 3 new keywords to learn: async def, await, asyncio

# async def: This is used to define an asynchronous function. It tells Python that the function will contain asynchronous operations and can be paused and resumed.

# Await: This keyword is used inside an asynchronous function to pause its execution until the awaited operation is complete. It allows other tasks to run while waiting.

# asyncio: This is a Python library that provides tools for writing asynchronous code. It includes an event loop that manages the execution of asynchronous tasks, allowing them to run concurrently.

# async def say_hello():
#     print("Hello")
#     await asyncio.sleep(5)
#     print("World")

# asyncio.run(say_hello())


# async def fetch_data(name, delay):
#     print(f"Fetching data for {name}...")
#     await asyncio.sleep(delay)
#     print(f"Data for {name} fetched after {delay} seconds.")
#     return f"Data for {name}"

# async def main():
#     results = await asyncio.gather(
#         fetch_data("Alice", 3),
#         fetch_data("Bob", 2),
#         fetch_data("Charlie", 1)
#     )
#     print("All data fetched:", results)
#     print("thanks and good bye")

# asyncio.run(main())

# note: await can only be used inside an async def function. using it outside will cause a SyntaxError. 

# def cow():
#     results = await asyncio.gather(
#         fetch_data("Alice", 3),
#         fetch_data("Bob", 2),
#         fetch_data("Charlie", 1)
#     )
#     print("All data fetched:", results)
#     print("thanks and good bye")

# cow() this is wrong


# async def fetch_price(coin):
#     params   = {"ids": coin, "vs_currencies": "usd"}
#     response = await requests.get(URL, params=params, timeout=10)
#     price    = response.json()[coin]["usd"]
#     print(f"  {coin}: ${price:,.2f}")
#     return price


# aiohttp is a popular library for making asynchronous HTTP requests in Python. It allows you to perform network operations without blocking the execution of your program, making it ideal for tasks like fetching data from APIs concurrently.
# To use aiohttp, you need to install it first using pip:
# pip install aiohttp



 
# async def fetch_price(session, coin):
#     """Fetch the USD price of one coin."""
#     url    = "https://api.coingecko.com/api/v3/simple/price"
#     params = {"ids": coin, "vs_currencies": "usd"}
#     async with session.get(url, params=params) as response:
#         data  = await response.json()
#         price = data[coin]["usd"]
#         return coin, price
 
# async def main():
#     coins = ["bitcoin","ethereum","solana","cardano","dogecoin"]
    
#     # ClientSession is like requests but async — reuse it for all calls
#     async with aiohttp.ClientSession() as session:
#         tasks   = [fetch_price(session, coin) for coin in coins]
#         results = await asyncio.gather(*tasks)   # run all at once
    
#     print("Crypto Prices (USD):")
#     for coin, price in results:
#         print(f"  {coin:<12}: ${price:>12,.4f}")
 
# asyncio.run(main())




 
# async def safe_fetch(session, url, params=None, label="request"):
#     """Fetch a URL safely — returns None on any error."""
#     try:
#         async with session.get(url, params=params, timeout=aiohttp.ClientTimeout(total=10)) as r:
#             if r.status == 200:
#                 return await r.json()
#             else:
#                 print(f"  [{label}] HTTP {r.status}")
#                 return None
#     except aiohttp.ClientConnectorError:
#         print(f"  [{label}] Connection error")
#         return None
#     except asyncio.TimeoutError:
#         print(f"  [{label}] Timed out")
#         return None

# async def main():
#     async with aiohttp.ClientSession() as session:
#         # Fetch weather and news at the same time
#         weather_data, news_data = await asyncio.gather(
#             # safe_fetch(session, "https://api.openweathermap.org/data/2.5/weather", params={"q": "Lagos", "appid": "YOUR_API_KEY"}, label="weather"),
#             safe_fetch(session, "https://hacker-news.firebaseio.com/v0/topstories.json", label="news"),
#         )
    
#     if weather_data:
#         temp = weather_data["current_condition"][0]["temp_C"]
#         print(f"Lagos temp: {temp}°C")
#     if news_data:
#         print(f"Top story ID: {news_data[0]}")
 
# asyncio.run(main())



# Webhook and polling
# Polling is a technique whereby a client  repeatedly check (polls) a server at regular intervals for new data or status update. Polling is like checking your phone for new messages every 30 seconds. Whether there is a message or not, you keep checking. Wasteful if messages are rare.

# types of polling: 
# 1. short polling, 
# 2. long polling


# short polling: The client sends a request to the server at regular intervals (e.g., every few seconds) to check for new data. If there is no new data, the server responds with an empty response or a "no new data" message. This can lead to unnecessary network traffic and increased server load if the polling frequency is high.

# example of short polling:
# import time
# import requests
# import asyncio
# import aiohttp

# # SYNCHRONOUS POLLING
# def poll_server_sync(url, interval=5, max_attempts=10):
#     """Poll a server every 5 seconds for new data"""
#     for attempt in range(max_attempts):
#         try:
#             response = requests.get(url)
#             if response.status_code == 200:
#                 data = response.json()
#                 if data.get('new_data'):
#                     print(f"New data received: {data}")
#                     return data
#                 else:
#                     print(f"Attempt {attempt + 1}: No new data")
#             else:
#                 print(f"Error: {response.status_code}")
#         except requests.RequestException as e:
#             print(f"Request failed: {e}")
        
#         time.sleep(interval)
    
#     print("Max attempts reached. No new data.")
#     return None

# poll_server_sync("https://api.example.com/data", interval=5, max_attempts=10)


# ASYNCHRONOUS POLLING
# async def poll_server_async(url, interval=5, max_attempts=10):
#     """Async polling with aiohttp"""
#     async with aiohttp.ClientSession() as session:
#         for attempt in range(max_attempts):
#             try:
#                 async with session.get(url) as response:
#                     if response.status == 200:
#                         data = await response.json()
#                         if data.get('new_data'):
#                             print(f"New data: {data}")
#                             return data
#                         print(f"Attempt {attempt + 1}: No new data")
#             except Exception as e:
#                 print(f"Error: {e}")
            
#             await asyncio.sleep(interval)
    
#     print("Polling exhausted")
#     return None

# # Example: Monitoring a job status
# def poll_job_status(job_id):
#     """Poll for job completion status"""
#     url = f"https://api.example.com/jobs/{job_id}/status"
#     poll_count = 0
    
#     while poll_count < 30:  # Max 30 attempts
#         response = requests.get(url)
#         if response.status_code == 200:
#             status = response.json()
            
#             if status['state'] == 'COMPLETED':
#                 print(f"Job {job_id} completed!")
#                 return status['result']
#             elif status['state'] == 'FAILED':
#                 print(f"Job {job_id} failed: {status.get('error')}")
#                 return None
#             else:
#                 print(f"Status: {status['state']} (Attempt {poll_count + 1})")
        
#         time.sleep(2)  # Wait 2 seconds between polls
#         poll_count += 1
    
#     return None


# long polling: The client sends a request to the server, and if there is no new data, the server holds the request open until new data becomes available or a timeout occurs. Once new data is available, the server responds immediately, and the client can process the data. This reduces unnecessary network traffic compared to short polling, as the client doesn't need to send frequent requests when there is no new data. However, it can still lead to some latency if the server takes time to respond.

# Webhooks: Webhooks are a more efficient alternative to polling. Instead of the client repeatedly checking for new data, the server sends an HTTP request (a webhook) to a predefined URL on the client whenever new data is available. This allows for real-time updates without the need for constant polling, reducing network traffic and server load. 
# 
# # 
# from flask import Flask, request, jsonify
# import json
# import hmac
# import hashlib
# from datetime import datetime

# app = Flask(__name__)
# WEBHOOK_SECRET = b"your-secret-key-here"  # Shared secret for verification

# # Store received webhooks for demonstration
# received_webhooks = []

# @app.route('/webhook', methods=['POST'])
# def handle_webhook():
#     """Handle incoming webhook requests"""
    
#     # 1. Verify the webhook signature (for security)
#     signature = request.headers.get('X-Webhook-Signature')
#     if not signature:
#         return jsonify({'error': 'Missing signature'}), 401
    
#     # Calculate expected signature
#     payload = request.get_data()
#     expected = hmac.new(WEBHOOK_SECRET, payload, hashlib.sha256).hexdigest()
    
#     if not hmac.compare_digest(signature, expected):
#         return jsonify({'error': 'Invalid signature'}), 401
    
#     # 2. Process the webhook payload
#     data = request.get_json()
#     if not data:
#         return jsonify({'error': 'Invalid JSON'}), 400
    
#     # 3. Log the webhook
#     print(f"Received webhook at {datetime.now()}")
#     print(f"Event type: {data.get('event')}")
#     print(f"Payload: {json.dumps(data, indent=2)}")
    
#     # 4. Process based on event type
#     event_type = data.get('event')
#     if event_type == 'order.created':
#         process_new_order(data.get('data'))
#     elif event_type == 'payment.succeeded':
#         process_payment_success(data.get('data'))
#     elif event_type == 'user.registered':
#         process_user_registration(data.get('data'))
    
#     # Store for later reference
#     received_webhooks.append({
#         'timestamp': datetime.now().isoformat(),
#         'data': data
#     })
    
#     # 5. Respond quickly (within 3-5 seconds)
#     return jsonify({'status': 'received'}), 200

# def process_new_order(order_data):
#     """Process new order events"""
#     order_id = order_data.get('id')
#     amount = order_data.get('amount')
#     print(f"Processing order {order_id} for ${amount}")

# def process_payment_success(payment_data):
#     """Process successful payment events"""
#     transaction_id = payment_data.get('transaction_id')
#     print(f"Payment successful: {transaction_id}")

# def process_user_registration(user_data):
#     """Process new user registration events"""
#     email = user_data.get('email')
#     print(f"New user registered: {email}")

# # Endpoint to view received webhooks
# @app.route('/webhooks', methods=['GET'])
# def get_webhooks():
#     """Retrieve received webhooks"""
#     return jsonify(received_webhooks)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)




# Rate Limiting: Rate limiting is a technique used to control the number of requests a client can make to a server within a specific time frame. It helps prevent abuse, ensures fair usage, and protects the server from being overwhelmed by too many requests. Rate limiting can be implemented using various strategies, such as token buckets, leaky buckets, or fixed windows.


# import requests, time
 
# def fetch_with_retry(url, params=None, max_retries=3):
#     """
#     Fetch a URL with exponential backoff retry.
#     Retries on 429 (rate limit) and 5xx (server errors).
#     """
#     delay = 1   # start with 1 second wait
 
#     for attempt in range(1, max_retries + 1):
#         try:
#             r = requests.get(url, params=params, timeout=10)
 
#             if r.status_code == 200:
#                 return r.json()
 
#             elif r.status_code == 429:
#                 retry_after = int(r.headers.get("Retry-After", delay))
#                 print(f"  Rate limited. Waiting {retry_after}s (attempt {attempt})")
#                 time.sleep(retry_after)
#             elif r.status_code >= 500:
#                 print(f"  Server error {r.status_code}. Retry in {delay}s (attempt {attempt})")
#                 time.sleep(delay)
#                 delay *= 2   # exponential backoff: 1s, 2s, 4s, 8s...
 
#             else:
#                 r.raise_for_status()   # 4xx errors we cannot retry
#                 return None
 
#         except requests.exceptions.Timeout:
#             print(f"  Timeout. Retry in {delay}s (attempt {attempt})")
#             time.sleep(delay)
#             delay *= 2
 
#         except requests.exceptions.ConnectionError:
#             print(f"  Connection error. Retry in {delay}s (attempt {attempt})")
#             time.sleep(delay)
#             delay *= 2
 
#     print(f"  Failed after {max_retries} attempts.")
#     return None
 
# # Usage
# data = fetch_with_retry("https://api.coindesk.com/v1/bpi/currentprice.json")

# assignment
# 1. Build an async program that monitors a list of coins, refreshes every 10 seconds, shows the % change since the LAST check (not 24h), saves each snapshot to a JSON log file with a timestamp, and prints a formatted table. Runs until you press Ctrl+C (handle KeyboardInterrupt gracefully).

#  2. Using asyncio.gather(), fetch these three things simultaneously and display the results. Measure how much faster it is than doing them one by one.
# import aiohttp, asyncio, time
 
# async def get_btc_price(session): ...
# async def get_top_news(session): ...
# async def get_weather(session, city="Lagos"): ...
 
# async def main():
#     start = time.time()
#     async with aiohttp.ClientSession() as session:
#         price, news, weather = await asyncio.gather(
#             get_btc_price(session),
#             get_top_news(session),
#             get_weather(session),
#         )
#     print(f"All fetched in {time.time()-start:.2f}s")
#     # Display results...
 
# asyncio.run(main())


# Structuring a multi file python project:
# 1. Create a project directory: my_project/    
# 2. Inside my_project/, create a subdirectory for your package: my_package/
# 3. Inside my_package/, create an __init__.py file (can be empty) to mark it as a package.
# 4. Create your module files (e.g., sync_async.py) inside my_package/.
# 5. Create a main.py file in the my_project/ directory to serve as the entry point of your application.
# 6. Optionally, create a requirements.txt file in my_project/ to list your dependencies (e.g., aiohttp).

# pip install -r requirements.txt

# my_project/
# ├── .env                   # secrets (never commit to git)
# ├── .gitignore             # list of files git should ignore
# ├── requirements.txt       # list of dependencies
# ├── README.md              # project description
# ├── main.py                # entry point — runs the app
# │
# ├── config.py              # loads .env, defines constants
# ├── api/                   # API-related code
# │   ├── __init__.py        # makes it a package
# │   ├── weather.py         # weather API calls
# │   ├── crypto.py          # crypto price API calls
# │   └── news.py            # news API calls
# │
# ├── utils/                 # shared utilities
# │   ├── __init__.py
# │   ├── cache.py           # JSON caching logic
# │   └── formatter.py       # display/formatting helpers
# │
# └── data/                  # local data files
#     └── cache.json         # cached API responses



