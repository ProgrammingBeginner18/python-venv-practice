from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from my FastAPI application!"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


def add(a, b):
    return a + b


# print("Hello from my Python project!")