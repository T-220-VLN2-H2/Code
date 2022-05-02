from django.shortcuts import render

URL = '../templates/user'

def home(request):
    return render(request, '../templates/user/index.html')

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

    return render(request, f'{URL}/index.html', context=ctx)

def edit(request, id):
    return render(request, f'{URL}/edit.html')

def history(request, id):
    return render(request, f'{URL}/history.html')

def messages(request, id):
    return render(request, f'{URL}/messages.html')

