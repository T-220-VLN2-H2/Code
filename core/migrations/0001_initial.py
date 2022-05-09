# Generated by Django 4.0.4 on 2022-05-09 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('parent', models.BigIntegerField(default=None, null=True)),
            ],
            options={
                'db_table': 'core_category',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='images/')),
                ('default', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='Item', max_length=128)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('condition', models.CharField(choices=[('NEW', 'A brand-new, unused, unopened, undamaged item in its original packaging.'), ('USED', 'An item that has been used previously.'), ('USED_LIKE_NEW', 'Seller referbished.'), ('FOR_PARTS', 'An item that does not function as intended and is not fully operational. ')], max_length=128)),
                ('delivery_Option', models.CharField(choices=[('DELIVERY', 'Home delivery'), ('PICKUP', 'Self pickup'), ('HANDOFF', 'Inperson handoff')], default='PICKUP', max_length=128)),
                ('description', models.TextField(max_length=1800, null=True)),
                ('is_sold', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.category')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'core_item',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer_users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'core_order',
            },
        ),
        migrations.CreateModel(
            name='PaymentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardholder_name', models.CharField(max_length=128)),
                ('card_number', models.CharField(max_length=16)),
                ('cvc', models.CharField(max_length=3)),
                ('expiry_month', models.IntegerField()),
                ('expiry_year', models.IntegerField()),
            ],
            options={
                'db_table': 'core_payment_info',
            },
        ),
        migrations.CreateModel(
            name='ShippingDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=128)),
                ('postal_code', models.SmallIntegerField()),
                ('city', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'core_shipping_details',
            },
        ),
        migrations.CreateModel(
            name='UserRatings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=0, max_digits=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.order')),
            ],
            options={
                'db_table': 'core_user_ratings',
            },
        ),
        migrations.CreateModel(
            name='UserBids',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('expires', models.DateTimeField(blank=True)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.item')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'core_user_bids',
            },
        ),
        migrations.CreateModel(
            name='SearchHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_string', models.CharField(max_length=128)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'core_search_history',
            },
        ),
        migrations.CreateModel(
            name='RatingUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Rater', ''), ('Ratee', '')], max_length=128)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_rating', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.userratings')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=500)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'core_profile',
            },
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.ManyToManyField(to='core.item')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.order')),
            ],
            options={
                'db_table': 'core_order_items',
            },
        ),
        migrations.CreateModel(
            name='OrderHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_array', models.ManyToManyField(to='core.order')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'core_order_history',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='order_items',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.orderitems'),
        ),
        migrations.AddField(
            model_name='order',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller_users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('message', models.CharField(max_length=128)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('read', models.BooleanField(default=False)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'core_question',
            },
        ),
        migrations.CreateModel(
            name='ItemImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ManyToManyField(to='core.image')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.item')),
            ],
        ),
    ]
