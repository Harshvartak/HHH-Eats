# Generated by Django 3.1.2 on 2020-10-29 18:21

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('f_name', models.CharField(blank=True, max_length=20, null=True)),
                ('m_name', models.CharField(blank=True, max_length=40, null=True)),
                ('l_name', models.CharField(blank=True, max_length=20, null=True)),
                ('address_line_1', models.TextField(blank=True)),
                ('address_line_2', models.TextField(blank=True)),
                ('City', models.CharField(max_length=200)),
                ('pin_code', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(message='Enter a valid pin code', regex='^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$')])),
                ('i_agree', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_customer', models.BooleanField(default=False)),
                ('is_owner', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField(default=0)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodapp.item')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total_amount', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('delivery_addr', models.CharField(blank=True, max_length=50)),
                ('status', models.CharField(choices=[('Waiting', 'Waiting'), ('Placed', 'Placed'), ('Acknowledged', 'Acknowledged'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled'), ('Dispatched', 'Dispatched')], default='Waiting', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rname', models.CharField(max_length=100)),
                ('info', models.CharField(max_length=40)),
                ('min_ord', models.CharField(max_length=5)),
                ('location', models.CharField(max_length=40)),
                ('r_logo', models.FileField(upload_to='')),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Closed', 'Closed')], default='Open', max_length=50)),
                ('approved', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('account_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='foodapp.account')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_images')),
            ],
            options={
                'abstract': False,
            },
            bases=('foodapp.account',),
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('account_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='foodapp.account')),
                ('Registration_Number', models.IntegerField()),
                ('pan_no', models.CharField(blank=True, max_length=10, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logo')),
            ],
            options={
                'abstract': False,
            },
            bases=('foodapp.account',),
        ),
        migrations.CreateModel(
            name='orderItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(default=0)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodapp.menu')),
                ('ord_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodapp.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='r_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodapp.restaurant'),
        ),
        migrations.AddField(
            model_name='menu',
            name='r_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodapp.restaurant'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='foodapp.owner'),
        ),
        migrations.AddField(
            model_name='order',
            name='orderedBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodapp.customer'),
        ),
    ]
