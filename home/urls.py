from django.urls import path

from.import views

urlpatterns = [
    path('', views.index, name='index'),
    path('due_adm_entry/', views.due_adm_entry, name='due_adm_entry'),
    path('payment_adm_entry/', views.payment_adm_entry, name='payment_adm_entry'),
    path('due_auto/', views.due_auto, name='due_auto'),
    path('payment_auto/', views.payment_auto, name='payment_auto'),
    path('dues_id_student_wise/', views.dues_id_student_wise, name='dues_id_student_wise'),
    path('dues_id_student_wise/open_dues_id_student_wise/', views.open_dues_id_student_wise, name='open_dues_id_student_wise'),
    path('view_dues_st_wise/', views.view_dues_st_wise, name='view_dues_st_wise'),

]