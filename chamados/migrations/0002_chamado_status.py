# Generated by Django 4.1.1 on 2022-09-21 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamados', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chamado',
            name='status',
            field=models.CharField(choices=[('Solicitação', 'Solicitação'), ('Dúvida', 'Dúvida')], max_length=200, null=True),
        ),
    ]
