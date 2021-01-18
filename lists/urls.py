"""superlists URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from lists import views

urlpatterns = [
    url(r'^new$', views.new_list, name='new_list'),
    url(r'^(\d+)/$', views.view_list, name='view_list'),
    url(r'^(\d+)/add_item$', views.add_item, name='add_item'),
  
  ]
"""
r'^(\d+)/$'ist eine regularexpression, 
    \d+  steht für eine irgendeine zahl vom typ int. (ohne plus wären nur integer mit einer dezimalzahl: 0 bis 9 gesucht)
    das r steht für raw string. 
    ^ = start, $ = end -- match the start or end of the string 
            ->  durch ^ wird festgelegt, dass die übereinstimmung genau am Anfang sein muss.
                durch $ , dass nichts weiter kommen darf. => es werden nur int Zahlen >=0 gefolgt von / angenommen.
"""