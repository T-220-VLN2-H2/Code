# file split up according to guide
# https://cpske.github.io/ISP/django/separate-model-classes
from .category import Category
from .image import Image
from .item import Item
from .notifications import Notification
from .order import Order
from .payment_info import PaymentInfo
from .search_history import SearchHistory
from .shipping_details import ShippingDetails
from .user import Profile
from .user_bids import UserBids
from django.contrib.auth.models import User
