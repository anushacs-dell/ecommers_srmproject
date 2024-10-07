from django.urls import path
from.import views

urlpatterns = [
    path('',views.dashboard_page,name='dashboard'),
    path('login',views.login_page,name='login'),
    path('logout',views.logout_page,name='logout'),
    path('create',views.create_admin,name='create'),
    path('list',views.admin_list,name='list'),
    path('delete<int:id>',views.delete_admin,name='delete'),
]
