from . import views
from django.urls import path

urlpatterns = [
    path("",views.home, name="home"),
    # path("shop/",views.shop, name="shop"),
    # path("search/",views.search, name="search"),
    # path("login/",views.login, name="login"),
    # path("logout/",views.logout, name="logout"),
    # path("cart/",views.cart, name="cart"),
    # path("registration/",views.registaration, name="registration"),
    # path("forget-password/",views.forget_password, name="forget-password"),
    # path("order/",views.order, name="order"),
    # path("payment/",views.payment, name="payment"),
    # path("account/",views.search, name="account"),
    
]