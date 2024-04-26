from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.user_login, name="login"),
    path("register/", views.user_register, name="register"),
    path("registered/", views.registered, name="registered"),
    path("logindone/", views.logindone, name="logindone"),
    path("logout/", views.user_logout, name="logout"),
    path("profile/", views.user_profile, name="user_profile"),
    path("aboutUs/", views.aboutUs, name="aboutUs"),
    path("popularDishes/", views.popularDishes, name="popularDishes"),
    path("add-to-cart/<int:item_id>/", views.add_to_cart, name="add_to_cart"),
    path("view-cart/", views.view_cart, name="view_cart"),
    path("Search/", views.Search, name="Search"),
    path("gotoorder/", views.gotoorder, name="gotoorder"),
    # path("makepayment/", views.makepayment, name="makepayment"),
    path("offline/", views.offline_way, name="offline"),
    path("online/", views.online_way, name="online"),
    path("orderconfirm/", views.orderconfirm, name="orderconfirm"),
    # path("gotoorder/", views.gotoorder, name="gotoorder"),
    path(
        "remove-from-cart/<int:item_id>/",
        views.remove_from_cart,
        name="remove_from_cart",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
