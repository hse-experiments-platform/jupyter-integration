import requests
from jupyter_utils import request_jupyter
import time


def create_lab(user_id: str):    
    user_creation_url = f"hub/api/users/{user_id}"
    request_jupyter(requests.post, user_creation_url, assert_success=False)
    
    token_creation_url = f"hub/api/users/{user_id}/tokens"
    user_token_response = request_jupyter(requests.post, token_creation_url)
    user_api_token = user_token_response["token"]
   
    server_creation_url = f"hub/api/users/{user_id}/server"
    request_jupyter(requests.post, server_creation_url, assert_success=False)

    max_retries = 12
    server_status = False
    server_ready_url = f"hub/api/users/{user_id}"
    for i in range(max_retries):
        result = request_jupyter(requests.get, server_ready_url)
        if result["servers"][""]:
            server = result["servers"][""]
            status = server["ready"]
            if status:
                break
        time.sleep(5)
    if not status:
        raise ValueError(f"Server for user {user_id} was not ready after {max_retries} retries.")

    return user_api_token