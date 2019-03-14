from django.urls import path
from mainapp import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include

urlpatterns = [
    path('toys/', views.ToysList.as_view(), name='toys'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toy'),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('logout', views.Logout.as_view()),
]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
urlpatterns = format_suffix_patterns(urlpatterns)
