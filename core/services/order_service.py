from core.models import Order


class OrderService:
    @classmethod
    def create_order(cls, buyer_id, item_id, seller_id):
        new_order = Order()
        new_order.buyer_id = buyer_id
        new_order.item_id = item_id
        new_order.seller_id = seller_id
        new_order.save()
        return new_order

    @classmethod
    def get_order_details(self, order_id):
        order = Order.objects.get(id=order_id)
        return order
        # TODO: retreive shipping & payment information and return. Return status 404 if not found.

    @classmethod
    def get_orders(self, user):
        """Returns given users orders"""
        orders = Order.objects.filter(buyer=user)
        return orders
