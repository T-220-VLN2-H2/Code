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

    def get_order_details(self):
        print("Do something")
        # TODO: retreive shipping & payment information and return. Return status 404 if not found.
