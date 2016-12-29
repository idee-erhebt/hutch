from django.shortcuts import render,render_to_response,redirect
from home.forms import IdeaForm,quesForm,RegForm,EmailIdForm
from django.http import HttpResponse,HttpResponseRedirect
from .models import idearegister,addques
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.core.mail import send_mail
from handle_uploaded_file import handle_uploaded_file,handle_upload_sendidea,handle_uploaded
from django.views.static import serve
from wsgiref.util import FileWrapper
import os
counted=0


def index(request):
#    return HttpResponse("<h1>hellloo</h1>")
    return render(request,'home/index.html')
def schedule(request):
    return render(request,'home/schedule.html')
def venue(request):
    return render(request,'home/venue.html')

@csrf_exempt
def registration(request,registration_id):
    form_class = RegForm
    if request.method == "POST":
        form = RegForm(request.POST, request.FILES)
      #  messages.error(request, "Error")
        p = idearegister.objects.raw('select * from home_idearegister where id=' + str(registration_id) )
        for i in p:
            named=i.ideaTitle
            k=i.idea
            reciepentMailId=i.mailId
        if form.is_valid():
            model_inst=form.save(commit=False)
            model_inst.ideaTitle=named
            model_inst.idea=k
            senderMailId=model_inst.mailId
            resume="uploads/"+str(model_inst.ideaFile)
            model_inst.save()

            handle_uploaded_file(reciepentMailId,senderMailId,resume,named)
            return redirect('/')
        else:
             print 'heeyya'
             print form.errors
             print type(list(form.errors))
             return HttpResponse('try again')

        #PLEASE FILL 404 REQUEST

    return render(request, 'home/ideareg.html', {
        'form': form_class,
    })

def forumed(request,forum_id):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EmailIdForm(request.POST)
        # check whether it's valid:
        t=0
        if form.is_valid():
            eid=form.cleaned_data['emailId']
            p = idearegister.objects.raw("select * from home_idearegister where checked=" + str(1)+" and mailId='"+str(eid)+"' and accessToIdea="+str(1))
            for i in p:
                t=t+1
        if(t>0):
            return HttpResponseRedirect('/forum/'+str(forum_id))
        else:
            return render(request, 'home/forumed.html', {'form': form,'message':'not yet registered'})

    # if a GET (or any other method) we'll create a blan
    else:
        form = EmailIdForm()
    return render(request, 'home/forumed.html', {'form': form})

@csrf_exempt
def forum(request,forum_id):
    form_class = quesForm
#    print form_class
    global counted
    if request.method == "POST":
        form = quesForm(request.POST)
    #    print form
        counted=0
        l=[]
        messages.error(request, "Error")
        if form.is_valid():
            form.save()
            tp=-999999
            p = addques.objects.raw('select * from home_addques where idforum='+str(forum_id) +' or idForum='+str(tp))
            # sendit={}
   #         s={}
