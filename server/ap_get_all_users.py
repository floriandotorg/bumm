import ap_get_attributes
import ap_get_user_by_name
import ap_search_user
import cl_core
from ap_get_attributes import get_attr
from apix_handler import add_api2doc, str2uni, objId2xapi, objId2object

def param_def():
    return ()

def do_it(request):
    from admin import op_fsusage
    from admin import bs_admutil
    all_users = bs_admutil.userlist(None, True)[0]
    result = []
  
    mem_list = {}
    for user in op_fsusage.load_lists((True, False), False)[0]:
        mem_list[user[0]] = user[2]

    for user in all_users:
        user_info = {}
        #user_info = ap_get_user_by_name.do_it(request, user[0])
        user_info["user_id"] = user.__id__
        user_info["name"] = user.def_fullname()
        user_info["longname"] = user.fullname
        user_info["email"] = user.addresses[0].name
        user_info["secondary_email"] = [adr.name for adr in user.addresses[1:]]
        
        
        if user_info["name"] in mem_list:
          user_info["used_memory"] = mem_list[user.name]
        else:
          user_info["used_memory"] = 0
          
        result.append(user_info)
        
    return result