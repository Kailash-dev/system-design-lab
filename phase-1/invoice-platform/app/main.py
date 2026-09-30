from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def health_check():
    return {"message": "Invoice Platform API is running"}