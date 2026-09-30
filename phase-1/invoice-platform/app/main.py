from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def server_status():
    return {"message": "Invoice Platform API is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/invoices")
def get_invoices():
    # Placeholder for fetching invoices logic
    return {"invoices": []}

@app.post("/invoices")
def create_invoice(invoice: dict):
    # Placeholder for creating an invoice logic
    return {"message": "Invoice created", "invoice": invoice}