import requests
from jupyter_utils import request_jupyter

def _create_body(dataset_name, dataset_url):
    return {
        "type": "notebook",
        "format": "json",
        "content": {
            "metadata": {
            "kernelspec": {
                "name": "python3",
                "display_name": "Python 3 (ipykernel)",
                "language": "python"
            },
            "language_info": {
                "name": "python",
                "version": "3.11.9",
                "mimetype": "text/x-python",
                "codemirror_mode": {
                "name": "ipython",
                "version": 3
                },
                "pygments_lexer": "ipython3",
                "nbconvert_exporter": "python",
                "file_extension": ".py"
            }
            },
            "nbformat_minor": 5,
            "nbformat": 4,
            "cells": [
            {
                "id": "f63b63a6-16a2-453c-aaba-50feff231036",
                "cell_type": "code",
                "source": f"import pandas as pd\nurl = \"{dataset_url}\"\ndataframe = pd.read_csv(url)",
                "metadata": {
                "trusted": True
                },
                "outputs": [],
            }
            ]
        },
        "path": f"{dataset_name}.ipynb"
    }

def create_notebook(user_id, dataset_name, dataset_url):
    lab_api = f'user/{user_id}/api'

    notebook_creation_url = f"{lab_api}/contents"
    body = { "type": "notebook" }
    response = request_jupyter(requests.post, notebook_creation_url, body)
    default_name = response["path"]

    rename_notebook_url = f"{lab_api}/contents/{default_name}"
    body = {
        "path": f"/{dataset_name}.ipynb",
    }
    request_jupyter(requests.patch, rename_notebook_url, body)

    set_content_url = f"{lab_api}/contents/{dataset_name}.ipynb"
    request_jupyter(requests.put, set_content_url, _create_body(dataset_name, dataset_url))