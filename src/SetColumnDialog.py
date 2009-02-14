from PyQt4 import QtCore, QtGui, Qt
from ui_SetColoumnDialog import Ui_SetColoumnDialog

class SetColoumnDialog(QtGui.QDialog, Ui_SetColoumnDialog):
    def __init__(self, p_list):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)

        for i in p_list:
            if   i[0] == 'user_id':
                self._chkbox_user_id.setCheckState(QtCore.Qt.Checked)
            elif i[0] == 'name':
                self._chkbox_name.setCheckState(QtCore.Qt.Checked)
            elif i[0] == 'longname':
                self._chkbox_email.setCheckState(QtCore.Qt.Checked)
            elif i[0] == 'email':
                self._chkbox_name.setCheckState(QtCore.Qt.Checked)
            elif i[0] == 'secondary_email':
                self._chkbox_secondary_mail.setCheckState(QtCore.Qt.Checked)
            elif i[0] == 'organization':
                self._chkbox_organization.setCheckState(QtCore.Qt.Checked)
            elif i[0] == 'phone_home':
                self._chkbox_phone_home.setCheckState(QtCore.Qt.Checked)
            elif i[0] == 'phone_mobile':
                self._chkbox_phone_mobile.setCheckState(QtCore.Qt.Checked)
            elif i[0] == 'phone_office':
                self._chkbox_phone_office.setCheckState(QtCore.Qt.Checked)
            elif i[0] == 'fax':
                self._chkbox_fax.setCheckState(QtCore.Qt.Checked)
            elif i[0] == 'language':
                self._chkbox_language.setCheckState(QtCore.Qt.Checked)
            elif i[0] == 'address':
                self._chkbox_address.setCheckState(QtCore.Qt.Checked)
            elif i[0] == 'url_homepage':
                self._chkbox_url_homepage.setCheckState(QtCore.Qt.Checked)
            elif i[0] == 'url':
                self._chkbox_url.setCheckState(QtCore.Qt.Checked)
            elif i[0] == 'messaging_services':
                self._chkbox_messaging_services.setCheckState(QtCore.Qt.Checked)
            elif i[0] == 'additional_info':
                self._chkbox_additional_info.setCheckState(QtCore.Qt.Checked)
            elif i[0] == 'photo':
                self._chkbox_photo.setCheckState(QtCore.Qt.Checked)
            elif i[0] == 'locked':
                self._chkbox_locked.setCheckState(QtCore.Qt.Checked)
            elif i[0] == 'used_memory':
                self._chkbox_used_memory.setCheckState(QtCore.Qt.Checked)
            elif i[0] == 'last_login':
                self._chkbox_last_login.setCheckState(QtCore.Qt.Checked)
            elif i[0] == 'create_time':
                self._chkbox_create_time.setCheckState(QtCore.Qt.Checked)
            elif i[0] == 'files':
                self._chkbox_files.setCheckState(QtCore.Qt.Checked)
            elif i[0] == 'admin':
                self._chkbox_admin.setCheckState(QtCore.Qt.Checked)
            elif i[0] == 'workspaces':
                self._chkbox_workspaces.setCheckState(QtCore.Qt.Checked)
            elif i[0] == 'access_right':
                self._chkbox_access_right.setCheckState(QtCore.Qt.Checked)

    def getHeaderData(self):
        result = []
        if self._chkbox_user_id.checkState() == QtCore.Qt.Checked:
            result.append(("user_id",_chkbox_user_id.text()))
        if self._chkbox_name.checkState() == QtCore.Qt.Checked:
            result.append(("name",_chkbox_name.text()))
        if self._chkbox_longname.checkState() == QtCore.Qt.Checked:
            result.append(("longname",_chkbox_longname.text()))
        if self._chkbox_email.checkState() == QtCore.Qt.Checked:
            result.append(("email",_chkbox_email.text()))
        if self._chkbox_secondary_email.checkState() == QtCore.Qt.Checked:
            result.append(("secondary_email",_chkbox_secondary_email.text()))
        if self._chkbox_organization.checkState() == QtCore.Qt.Checked:
            result.append(("organization",_chkbox_organization.text()))
        if self._chkbox_phone_home.checkState() == QtCore.Qt.Checked:
            result.append(("phone_home",_chkbox_phone_home.text()))
        if self._chkbox_phone_mobile.checkState() == QtCore.Qt.Checked:
            result.append(("phone_mobile",_chkbox_phone_mobile.text()))
        if self._chkbox_phone_office.checkState() == QtCore.Qt.Checked:
            result.append(("phone_office",_chkbox_phone_office.text()))
        if self._chkbox_fax.checkState() == QtCore.Qt.Checked:
            result.append(("fax",_chkbox_fax.text()))
        if self._chkbox_language.checkState() == QtCore.Qt.Checked:
            result.append(("language",_chkbox_language.text()))
        if self._chkbox_address.checkState() == QtCore.Qt.Checked:
            result.append(("address",_chkbox_address.text()))
        if self._chkbox_url_homepage.checkState() == QtCore.Qt.Checked:
            result.append(("url_homepage",_chkbox_url_homepage.text()))
        if self._chkbox_url.checkState() == QtCore.Qt.Checked:
            result.append(("url",_chkbox_url.text()))
        if self._chkbox_messaging_service.checkState() == QtCore.Qt.Checked:
            result.append(("messaging_service",_chkbox_messaging_service.text()))
        if self._chkbox_additional_info.checkState() == QtCore.Qt.Checked:
            result.append(("additional_info",_chkbox_additional_info.text()))
        if self._chkbox_photo.checkState() == QtCore.Qt.Checked:
            result.append(("photo",_chkbox_photo.text()))
        if self._chkbox_locked.checkState() == QtCore.Qt.Checked:
            result.append(("locked",_chkbox_locked.text()))
        if self._chkbox_used_memory.checkState() == QtCore.Qt.Checked:
            result.append(("used_memory",_chkbox_used_memory.text()))
        if self._chkbox_last_login.checkState() == QtCore.Qt.Checked:
            result.append(("last_login",_chkbox_last_login.text()))
        if self._chkbox_create_time.checkState() == QtCore.Qt.Checked:
            result.append(("create_time",_chkbox_create_time.text()))
        if self._chkbox_files.checkState() == QtCore.Qt.Checked:
            result.append(("files",_chkbox_files.text()))
        if self._chkbox_admin.checkState() == QtCore.Qt.Checked:
            result.append(("admin",_chkbox_admin.text()))
        if self._chkbox_workspaces.checkState() == QtCore.Qt.Checked:
            result.append(("workspaces",_chkbox_workspaces.text()))
        if self._chkbox_access_right.checkState() == QtCore.Qt.Checked:
            result.append(("access_right",_chkbox_access_right.text()))

    def TupleByKey(p_list):
        result = []
        for i in p_list:
            if i == 'user_id':
                result.append((i,_chkbox_user_id.text()))
            elif i == 'name':
                result.append((i,_chkbox_name.text()))
            elif i == 'longname':
                result.append((i,_chkbox_longname.text()))
            elif i == 'email':
                result.append((i,_chkbox_email.text()))
            elif i == 'secondary_email':
                result.append((i,_chkbox_secondary_email.text()))
            elif i == 'organization':
                result.append((i,_chkbox_organization.text()))
            elif i == 'phone_home':
                result.append((i,_chkbox_phone_home.text()))
            elif i == 'phone_mobile':
                result.append((i,_chkbox_phone_mobile.text()))
            elif i == 'phone_office':
                result.append((i,_chkbox_phone_office.text()))
            elif i == 'fax':
                result.append((i,_chkbox_fax.text()))
            elif i == 'language':
                result.append((i,_chkbox_language.text()))
            elif i == 'address':
                result.append((i,_chkbox_address.text()))
            elif i == 'url_homepage':
                result.append((i,_chkbox_url_homepage.text()))
            elif i == 'url':
                result.append((i,_chkbox_url.text()))
            elif i == 'messaging_services':
                result.append((i,_chkbox_messaging_services.text()))
            elif i == 'additional_info':
                result.append((i,_chkbox_additional_info.text()))
            elif i == 'photo':
                result.append((i,_chkbox_photo.text()))
            elif i == 'locked':
                result.append((i,_chkbox_locked.text()))
            elif i == 'used_memory':
                result.append((i,_chkbox_messaging_services.text()))
            elif i == 'last_login':
                result.append((i,_chkbox_last_login.text()))
            elif i == 'reate_time':
                result.append((i,_chkbox_create_time.text()))
            elif i == 'files':
                result.append((i,_chkbox_files.text()))
            elif i == 'admin':
                result.append((i,_chkbox_admin.text()))
            elif i == 'workspaces':
                result.append((i,_chkbox_workspaces.text()))
            elif i == 'access_right':
                result.append((i,_chkbox_access_right.text()))
            return result
    TupleByKey = staticmethod(TupleByKey)



