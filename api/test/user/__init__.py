from functools import wraps


def create_user(username: str, password: str = 'password'):
    def wrapper(f):
        @wraps(f)
        def wrapped(self, *f_args, **f_kwargs):
            self.app.post('/api/user/register', data=dict(
                username=username,
                password=password
            ))
            f(self, *f_args, **f_kwargs)
        return wrapped
    return wrapper
