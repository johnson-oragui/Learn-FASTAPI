from typing import Union
from fastapi import FastAPI


app = FastAPI(debug=True, redirect_slashes=True)

@app.get('/', tags=['root'])
def read_root() -> dict:
    """

    """
    return {"Hello": "World"}

@app.get('/items/{item_id}', tags=['item'])
def read_item(item_id: int, q: Union[str, None]) -> dict:
    """

    """
    print()
    return {"item_id": item_id, "q": q}
