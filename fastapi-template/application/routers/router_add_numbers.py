from celery.result import AsyncResult
from celery.utils.log import get_task_logger
from config.config_limiter import limiter
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from models.model_celery_tasks import add_numbers as add

logger = get_task_logger(__name__)

router = APIRouter()


@router.post("", include_in_schema=True)
def add_numbers(request: Request, x: int, y: int) -> JSONResponse:
    logger.info("Adding {0} + {1}".format(str(x), str(y)))
    try:
        result_task = add.delay(x, y)
    except Exception as e:
        raise HTTPException(status_code=404) from e
    return JSONResponse({"task_id": result_task.id})


@router.get("/{task_id}")
async def get_status(task_id: str) -> JSONResponse:
    logger.info("Getting status of task {0}".format(task_id))
    try:
        result_task = AsyncResult(task_id)
    except Exception as e:
        raise HTTPException(status_code=404) from e
    return JSONResponse(
        {"task_id": result_task.id, "task_status": result_task.status, "task_result": result_task.result}
    )
