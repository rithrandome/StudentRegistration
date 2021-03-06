# Generated by Django 2.1.7 on 2020-08-04 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('First_name', models.CharField(max_length=200)),
                ('Last_name', models.CharField(max_length=200)),
                ('Email', models.EmailField(max_length=254)),
                ('Mobile_number', models.CharField(max_length=10)),
                ('Date_of_birth', models.DateField(blank=True, default='', null=True)),
                ('Address', models.TextField(max_length=500)),
                ('Pin_code', models.CharField(max_length=10)),
                ('City', models.CharField(max_length=30)),
                ('State', models.CharField(max_length=30)),
                ('Country', models.CharField(max_length=30)),
                ('Course_applied', models.ManyToManyField(related_name='_studentinfo_Course_applied_+', to='StudentRegistration.StudentInfo')),
                ('Gender', models.ManyToManyField(related_name='_studentinfo_Gender_+', to='StudentRegistration.StudentInfo')),
                ('Hobbies', models.ManyToManyField(related_name='_studentinfo_Hobbies_+', to='StudentRegistration.StudentInfo')),
            ],
        ),
    ]
