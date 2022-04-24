import config


def verify_api_token(token: str) -> bool:
    """
    Verify that API token is valid.

    Args:
        token: API Token

    Returns:
        valid_token
    """
    if config.DEFAULT_USER:
        return token == "default"

    # TODO: Add API token verification via database
    raise NotImplementedError()
