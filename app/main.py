from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routers.detector import router
from app.configs import CFG

app = FastAPI(title="Calorie estimation")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)


app.include_router(router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=CFG.HOST, port=CFG.PORT)
