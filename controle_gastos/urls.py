"""controle_gastos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from contas.views import home, listagem, nova_transacao, update, delete, ControleGastosListView, ControleGastosView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('', listagem, name='url_listagem'),
    path('nova', nova_transacao, name='url_nova'),
    path('update/<int:pk>/', update, name='url_update'),
    path('delete/<int:pk>/', delete, name='url_delete'),
    path('api/ControleGastosListView', ControleGastosListView.as_view()),
    path('api/ControleGastosView', ControleGastosView.as_view()),
    path('api/ControleGastosView/<int:id>', ControleGastosView.as_view())
]