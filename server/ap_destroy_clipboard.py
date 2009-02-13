def param_def():
    from api_def import ASCII, ARRAY, INT
    return (
		('outdated', INT, 0),
        ('user_names', ARRAY, 0, [('user_name', ASCII, 1)]),
    )
	
def do_it(request, outdated, user_names):
	from admin import bs_admutil
	from admin import op_rmwaste
	from cl_request import Request
	import time
	
	if not request.user.is_admin():
		return None
		
	req = Request()
	outdated = time.time() - 24 * 3600 * outdated
	users = bs_admutil.userlist(user_names or None)[0]

	for user in users:
		req.set_user(user.name)
		op_rmwaste.clear_waste(req, user.bag, outdated, True, False)