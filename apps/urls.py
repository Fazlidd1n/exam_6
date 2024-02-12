from django.conf.urls.static import static
from django.urls import path

from apps.views import CarbonadListVeiw, CarbonadDeleteView, CarbonadUpdateView
from root.settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
                  path('', CarbonadListVeiw.as_view(), name='carbonad_list'),
                  path('delete/<int:pk>', CarbonadDeleteView.as_view(), name='carbonad_delete'),
                  path('update/<int:pk>', CarbonadUpdateView.as_view(), name='carbonad_update'),
              ] + static(MEDIA_URL, document_root=MEDIA_ROOT)
