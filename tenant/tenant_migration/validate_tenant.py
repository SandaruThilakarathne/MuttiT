from functools import wraps
from tenant.response_handler.connection_utills import mk_response
from http import HTTPStatus


def check_tenant(db):
    def mydecorator(f):
        @wraps(f)
        async def wrapped(*args, **kwargs):
            schema = kwargs.get("request").headers.get("TENANT")
            if not schema:
                return mk_response("Tenant identification failed", HTTPStatus.BAD_REQUEST)
            async with db.acquire():
                await db.status(f"SET search_path TO {schema}")
                return await f(*args, **kwargs)

        return wrapped

    return mydecorator
