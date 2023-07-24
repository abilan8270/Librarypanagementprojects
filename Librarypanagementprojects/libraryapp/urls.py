from django.urls import path

from libraryapp import views

urlpatterns =[
    path('',views.login_fun,name='log'),
    path('logdata',views.logdata_fun),# login fun

    path('admin',views.admin_fun,name='admin'),
    path('admindata',views.admindata_fun),#admin fun

    path('student',views.student_fun,name='stu'),
    path('studentdata',views.studentdata_fun),#student fun

    path('shome',views.shome_fun,name='shome'),#student home

    path('ahome',views.adminhome_fun,name='ahome'),#admin home
  
    path('addbook',views.addbook_fun,name='add'),
    path('adddata',views.addbookdata_fun),

    path('DisplayBook',views.display_fun,name='disp'),#display

    path('Update/<int:id>',views.update_fun,name='up'),
    path('Delete/<int:id>',views.del_fun,name='del'),

    path('Logout',views.logout_fun,name='logo'),

    path('assing',views.assing_fun,name='ass'),
    path('assingdata',views.assingdata_fun),
    path('assreaddata',views.assreadadata_fun,name='assread'),

    path('issued',views.issueddisplay_fun,name='iss'),

    path('studentredata',views.studentprofile_fun,name='stpro'),
    path('updateprof/<int:id>',views.updateprof_fun,name='updateprof'),

    path('sissue',views.stuissue_fun,name='sissue'),

    path('slog_out',views.slogout_fun,name='slog_out'),


    path('Updt/<int:id>',views.assingupdate_fun,name='updt'),
    path('Dele/<int:id>',views.assingdelet_fun,name='dele'),
]