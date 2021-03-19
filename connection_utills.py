def _mk_response(content: Any, status: int):
    return ConnexionResponse(body=content, status_code=status)
