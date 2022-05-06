from django.shortcuts import redirect
from core.models.user import Profile

class UserService:

    def get_user_info(self, user_id):
        user = Profile.objects.filter(id = user_id)
        return user

    def set_user_info(self, user_id, **kwargs):
        user = self.get_user_info(user_id)
        updated_information = []
        for item in kwargs.items():
            updated_information.append(item)
        for item in updated_information:
            user.item
        #TODO find the corresponding user in DB and update information. Else raise 404 error.

    # nauðsynlegt?
    # def delete_user(user_id):
    #     print(1)
    #     #TODO forward to DB to remove information, return success. Else raise error.
        
    def create_user(self, username, first_name, last_name, email, password):
        new_user = Profile(username, first_name, last_name, email, password)
        new_user.save()
        #return redirect("accounts/profile/") #finna url til að redirecta

def main():
    new_user = UserService.create_user('Hellibelli', 'Helgi', 'Hákonarson', 'Helgihak@gmail.com', 'abc123')

if __name__ == "__main__":
    main()