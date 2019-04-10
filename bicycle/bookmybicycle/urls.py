from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path("",views.index, name="index"),
    path("loggedout",views.log_me_out, name="logout"),
    path("login",views.login_r,name="login"),
    # path("login",views.register,name="login"),
    path("home",views.home,name="home"),
    path("register",views.register,name="register"),
    path("welcomeuser", views.my_login, name="welcomeuser"),
    # path("reg_success", views.my_register, name="success"),
    path("trial", views.trialpage, name="trialpage"),
    path("profile", views.profile, name="profile"),
    path("get_city", views.get_city),
    path("get_loc", views.get_loc),
    url(r'^signup/$', views.signup, name="success"),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/bookmybicycle/reg_success.html/$',
        views.activate, name='activate'),
    path("delete_user", views.delete_user, name="del"),
    path("booking_the_cycle",views.book_bicycle,name="book_bicycle"),
]
