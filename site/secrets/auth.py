from flask import session, redirect
from functools import wraps


def session_key_required(session_key_name, session_value=True,
                         failure_url='/'):
    """
    This decorator is modeled after flashexts.login.login_required,
    and requires that a user's session have a given session variable
    set to a given value in order to access the view.
    """

    def inner_func(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if session.get(session_key_name) != session_value:
                return redirect(failure_url)
            return fn(*args, **kwargs)
        return decorated_view
    return inner_func
