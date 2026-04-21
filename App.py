from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Add API")


class AddRequest(BaseModel):
    a: float
    b: float


class AddResponse(BaseModel):
    result: float
    message: str


def add(a, b):
    return a + b


@app.post("/add", response_model=AddResponse)
def add_endpoint(request: AddRequest):
    result = add(request.a, request.b)
    return AddResponse(
        result=result,
        message=f"The sum of {request.a} and {request.b} is: {result}"
    )


@app.get("/")
def root():
    return {"message": "Welcome to the Add API. Use POST /add to add two numbers."}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
