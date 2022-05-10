from django.urls import path

from ..views import checkout

urlpatterns = [
    path("checkout/user", checkout.user, name="checkout_user"),
    path("checkout/delivery", checkout.delivery, name="checkout_delivery"),
    path("checkout/payment", checkout.payment, name="checkout_payment"),
    path("checkout/summary", checkout.summary, name="checkout_summary"),
]
