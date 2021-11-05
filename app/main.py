from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.params import Depends

from fastapi_crudrouter import OrmarCRUDRouter

from app.core.config import settings
from app.db import database
from app.utils.dependencies import verify_token

from app.models.reference import PimEan
from app.routers import pim_ean



app = FastAPI()
app.state.database = database


# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        )


@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()


app.include_router(
    OrmarCRUDRouter(
        schema=PimEan,
        prefix="reference/pim_ean",
        tags=['CRUD'],
        get_all_route=[Depends(verify_token)],
        get_one_route=[Depends(verify_token)],
        create_route=[Depends(verify_token)],
        update_route=[Depends(verify_token)],
        delete_one_route=[Depends(verify_token)],
        delete_all_route=[Depends(verify_token)]
    )
)

app.include_router(
    pim_ean.router,
    tags=["EAN lookup"]
)
