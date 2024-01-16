from config.config_mongo import SettingsMongo
from config.config_logging import setup_logging
from db.db_mongodb import close_db_connect
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from routers import router_db_health, router_items, router_add_numbers
from schemas.schema_error import BadRequest, UnprocessableError
import json
import logging

tags_metadata = open("docs/metadata.json", "r")
description = open("docs/documentation.md", "r")

# Logging
setup_logging()

app = FastAPI(
    openapi_tags=json.load(tags_metadata),
    servers=[{"url": "/", "description:": "Root URL"}],
    redoc_url=None,
    title="FastAPI Template",
    version="0.1",
    description=description.read(),
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
    contact={"name": "Juan Caviedes", "email": "jcaviedesv@unal.edu.co"},
)

app.add_event_handler("startup", SettingsMongo.app_settings_validate)
app.add_event_handler("shutdown", close_db_connect)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(BadRequest)
async def bad_request_handler(request: Request, exc: BadRequest) -> JSONResponse:
    return exc.gen_err_resp()


@app.exception_handler(RequestValidationError)
async def invalid_req_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
    logging.error(f"Request invalid. {str(exc)}")
    return JSONResponse(
        status_code=400,
        content={
            "type": "about:blank",
            "title": "Bad Request",
            "status": 400,
            "detail": [str(exc)],
        },
    )


@app.exception_handler(UnprocessableError)
async def unprocessable_error_handler(request: Request, exc: UnprocessableError) -> JSONResponse:
    return exc.gen_err_resp()


app.include_router(router_db_health.router, prefix="/health", tags=["Health"])
app.include_router(router_items.router, prefix="/items", tags=["Items"])
app.include_router(router_add_numbers.router, prefix="/add", tags=["Math"])


@app.get("/", response_class=RedirectResponse, status_code=302, include_in_schema=False)
async def redirect_tim():
    response = RedirectResponse(url="/docs")
    return response


# Close docs files
tags_metadata.close()
description.close()
