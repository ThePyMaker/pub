from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from home.models import DuesAdmissionEntryForm, DuesAdmissionEntry, PaymentAdmissionEntryForm, PaymentAdmissionEntry, \
    DuesEntryAutoForm, DuesEntryAuto, PaymentEntryAuto, PaymentEntryAutoForm


# Create your views here.
def index(request):
    return render(request, 'index.html')

def due_adm_entry(request):
    if request.method == 'POST':
        form = DuesAdmissionEntryForm(request.POST)
        if form.is_valid():
            data = DuesAdmissionEntry()
            data.student_id = form.cleaned_data['student_id']
            data.year = form.cleaned_data['year']
            data.season = form.cleaned_data['season']
            data.semester = form.cleaned_data['semester']
            data.program = form.cleaned_data['program']
            data.amount = form.cleaned_data['amount']
            data.date = form.cleaned_data['date']

            data.ip = request.META.get('REMOTE_ADDR')
            data.save()

            messages.success(request, "Information has been successfully submitted to the database.")
            return HttpResponseRedirect('/due_adm_entry/')
    form = DuesAdmissionEntryForm
    context = {
        'form': form,
    }

    return render(request, 'due_adm_entry.html', context)


def payment_adm_entry(request):
    if request.method == 'POST':
        form = PaymentAdmissionEntryForm(request.POST)
        if form.is_valid():
            data = PaymentAdmissionEntry()
            data.p_student_id = form.cleaned_data['p_student_id']
            data.p_semester = form.cleaned_data['p_semester']
            data.p_amount = form.cleaned_data['p_amount']
            data.p_money_receipt = form.cleaned_data['p_money_receipt']
            data.p_mode_payment = form.cleaned_data['p_mode_payment']
            data.p_campus = form.cleaned_data['p_campus']
            data.p_date = form.cleaned_data['p_date']

            data.ip = request.META.get('REMOTE_ADDR')
            data.save()

            messages.success(request, "Information has been successfully submitted to the database.")
            return HttpResponseRedirect('/payment_adm_entry/')
    form = PaymentAdmissionEntryForm
    context = {
        'form': form,
    }

    return render(request, 'payment_adm_entry.html', context)


def due_auto(request):
    if request.method == 'POST':
        form = DuesEntryAutoForm(request.POST)
        if form.is_valid():
            data = DuesEntryAuto()
            data.dues_auto_student_id = form.cleaned_data['dues_auto_student_id']
            data.dues_auto_year = form.cleaned_data['dues_auto_year']
            data.dues_auto_season = form.cleaned_data['dues_auto_season']
            data.dues_auto_program = form.cleaned_data['dues_auto_program']
            data.dues_auto_discount = form.cleaned_data['dues_auto_discount']
            data.dues_auto_date = form.cleaned_data['dues_auto_date']

            data.ip = request.META.get('REMOTE_ADDR')
            data.save()

            messages.success(request, "Information has been successfully submitted to the database.")
            return HttpResponseRedirect('/due_auto/')
    form = DuesEntryAutoForm
    context = {
        'form': form,
    }

    return render(request, 'due_auto.html', context)


def payment_auto(request):
    if request.method == 'POST':
        form = PaymentEntryAutoForm(request.POST)
        if form.is_valid():
            data = PaymentEntryAuto()
            data.p_auto_student_id = form.cleaned_data['p_auto_student_id']
            data.p_auto_amount = form.cleaned_data['p_auto_amount']
            data.p_auto_money_receipt = form.cleaned_data['p_auto_money_receipt']
            data.p_auto_campus = form.cleaned_data['p_auto_campus']
            data.p_auto_mode_payment = form.cleaned_data['p_auto_mode_payment']
            data.p_auto_date = form.cleaned_data['p_auto_date']

            data.ip = request.META.get('REMOTE_ADDR')
            data.save()

            messages.success(request, "Information has been successfully submitted to the database.")
            return HttpResponseRedirect('/payment_auto/')
    form = PaymentEntryAutoForm
    context = {
        'form': form,
    }

    return render(request, 'payment_auto.html', context)


def dues_id_student_wise(request):
    return render(request, 'dues_id_student_wise.html')


def view_dues_st_wise(request):
    return render(request, 'view_dues_st_wise.html')