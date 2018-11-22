from scalio.util import webtoken
from jwt.exceptions import DecodeError


def get_username_from_request(request):
    token = request.headers.get('Authorization')
    try:
        return webtoken.get_username_from_token(token.split(' ')[1])
    except (AttributeError, DecodeError, webtoken.InvalidWebtokenError):
        return None
