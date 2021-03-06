# Generated by Django 4.0.4 on 2022-05-13 14:55

from decimal import Decimal
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=128)),
            ],
            options={
                "db_table": "core_category",
            },
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("image", models.ImageField(upload_to="images/")),
                ("default", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Item",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(default="Item", max_length=128)),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        validators=[
                            django.core.validators.MinValueValidator(Decimal("0.01"))
                        ],
                    ),
                ),
                (
                    "condition",
                    models.CharField(
                        choices=[
                            (
                                "NEW",
                                "A brand-new, unused, unopened, undamaged item in its original packaging.",
                            ),
                            ("USED", "An item that has been used previously."),
                            ("USED_LIKE_NEW", "Seller referbished."),
                            (
                                "FOR_PARTS",
                                "An item that does not function as intended and is not fully operational. ",
                            ),
                        ],
                        max_length=128,
                    ),
                ),
                (
                    "delivery_Option",
                    models.CharField(
                        choices=[
                            ("DELIVERY", "Home delivery"),
                            ("PICKUP", "Self pickup"),
                            ("HANDOFF", "Inperson handoff"),
                        ],
                        default="PICKUP",
                        max_length=128,
                    ),
                ),
                ("description", models.TextField(max_length=1800, null=True)),
                ("is_sold", models.BooleanField(default=False)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.category"
                    ),
                ),
                ("images", models.ManyToManyField(to="core.image")),
                (
                    "seller",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "core_item",
            },
        ),
        migrations.CreateModel(
            name="PaymentInfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cardholder_name", models.CharField(max_length=128)),
                ("card_number", models.CharField(max_length=16)),
                ("cvc", models.CharField(max_length=3)),
                ("expiry_month", models.IntegerField()),
                ("expiry_year", models.IntegerField()),
            ],
            options={
                "db_table": "core_payment_info",
            },
        ),
        migrations.CreateModel(
            name="ShippingDetails",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("full_name", models.CharField(max_length=128)),
                ("address", models.CharField(max_length=128)),
                ("postal_code", models.SmallIntegerField()),
                ("city", models.CharField(max_length=128)),
                ("country", django_countries.fields.CountryField(max_length=2)),
            ],
            options={
                "db_table": "core_shipping_details",
            },
        ),
        migrations.CreateModel(
            name="UserBids",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        validators=[
                            django.core.validators.MinValueValidator(Decimal("0.01"))
                        ],
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("expires", models.DateTimeField(blank=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("REJECTED", "Rejected"),
                            ("ACCEPTED", "Accepted"),
                            ("PENDING", "Pending"),
                            ("COMPLETED", "Completed"),
                        ],
                        default="PENDING",
                        max_length=128,
                    ),
                ),
                (
                    "item_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.item"
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "core_user_bids",
            },
        ),
        migrations.CreateModel(
            name="SearchHistory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("search_string", models.CharField(max_length=128)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "core_search_history",
            },
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.TextField(blank=True, max_length=500)),
                (
                    "image",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.image",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "core_profile",
            },
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "rating",
                    models.SmallIntegerField(
                        blank=True,
                        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)],
                        null=True,
                    ),
                ),
                (
                    "buyer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="buyer_users",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.item"
                    ),
                ),
                (
                    "seller",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="seller_users",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "core_order",
            },
        ),
        migrations.CreateModel(
            name="Notification",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=128)),
                ("message", models.CharField(max_length=280)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("read", models.BooleanField(default=False)),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "core_notifications",
            },
        ),
        migrations.CreateModel(
            name="DeliveryMethod",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "del_choice",
                    models.CharField(
                        choices=[
                            ("DS", "Delivery service"),
                            ("PU", "Pick up"),
                            ("PB", "Postbox"),
                            ("SWS", "Speak with seller"),
                        ],
                        max_length=128,
                    ),
                ),
                (
                    "bid_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.userbids"
                    ),
                ),
            ],
            options={
                "db_table": "core_delivery_method",
            },
        ),
    ]
