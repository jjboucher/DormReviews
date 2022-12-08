# Generated by Django 4.1.1 on 2022-12-08 04:31

from django.db import migrations

def addLogos(apps, schema_editor):
    
    # get models from app
    university = apps.get_model('dormapp', 'University')
    logo = apps.get_model('dormapp', 'UniversityPhoto')

    syracuseU = university.objects.get(name='Syracuse University')
    cornellU = university.objects.get(name='Cornell University')
    syracuseLogo = logo.objects.create(university=syracuseU, photo='university-photos/test_data_syracuse_logo.png')
    cornellLogo = logo.objects.create(university=cornellU, photo='university-photos/test_data_cornell_logo.png')

class Migration(migrations.Migration):

    dependencies = [
        ('dormapp', '0003_adding_logos'),
    ]

    operations = [
        migrations.RunPython(addLogos)
    ]
