from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from app import services
from app.schema import UserIn, BaseResponse, UserListOut

# 1. Define FastAPI app
app = FastAPI()

# 2. Setup Prometheus metrics
instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app, endpoint="/metrics")

# 3. Routes
@app.get("/")
async def index():
    return {"message": "Hello from FastAPI -@kiranrakh155@gmail.com ;)"}

@app.post("/users", response_model=BaseResponse)
async def user_create(user: UserIn):
    try:
        services.add_userdata(user.dict())
    except:
        return {"success": False}
    return {"success": True}

@app.get("/users", response_model=UserListOut)
async def get_users():
    return services.get_all_users()

