from django.contrib.auth import authenticate

user = authenticate(username="siggi", password="testpassword")
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
        "category": 2,
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

ratings = [{
  "name": "Ronnie Harsent",
  "rating": 1.3
}, {
  "name": "Arabella Riggeard",
  "rating": 2.5
}, {
  "name": "Abelard Jonathon",
  "rating": 1.5
}, {
  "name": "Rutherford Trubshawe",
  "rating": 3.4
}, {
  "name": "Putnam Wheatman",
  "rating": 3.9
}, {
  "name": "Teodoro Skedge",
  "rating": 3.8
}, {
  "name": "Hurlee Baine",
  "rating": 2.3
}, {
  "name": "Stephen Keiley",
  "rating": 1.2
}, {
  "name": "Cheslie Erdely",
  "rating": 3.3
}, {
  "name": "Becki Lyall",
  "rating": 2.1
}]

user_messages = [{
  "sender": "Edik Arnoldi",
  "message": "amet consectetuer adipiscing elit proin risus praesent lectus vestibulum quam sapien varius ut blandit non interdum",
  "title": "Tarzan's Greatest Adventure"
}, {
  "sender": "Tori Scholler",
  "message": "imperdiet nullam orci pede venenatis non sodales sed tincidunt eu felis",
  "title": "Big Fella"
}, {
  "sender": "Elwood Sappson",
  "message": "faucibus cursus urna ut tellus nulla ut erat id mauris vulputate",
  "title": "Alphabet"
}, {
  "sender": "Hailey Drugan",
  "message": "orci mauris lacinia sapien quis libero nullam sit amet turpis elementum ligula vehicula consequat morbi a",
  "title": "Prince of Egypt, The"
}, {
  "sender": "Jillayne Melanaphy",
  "message": "natoque penatibus et magnis dis parturient montes nascetur ridiculus mus etiam",
  "title": "Guru, The"
}, {
  "sender": "Shara Bagenal",
  "message": "non velit donec diam neque vestibulum eget vulputate ut ultrices vel augue vestibulum ante ipsum primis in faucibus orci luctus",
  "title": "A Most Violent Year"
}, {
  "sender": "Chalmers Kilner",
  "message": "adipiscing elit proin interdum mauris non ligula pellentesque ultrices phasellus id sapien",
  "title": "What Will You Do When You Catch Me? (Co mi zrobisz jak mnie zlapiesz?)"
}, {
  "sender": "Leta Buey",
  "message": "amet eros suspendisse accumsan tortor quis turpis sed ante vivamus tortor duis mattis",
  "title": "Butterfly on a Wheel (Shattered)"
}, {
  "sender": "Traci Mannion",
  "message": "aenean lectus pellentesque eget nunc donec quis orci eget orci vehicula condimentum curabitur in libero ut",
  "title": "Silences of the Palace, The (Saimt el Qusur)"
}, {
  "sender": "Ddene Spellacey",
  "message": "duis faucibus accumsan odio curabitur convallis duis consequat dui nec nisi volutpat eleifend donec ut dolor morbi vel lectus in",
  "title": "College Road Trip"
}, {
  "sender": "Gabbey Bracchi",
  "message": "eget massa tempor convallis nulla neque libero convallis eget eleifend luctus ultricies eu nibh quisque id justo",
  "title": "Nutty Professor, The"
}, {
  "sender": "Queenie Tootin",
  "message": "nec euismod scelerisque quam turpis adipiscing lorem vitae mattis nibh ligula nec sem duis",
  "title": "Dirty Story"
}, {
  "sender": "Harmonie Goch",
  "message": "sagittis dui vel nisl duis ac nibh fusce lacus purus aliquet at feugiat non pretium quis lectus suspendisse potenti",
  "title": "Think Like a Man"
}, {
  "sender": "Wilt Goligher",
  "message": "turpis enim blandit mi in porttitor pede justo eu massa donec dapibus duis at",
  "title": "Singh Is Kinng"
}, {
  "sender": "Che Bartleman",
  "message": "diam id ornare imperdiet sapien urna pretium nisl ut volutpat sapien arcu sed augue aliquam erat",
  "title": "Henry: Portrait of a Serial Killer"
}, {
  "sender": "Boy Ielden",
  "message": "elementum in hac habitasse platea dictumst morbi vestibulum velit id pretium iaculis diam erat fermentum justo",
  "title": "Wyrmwood"
}, {
  "sender": "Richie Perell",
  "message": "morbi a ipsum integer a nibh in quis justo maecenas rhoncus aliquam",
  "title": "Cheetah"
}, {
  "sender": "Avram Dunlea",
  "message": "libero ut massa volutpat convallis morbi odio odio elementum eu interdum eu tincidunt in leo maecenas",
  "title": "Comandante"
}, {
  "sender": "Dasya Hindrick",
  "message": "aliquet ultrices erat tortor sollicitudin mi sit amet lobortis sapien",
  "title": "Seraphim Falls"
}, {
  "sender": "Dal Brech",
  "message": "nulla mollis molestie lorem quisque ut erat curabitur gravida nisi at nibh in hac habitasse platea dictumst aliquam",
  "title": "March of the Movies (Film Parade, The)"
}]

# print(categories_with_parents)
