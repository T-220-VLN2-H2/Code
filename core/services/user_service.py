from django.shortcuts import redirect, render
from core.models.user import User

class UserService:
    def get_user_info(user_id):
        print('do something')
        #TODO validate the request, find the corresponding user in DB and return object. Else raise error.
    
    def set_user_info(id, **kwargs):
        print('do something')
        #TODO validate the request, find the corresponding user in DB and update information. Else raise error.

    def delete_user(user_id):
        print(1)
        #TODO validate the request, forward to DB to remove information, return success. Else raise error.
        

    def create_user(**kwargs):
        new_user = User(**kwargs)
        new_user.save()