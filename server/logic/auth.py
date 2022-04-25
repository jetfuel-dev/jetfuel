from typing import Optional
from logic import database
import config
import uuid


def create_user(email: str) -> uuid.UUID:
    """
    Create user.
    """
    user_id = uuid.uuid4()
    database.create_user(email=email, user_id=user_id)

    return user_id


def generate_api_token(user_id: uuid.UUID, api_token: Optional[str] = None) -> None:
    """
    Generate a api_token for a user.

    Args:
        user_id: Which user
        api_token: Optional default api_token
    """
    if api_token is None:
        # TODO: Add way to generate new api_token
        raise NotImplementedError()

    database.update_api_token(user_id, api_token)


def verify_api_token(api_token: str) -> Optional[uuid.UUID]:
    """
    Verify an api_token. Returns None if api_token is invalid.

    Returns:
        user_id
    """
    return database.verify_api_token(api_token)
