from fastapi import FastAPI, Request
from service.productservice import ProductService
from fastapi.responses import FileResponse

app = FastAPI()
service = ProductService()

@app.get("/products")
async def products():
    return service.find_all_products()
    

@app.post("/products/save")
async def products(request: Request):
    data = await request.json()
    return service.save_product(data)
    
@app.get("/", response_class=FileResponse)
async def view():
    return "view/front/index.html"



@app.get("/listagem", response_class=FileResponse)
async def view():
    return "view/front/listagem.html"

