def param_def():
    from api_def import INT, ASCII, UNICODE, DATETIME, BOOLEAN, DOUBLE, BASE64, ARRAY, STRUCT
    return (
        ('user_name', ASCII, 0),
    )
	
def do_it(request, user_name):
	import cl_core
	user = cl_core.User(user_name)
	return str(user.locking)