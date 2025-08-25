from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html',{'name':'Venkat'})

def add(request):
    
    val1 = int(request.POST.get('num1'))
    val2 = int(request.POST.get('num2'))
    val3 = val1 + val2
    return render(request, 'result.html', {'result': val3})
    