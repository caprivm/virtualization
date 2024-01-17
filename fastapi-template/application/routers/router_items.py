from config.config_limiter import limiter
from db.db_postgres import get_db
from fastapi import APIRouter, HTTPException, Request
from fastapi.params import Depends
from sqlalchemy.orm import Session
from schemas.schema_item import (
    Item,
    ItemCreate,
    ItemUpdate,
    read_db_item,
    create_db_item,
    update_db_item,
    delete_db_item,
)

router = APIRouter()


@router.get("/{item_id}")
@limiter.limit("1/second")
def read_item(request: Request, item_id: int, db: Session = Depends(get_db)) -> Item:
    try:
        db_item = read_db_item(item_id, db)
    except Exception as e:
        raise HTTPException(status_code=404) from e
    return Item(**db_item.__dict__)


@router.post("")
@limiter.limit("1/second")
def create_item(request: Request, item: ItemCreate, db: Session = Depends(get_db)) -> Item:
    db_item = create_db_item(item, db)
    return Item(**db_item.__dict__)


@router.patch("/{item_id}")
@limiter.limit("1/second")
def update_item(request: Request, item_id: int, item: ItemUpdate, db: Session = Depends(get_db)) -> Item:
    try:
        db_item = update_db_item(item_id, item, db)
    except Exception as e:
        raise HTTPException(status_code=404) from e
    return Item(**db_item.__dict__)


@router.delete("/{item_id}")
@limiter.limit("1/second")
def delete_item(request: Request, item_id: int, db: Session = Depends(get_db)) -> Item:
    try:
        db_item = delete_db_item(item_id, db)
    except Exception as e:
        raise HTTPException(status_code=404) from e
    return Item(**db_item.__dict__)
