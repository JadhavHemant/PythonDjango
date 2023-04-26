"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from MyApp import views
from MyApp import UserData
from MyApp import MarksData
from MyApp import StudentViews
from MyApp import CompanyViews
from MyApp import AjaxView
from MyApp import OrmViews
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('first', views.FirstView),
    # path('Addition', views.PageView),
    # path('pagedata',UserData.PageData),
    # path('per',MarksData.Data),
    # path("",StudentViews.StudentView),
    
    
    
    # path("",CompanyViews.CommonView),
    # path("home",CompanyViews.HomeView),
    # path("about-us",CompanyViews.AboutView),
    # path("contact-us",CompanyViews.ContactView),
    # path("service",CompanyViews.ServiceView),
    # path("",AjaxView.StudentView),
    # path("studentlist",AjaxView.studentlist),
    # path("addstudent",AjaxView.AddStudentView),
    # path("updatestudent",AjaxView.UpdateStudentView),
    # path("deletestudent",AjaxView.DeleteStudentView),
    # path("viewstudent",AjaxView.StudentbyRnoView),
    
    path("",OrmViews.StudentView)
    

    
    
]
