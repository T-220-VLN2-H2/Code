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
  "sender": "Chaddie Cordes",
  "message": "lacus at velit vivamus vel nulla eget eros elementum pellentesque quisque porta volutpat erat quisque erat eros viverra eget congue eget semper rutrum nulla nunc purus phasellus in felis donec semper sapien a libero nam dui proin leo odio porttitor id consequat in consequat ut nulla sed accumsan felis ut at dolor quis odio consequat varius integer ac leo pellentesque ultrices mattis odio donec vitae nisi nam ultrices libero non",
  "title": "By the Gun"
}, {
  "sender": "Kira Kobsch",
  "message": "luctus tincidunt nulla mollis molestie lorem quisque ut erat curabitur gravida nisi at nibh in hac habitasse platea dictumst aliquam augue quam sollicitudin vitae consectetuer eget rutrum at lorem integer tincidunt ante vel ipsum praesent blandit lacinia erat vestibulum sed magna at nunc commodo placerat praesent blandit nam nulla integer pede justo lacinia eget tincidunt eget tempus vel pede morbi porttitor lorem id ligula suspendisse ornare consequat lectus in est risus auctor sed tristique in tempus sit amet sem fusce consequat nulla nisl nunc nisl duis",
  "title": "Johnny Suede"
}, {
  "sender": "Fenelia Sessions",
  "message": "sollicitudin mi sit amet lobortis sapien sapien non mi integer ac neque duis bibendum morbi non quam nec dui luctus rutrum nulla tellus in sagittis dui vel nisl duis ac nibh fusce lacus purus aliquet at feugiat non pretium quis lectus suspendisse potenti in eleifend quam a odio in hac habitasse platea dictumst maecenas ut massa quis augue luctus tincidunt nulla mollis molestie lorem quisque ut erat curabitur gravida nisi at nibh in hac habitasse platea dictumst aliquam augue quam sollicitudin vitae consectetuer",
  "title": "Rocket Singh: Salesman of the Year"
}, {
  "sender": "Annecorinne Facchini",
  "message": "bibendum imperdiet nullam orci pede venenatis non sodales sed tincidunt eu felis fusce posuere felis sed lacus morbi sem mauris laoreet ut rhoncus aliquet pulvinar sed nisl nunc rhoncus dui vel sem sed sagittis nam congue risus semper porta volutpat quam pede lobortis ligula sit amet eleifend pede libero quis orci nullam molestie nibh in lectus pellentesque at nulla suspendisse potenti cras in purus eu magna vulputate luctus cum sociis natoque penatibus et magnis dis parturient montes nascetur ridiculus mus vivamus vestibulum sagittis sapien cum sociis natoque penatibus et magnis dis parturient montes nascetur ridiculus mus etiam",
  "title": "Saint Ange (House of Voices)"
}, {
  "sender": "Liuka Bellard",
  "message": "maecenas tincidunt lacus at velit vivamus vel nulla eget eros elementum pellentesque quisque porta volutpat erat quisque erat eros viverra eget congue eget semper rutrum nulla nunc purus phasellus in felis donec semper sapien a libero nam dui proin leo odio porttitor id consequat in consequat ut nulla sed accumsan felis ut at dolor quis odio consequat varius integer ac leo pellentesque ultrices mattis odio donec vitae nisi nam ultrices libero non mattis pulvinar nulla pede ullamcorper augue a suscipit nulla elit ac nulla sed vel enim sit amet nunc viverra dapibus nulla suscipit ligula in lacus curabitur at ipsum",
  "title": "Deception"
}, {
  "sender": "Heather Kilmaster",
  "message": "at turpis a pede posuere nonummy integer non velit donec diam neque vestibulum eget vulputate ut ultrices vel augue vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae donec pharetra magna vestibulum aliquet ultrices erat tortor sollicitudin mi sit amet lobortis sapien sapien non mi integer ac neque duis bibendum morbi non quam nec dui luctus rutrum nulla tellus in sagittis dui vel nisl duis ac nibh fusce lacus purus aliquet at feugiat non pretium quis lectus suspendisse potenti in eleifend quam a odio in hac habitasse platea dictumst maecenas ut massa quis",
  "title": "Romance on the High Seas"
}, {
  "sender": "Chaim Tankard",
  "message": "id ligula suspendisse ornare consequat lectus in est risus auctor sed tristique in tempus sit amet sem fusce consequat nulla nisl nunc nisl duis bibendum felis sed interdum venenatis turpis enim blandit mi in porttitor pede justo eu massa donec dapibus duis at velit eu est congue elementum in hac habitasse platea dictumst morbi vestibulum velit id pretium iaculis diam erat fermentum justo nec condimentum neque sapien placerat ante nulla justo aliquam",
  "title": "Incredible Hulk, The"
}, {
  "sender": "Kin Morehall",
  "message": "hac habitasse platea dictumst maecenas ut massa quis augue luctus tincidunt nulla mollis molestie lorem quisque ut erat curabitur gravida nisi at nibh in hac habitasse platea dictumst aliquam augue quam sollicitudin vitae consectetuer eget rutrum at lorem integer tincidunt ante vel ipsum praesent blandit lacinia erat vestibulum sed magna at nunc commodo placerat praesent blandit nam nulla integer pede justo lacinia eget tincidunt eget tempus vel pede morbi porttitor lorem id ligula suspendisse ornare consequat lectus in est risus auctor sed tristique in tempus sit",
  "title": "Adventures of Food Boy, The (aka High School Superhero)"
}, {
  "sender": "Byron Manjot",
  "message": "potenti nullam porttitor lacus at turpis donec posuere metus vitae ipsum aliquam non mauris morbi non lectus aliquam sit amet diam in magna bibendum imperdiet nullam orci pede venenatis non sodales sed tincidunt eu felis fusce posuere felis sed lacus morbi sem mauris laoreet ut rhoncus aliquet pulvinar sed nisl nunc rhoncus dui vel sem sed sagittis nam congue risus semper porta volutpat quam pede lobortis",
  "title": "Descent, The"
}, {
  "sender": "Erroll Rigmond",
  "message": "sit amet diam in magna bibendum imperdiet nullam orci pede venenatis non sodales sed tincidunt eu felis fusce posuere felis sed lacus morbi sem mauris laoreet ut rhoncus aliquet pulvinar sed nisl nunc rhoncus dui vel sem sed sagittis nam congue risus semper porta volutpat quam pede lobortis ligula sit amet eleifend pede libero quis orci nullam molestie nibh in lectus pellentesque at nulla suspendisse potenti cras in purus eu magna vulputate luctus cum sociis natoque penatibus et magnis dis parturient montes nascetur ridiculus mus vivamus vestibulum sagittis sapien cum sociis natoque penatibus et magnis dis",
  "title": "She Wouldn't Say Yes"
}]

# print(categories_with_parents)
