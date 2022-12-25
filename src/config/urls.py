
from django.http import JsonResponse
from django.contrib import admin
from django.urls import path, include

def check(request):
    #return HttpResponse("Hello")
    data = {"name": "Dima"}
    #return HttpResponse(str(data), content_type="application/json")
    return JsonResponse(data)
    

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health-check/', check),
    path('posts/', include('posts.urls')),
 


]
