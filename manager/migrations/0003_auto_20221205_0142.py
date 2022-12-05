# Generated by Django 3.2.16 on 2022-12-05 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_email_created_on'),
    ]

    operations = [
        migrations.CreateModel(
            name='Password',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(default='password', max_length=255)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(default='example', max_length=255, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Username',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='username', max_length=255)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='email',
            name='email',
            field=models.EmailField(default='abc@example.com', max_length=255, unique=True),
        ),
        migrations.CreateModel(
            name='PasswordService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.email')),
                ('password', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.password')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.service')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.username')),
            ],
        ),
    ]
