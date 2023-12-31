# Generated by Django 4.2.2 on 2023-07-14 09:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental_app', '0002_alter_ad_posted_logs_user_posted_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='send_text_to_owner',
            name='reciever_seen',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='ad_posted_logs',
            name='user_posted_date',
            field=models.DateField(default=datetime.datetime(2023, 7, 14, 9, 52, 16, 47336), null=True),
        ),
        migrations.AlterField(
            model_name='ad_posting_payments_details',
            name='created_At',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 14, 9, 52, 16, 47336), null=True),
        ),
        migrations.AlterField(
            model_name='deleted_post_details',
            name='deleted_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 14, 9, 52, 16, 47336), null=True),
        ),
        migrations.AlterField(
            model_name='failure_response',
            name='created_At',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 14, 9, 52, 16, 47336), null=True),
        ),
        migrations.AlterField(
            model_name='property_details',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 14, 9, 52, 16, 47336), null=True),
        ),
        migrations.AlterField(
            model_name='property_details',
            name='post_expire_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 13, 9, 52, 16, 47336)),
        ),
        migrations.AlterField(
            model_name='razorpay_payment_order_details',
            name='created_At',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 14, 9, 52, 16, 47336), null=True),
        ),
        migrations.AlterField(
            model_name='send_text_to_owner',
            name='request_user_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 14, 9, 52, 16, 47336)),
        ),
        migrations.AlterField(
            model_name='super_admin_users',
            name='created_At',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 14, 9, 52, 16, 47336), null=True),
        ),
        migrations.AlterField(
            model_name='super_admin_users',
            name='last_login_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 14, 9, 52, 16, 47336), null=True),
        ),
        migrations.AlterField(
            model_name='unsafe_images',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 14, 9, 52, 16, 47336)),
        ),
        migrations.AlterField(
            model_name='user_collections',
            name='active_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 14, 9, 52, 16, 47336)),
        ),
        migrations.AlterField(
            model_name='user_collections',
            name='visted_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 14, 9, 52, 16, 47336)),
        ),
        migrations.AlterField(
            model_name='user_free_limits',
            name='unlocked_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 14, 9, 52, 16, 47336), null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 14, 9, 52, 16, 47336), null=True),
        ),
        migrations.AlterField(
            model_name='users_credentials_app_token',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 14, 9, 52, 16, 47336)),
        ),
        migrations.AlterField(
            model_name='users_credentials_ips',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 14, 9, 52, 16, 47336)),
        ),
    ]
