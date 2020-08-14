from django.urls import path
from . import views
urlpatterns=[
  path('',views.dtodo),
  path('atodo',views.atodo),
  path('deltodo/<int:di>',views.deltodo)
]