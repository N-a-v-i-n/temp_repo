# Generated by Django 4.2.2 on 2023-07-21 10:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental_app', '0003_send_text_to_owner_reciever_seen_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad_posted_logs',
            name='user_posted_date',
            field=models.DateField(default=datetime.datetime(2023, 7, 21, 10, 37, 32, 288796), null=True),
        ),
        migrations.AlterField(
            model_name='ad_posting_payments_details',
            name='created_At',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 21, 10, 37, 32, 288796), null=True),
        ),
        migrations.AlterField(
            model_name='deleted_post_details',
            name='deleted_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 21, 10, 37, 32, 288796), null=True),
        ),
        migrations.AlterField(
            model_name='failure_response',
            name='created_At',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 21, 10, 37, 32, 288796), null=True),
        ),
        migrations.AlterField(
            model_name='property_details',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 21, 10, 37, 32, 273182), null=True),
        ),
        migrations.AlterField(
            model_name='property_details',
            name='post_expire_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 20, 10, 37, 32, 273182)),
        ),
        migrations.AlterField(
            model_name='razorpay_payment_order_details',
            name='created_At',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 21, 10, 37, 32, 288796), null=True),
        ),
        migrations.AlterField(
            model_name='send_text_to_owner',
            name='request_user_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 21, 10, 37, 32, 273182)),
        ),
        migrations.AlterField(
            model_name='super_admin_users',
            name='created_At',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 21, 10, 37, 32, 288796), null=True),
        ),
        migrations.AlterField(
            model_name='super_admin_users',
            name='last_login_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 21, 10, 37, 32, 288796), null=True),
        ),
        migrations.AlterField(
            model_name='unsafe_images',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 21, 10, 37, 32, 273182)),
        ),
        migrations.AlterField(
            model_name='user_collections',
            name='active_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 21, 10, 37, 32, 288796)),
        ),
        migrations.AlterField(
            model_name='user_collections',
            name='visted_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 21, 10, 37, 32, 288796)),
        ),
        migrations.AlterField(
            model_name='user_free_limits',
            name='unlocked_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 21, 10, 37, 32, 288796), null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 21, 10, 37, 32, 273182), null=True),
        ),
        migrations.AlterField(
            model_name='users_credentials_app_token',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 21, 10, 37, 32, 273182)),
        ),
        migrations.AlterField(
            model_name='users_credentials_ips',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 21, 10, 37, 32, 273182)),
        ),
    ]
