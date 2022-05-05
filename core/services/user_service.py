from django.shortcuts import redirect, render
from Code.core.forms.user_form import UserCreateForm

class UserService:
    def get_user_info(request):
        print('do something')
        #TODO validate the request, find the corresponding user in DB and return object. Else raise error.
    
    def set_user_info(id):
        print('do something')
        #TODO validate the request, find the corresponding user in DB and update information. Else raise error.

    def delete_user(user_id):
        print(1)
        #TODO validate the request, forward to DB to remove information, return success. Else raise error.
        

    def create_user():
        print(1)
        #TODO validate the request, forward to DB to store information, return success. Else raise error.
        
