from config.config_limiter import limiter
from db.db_mongodb import get_db as mongodb_get_db
from db.db_postgres import session_local as postgres_get_db
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from sqlalchemy import exc, text
import platform
import psutil

postgres_db = postgres_get_db()
mongo_db = mongodb_get_db()

router = APIRouter()


@router.get("", include_in_schema=True)
@limiter.limit("4/second")
def health(request: Request) -> JSONResponse:
    """
    API to get the status of the application and the system. You can get a JSON response with the status of the MongoDB and Postgres databases, and the system information.
    """
    # Get MongoDB status
    mongo_db_details = ""
    try:
        mongo_db_status = "up"
        mongo_db.list_collections()
    except Exception as e:
        mongo_db_status = "down"
        mongo_db_details = f"MongoDB connection error: {e}"

    # Get Postgres status
    postgres_db_details = ""
    try:
        postgres_db_status = "up"
        postgres_db.execute(text("SELECT 1"))
    except exc.SQLAlchemyError as e:
        postgres_db_status = "down"
        postgres_db_details = f"Postgres connection error: {e}"
    finally:
        postgres_db.close()

    # Get system information
    system_info = {
        "system": platform.system(),
        "processor": platform.processor(),
        "architecture": platform.architecture(),
        "memory": psutil.virtual_memory()._asdict(),
        "disk": psutil.disk_usage("/")._asdict(),
    }

    return JSONResponse(
        {
            "mongodb": {"status": mongo_db_status, "details": mongo_db_details},
            "postgres": {"status": postgres_db_status, "details": postgres_db_details},
            "system_info": system_info,
        }
    )
