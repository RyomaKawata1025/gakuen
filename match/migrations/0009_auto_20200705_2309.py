# Generated by Django 2.1.5 on 2020-07-05 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0008_auto_20200702_2034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('JAVA', 'JAVA'), ('C', 'C'), ('C++', 'C++'), ('C#', 'C#'), ('Javascript', 'Javascript'), ('jQuery', 'jQuery'), ('HTML・CSS', 'HTML・CSS'), ('PHP', 'PHP'), ('Ruby', 'Ruby'), ('Python', 'Python'), ('Objective-c', 'Objective-c'), ('Swift', 'Swift'), ('その他', 'その他')], max_length=25, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='skill',
            old_name='target',
            new_name='pro_id',
        ),
        migrations.RemoveField(
            model_name='recruit',
            name='language',
        ),
        migrations.AddField(
            model_name='language',
            name='rec_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='match.Recruit'),
        ),
    ]