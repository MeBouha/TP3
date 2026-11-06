from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "it works !"}

@app.get("/addition")
def add_numbers(a: int, b: int):
    return {"result a+b=": a + b, "developer": "Dev1"}


@app.post("/multiply")
def multiply_numbers(a: int, b: int):
    return {"result a*b=": a * b, "developer": "Dev2"}


@app.post("/divide")
def divide_numbers(a: int, b: int):
    if b == 0:
        return {"error": "Division by zero is not allowed"}
    return {"result a/b=": a / b, "developer": "Leader"}


@app.delete("/remove/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item {item_id} deleted successfully"}

@app.put("/update/{item_id}")
def update_item(item_id: int, name: str):
    return {"message": f"Item {item_id} updated successfully", "new_name": name}
@app.post("/subtract")
def subtract_numbers(a: int, b: int):
    return {"result a-b=": a - b, "developer": "Ahmed"}