# Create your views here.
# -*- coding: utf-8 -*-
from mysite.ncsdd.models import *
from django.shortcuts import render_to_response
import time
import os
import logging
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from mysite.myauth import dd_required
from django.contrib.auth.models import Group
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist#,DoesNotExist
from django.forms.models  import modelform_factory
import mysite.ncsdd.models
from datetime import datetime
from django.forms import ModelForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.context_processors import csrf
#from django.utils import simplejson
import json
# class CantactForm(ModelForm):
    # class Meta:
        # model = Contact
        # widgets = {
            # 'datetime': DateTimeWidget(attrs={'id':"jieshou_date"}, usel10n = True)
        # }
#SampleForm = modelform_factory(Sample)
# @login_required 
# def load(request, class_alias, key):
    # klass = pyamf.load_class(class_alias).klass
    # return klass.objects.get(id=key)
# #@login_required 
# def loadAll(request, class_alias):
    # klass = pyamf.load_class(class_alias).klass
    # print klass
    # return klass.objects.all()
# #@login_required 
# def loadAttr(request, class_alias, key, attr):
    # obj = load(request,class_alias, key)
# #    print "load attr",obj
# #    print attr
    # r=getattr(obj, attr)
    # r=r.all()
# #    print r[0].user,type(r[0].user)
    # return r
# #@login_required 
# def save(request, obj):
    # logging.warn("save===============")
    # print obj,dir(obj)
    # obj.save()
# #@login_required 
# def saveList(request, objs):
    # for obj in objs:
        # obj.save()
# #@login_required 
# def remove(request, class_alias, key):
    # klass = pyamf.load_class(class_alias).klass
    # obj = klass.objects.get(id=key)
    # obj.delete()
# #@login_required    
# def removeList(request, class_alias, keys):
    # for key in keys:
        # remove(request,class_alias, key)
@login_required 
def getCurrentContacts(request):        
    return request.user.contact_set.all()
@login_required 
def getCurrentUser(request):
    return request.user
def saveuser(request):
    bh=request.POST["username"]
    password=request.POST["password"]
    try:
        u=User.objects.get(username=bh)
    except ObjectDoesNotExist,e:
        u=User(username=bh)
        u.set_password(password)
        u.save()
        user = authenticate(username=bh, password=password)
        if user is not None:
            login(request, user)
            r=HttpResponseRedirect("/dd/afterlogin")
            return(r)
        else:
            return HttpResponse("login fail")
    else:
        err=bh+" already used by others"
        r=render_to_response("registration/register.html",{"err":err})
    return r
def register(request):
    r=render_to_response("registration/register.html")
    return r

@login_required    
def afterlogin(request):
    user=request.user
    dd=Group.objects.get(name="dd")
    if dd in user.groups.all():
        r=HttpResponseRedirect("/dd/")
    else:
        r=HttpResponseRedirect("/dd/")
    return(r)
#@staff_member_required
def loginpage(request):
    c={}
    c.update(csrf(request))
    r=render_to_response("registration/login.html",c)
    return(r)
def mylogin(request):
    username = request.POST['username']
    password = request.POST['password']
    print username,password
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        r=HttpResponseRedirect("/dd/afterlogin")
        return(r)
        # Redirect to a success page.
    else:
        return HttpResponse("login faile")
        # Return an error message
def mylogout(request):
    logout(request)
    return HttpResponseRedirect("/accounts/login/")
def logout_user(http_request):
    logout(http_request)
 
def login_user(http_request, username, password):
    user = authenticate(username=username, password=password)
    if user is not None:
        login(http_request, user)
        return user
    return None

@login_required    
def index(request):
    logging.info("index")
    print dir(request.session)
    print request.session.keys
    print request.session.items
    print request.session._get_session_key()
    objects=Contact.objects.all()
    paginator= Paginator(objects, 5)#contact number per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    r=render_to_response("dd/dd_index.html",{"user":request.user,"contacts":contacts})
##    print dir(r)
    # r.headers["Pragma"]="No-cache"
    # r.headers["Cache-Control"]="no-cache"
    # r.headers["Expires"]="0"
##    print r.headers
    return(r)