#            g={}
            for i in p:
                l.append(i.timetaken)
            if(len(l)):
                n=max(l)
            else:
                n=0
            counted=n+1
            flag=0
            for i in p:
  #              s[i.name] = i.question
                k=addques(name=i.name,question=i.question,timetaken=i.timetaken,idForum=i.idForum)
                for j in p:
                    if (j.name == k.name and j.question == k.question and  k.timetaken==0 and k.timetaken!=j.timetaken):
                        addques.objects.filter(timetaken=0).delete()
                        addques.objects.filter(idForum=-999999).delete()
                        flag = 1
                if (k.timetaken == 0 and flag==0):
                    k.timetaken = counted
                    k.idForum=forum_id
                    k.save()
                    addques.objects.filter(timetaken=0).delete()
                    addques.objects.filter(idForum=-999999).delete()
                    print "i enter in ", k, k.timetaken
                    counted = counted + 1

            g = {}
            for i in p:
                g[i.timetaken] = {i.name: i.question}
            # counted = counted + 1
            print g
            l = list(g)
            print l
            print 'in the inner loop'
 #           print "hheeee"
            # d=SortedDis
            allInIdea = idearegister.objects.raw("select * from home_idearegister where id=" + str(forum_id) + " and accessToIdea=" + str(1))

            t = {}
            co = 0
            for i in allInIdea:
                name = i.firstName + " " + i.lastName
                mailed = i.mailId
                phno = i.phoneNumber
                k = name + "      " + "       " + mailed + "       " + phno
                t[co] = k
                co = co + 1
            return render(request, 'home/commentinput.html', {
                'form': form_class, 'material': g, 'lists': l,'formId':forum_id,'finalised':t
            })
    allInIdea = idearegister.objects.raw("select * from home_idearegister where id=" + str(forum_id) +" and accessToIdea=" + str(1))

    p = addques.objects.raw('select * from home_addques where idForum='+str(forum_id))
    g = {}
    print 'in the outer loop'
    for i in p:
        print 'heyy'
        print i.timetaken,i.name,i.question
        print 'hello'
        g[i.timetaken] = {i.name: i.question}
    print 'hwllo'
    #counted = counted + 1
    print g
    l=list(g)
    print l
    t={}
    co=0
    for i in allInIdea:
        name=i.firstName+" "+i.lastName
        mailed=i.mailId
        phno=i.phoneNumber
        k=name+"      "+"       "+mailed+"       "+phno
        t[co]=k
        co=co+1
    print "hheeee"
                # d=SortedDis
    return render(request, 'home/commentinput.html', {
                'form': form_class,'material':g,'lists':l,'finalised':t,'formId':forum_id,
            })

def dashboard(request):
    idea={}
    p=idearegister.objects.raw("select * from home_idearegister where checked="+str(1))

    for i in p:
        print i.id,i.ideaTitle
        idea[i.id]={i.ideaTitle:i.idea}
    print idea
    return render(request, 'home/dashboard.html',{'idea':idea,})

@csrf_exempt
def submitit(request):
    flagIdeatitle=0
    if request.method == "POST":
        form = IdeaForm(request.POST, request.FILES)
        #messages.error(request, "Error")
        if form.is_valid():
            model_inst = form.save(commit=False)
            model_inst.accessToIdea = 1
            model_inst.headOfIdea = 1
            k = idearegister.objects.raw('select * from home_idearegister ')
            for m in k:
                if(m.ideaTitle==model_inst.ideaTitle):
                    flagIdeatitle=1
            fileOfIdea = str(model_inst.ideaFile)
            nameOfIdea = str(model_inst.ideaTitle)
            mailSender=str(model_inst.mailId)
            if(flagIdeatitle==0):
                model_inst.save()
            else:
                return HttpResponse("<script>alert('Try a Different Idea Name');</script><a href='/submittion'>Clcik here to return back to idea submission</a>")
            handle_upload_sendidea(fileOfIdea,nameOfIdea)
            handle_uploaded(mailSender)
        else:
            print form.errors
            messages.error(request, "Error")
          #  print messages.error()
            #         print type(list(form.errors))
#            return HttpResponse("uoeeeeeeeeeeeee")
            k= list(form.errors)
            print k
            if(k[0]=='mailId'):
                return HttpResponse("<script>alert('enetr a correct mailid');</script><a href='/submittion'>Clcik here to return back to idea submission</a>")
            return HttpResponse("<h1>TRY AGAIN </h1>")
    form_class=IdeaForm()
    return render(request, 'home/ideainput.html', {
        'form': form_class,
    })

def getting(request,forum_id):
    k = idearegister.objects.raw('select * from home_idearegister where id='+str(forum_id))
    for i in k:
        t=str(i.ideaFile)
    filename = t
    wrapper = FileWrapper(file(filename))
    response = HttpResponse(wrapper, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=%s' % os.path.basename(filename)
    response['Content-Length'] = os.path.getsize(filename)
    return response