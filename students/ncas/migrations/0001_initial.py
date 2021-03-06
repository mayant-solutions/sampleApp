# Generated by Django 2.1.5 on 2019-02-15 05:28

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='Name')),
                ('hod', models.CharField(max_length=20, verbose_name='HOD')),
            ],
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('sem', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)], verbose_name='Sem')),
                ('s_mark1', models.IntegerField(validators=[django.core.validators.MaxValueValidator(50), django.core.validators.MinValueValidator(0)], verbose_name='First Internal mark')),
                ('s_mark2', models.IntegerField(validators=[django.core.validators.MaxValueValidator(50), django.core.validators.MinValueValidator(0)], verbose_name='Second Internal mark')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('adm_no', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000)], verbose_name='Admission No')),
                ('reg_no', models.IntegerField(primary_key=True, serialize=False, verbose_name='Reg No')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ncas.Course', verbose_name='Course')),
                ('details', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ncas.Course', verbose_name='Course')),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('detail', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ncas.Tutor', verbose_name='Tutor'),
        ),
        migrations.AddField(
            model_name='mark',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ncas.Student', verbose_name='Student'),
        ),
        migrations.AddField(
            model_name='mark',
            name='sub',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ncas.Subject', verbose_name='Subject'),
        ),
    ]
