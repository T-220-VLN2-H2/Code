from core.models.item import Item

class ItemService:

    def create_item(price, condition, category, delivery_option):
        new_item = Item(price, condition, category, delivery_option)
        new_item.save()
        print('Do something')
        #TODO validate that all item information is correct and add to the DB. 

    def delete_item(id):
        print('Do something')
        #TODO remove item from DB 

    def update_item(**kwargs):
        print('Do something')
        #TODO update item in DB

    def get_all_items(self):
        print('Do something')
        #TODO get a list of objects from DB and return, could possibly have filters for user items, category items etc.

    def get_all_images(self):
        print('Do something')
        #TODO get all images with itemID and return

    def sort_items(**kwargs):
        print('Do something')
        #TODO sort items by name or price