from typing import Annotated
from fastapi import FastAPI, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from internal_client import *
from jupyterhub_client import *
from jupyterlab_client import *
from jupyter_utils import *
from internal_client import *


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DatasetRequest(BaseModel):
    dataset_name: str
    dataset_id: str

@app.exception_handler(ValueError)
async def value_error_handler(request, exc):
    raise HTTPException(status_code=500, detail=str(exc))


@app.post("/jupyter-notebook-for-dataset")
def create_jupyter_notebook_for_dataset(request: DatasetRequest, authorization: Annotated[str | None, Header()] = None):
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing Authorization header")

    user_id = get_user_id(authorization)
    dataset_url = get_dataset_url(request.dataset_id, authorization)

    user_token = create_lab(user_id)
    create_notebook(user_id, request.dataset_name, dataset_url, user_token=user_token)

    notebook_url = get_notebook_url(user_id, request.dataset_name, user_token)

    return notebook_url


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000)