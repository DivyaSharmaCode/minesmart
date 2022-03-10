# Generated by Django 3.0.4 on 2020-03-23 03:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MachineParty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('contact', models.IntegerField()),
                ('village', models.CharField(max_length=50)),
                ('crasher', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('measurement', models.CharField(max_length=30)),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MixCredit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('category', models.CharField(choices=[('machine_party', 'machine_party'), ('vehicle_party', 'vehicle_party'), ('daily_work', 'daily_work')], max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MixDebit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('category', models.CharField(choices=[('part_debit', 'part_debit'), ('owner_debit', 'owner_debit'), ('purchase_debit', 'purchase_debit'), ('worker_debit', 'worker_debit'), ('daily_expense_debit', 'daily_expense_debit')], max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('contact', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='VehicleParty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('contact', models.IntegerField()),
                ('village', models.CharField(max_length=50)),
                ('credit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.MixCredit')),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('contact', models.IntegerField()),
                ('village', models.CharField(max_length=30)),
                ('salary', models.IntegerField()),
                ('exit_date', models.DateField(blank=True, null=True)),
                ('debit_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='database.MixDebit')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Owner')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleSupply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('quantity', models.IntegerField()),
                ('Material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Material')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Owner')),
            ],
        ),
        migrations.CreateModel(
            name='Recorder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Owner')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseParty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('contact', models.IntegerField()),
                ('village', models.CharField(max_length=50)),
                ('debit_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='database.MixDebit')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Owner')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('quantity', models.IntegerField()),
                ('rate', models.FloatField()),
                ('net_amount', models.FloatField()),
                ('remark', models.CharField(blank=True, max_length=50)),
                ('paid', models.BooleanField(default=False)),
                ('payment', models.FloatField()),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Material')),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.PurchaseParty')),
            ],
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('debit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.MixDebit')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Owner')),
            ],
        ),
        migrations.AddField(
            model_name='mixdebit',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Owner'),
        ),
        migrations.AddField(
            model_name='mixcredit',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Owner'),
        ),
        migrations.AddField(
            model_name='material',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Owner'),
        ),
        migrations.CreateModel(
            name='MachineSupply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('quantity', models.IntegerField()),
                ('drilling_feet', models.FloatField(default=0)),
                ('Material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Material')),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.MachineParty')),
            ],
        ),
        migrations.AddField(
            model_name='machineparty',
            name='credit_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.MixCredit'),
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Owner')),
            ],
        ),
        migrations.CreateModel(
            name='Debit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('debit_amount', models.IntegerField()),
                ('remark', models.CharField(blank=True, max_length=50)),
                ('debit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.MixDebit')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Owner')),
            ],
        ),
        migrations.CreateModel(
            name='DailyWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('village', models.CharField(max_length=50)),
                ('five_feet', models.FloatField()),
                ('five_feet_rate', models.FloatField()),
                ('two_half_feet', models.FloatField()),
                ('two_half_feet_rate', models.FloatField()),
                ('diesel_spend', models.FloatField()),
                ('net_amount', models.FloatField()),
                ('date', models.DateField()),
                ('credit_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='database.MixCredit')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='DailyExpense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('staff', 'staff'), ('petrol', 'petrol'), ('food', 'food'), ('office_accesories', 'office_accesories'), ('other', 'other')], max_length=50)),
                ('debit_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='database.MixDebit')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Owner')),
            ],
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('credit_amount', models.FloatField()),
                ('remark', models.CharField(blank=True, max_length=50)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Owner')),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.MixCredit')),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_credit', models.IntegerField(default=0)),
                ('total_debit', models.IntegerField(default=0)),
                ('balance', models.IntegerField(default=0)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='database.Owner')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('feet', models.FloatField()),
                ('five_feet', models.FloatField()),
                ('two_half_feet', models.FloatField()),
                ('remark', models.CharField(blank=True, max_length=50)),
                ('paid', models.BooleanField(default=False)),
                ('payment', models.FloatField(default=0)),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.VehicleParty')),
            ],
            options={
                'unique_together': {('party', 'date')},
            },
        ),
        migrations.CreateModel(
            name='MachineWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('drilling_feet', models.FloatField()),
                ('diesel_amount', models.FloatField()),
                ('remark', models.CharField(blank=True, max_length=50)),
                ('paid', models.BooleanField(default=False)),
                ('holes', models.IntegerField(default=0)),
                ('payment', models.FloatField(default=0)),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Machine')),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.MachineParty')),
            ],
            options={
                'unique_together': {('party', 'date')},
            },
        ),
    ]
