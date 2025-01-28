from typing import Union

from fastapi import FastAPI

import tasks

app = FastAPI()
app.include_router(tasks.router)


@app.get("")
def read_root():
    return {"message": "Hello World"}
