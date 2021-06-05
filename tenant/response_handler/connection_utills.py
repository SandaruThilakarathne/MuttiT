from connexion.lifecycle import ConnexionResponse
from typing import Any


def mk_response(content: Any, status: int):
    return ConnexionResponse(body=content, status_code=status)
