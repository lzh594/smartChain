# Generated by Django 4.2.1 on 2023-08-01 09:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('handle', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='history',
            old_name='所选app',
            new_name='App',
        ),
        migrations.RenameField(
            model_name='history',
            old_name='操作',
            new_name='Op',
        ),
        migrations.RenameField(
            model_name='history',
            old_name='手机号',
            new_name='Phone',
        ),
        migrations.RenameField(
            model_name='history',
            old_name='应用商',
            new_name='Superior',
        ),
        migrations.RenameField(
            model_name='history',
            old_name='时间戳',
            new_name='TimeStamp',
        ),
        migrations.RenameField(
            model_name='usrdata',
            old_name='所选app',
            new_name='App',
        ),
        migrations.RenameField(
            model_name='usrdata',
            old_name='哈希索引',
            new_name='HashID',
        ),
        migrations.RenameField(
            model_name='usrdata',
            old_name='操作',
            new_name='Op',
        ),
        migrations.RenameField(
            model_name='usrdata',
            old_name='手机号',
            new_name='Phone',
        ),
        migrations.RenameField(
            model_name='usrdata',
            old_name='当前状态',
            new_name='State',
        ),
        migrations.RenameField(
            model_name='usrdata',
            old_name='应用商',
            new_name='Superior',
        ),
        migrations.RenameField(
            model_name='usrdata',
            old_name='时间戳',
            new_name='TimeStamp',
        ),
    ]
