# Generated by Django 4.1.4 on 2023-01-20 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=60)),
                ('author_name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=50)),
                ('s_phone', models.BigIntegerField()),
                ('s_sem', models.IntegerField()),
                ('s_password', models.CharField(max_length=50)),
                ('s_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryapp.course')),
            ],
        ),
        migrations.CreateModel(
            name='Issue_book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('bo_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryapp.books')),
                ('stu_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryapp.student')),
            ],
        ),
        migrations.AddField(
            model_name='books',
            name='course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryapp.course'),
        ),
    ]