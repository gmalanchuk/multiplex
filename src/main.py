from datetime import datetime

from fastapi import FastAPI
from starlette import status
from starlette.responses import JSONResponse


app = FastAPI(title="Multiplex API", version="1.0.0", docs_url="/api/docs/")


@app.get(path="/api/ping/", tags=["Health Check"])
async def ping() -> JSONResponse:
    return JSONResponse(content={"ping": "pong"}, status_code=status.HTTP_200_OK)


@app.on_event("startup")
async def startup() -> None:
    """Executed before the server starts"""

    start_time = datetime.now()
    end_time = datetime.now()

    print(f"Startup time: {end_time - start_time}")
