import os
from typing import Union, Annotated
from fastapi import FastAPI, Query, HTTPException
from .types_models.models import User, Item, ProductOption
import json


app = FastAPI(debug=True, redirect_slashes=True)

@app.get('/', tags=['root'])
def read_root() -> dict:
    """
    Root to the Item API
    """
    return {"Hello": "World"}

@app.get('/items/{item_id}', tags=['item'])
def read_item(item_id: int, q: Annotated[str, None, Query(max_length=50)]) -> dict:
    """

    """
    print()
    return {"item_id": item_id, "q": q}

@app.put('/items/{item_id}', tags=['items'])
def update_item(item_id: int, item: Item) -> dict:
    """

    """
    if item and item.name:
        print(item)
        return {"item_name": item.name, "item_id": item_id}
    else:
        print('item')
        return {"item_id": item_id, "item_name": ""}


@app.post('/user', tags=['user'])
def create_user(usr: User) -> dict:
    """

    """
    USERS = {}
    try:
        if os.path.exists("USERs.json"):
            with open("USERs.json", mode="r", encoding="utf-8") as f:
                content = f.read().strip()
                if content:
                    users = json.loads(content)
                    USERS['users'] = users
                else:
                    USERS['users'] = {}
        else:
            USERS['users'] = {}

        if usr.username in USERS['users']:
            raise HTTPException(status_code=400, detail="username already exists")

        USERS['users'][usr.username] = usr.model_dump()

        with open("USERs.json", mode="w", encoding="utf-8") as f:
            json.dump(USERS['users'], f, indent=4)
        return {"status": "success", "message": "user successfully created", "user": usr}

    except FileNotFoundError:
        USERS['users'] = {}
        USERS['users'][usr.username] = usr.model_dump()
        with open("USERs.json", mode="w", encoding="utf-8") as f:
            json.dump(USERS['users'], f, indent=4)
        return {"status": "success", "message": "user successfully created", "user": usr}
