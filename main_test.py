from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# 1. Required Test: Subtraction
def test_soustraction():
    response = client.post("/subtract?a=10&b=4")
    assert response.status_code == 200
    assert response.json()["result a-b="] == 6

# 2. Tests for your existing endpoints to get >90% coverage
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "it works !"}

def test_addition():
    response = client.get("/addition?a=5&b=5")
    assert response.status_code == 200
    assert response.json()["result a+b="] == 10

def test_multiply():
    response = client.post("/multiply?a=3&b=4")
    assert response.status_code == 200
    assert response.json()["result a*b="] == 12

def test_divide_success():
    response = client.post("/divide?a=10&b=2")
    assert response.status_code == 200
    assert response.json()["result a/b="] == 5.0

def test_divide_by_zero():
    response = client.post("/divide?a=10&b=0")
    assert response.status_code == 200
    assert response.json() == {"error": "Division by zero is not allowed"}

def test_delete_item():
    response = client.delete("/remove/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Item 1 deleted successfully"}

def test_update_item():
    response = client.put("/update/1?name=NewName")
    assert response.status_code == 200
    assert response.json() == {"message": "Item 1 updated successfully", "new_name": "NewName"}