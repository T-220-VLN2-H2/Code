from django.contrib.auth import authenticate
user = None
#user = authenticate(username="siggi", password="testpassword")
#user.save()
#user.profile.description = "Frekar flottur gæji"
#user.save()
categories = [
    {"id": 1, "name": "Electronics", "parent": None},
    {"id": 2, "name": "Furniture", "parent": None},
    {"id": 3, "name": "Clothing", "parent": None},
    {"id": 4, "name": "Other", "parent": None},
    {"id": 5, "name": "Processors", "parent": 1},
    {"id": 9, "name": "Intel", "parent": 5},
    {"id": 6, "name": "Graphics cards", "parent": 1},
    {"id": 8, "name": "Sound", "parent": 1},
    {"id": 7, "name": "chairs", "parent": 2},
]
items = [
    {
        "id": 1,
        "name": "Intel i5 processor",
        "price": 1000.00,
        "category": 5,
        "condition": "Refurbished",
        "auction": False,
    },
    {
        "id": 2,
        "name": "A good chair",
        "price": 250.00,
        "category": 7,
        "condition": "Refurbished",
        "auction": False,
    },
    {
        "id": 3,
        "name": "Sweater for all occations",
        "price": 10.00,
        "category": 3,
        "condition": "Refurbished",
        "auction": False,
    },
    {
        "id": 4,
        "name": "Intel i7 processor",
        "price": 2000.00,
        "category": 5,
        "condition": "Refurbished",
        "auction": False,
    },
    {
        "id": 5,
        "name": "nVidia RTX 3070",
        "price": 5000.00,
        "category": 6,
        "condition": "Refurbished",
        "auction": False,
    },
    {
        "id": 6,
        "name": "nVidia RTX 3080",
        "price": 6000.00,
        "category": 6,
        "condition": "Refurbished",
        "auction": False,
    },
    {
        "id": 7,
        "name": "nVidia RTX 3090",
        "price": 7000.00,
        "category": 6,
        "condition": "Refurbished",
        "auction": False,
    },
    {
        "id": 8,
        "name": "Speaker system",
        "price": 400.00,
        "category": 8,
        "condition": "Refurbished",
        "auction": False,
    },
    {
        "id": 9,
        "name": "a nice time with older gentleman",
        "price": 0.00,
        "category": 4,
        "condition": "Refurbished",
        "auction": False,
    },
]
categories_with_parents = {}
for cat in categories:
    if cat["parent"] is not None:
        if cat["parent"] in categories_with_parents:
            categories_with_parents[cat["parent"]].append(cat)
        else:
            categories_with_parents[cat["parent"]] = [cat]

print(categories_with_parents)
