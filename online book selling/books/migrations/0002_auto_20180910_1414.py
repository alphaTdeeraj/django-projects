# Generated by Django 2.1.1 on 2018-09-10 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='branch',
            field=models.CharField(choices=[('Mechanical', 'Mechanical'), ('Computer Science', 'Computer Science'), ('Information Science', 'Information Science'), ('Chemical Engineering', 'Chemical Engineering'), ('Civil Engineering', 'Civil Engineering'), ('Electrical Engineering', 'Electrical Engineering'), ('Electronic and Communication', 'Electronic and Communication'), ('Medical Electronics', 'Medical Electronics'), ('Instrumentaion Engineering', 'Instrumentaion Engineering'), ('Architecture', 'Architecture'), ('Biotechnology', 'Biotechnology')], max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='sem',
            field=models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)]),
        ),
    ]