from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'smsapp.views.home', name='home'),
    url(r'^employeemessage/', 'smsapp.views.submit_employee_message_form', name='submit_employee_message_form'),
    url(r'^departmentmessage/', 'smsapp.views.submit_department_message_form', name='submit_department_message_form'),
    url(r'^groupmessage/', 'smsapp.views.submit_group_message_form', name='submit_group_message_form'),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.contrib.auth.views',
    url(r'^login/$', 'login', {'template_name': 'login.html'},
        name='login'),
    url(r'^logout/$', 'logout', {'next_page': '/'}, name='logout'),
)
