def param_def():
    from api_def import ASCII, ARRAY
    return (
        ('user_names', ARRAY, 0, [('user_name', ASCII, 1)]),
    )
	
def do_it(request, user_names):
	from admin import op_rmuser
	
	if not request.user.is_admin():
		return None
		
	result = []	
		
	for user_name in user_names:
		try:
			op_rmuser.handle_main(["bsadmin rmuser", user_name])
		except:
			result.append(user_name)
			
	return result