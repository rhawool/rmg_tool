# Generated by Django 4.1.4 on 2022-12-21 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='associate',
            name='advance_java',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='associate',
            name='agile',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='associate',
            name='attitude',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='associate',
            name='cloud_tech',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='associate',
            name='core_java',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='associate',
            name='devops',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='associate',
            name='emp_name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='associate',
            name='experience',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='associate',
            name='experience_range',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='associate',
            name='frontend_angular',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='associate',
            name='frontend_html_css_javascript',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='associate',
            name='frontend_react',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='associate',
            name='general_communication',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='associate',
            name='grade',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='associate',
            name='location_constraint',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='associate',
            name='non_relational_database',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='associate',
            name='orm_jpa_hibernate',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='associate',
            name='overall_feedback',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='associate',
            name='relational_database',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='associate',
            name='servlet_and_jsp',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='associate',
            name='skill_cluster',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='associate',
            name='spring_boot',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='associate',
            name='spring_framework',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='associate',
            name='spring_mvc',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='associate',
            name='spring_security',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='associate',
            name='struts',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='associate',
            name='web_services_rest_api',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='associate',
            name='web_services_soap',
            field=models.CharField(max_length=250),
        ),
    ]
