# Generated by Django 4.2 on 2023-05-28 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('licitagil', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_envio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=10)),
            ],
        ),
        migrations.RenameField(
            model_name='licitacao',
            old_name='data_pregao',
            new_name='data_disputa',
        ),
        migrations.RenameField(
            model_name='licitacao',
            old_name='item',
            new_name='equipamento',
        ),
        migrations.RemoveField(
            model_name='licitacao',
            name='data_entrega',
        ),
        migrations.RemoveField(
            model_name='licitacao',
            name='numero',
        ),
        migrations.AddField(
            model_name='licitacao',
            name='disputa',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='licitacao',
            name='documentos',
            field=models.CharField(default='https://alunounivespbr-my.sharepoint.com/:f:/r/personal/1806596_aluno_univesp_br/Documents/PJI110/Teste?csf=1&web=1&e=sydN8n', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='licitacao',
            name='local_entrega',
            field=models.CharField(default='SÃO PAULO', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='licitacao',
            name='tipo_compra',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='licitagil.tipo_compra'),
        ),
        migrations.AddField(
            model_name='licitacao',
            name='tipo_envio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='licitagil.tipo_envio'),
        ),
    ]
