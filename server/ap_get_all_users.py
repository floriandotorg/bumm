class request_dummy(object):
	def want(self, a,b):
		pass
		
def param_def():
	return ()

def do_it(request):
	import time
	import datetime
	from admin import op_fsusage
	from admin import bs_admutil
	from admin import op_members
	import config_meet
	from ap_get_access_rights_all import access_rights_all
	
	all_users = bs_admutil.userlist(None, True)[0]
	result = []

	mem_list = {}
	for user in op_fsusage.load_lists((True, True), False)[0]:
		mem_list[user[0]] = (user[2], user[1])

	for user in all_users:
		user_info = {}
		user_info["user_id"] = user.__id__
		user_info["name"] = user.def_fullname()
		user_info["longname"] = user.fullname
		user_info["email"] = user.addresses[0].name
		user_info["secondary_email"] = [adr.name for adr in user.addresses[1:]]
		user_info["organization"] = user.org 
		user_info["phone_home"] = user.homephone
		user_info["phone_mobile"] = user.mobile
		user_info["phone_office"] = user.phone
		user_info["fax"] = user.fax
		user_info["language"] = user.def_language()
		user_info["address"] = user.post
		user_info["url"] = user.url
		user_info["url_home"] = user.home_url
		user_info["messaging_services"] = {}
		for (name, url, link, icon, id) in config_meet.MessagingServices:
			if id in user.messaging_services.keys():
				user_info["messaging_services"][name] = user.messaging_services[id]
		user_info["additional_info"] = user.description()
		user_info["photo"] = user.image
		user_info["locked"] = user.is_locked()
		user_info["admin"] = user.is_admin()
		try:
		  user_info["used_memory"] = mem_list[user.name][0]
		except:
		  user_info["used_memory"] = 0
		try:
		  user_info["files"] = mem_list[user.name][1]
		except:
		  user_info["files"] = 0
		try:
			y,m,d,H,M,S,w,c,s = time.localtime(user.accessCount.lastlog)
			user_info["last_login"] = datetime.datetime(y,m,d,H,M,S)
		except:
			user_info["last_login"] = None
		try:
			y,m,d,H,M,S,w,c,s = time.localtime(user.createEvent.time)
			user_info["create_time"] = datetime.datetime(y,m,d,H,M,S)
		except:
			user_info["create_time"] = None
		wsgrps=[]
		visited=[]
		op_members.get_wsgroups(user.home, wsgrps, visited, user)
		op_members.get_wsgroups(user.bag, wsgrps, visited, user)
		op_members.get_wsgroups(user.waste, wsgrps, visited, user)
		user_info["workspaces"] = [wsgrp.name[1:] for wsgrp in wsgrps]
		access_rights = access_rights_all(request_dummy(), user, True)
		try:
			user_info["access_rights"] = {	'owner' : access_rights['R0owner'],
											'manager' : access_rights['R2manager'],
											'other' : access_rights['R0other']}
		except:
			user_info["access_rights"] = None
		result.append(user_info)
		
	return result