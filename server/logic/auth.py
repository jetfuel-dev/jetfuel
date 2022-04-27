from typing import Optional
from logic import queries
import config
import uuid


def create_user(email: str) -> uuid.UUID:
    """
    Create user.
    """
    user_id = uuid.uuid4()
    queries.create_user(email=email, user_id=user_id)

    return user_id


def get_user_id(email: str) -> uuid.UUID:
    """
    Get a user.
    """
    user_id = queries.get_user_id(email=email)

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

    queries.update_api_token(user_id, api_token)


def verify_api_token(api_token: str) -> Optional[uuid.UUID]:
    """
    Verify an api_token. Returns None if api_token is invalid.

    Returns:
        user_id
    """
    return queries.verify_api_token(api_token)


def verify_user_token(user_token: str) -> Optional[uuid.UUID]:
    """
    Verify user token (Auth0 or "default").

    Args:
        user_token: User's token

    Returns:
        user_id
    """
    email: Optional[str] = None

    if config.DEFAULT_USER and user_token == "default":
        email = user_token

    # TODO: Add Auth0 email verification

    assert email is not None

    return queries.get_user_id(email)
