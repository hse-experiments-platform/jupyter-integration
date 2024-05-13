import os
import requests

def get_user_id(auth_token: str):
    base_url = os.getenv("AUTH_SERVICE_URL")
    headers = {"Authorization": auth_token}

    response = requests.get(f"{base_url}/validate", headers=headers)
    if response.status_code != 200:
        raise ValueError(f"Failed to get user id. Response: {response.json()}")

    return response.json()["user_id"]


def get_dataset_url(dataset_id: str, auth_token: str):
    base_url = os.getenv("DATASET_SERVICE_URL")
    headers = {"Authorization": auth_token}

    response = requests.get(f"{base_url}/datasets/{dataset_id}/download", headers=headers)
    if response.status_code != 200:
        raise ValueError(f"Failed to get dataset url for dataset {dataset_id}. Response: {response.json()}")

    return response.json()["url"]