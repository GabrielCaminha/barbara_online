# Generated by Django 5.1.1 on 2024-10-28 14:29

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barbara_app', '0008_remove_agressor_historico_ocorrencia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ocorrencia',
            name='nome_agressor',
        ),
        migrations.AddField(
            model_name='agressor',
            name='ficha_criminal',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='agressor',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos_agressores/'),
        ),
        migrations.AddField(
            model_name='agressor',
            name='ultima_vitima',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='barbara_app.vitima'),
        ),
        migrations.AddField(
            model_name='agressor',
            name='vitimas',
            field=models.ManyToManyField(blank=True, related_name='agressores', to='barbara_app.vitima'),
        ),
        migrations.AddField(
            model_name='botaopanico',
            name='data_ocorrido',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='botaopanico',
            name='hora',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='botaopanico',
            name='localizacao',
            field=models.TextField(default='Endereço não informado'),
        ),
        migrations.AddField(
            model_name='ocorrencia',
            name='agressor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ocorrencias', to='barbara_app.agressor'),
        ),
        migrations.AlterField(
            model_name='ocorrencia',
            name='data_ocorrencia',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
