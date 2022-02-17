# Generated by Django 4.0.2 on 2022-02-17 11:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('interview_scheduler', '0003_rename_time_slot_interviewer_from_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interviewer',
            name='from_date',
        ),
        migrations.RemoveField(
            model_name='interviewer',
            name='to_date',
        ),
        migrations.RemoveField(
            model_name='student',
            name='from_date',
        ),
        migrations.RemoveField(
            model_name='student',
            name='to_date',
        ),
        migrations.AddField(
            model_name='interviewer',
            name='from_time',
            field=models.CharField(choices=[('9', '09:00 AM'), ('10', '10:00 AM'), ('11', '11:00 AM'), ('12', '12:00 PM'), ('13', '01:00 PM'), ('14', '02:00 PM'), ('15', '03:00 PM'), ('16', '04:00 PM'), ('17', '05:00 PM'), ('18', '06:00 PM'), ('19', '07:00 PM')], default='9', max_length=2),
        ),
        migrations.AddField(
            model_name='interviewer',
            name='to_time',
            field=models.CharField(choices=[('9', '09:00 AM'), ('10', '10:00 AM'), ('11', '11:00 AM'), ('12', '12:00 PM'), ('13', '01:00 PM'), ('14', '02:00 PM'), ('15', '03:00 PM'), ('16', '04:00 PM'), ('17', '05:00 PM'), ('18', '06:00 PM'), ('19', '07:00 PM')], default='10', max_length=2),
        ),
        migrations.AddField(
            model_name='student',
            name='from_time',
            field=models.CharField(choices=[('9', '09:00 AM'), ('10', '10:00 AM'), ('11', '11:00 AM'), ('12', '12:00 PM'), ('13', '01:00 PM'), ('14', '02:00 PM'), ('15', '03:00 PM'), ('16', '04:00 PM'), ('17', '05:00 PM'), ('18', '06:00 PM'), ('19', '07:00 PM')], default='9', max_length=2),
        ),
        migrations.AddField(
            model_name='student',
            name='to_time',
            field=models.CharField(choices=[('9', '09:00 AM'), ('10', '10:00 AM'), ('11', '11:00 AM'), ('12', '12:00 PM'), ('13', '01:00 PM'), ('14', '02:00 PM'), ('15', '03:00 PM'), ('16', '04:00 PM'), ('17', '05:00 PM'), ('18', '06:00 PM'), ('19', '07:00 PM')], default='10', max_length=2),
        ),
        migrations.AlterField(
            model_name='interviewer',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 2, 17, 11, 56, 46, 965090, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='student',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 2, 17, 11, 56, 46, 965090, tzinfo=utc)),
        ),
    ]