@login_required
def newcontact(request):
    dic = {}
    dic.update(csrf(request))
    dic["new"]="1"
    r=render_to_response("dd/newcontact.html",dic)
    return(r)
@login_required
def savecontact(request):
    logging.info(request.POST)
    username=request.POST["user"]
    try:
        u=User.objects.get(username=username)
    except ObjectDoesNotExist,e:
        u=request.user
    # user =  models.ForeignKey(User)#委托人
    # shenqing_date = models.DateTimeField()#申请时间
    # danwei = models.CharField(max_length=30)#用户单位
    # sampletype=models.CharField(max_length=30)#样品类型
    # samplect=models.IntegerField()#样品数量
    # yiqi=models.CharField(max_length=30)#仪器或技术
    # fenxizhouqi=models.FloatField()#分析周期
    # wtbz = models.CharField(max_length=100)#委托备注
    # #======应用中心=====
    # jieshou_date = models.DateTimeField()#接收时间
    # contactbh = models.CharField(max_length=30,null=True)#委托单编号
    # state=models.IntegerField(default=0)#进度 状态
    # fxy =  models.IntegerField(null=True)#分析员
    # gj_date= models.DateTimeField(null=True)#预计完成时间
    # sj_date= models.DateTimeField(null=True)#实际完成时间
    # manyidu=models.CharField(max_length=30)#满意度
    # fxbz= models.CharField(max_length=100)#分析备注
    #===============
    new=request.POST["new"]
    shenqing=request.POST["shenqing"]
    danwei=request.POST["danwei"]
    sampletype=request.POST["sampletype"]
    samplect=request.POST["samplect"]
    yiqi=request.POST["yiqi"]
    fenxizhouqi=request.POST["fenxizhouqi"]
    wtbz=request.POST["wtbz"]
    
    jieshou=request.POST["jieshou"]
    bh=request.POST["contactbh"]
    state=request.POST["state"]
    if state=="" :
        state=0
    fxy =request.POST["fxy"]#分析员
    if fxy=="" :
        fxy=0
    gj_date=request.POST["gj_date"]#预计完成时间
    if gj_date=="":
        gj_date=None
    sj_date= request.POST["sj_date"]#实际完成时间
    if sj_date=="":
        sj_date=None
    manyidu=request.POST["manyidu"]#满意度
    fxbz= request.POST["fxbz"]#分析备注
    if new=="1":
        u.contact_set.create(contact_date=datetime.now()
            ,shenqing_date=shenqing
            ,danwei=danwei
            ,sampletype=sampletype
            ,samplect=samplect
            ,yiqi=yiqi
            ,fenxizhouqi=fenxizhouqi
            ,wtbz=wtbz
            
            ,jieshou_date=jieshou
            ,contactbh=bh
            ,state=state
            ,fxy =fxy#分析员
            ,gj_date=gj_date#预计完成时间
            ,sj_date= sj_date#实际完成时间
            ,manyidu=manyidu#满意度
            ,fxbz= fxbz#分析备注
            )
    else:
        contact_id=request.POST["contact_id"]
        c=u.contact_set.get(id=contact_id)
        c.shenqing_date=shenqing
        c.danwei=danwei
        c.sampletype=sampletype
        c.samplect=samplect
        c.yiqi=yiqi
        c.fenxizhouqi=fenxizhouqi
        c.wtbz=wtbz
        
        c.jieshou_date=jieshou
        c.contactbh=bh
        c.state=state
        c.fxy =fxy#分析员
        c.gj_date=gj_date#预计完成时间
        c.sj_date= sj_date#实际完成时间
        c.manyidu=manyidu#满意度
        c.fxbz= fxbz#分析备注
        c.show()
        c.save()
    r=HttpResponseRedirect("/dd/")
    return(r)
@login_required
def editcontact(request):
    #print request.GET
    dic = {}
    dic.update(csrf(request))
    contact_id=request.GET["id"]
    c=Contact.objects.get(id=contact_id)
    dic["user"]=request.user
    dic["contact"]=c
    dic["new"]=0
    r=render_to_response("dd/newcontact.html",dic)
    print c.jieshou_date
    return(r)
    # bh=getBh()#request.POST["contactbh"]
    # print bh
    # #user_id=request.POST["user_id"]
    # u=request.user
    # u.contact_set.create(contact_date=datetime.now(),contactbh=bh)
    # print dir(u.contact_set)
    # r=HttpResponseRedirect("/dd/")
    # return(r)
