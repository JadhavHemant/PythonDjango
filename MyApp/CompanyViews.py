from django.shortcuts import render
def CommonView(request):
    return render(request,"Company.html")
def HomeView(request):
    return render(request,"Home.html")
def AboutView(request):
    return render(request,"AboutUs.html")
def ContactView(request):
    return render(request,"ContactUs.html")
def ServiceView(request):
    return render(request,"Services.html")