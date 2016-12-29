from django.shortcuts import render,redirect
from .forms import UserForm,tryform
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from .models import registered
@csrf_exempt
def index(request):
    form_class = UserForm
    if request.method == "POST":
        form = UserForm(request.POST)
        messages.error(request, "Error")
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
             print 'heeyya'
             return HttpResponse('try again')
             print form.errors
            #            print type(list(form.errors))
        #PLEASE FILL 404 REQUEST
    return render(request, 'regi/signup.html', {
        'form': form_class,
    })

def CheckUser(request):
    print "hiii there "
    form_class = tryform
    eid=""
    if request.method == "POST":
        form = tryform(request.POST)
        messages.error(request, "Error")
        if form.is_valid():
   #         form.save()
            print form.cleaned_data['eid']
            eid=form.cleaned_data['eid']
            passwd=form.cleaned_data['password1']
            print eid
            p = registered.objects.raw('select * from regi_registered where emailid="'+eid +'" and password="'+passwd+'"')
            for i in p:
                if(i.emailid==eid and i.password==passwd):#will check for the list of ids and password if they are going
                    k=i.id
                    print k
                    kt='/logged/'+str(k)
                    return redirect(kt)
                #this will redirect the user to his login page and all other such info
            return render(request, 'regi/userSaved.html')
        else:
             print 'heeyya'
             return HttpResponse('<h1>try again</h1>')
             print form.errors
            #            print type(list(form.errors))
        #PLEASE FILL 404 REQUEST
    return render(request, 'regi/login.html', {
        'form': form_class,
    })
