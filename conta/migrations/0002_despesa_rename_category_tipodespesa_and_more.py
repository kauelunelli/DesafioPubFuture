# Generated by Django 4.0.1 on 2022-01-13 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('conta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
                ('dataPagamento', models.DateField(default=django.utils.timezone.now)),
                ('dataPagamentoEsperado', models.DateField(default=django.utils.timezone.now)),
                ('descricao', models.TextField()),
                ('tipoDespesa', models.CharField(max_length=266)),
                ('dono', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameModel(
            old_name='Category',
            new_name='TipoDespesa',
        ),
        migrations.AlterModelOptions(
            name='tipodespesa',
            options={'verbose_name_plural': 'TipoDespesas'},
        ),
        migrations.RemoveField(
            model_name='receita',
            name='conta',
        ),
        migrations.DeleteModel(
            name='Expense',
        ),
    ]
