from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("polls.urls")),
    # path("shop/",include("polls.urls")),
    # path("search/",include("polls.urls")),
    # path("login/",include("polls.urls")),
    # path("logout/",include("polls.urls")),
    # path("cart/",include("polls.urls")),
    # path("registration/",include("polls.urls")),
    # path("forget-password/",include("polls.urls")),
    # path("order/",include("polls.urls")),
    # path("payment/",include("polls.urls")),
    # path("account/",include("polls.urls")),
]
