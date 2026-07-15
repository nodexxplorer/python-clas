from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

app = FastAPI(title="Simple FastAPI Application", description="This is a simple FastAPI application that demonstrates the basic functionality of FastAPI.", version="1.0.0")

tasks = [
    {"id": 1, "title": "learn fastapi basics", "description": "This is the first task.", "completed": False},
    {"id": 2, "title": "build a simple api", "description": "This is the second task.", "completed": False},
    {"id": 3, "title": "deploy the api", "description": "This is the third task.", "completed": False},
]
next_id = 4

@app.get("/")
def home():
    return HTMLResponse(content=
    "<h1>Welcome to the Simple FastAPI Application!</h1>"
    "<p>This is a simple FastAPI application that demonstrates the basic functionality of FastAPI.</p>"
    "<a href='/about'>About</a>", status_code=200)

@app.get("/about")
def about():
    return HTMLResponse(content=
    "<h1>About</h1>"
    "<p>This is a simple FastAPI application.</p>"
    "<a href='/'>Home</a>" "<br>"
    "<a href='/tasks'>Tasks</a>", status_code=200)


@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.post("/tasks", status_code=201)
def create_task(title: str):
    global next_id
    new_task = {"id": next_id, "title": title, "description": "", "completed": False}
    next_id += 1
    return new_task

@app.put("/tasks/{task_id}")
def update_task(task_id: int, title: str = None, description: str = None, completed: bool = None):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        return {"error": "Task not found"}

    if title is not None:
        task["title"] = title
    if description is not None:
        task["description"] = description
    if completed is not None:
        task["completed"] = completed

    return task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    global tasks
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    tasks = [t for t in tasks if t["id"] != task_id]
    return {"message": "Task deleted successfully"} 

from fastapi import FastAPI, HTTPException
 
app = FastAPI(title="Student Grades API")
 
students = {
    1: {"name":"Fortune","scores":[92,85,78]},
    2: {"name":"Ada",    "scores":[88,90,76]},
}
next_id = 3
 
@app.get("/students")
def get_all():
    """Get all students with their average score."""
    result = []
    for sid, data in students.items():
        avg = sum(data["scores"]) / len(data["scores"])
        result.append({"id":sid,"name":data["name"],"average":round(avg,2)})
    return result
 
@app.get("/students/{student_id}")
def get_one(student_id: int):
    if student_id not in students:
        raise HTTPException(404, f"Student {student_id} not found")
    data = students[student_id]
    avg  = sum(data["scores"]) / len(data["scores"])
    return {"id":student_id,"name":data["name"],"scores":data["scores"],"average":round(avg,2)}
 
@app.post("/students", status_code=201)
def add_student(name: str, score: float):
    global next_id
    students[next_id] = {"name":name,"scores":[score]}
    new_id = next_id; next_id += 1
    return {"id":new_id,"name":name,"scores":[score]}
 
@app.post("/students/{student_id}/scores")
def add_score(student_id: int, score: float):
    if student_id not in students:
        raise HTTPException(404, "Student not found")
    students[student_id]["scores"].append(score)
    return {"message":"Score added","scores":students[student_id]["scores"]}
 
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        raise HTTPException(404, "Student not found")
    del students[student_id]
    return {"message":f"Student {student_id} removed"}


# for product catalogue, we can create a simple API using FastAPI. The API will have endpoints to get all products, get a specific product by ID, add a new product, update an existing product, and delete a product. The product information will include ID, name, price, stock quantity, and category.

from fastapi import FastAPI, HTTPException
 
app = FastAPI(title="Product Catalogue")
 
products = [
    {"id":1,"name":"Indomie Noodles","price":150,"stock":500,"category":"Food"},
    {"id":2,"name":"Peak Milk",       "price":350,"stock":200,"category":"Food"},
    {"id":3,"name":"USB Cable",        "price":800,"stock":100,"category":"Electronics"},
]
next_id = 4

@app.get("/products")
def get_products(category: str = None):
    """Get all products. Filter by category if provided."""
    if category:
        return [p for p in products if p["category"].lower()==category.lower()]
    return products
 
@app.get("/products/{product_id}")
def get_product(product_id: int):
    for p in products:
        if p["id"]==product_id: return p
    raise HTTPException(404,"Product not found")
 
@app.post("/products",status_code=201)
def add_product(name:str,price:float,stock:int,category:str):
    global next_id
    new = {"id":next_id,"name":name,"price":price,"stock":stock,"category":category}
    products.append(new); next_id+=1
    return new
 
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for i,p in enumerate(products):
        if p["id"]==product_id:
            products.pop(i)
            return {"message":f"{p['name']} deleted"}
    raise HTTPException(404,"Product not found")




# create a /get.product, /get.student and /get.contact endpoint that returns a contact information in JSON format. The contact information should include name, email, address, and phone number.
# what is the difference between taskcreate and taskupdate endpoints in the above code?The difference between the `create_task` and `update_task` endpoints in the provided FastAPI code.