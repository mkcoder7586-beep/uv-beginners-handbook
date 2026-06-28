from fastapi import FastAPI
from shared_lib import get_greeting

app = FastAPI()

@app.get("/")
def read_root():
    return {"greeting": get_greeting("API User")}
