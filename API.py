from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def Start(name:str):
    return "Hallo "+name