from models.model_item import Item as DBItem
from typing import Optional
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session


class Item(BaseModel):
    id: int
    name: str = Field(default="Notebook", max_length=255)
    description: Optional[str] = Field(default="Death Note", max_length=255)


class ItemCreate(BaseModel):
    name: str = Field(default="Notebook", max_length=255)
    description: Optional[str] = Field(default="Death Note", max_length=255)


class ItemUpdate(BaseModel):
    name: Optional[str] = Field(default="Notebook to patch", max_length=255)
    description: Optional[str] = Field(default="New notebook", max_length=255)


def read_db_item(item_id: int, session: Session, offset: int = 0, limit: int = 10000) -> DBItem:
    """
    Read an item from the database.

    :param item_id: Item :code:`id` stored in the database. If :code:`0` is given, all items are returned.
    :type item_id: int
    :param session: Session to use for the database.
    :type session: Session
    :param offset: Offset to use for the query, defaults to 0.
    :type offset: int
    :param limit: Limit to use for the query, defaults to 10000.
    :type limit: int
    :raises Exception: Exception if item is not found.
    :return: Item found in the database.
    :rtype: DBItem
    """
    if item_id == 0:
        db_item = session.query(DBItem).offset(offset).limit(limit).all()
    else:
        db_item = session.query(DBItem).filter(DBItem.id == item_id).first()
    if db_item is None:
        raise Exception(f"Item with id {item_id} not found.")
    return db_item


def create_db_item(item: ItemCreate, session: Session) -> DBItem:
    """
    Create an item in the database.

    :param item: Item to create.
    :type item: ItemCreate
    :param session: Session to use for the database.
    :type session: Session
    :return: Item created in the database.
    :rtype: DBItem
    """
    db_item = DBItem(**item.model_dump(exclude_none=True))
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item


def update_db_item(item_id: int, item: ItemUpdate, session: Session) -> DBItem:
    """
    Update an item in the database.

    :param item_id: Item :code:`id` stored in the database.
    :type item_id: int
    :param item: Item fields to update.
    :type item: ItemUpdate
    :param session: Session to use for the database.
    :type session: Session
    :return: Item updated in the database.
    :rtype: DBItem
    """
    db_item = read_db_item(item_id, session)
    for key, value in item.model_dump(exclude_none=True).items():
        setattr(db_item, key, value)
    session.commit()
    session.refresh(db_item)
    return db_item


def delete_db_item(item_id: int, session: Session) -> DBItem:
    """
    Delete an item from the database.

    :param item_id: Item :code:`id` stored in the database to be deleted.
    :type item_id: int
    :param session: Session to use for the database.
    :type session: Session
    :return: Item deleted from the database.
    :rtype: DBItem
    """
    db_item = read_db_item(item_id, session)
    session.delete(db_item)
    session.commit()
    return db_item
