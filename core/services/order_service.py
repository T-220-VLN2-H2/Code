from core.models import Order


class OrderService:
    def set_shipping_info(self):
        print("Do something")
        # TODO: Validate that all information is correct and forward to DB

    def set_payment_info(self):
        print("Do something")
        # TODO: Validate that all information is correct and forward to DB

    def create_invoice(self):
        print("Do something")
        # TODO: retreive payment, buyer information and create invoice to store on DB, return to user(?)

    def get_order_details(self, order_id):
        order = Order.objects.get(id=order_id)
        return order
        # TODO: retreive shipping & payment information and return. Return status 404 if not found.

    def get_orders(self, user):
        ''' Returns given users orders '''
        orders = Order.objects.filter(buyer=user)
        return orders
