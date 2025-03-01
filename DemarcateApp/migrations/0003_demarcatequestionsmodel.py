# Generated by Django 4.1.2 on 2023-05-16 13:41

import DemarcateApp.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ImagesApp', '0005_imagemodel_image_number'),
        ('QuestionsApp', '0014_questiongroupmodel_is_demarcate'),
        ('DemarcateApp', '0002_alter_demarcatequestion_question_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DemarcateQuestionsModel',
            fields=[
                ('Id_Question', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('Question_Number', models.IntegerField(default=DemarcateApp.models.DemarcateQuestionsModel.number, unique=True)),
                ('Question_Text', models.CharField(blank=True, max_length=5000, null=True)),
                ('Question_Marks', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('Group_Name_Of_Quesitons', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='QuestionsApp.questiongroupmodel', verbose_name='Group Name of Subject')),
                ('Image_For_Question', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ImagesApp.imagemodel', verbose_name='Link Image')),
            ],
        ),
    ]
