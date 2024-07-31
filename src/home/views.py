from django.shortcuts import render
from visitors.models import PageVisitors
def home(request):
    qs= PageVisitors.objects.all()
    page_qs = PageVisitors.objects.filter(path=request.path)
    PageVisitors.objects.create(path=request.path)
    return render(request,"index.html",context={'page_title':"My Page", "total_visitors":qs.count, 'page_visitors':page_qs.count() })