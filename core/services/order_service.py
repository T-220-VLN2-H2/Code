from core.models import Order


class OrderService:
    @classmethod
    def set_shipping_info(cls):
        print("Do something")
        # TODO: Validate that all information is correct and forward to DB

    @classmethod
    def set_payment_info(cls):
        print("Do something")
        # TODO: Validate that all information is correct and forward to DB

    @classmethod
    def create_invoice(cls):
        print("Do something")
        # TODO: retreive payment, buyer information and create invoice to store on DB, return to user(?)

    @classmethod
    def get_order_details(self, order_id):
        order = Order.objects.get(id=order_id)
        return order
        # TODO: retreive shipping & payment information and return. Return status 404 if not found.

    @classmethod
    def get_orders(self, user):
        ''' Returns given users orders '''
        orders = Order.objects.filter(buyer=user)
        return orders
