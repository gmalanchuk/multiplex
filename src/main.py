from datetime import datetime

from fastapi import FastAPI, APIRouter
from fastapi_pagination import add_pagination
from starlette import status
from starlette.responses import JSONResponse

from src.api.include_routers import all_routers

app = FastAPI(title="Multiplex API", version="1.0.0", docs_url="/api/docs/")


@app.get(path="/api/ping/", tags=["Health Check"])
async def ping() -> JSONResponse:
    return JSONResponse(content={"ping": "pong"}, status_code=status.HTTP_200_OK)


async def include_routers(routers: tuple) -> None:
    """Includes all api specified in the all_routers tuple"""

    api_router = APIRouter(prefix="/api")

    for router in routers:
        api_router.include_router(router)

    app.include_router(api_router)
    add_pagination(app)


@app.on_event("startup")
async def startup() -> None:
    """Executed before the server starts"""

    start_time = datetime.now()

    await include_routers(all_routers)

    end_time = datetime.now()

    print(f"Startup time: {end_time - start_time}")
