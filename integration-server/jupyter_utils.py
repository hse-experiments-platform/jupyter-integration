import os

def request_jupyter(method, relative_url, body=None, assert_success=True):
    hub_url = os.getenv("JUPYTER_URL")
    token = os.getenv('SERVER_API_TOKEN')
    headers = {"Authorization": f"token {token}"}

    api_url = f"{hub_url}/{relative_url}"
    response = method(api_url, headers=headers, json=body)

    if assert_success and (response.status_code < 200 or response.status_code >= 300):
        raise ValueError(f"Failed to make a Jupyter call to {api_url}. Response: {response.json()}")

    try:
        return response.json()
    except:
        pass

def get_notebook_url(user_id, dataset_name, token):
    hub_url = os.getenv("JUPYTER_URL")

    return f"{hub_url}/user/{user_id}/lab/tree/{dataset_name}.ipynb?token={token}"