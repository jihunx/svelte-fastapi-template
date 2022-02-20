from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
api_router = APIRouter()

origins = ["http://0.0.0.0:4000", "http://localhost:4000", ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@api_router.get("/get_square/{number}")
async def get_square(number: int):
    return {"answer": number ** 2}


app.include_router(api_router, prefix="/api")
