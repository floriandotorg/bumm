def param_def():
    from api_def import INT, ASCII, UNICODE, DATETIME, BOOLEAN, DOUBLE, BASE64, ARRAY, STRUCT
    return (
        ('user_names', ARRAY, 0, [('user_name', ASCII, 1)]),
    )
	
def do_it(request, user_names):
	from admin import op_rmuser
	result = []
	
	for user_name in user_names:
		try:
			op_rmuser.handle_main(["bsadmin rmuser", user_name])
		except:
			result.append(user_name)
			
	return result