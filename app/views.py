from django.shortcuts import render

# Create your views here.
def data_render(request):
    data='This data is our assumption'
    d={'assumption':data}

    return render(request,'data_render.html',context=d)

def login(request):
    data='Login page'
    d={'username':data,'age':15}

    return render(request,'login.html',context=d)