@login_required
def deletecontact(request):
    print request.GET
    contact_id=request.GET["id"]
    c=Contact.objects.get(id=contact_id)
    c.delete()
    r=HttpResponseRedirect("/dd/")
    return(r)
@login_required
def finishcontact(request):
    r=HttpResponseRedirect("/dd/")
    return(r)
@login_required
def printcontact_old(request):
    print request.GET
    contact_id=request.GET["id"]
    c=Contact.objects.get(id=contact_id)
    samples=c.sample_set.all()
    s_i=[]
    for s in samples:
        s_i.append({"sample":s,"items":s.item_set.all()})
    r=render_to_response("dd/printcontact.html",{"contact":c,"samples_items":s_i})
    return(r)
@login_required
def printcontact(request):
    print request.GET
    contact_id=request.GET["id"]
    c=Contact.objects.get(id=contact_id)
    r=render_to_response("dd/printcontact.html",{"contact":c})
    return(r)
def user_lists(request, username): 
    todo_lists = Contact.objects.all()
    return object_list(request, queryset=todo_lists) 

def server_processing(reauest):
    objs= Ajax.objects.all()
    output = {
        "sEcho" : 1,
        "iTotalRecords" : 1,
        "iTotalDisplayRecords" : 1,
        "aaData" : []
    }
    outdata=[]
    for  row in objs:
        outrow = []
        outrow.append(row.engine)# = models.CharField(max_length=30)
        outrow.append(row.browser)#=models.CharField(max_length=30,null=True)
        outrow.append(row.platform)#=models.CharField(max_length=30,null=True)
        outrow.append(row.version)#=models.FloatField()
        outrow.append(row.grade)#=models.CharField(max_length=30,null=True)
        outdata.append(outrow)
    output['aaData']= outdata
    return HttpResponse(simplejson.dumps(output, ensure_ascii=False))
def ajax(reauest):
    objs= Ajax.objects.all()
    a=objs[0].engine
    return HttpResponse(simplejson.dumps(a, ensure_ascii=False))
def post(request):
    logging.info("==========")
    logging.info(request.POST)
    objs= Ajax.objects.all()
    output = {
        "sEcho" : 1,
        "iTotalRecords" : 1,
        "iTotalDisplayRecords" : 1,
        "aaData" : []
    }
    outdata=[]
    for  row in objs:
        outrow = []
        outrow.append(row.engine)# = models.CharField(max_length=30)
        outrow.append(row.browser)#=models.CharField(max_length=30,null=True)
        outrow.append(row.platform)#=models.CharField(max_length=30,null=True)
        outrow.append(row.version)#=models.FloatField()
        outrow.append(row.grade)#=models.CharField(max_length=30,null=True)
        outdata.append(outrow)
    output['aaData']= outdata
    return HttpResponse(simplejson.dumps(output, ensure_ascii=False))
def editable_ajax(request):
    print "---"
    logging.debug(request.POST)
    print request.POST
    print request
    return HttpResponse(request.POST['value']+' (server updated)')
def gserver(request):
    c={}
    c.update(csrf(request))
    r=render_to_response("dd/gserver.html",c)
    return(r)
def gedit(request):
    c={}
    c.update(csrf(request))
    r=render_to_response("dd/gedit.html",c)
    return(r)
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            encoded_object = str(obj)
        else:
            encoded_object =json.JSONEncoder.default(self, obj)
        return encoded_object    
def infinite(request):
    print request.POST
    print request.GET
    objs= Contact.objects.all()
    res={}

    res["header"]= "50 Greatest Composers of All Times";
    records=[]
    for  o in objs:
        records.append(o.todict())
    res["records"]=records
    res["total"]=len(records)
    
    return HttpResponse(json.dumps(res,cls=DateTimeEncoder, ensure_ascii=False))