def param_def():
    from api_def import ASCII, ARRAY
    return (
        ('user_names', ARRAY, 0, [('user_name', ASCII, 1)]),
    )
	
def do_it(request, user_names):
	import bs_passwd
	from cl_request import get_user
	
	if not request.user.is_admin():
		return None
	
	for user_name in user_names:
		bs_passwd.updatelock(get_user(user_name), bs_passwd.UNLOCK, bs_passwd.LCK_ADMIN)