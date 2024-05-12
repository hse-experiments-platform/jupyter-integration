import requests
from jupyter_utils import request_jupyter


def create_lab(user_id: str):    
    user_creation_url = f"hub/api/users/{user_id}"
    request_jupyter(requests.post, user_creation_url, assert_success=False)
    
    token_creation_url = f"hub/api/users/{user_id}/tokens"
    user_token_response = request_jupyter(requests.post, token_creation_url)
    user_api_token = user_token_response["token"]
   
    server_creation_url = f"hub/api/users/{user_id}/server"
    request_jupyter(requests.post, server_creation_url, assert_success=False)

    return user_api_token