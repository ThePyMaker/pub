from django.db import models

# Create your models here.
from django.forms import ModelForm


class DuesAdmissionEntry(models.Model):

    student_id = models.CharField(blank=False, max_length=14)
    year = models.CharField(blank=False, max_length=5)
    season = models.CharField(blank=False, max_length=10)
    semester = models.CharField(blank=False, max_length=5)
    program = models.CharField(blank=False, max_length=150)
    amount = models.CharField(blank=False, max_length=20)
    date = models.CharField(blank=False, max_length=20)

    ip = models.CharField(blank=True, max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student_id

class DuesAdmissionEntryForm(ModelForm):
    class Meta:
        model = DuesAdmissionEntry
        fields = ['student_id', 'year', 'season', 'semester', 'program', 'amount', 'date']


class PaymentAdmissionEntry(models.Model):

    p_student_id = models.CharField(blank=False, max_length=14)
    p_semester = models.CharField(blank=False, max_length=5)
    p_amount = models.CharField(blank=False, max_length=20)
    p_money_receipt = models.CharField(blank=False, max_length=25)
    p_mode_payment = models.CharField(blank=False, max_length=20)
    p_campus = models.CharField(blank=False, max_length=20)
    p_date = models.CharField(blank=False, max_length=20)

    ip = models.CharField(blank=True, max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.p_student_id

class PaymentAdmissionEntryForm(ModelForm):
    class Meta:
        model = PaymentAdmissionEntry
        fields = ['p_student_id', 'p_semester', 'p_amount', 'p_money_receipt', 'p_mode_payment', 'p_campus', 'p_date']


class DuesEntryAuto(models.Model):

    dues_auto_student_id = models.CharField(blank=False, max_length=14)
    dues_auto_year = models.CharField(blank=False, max_length=5)
    dues_auto_season = models.CharField(blank=False, max_length=10)
    dues_auto_program = models.CharField(blank=False, max_length=150)
    dues_auto_discount = models.CharField(blank=True, max_length=20)
    dues_auto_date = models.CharField(blank=False, max_length=20)

    ip = models.CharField(blank=True, max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student_id

class DuesEntryAutoForm(ModelForm):
    class Meta:
        model = DuesEntryAuto
        fields = ['dues_auto_student_id', 'dues_auto_year', 'dues_auto_season', 'dues_auto_program', 'dues_auto_discount', 'dues_auto_date']



class PaymentEntryAuto(models.Model):

    p_auto_student_id = models.CharField(blank=False, max_length=14)
    p_auto_amount = models.CharField(blank=False, max_length=20)
    p_auto_money_receipt = models.CharField(blank=False, max_length=25)
    p_auto_campus = models.CharField(blank=False, max_length=20)
    p_auto_mode_payment = models.CharField(blank=False, max_length=20)
    p_auto_date = models.CharField(blank=False, max_length=20)

    ip = models.CharField(blank=True, max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.p_student_id

class PaymentEntryAutoForm(ModelForm):
    class Meta:
        model = PaymentEntryAuto
        fields = ['p_auto_student_id', 'p_auto_amount', 'p_auto_money_receipt', 'p_auto_campus', 'p_auto_mode_payment', 'p_auto_date']
