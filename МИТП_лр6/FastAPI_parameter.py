from fastapi import FastAPI

app = FastAPI()

@app.get("/hello/{name}")
def hello_name(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "name": f"User {user_id}"}

@app.get("/books/{category}/{book_id}")
def get_book(category: str, book_id: int):
    return {
        "category": category,
        "book_id": book_id,
        "title": f"Book {book_id} in {category}"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
