from fastapi import HTTPException , status , Security
from fastapi.security import APIKeyHeader

from core.conf import settings

API_KEYS = [
    settings.API_KEY
]

api_key_header = APIKeyHeader(name="x-api-key", auto_error=False)

def get_api_key(
    api_key_header: str = Security(api_key_header),
) -> str:
    """Retrieve and validate an API key from the query parameters or HTTP header.

    Args:
        api_key_query: The API key passed as a query parameter.
        api_key_header: The API key passed in the HTTP header.

    Returns:
        The validated API key.

    Raises:
        HTTPException: If the API key is invalid or missing.
    """

    if api_key_header in API_KEYS  :
        return api_key_header
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or missing API Key",
    )
