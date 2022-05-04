from django.shortcuts import render

folder_path = "../templates/user"

categories = [{"id": 1, "name": "Electronics"}, {"id": 2, "name": "Furniture"}]


def home(request):
    ctx = {"categories": categories}

    return render(request, f"{folder_path}/index.html", context=ctx)


def edit(request):
<<<<<<< HEAD
    return render(request, f'{folder_path}/edit.html')
=======

    return render(request, f"{folder_path}/edit.html")

>>>>>>> main

def profile(request, id):
    users = [
        {"id": 1, "name": "John Doe"},
        {"id": 2, "name": "Helgi Hak"},
    ]
    ctx = None
    for user in users:
        if user["id"] == int(id):
            ctx = user
            break

    return render(request, f"{folder_path}/user.html", context=ctx)


<<<<<<< HEAD
def history(request):
    return render(request, f'{folder_path}/history.html')

def messages(request):
    return render(request, f'{folder_path}/messages.html')
=======
def history(request, id):
    ctx = {"categories": categories}

    return render(request, f"{folder_path}/history.html", context=ctx)

>>>>>>> main

def messages(request, id):
    return render(request, f"{folder_path}/messages.html")
