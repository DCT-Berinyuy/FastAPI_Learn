from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def main():
    return {"message": "Greatings from Mr.DCT Omarchy Linux PC"}
