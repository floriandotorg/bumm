def param_def():
    from api_def import ASCII
    return ( ('user_name', ASCII, 1), )

def do_it(request, user_name):
    from cl_core import User
    return User(user_name).is_locked()