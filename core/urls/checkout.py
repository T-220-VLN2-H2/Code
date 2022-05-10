from django.urls import path

from ..views import checkout

urlpatterns = [
    path("checkout/personal_info", checkout.personal_info, name="checkout_personal"),
    path("checkout/delivery_info", checkout.delivery_info, name="checkout_delivery"),
    path("checkout/payment_info", checkout.payment_info, name="checkout_payment"),
    path("checkout/summary", checkout.summary_display, name="checkout_summary"),
]
