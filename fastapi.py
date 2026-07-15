# fastapi is a python framework for building APIs with Python 3.6+ based on standard Python type hints. It is built on top of Starlette for the web parts and Pydantic for the data parts. FastAPI is designed to be easy to use and to provide high performance, making it a great choice for building APIs quickly and efficiently., we can create a simple API using FastAPI.
# 
# uses of fastapi in real world applications:
# 1. Building RESTful APIs for web and mobile applications.
# 2. Creating data-driven APIs with automatic validation and documentation.
# 3. Building APIs with real-time functionality using WebSockets.
# 4. Creating APIs for machine learning models and data science applications.
# 5. Building microservices and serverless applications.
# 6. Creating APIs for IoT devices and edge computing applications.
# 7. building APIs for e-commerce platforms and online marketplaces.
# 8. Creating APIs for social media platforms and messaging applications.
# 9. Building APIs for financial and banking applications.
# 10. Building APIs for bot backends and chat applications.
# 



#  Below is an example of how to set up a basic FastAPI application:
# 1. Install FastAPI and Uvicorn (an ASGI server) using pip:
#    pip install fastapi uvicorn

# 2. Create a new Python file (e.g., main.py) and add the following code:
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def home():
#     return {"message": "Hello, World!"}

# 3. Run the application using Uvicorn:
#    uvicorn main:app --reload, or python -m uvicorn main:app --reload

# 4. Open your web browser and navigate to http://localhost:8000 , you should see the message "Hello, World!" displayed in JSON format.

# 5. You can also access the automatically generated API documentation by navigating to http://localhost:8000/docs or http://localhost:8000/redoc .
