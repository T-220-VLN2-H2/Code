# file split up according to guide
# https://cpske.github.io/ISP/django/separate-model-classes
from .category import Category
from .item import Item
from .notifications import Notification
from .order_history import OrderHistory
from .order_items import OrderItems
from .order import Order
from .payment_info import PaymentInfo
from .search_history import SearchHistory
from .shipping_details import ShippingDetails
from .user_bids import UserBids
from .user import Profile
from django.contrib.auth.models import User
from .user_ratings import UserRatings
