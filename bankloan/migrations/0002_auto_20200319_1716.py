# Generated by Django 2.2.4 on 2020-03-19 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankloan', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='approvals',
            old_name='applicantincome',
            new_name='ApplicantIncome',
        ),
        migrations.RenameField(
            model_name='approvals',
            old_name='coapplicatincome',
            new_name='CoapplicatIncome',
        ),
        migrations.RenameField(
            model_name='approvals',
            old_name='credithistory',
            new_name='Credit_History',
        ),
        migrations.RenameField(
            model_name='approvals',
            old_name='dependants',
            new_name='Dependants',
        ),
        migrations.RenameField(
            model_name='approvals',
            old_name='graduatededucation',
            new_name='Education',
        ),
        migrations.RenameField(
            model_name='approvals',
            old_name='gender',
            new_name='Gender',
        ),
        migrations.RenameField(
            model_name='approvals',
            old_name='loanamt',
            new_name='LoanAmount',
        ),
        migrations.RenameField(
            model_name='approvals',
            old_name='loanterm',
            new_name='Loan_Amount_Term',
        ),
        migrations.RenameField(
            model_name='approvals',
            old_name='married',
            new_name='Married',
        ),
        migrations.RenameField(
            model_name='approvals',
            old_name='area',
            new_name='Property_Area',
        ),
        migrations.RenameField(
            model_name='approvals',
            old_name='selfemployed',
            new_name='Self_Employed',
        ),
    ]
