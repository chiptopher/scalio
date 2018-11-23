from functools import wraps

from scalio.util.webtoken import build_token


def create_weigh_in_for_user(weigh_in: dict, username: str):
    def wrapper(f):
        @wraps(f)
        def wrapped(self, *f_args, **f_kwargs):
            self.app.post('/api/weighin', data=weigh_in, headers={'Authorization': 'Bearer ' + build_token(username)})
            f(self, *f_args, **f_kwargs)
        return wrapped
    return wrapper
