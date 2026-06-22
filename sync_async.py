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




 
async def safe_fetch(session, url, params=None, label="request"):
    """Fetch a URL safely — returns None on any error."""
    try:
        async with session.get(url, params=params, timeout=aiohttp.ClientTimeout(total=10)) as r:
            if r.status == 200:
                return await r.json()
            else:
                print(f"  [{label}] HTTP {r.status}")
                return None
    except aiohttp.ClientConnectorError:
        print(f"  [{label}] Connection error")
        return None
    except asyncio.TimeoutError:
        print(f"  [{label}] Timed out")
        return None

async def main():
    async with aiohttp.ClientSession() as session:
        # Fetch weather and news at the same time
        weather_data, news_data = await asyncio.gather(
            # safe_fetch(session, "https://api.openweathermap.org/data/2.5/weather", params={"q": "Lagos", "appid": "YOUR_API_KEY"}, label="weather"),
            safe_fetch(session, "https://hacker-news.firebaseio.com/v0/topstories.json", label="news"),
        )
    
    if weather_data:
        temp = weather_data["current_condition"][0]["temp_C"]
        print(f"Lagos temp: {temp}°C")
    if news_data:
        print(f"Top story ID: {news_data[0]}")
 
asyncio.run(main())
