# Generated by Django 2.0.1 on 2018-01-03 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cor',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('referencia', models.CharField(max_length=30, unique=True)),
                ('nome', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=100)),
                ('descricao', models.CharField(blank=True, max_length=200, null=True)),
                ('detalhe', models.CharField(blank=True, max_length=50, null=True)),
                ('preco', models.FloatField()),
                ('foto', models.CharField(blank=True, max_length=200, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.Categoria')),
                ('cor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.Cor')),
            ],
        ),
        migrations.CreateModel(
            name='Tamanho',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.Categoria')),
            ],
        ),
        migrations.AddField(
            model_name='tamanho',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.Tipo'),
        ),
        migrations.AddField(
            model_name='produto',
            name='tamanho',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.Tamanho'),
        ),
        migrations.AddField(
            model_name='produto',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.Tipo'),
        ),
        migrations.AddField(
            model_name='cor',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.Tipo'),
        ),
    ]
