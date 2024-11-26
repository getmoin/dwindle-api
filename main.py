from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from services import get_client_data,  get_achievements_data, get_location_data

app = FastAPI()

# Configure CORS
origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/client")
async def get_client():
    try:
        client_data = get_client_data()
        return client_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/achievements")
async def get_achievements():
    try:
        client_data = get_achievements_data()
        return client_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/location")
async def get_location():
    try:
        client_data = get_location_data()
        return client_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)