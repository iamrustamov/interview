from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from app.v1.api import router as router_v1
from app.v1.utils.exceptions import validation_exception_handler


def set_custom_openapi(application: FastAPI):
    if not application.openapi_schema:
        application.openapi_schema = application.openapi()
    for _, method_item in application.openapi_schema.get("paths").items():
        for _, param in method_item.items():
            responses = param.get("responses")
            if "422" in responses:
                del responses["422"]


def get_application() -> FastAPI:
    application = FastAPI(
        title="Deposit API", version="1.0", root_path="/", docs_url="/", redoc_url=None
    )

    application.include_router(router_v1, prefix="/api/v1", tags=["/api/v1"])
    application.exception_handler(RequestValidationError)(validation_exception_handler)
    set_custom_openapi(application)

    return application


app = get_application()
