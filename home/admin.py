from django.contrib import admin

from home.models import DuesAdmissionEntry, PaymentAdmissionEntry, DuesEntryAuto, PaymentEntryAuto


# Register your models here.


class DuesAdmissionEntryAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'year', 'season', 'semester', 'program', 'amount', 'date']
    list_filter = ['student_id', 'year']

class PaymentAdmissionEntryAdmin(admin.ModelAdmin):
    list_display = ['p_student_id', 'p_semester', 'p_amount', 'p_money_receipt', 'p_mode_payment', 'p_campus', 'p_date']
    list_filter = ['p_student_id', 'p_campus']


class DuesEntryAutoAdmin(admin.ModelAdmin):
    list_display = ['dues_auto_student_id', 'dues_auto_year', 'dues_auto_season', 'dues_auto_program', 'dues_auto_discount', 'dues_auto_date']
    list_filter = ['dues_auto_student_id', 'dues_auto_year']

class PaymentEntryAutoAdmin(admin.ModelAdmin):
    list_display = ['p_auto_student_id', 'p_auto_amount', 'p_auto_money_receipt', 'p_auto_campus', 'p_auto_mode_payment', 'p_auto_date']
    list_filter = ['p_auto_student_id', 'p_auto_amount']


admin.site.register(DuesAdmissionEntry, DuesAdmissionEntryAdmin),
admin.site.register(PaymentAdmissionEntry, PaymentAdmissionEntryAdmin),

admin.site.register(DuesEntryAuto, DuesEntryAutoAdmin),
admin.site.register(PaymentEntryAuto, PaymentEntryAutoAdmin),
