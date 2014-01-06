# -*- coding: utf-8 -*-
import os
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
#from mysite.ncsdd.models import *
#from django.contrib.auth.models import Group,User
import requests
import json
#from mysite.ncsdd.models import Contact
def highest():
    url = "http://127.0.0.1:8000/api/v1/"
    doc = requests.get(url)
    print doc.content
def  xml():
    url = "http://127.0.0.1:8000/api/v1/"
    params = {'format':'xml'}
    print requests.get(url,params=params).content
def  schema():
    url = "http://localhost:8000/api/v1/contact/schema/"
    params = {'format':'json'}
    print requests.get(url,params=params).content
def getall():
    url = "http://localhost:8000/api/v1/contact/"
    params = {'format':'json','limit':0}
    c= requests.get(url,params=params).content
    print c
    l=json.loads(c)
    all=l["objects"]
    for one in all:
        print one
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            encoded_object = str(obj)
        else:
            encoded_object =json.JSONEncoder.default(self, obj)
        return encoded_object
def myjson(self):
    m=self._meta
    fs=m.fields#get_all_field_names()
    dic={}
    for f in fs:
        dic[f.attname]=self.__getattribute__(f.attname)
    return json.dumps(dic,cls=DateTimeEncoder, ensure_ascii=False)
def newContact():
    #u=User.objects.get(username="mahongquan")
    #print myjson(u)
    #print json.dumps(u, ensure_ascii=False)
    # url = "http://localhost:8000/api/v1/contact/"
    # postdata = {"collection": "/api/v1/contact/1/",'wrt': 'w1', 'yiqi': '750'} #urllib.urlencode([('q','python')])# urllib.urlencode({'value': 'v', 'result': 'r'})
    # headers = {'content-type': 'application/json'}
    # r=requests.post(url,data=json.dumps(postdata), headers=headers)
    # open("res.html","w").write(r.text)
    pass
def deleteContact():
    url = "http://localhost:8000/api/v1/contact/1/"
    headers = {'content-type': 'application/json'}
    params = {'format':'json'}
    print requests.delete(url,data=json.dumps(params), headers=headers).text 
def getContactbywtr():
    url = "http://localhost:8000/api/v1/contact/"
    params = {'format':'json',"apikey":"tetetgegegwt","wtr":"xs"}
    c=requests.get(url,params=params).content
    l=json.loads(c)
    all=l["objects"]
    print all
def getAllUser():
    url = "http://localhost:8000/api/v1/user/"
    params = {'format':'json',"apikey":"tetetgegegwt"}
    c=requests.get(url,params=params).content
    print c
    l=json.loads(c)
    all=l["objects"]
    print len(all) 
def newTodo():
    url = "http://localhost:8000/api/v1/todo/"
    postdata = {"collection": "/api/v1/todo/1/",'text': 'w1'} #urllib.urlencode([('q','python')])# urllib.urlencode({'value': 'v', 'result': 'r'})
    headers = {'content-type': 'application/json'}
    r=requests.post(url,data=json.dumps(postdata), headers=headers)
    open("res.html","w").write(r.text)
    pass
def deleteTodo():
    url = "http://localhost:8000/api/v1/todo/1/"
    headers = {'content-type': 'application/json'}
    params = {'format':'json'}
    print requests.delete(url,data=json.dumps(params), headers=headers).text 
def getAllTodo():
    url = "http://localhost:8000/api/v1/todo/"
    params = {'format':'json',"apikey":"tetetgegegwt","wtr":"xs"}
    c=requests.get(url,params=params).content
    print c
    l=json.loads(c)
    all=l["objects"]
    print all

if __name__=="__main__":
    # highest()
    # xml()
    # schema()
    #getAllUser()
    #getAllTodo()
    #newTodo()
    deleteTodo()