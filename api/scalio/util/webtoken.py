import jwt
import datetime


def build_token(username: str,
                expiration_time: datetime.datetime = datetime.datetime.utcnow() + datetime.timedelta(days=2)
                ):
    payload = {
        'sub': username,
        'exp': expiration_time
    }
    return jwt.encode(payload, 'secret-key', algorithm='HS256').decode('utf-8')


def get_username_from_token(token: str):
    try:
        return jwt.decode(token, 'secret-key', algorithms=['HS256'])['sub']
    except jwt.ExpiredSignatureError:
        raise InvalidWebtokenError


class InvalidWebtokenError(Exception):
    pass
