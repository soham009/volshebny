from django.urls import include, path

from generateletter import views

urlpatterns = [
    path("", views.list_view.as_view(), name="list"),
    path("russian_visa/<int:pk>", views.gen_rus_visa.as_view(), name="gen_rus_visa"),
    path("english_visa/<int:pk>", views.gen_eng_visa.as_view(), name="gen_eng_visa"),
    path("english_voucher/<int:pk>", views.gen_eng_voucher.as_view(), name="gen_eng_voucher"),
    path("russian_voucher/<int:pk>", views.gen_rus_voucher.as_view(), name="gen_rus_voucher"),
]
