from jwt.exceptions import DecodeError

from scalio.util import webtoken


def get_username_from_request(request):
    token = request.headers.get('Authorization')
    try:
        return webtoken.get_username_from_token(token.split(' ')[1])
    except (AttributeError, DecodeError, webtoken.InvalidWebtokenError):
        return None
