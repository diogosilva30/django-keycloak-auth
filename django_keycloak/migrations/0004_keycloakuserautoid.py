# Generated by Django 2.2 on 2021-12-31 11:16

from django.db import migrations, models
import django_keycloak.managers


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('django_keycloak', '0003_auto_20210406_1426'),
    ]

    operations = [
        migrations.CreateModel(
            name='KeycloakUserAutoId',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='username')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('keycloak_id', models.UUIDField(unique=True, verbose_name='keycloak_id')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'swappable': 'AUTH_USER_MODEL',
            },
            managers=[
                ('objects', django_keycloak.managers.KeycloakUserManagerAutoId()),
            ],
        ),
    ]
