# Generated by Django 4.2.4 on 2023-08-20 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionModelPricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, null=True)),
                ('pricing_type', models.CharField(choices=[('MONTHLY', '월'), ('ANNUAL', '년')], max_length=8, verbose_name='부과방식')),
                ('unit', models.IntegerField(verbose_name='금액')),
                ('vat', models.BooleanField(verbose_name='VAT')),
            ],
            options={
                'verbose_name': '구독모델 결제',
                'verbose_name_plural': '구독모델 결제',
                'db_table': 'subscription_model_pricing',
            },
        ),
        migrations.CreateModel(
            name='SubscriptionModelService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, null=True)),
                ('service_type', models.CharField(choices=[('MAIN', '주요 서비스'), ('INHERIT', '종속'), ('ETC', '기타 부대 업무')], max_length=8, verbose_name='서비스종류')),
                ('title', models.CharField(max_length=64, verbose_name='내용', blank=True)),
            ],
            options={
                'verbose_name': '구독모델 서비스',
                'verbose_name_plural': '구독모델 서비스목록',
                'db_table': 'subscription_model_service',
            },
        ),
        migrations.CreateModel(
            name='SubscriptionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Deleted At')),
                ('codename', models.CharField(choices=[('BASIC', 'Basic'), ('PREMIUM', 'Premium'), ('WARRANTY', 'Warranty')], max_length=16, verbose_name='코드네임')),
                ('name', models.CharField(max_length=16, verbose_name='이름')),
                ('pricings', models.ManyToManyField(db_table='subscription_model_to_pricing', related_name='models', to='subscription.subscriptionmodelpricing', verbose_name='결제방식')),
                ('services', models.ManyToManyField(db_table='subscription_model_to_service', related_name='models', to='subscription.subscriptionmodelservice', verbose_name='서비스')),
            ],
            options={
                'verbose_name': '구독모델',
                'verbose_name_plural': '구독모델',
                'db_table': 'subscription_model',
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Deleted At')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='subscription.subscriptionmodel', verbose_name='구독모델')),
            ],
            options={
                'verbose_name': '구독',
                'verbose_name_plural': '구독 목록',
                'db_table': 'subscription',
            },
        ),
    ]
