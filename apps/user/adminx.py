import xadmin
from .models import EmailVerifyRecord,Banner
from xadmin import  views

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSetting(object):
    site_title = '瑞哥的后台'
    site_footer = '龙潭虎穴'
    menu_style = 'accordion'

class EmailVerifyRecordAdmin(object):
    list_display = ['code','email','send_time']
    search_fields = ['code','email']
    list_filter = ['code','email','send_time']

class BannerAdmin(object):
    list_display = ['title', 'image', 'url','add_time']
    search_fields = ['title', 'image', 'url']
    list_filter = ['title', 'image', 'url','add_time']


xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSetting)
xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)
