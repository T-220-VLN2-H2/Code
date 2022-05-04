from django.shortcuts import render

folder_path = "../templates/user"

categories = [{"id": 1, "name": "Electronics"}, {"id": 2, "name": "Furniture"}]


def home(request):
    ctx = {"categories": categories, "user": "John Doe"}

    return render(request, f"{folder_path}/index.html", context=ctx)


def edit(request):

    return render(request, f"{folder_path}/edit.html")


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


def history(request):
    return render(request, f"{folder_path}/history.html")


def messages(request):
    return render(request, f"{folder_path}/messages.html")


def messages(request, id):
    return render(request, f"{folder_path}/messages.html")
