from django.shortcuts import render, redirect
from .models import *
from .forms import CreateInDiscussion
from django.core.mail import send_mail
from Dforum.settings import EMAIL_HOST_USER

def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if request.method == "POST":
        print(f'\n\n\nif part post request\n\n\n')
        if User_tab.objects.filter(username=username.strip(), password=password.strip()):
            user = User_tab.objects.get(username=username, password=password)
            request.session['user'] = [user.id, user.name,
                                       user.email, user.username, user.contact, user.password]
            return redirect("/")

    if request.session.has_key('user'):
        response = User_tab.objects.filter(id=request.session['user'][0])
        raw = response[0].__dict__
        name = raw['name']

        request.session['user'][1] = name

        forums = []

        response_ = forum.objects.all()
        
        for frm in response_:
            forum__ = frm.__dict__
            forum_name = User_tab.objects.filter(id=forum__['userid_id'])
            forum_name = forum_name[0].__dict__
            name = forum_name['name']
            email = forum_name['email']
            forum__['username'] = name
            forum__['email'] = email
            response_discus = Discussion.objects.filter(forum=forum__['id'])
            forum__['discuss'] = []
            for dis in response_discus:
                discu__ = dis.__dict__
                res_name = User_tab.objects.filter(id=discu__['userid_id'])
                res_name = res_name[0].__dict__
                name = res_name['name']
                discu__['username'] = name
                forum__['discuss'].append(discu__)

            forums.append(forum__)

        return render(request, 'home.html', {'name': name,'forums' : forums})
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        username = request.POST.get('username')

        username_ = username
        password_ = password
        message = f'usernmae :{username_} , password : {password_}'

        send_mail('Register Sucessfull', message, EMAIL_HOST_USER, [email])

        User_tab.objects.create(
            name=name, email=email, contact=phone, password=password, username=username)

        return redirect('/')
    return render(request, 'register.html', {})


def home(request):
    forums = forum.objects.all()
    count = forums.count()
    discussions = []
    for i in forums:
        discussions.append(i.discussion_set.all())

    context = {'forums': forums,
               'count': count,
               'discussions': discussions}
    return render(request, 'home.html', context)


def addInForum(request):
    if request.POST:
        if ('topic' not in request.POST):
            return render(request, 'addInForum.html', {})
        userid = request.session['user'][0]
        topic = request.POST['topic']
        description = request.POST['description']
        link = request.POST['link']
        forum.objects.create(userid_id=userid, topic=topic,
                             description=description, link=link)

        return redirect('/')

    if request.session.has_key('user'):
        response = User_tab.objects.filter(id=request.session['user'][0])
        raw = response[0].__dict__
        name = raw['name']

        request.session['user'][1] = name

        return render(request, 'addInForum.html', {'name': name})
    else:
        return redirect('/')


def addInDiscussion(request):
    if request.POST:
        userid  = request.session['user'][0]
        discuss = request.POST['discuss']
        forum_   = request.POST['forum']

        Discussion.objects.create(userid_id=userid, forum_id=forum_,
                             discuss=discuss)

        return redirect('/')

    if request.session.has_key('user'):
        response = User_tab.objects.filter(id=request.session['user'][0])
        raw = response[0].__dict__
        name = raw['name']

        request.session['user'][1] = name

        form_ = forum.objects.all()
        topics = []
        for top in form_:
            frm = top.__dict__
            topics.append(frm)

        return render(request, 'addInDiscussion.html', {'name': name,'topics':topics})
    else:
        return redirect('/')


def viewforum(request):

    if(request.GET):
        forum.objects.filter(id=request.GET['forumid']).delete()
        return redirect('view')

    forums = []

    response = forum.objects.filter(userid=request.session['user'][0])

    for frm in response:
        forum__ = frm.__dict__
        response_discus = Discussion.objects.filter(forum=forum__['id'])
        forum__['discuss'] = []
        for dis in response_discus:
            discu__ = dis.__dict__
            res_name = User_tab.objects.filter(id=discu__['userid_id'])
            res_name = res_name[0].__dict__
            name = res_name['name']
            discu__['username'] = name
            forum__['discuss'].append(discu__)

        forums.append(forum__)

    if request.session.has_key('user'):
        response = User_tab.objects.filter(id=request.session['user'][0])
        raw = response[0].__dict__
        name = raw['name']

        request.session['user'][1] = name

        return render(request, 'viewforum.html', {'forums': forums})
    else:
        return redirect('/')


def profile(request):

    if(request.POST):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        User_tab.objects.filter(id=request.session['user'][0]).update(
            name=name, email=email, contact=phone, password=password)

        return redirect('profile')

    if request.session.has_key('user'):
        response = User_tab.objects.filter(id=request.session['user'][0])
        raw = response[0].__dict__
        name = raw['name']

        request.session['user'][1] = name

        userinfo = User_tab.objects.filter(id=request.session['user'][0])
        userinfo = userinfo[0].__dict__
        return render(request, 'profile.html', {'user': userinfo})
    else:
        return redirect('/')


def logout(request):
    request.session.flush()
    request.session.clear_expired()
    return redirect('login')