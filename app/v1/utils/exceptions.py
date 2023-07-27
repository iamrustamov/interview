from fastapi import Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    error_msg = []
    for error in exc.errors():
        field = "Field " + ".".join(str(f) for f in error["loc"])
        error_msg.append(f"{field} {error['msg']};")
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST, content={"error": " ".join(error_msg)}
    )
