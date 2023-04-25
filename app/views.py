from django.shortcuts import render,redirect
from .models import candidates
import mysql.connector as msc
from datetime import date
# Create your views here.
def icp(request):
    # conn=msc.connect(host="localhost",user="root",password="aditya",database="icp")
    # c=conn.cursor()
    # c.execute("create table if not exists candidates(cid int primary key,cname varchar(20))")
    # conn.commit()
    # c.execute("create table if not exists interview(iid int primary key,i_name varchar(20),st varchar(20),et varchar(20),cand varchar(20))")
    # conn.commit()
    # c.execute("select cname from candidates")
    # d=c.fetchall()
    d1 = list(candidates.objects.all())
    print(d1)
    return render(request,"home.html",{"can":d1})
def add(request):
    conn=msc.connect(host="localhost",user="root",password="aditya",database="icp")
    c=conn.cursor()
    name=request.GET.get("name")
    st=request.GET.get("st")
    et=request.GET.get("et")
    d=request.GET.dict()
    del d['name']
    del d['st']
    del d['et']
    l=[]
    for i in d.keys():
        l.append(i)
    c.execute("select cname from candidates")
    e=c.fetchall()
    c.execute("select i_name,st,et,cand from interview")
    g=c.fetchall()
    p=0
    for i in g:
        if name.upper()==i[0].upper():
            p=1
    if p==1:
        return render(request,"home.html",{"can":e,"e1":"Meeting Name Cannot be Same as Previous"})
    if(len(l)<=2):
        return render(request,"home.html",{"can":e,"e1":"Select More than 2 Candidates"})
    if(st>=et):
        return render(request,"home.html",{"can":e,"e1":"Select Proper Time Interval"})
    k1=[]
    for i in e:
        k1.append(i[0])
    f=0
    if g!=[]:
        for i in g:
            l1=i[3].split(",")
            for j in l1:
                if j in k1:
                    if (st<i[1] and et>i[1]) or (st<i[2] and et>i[2]):
                        f=1
    if f==0 or g==[]:
        a=",".join(l)
        id=AID("interview")
        c.execute("insert into interview value('{}','{}','{}','{}','{}')".format(id,name,st,et,a))
        conn.commit()
        conn.close()
        return render(request,"home.html",{"can":e,"e1":"Meeting Created!"})
    elif f==1 and g!=[]:
        return render(request,"home.html",{"can":e,"e1":"Selected Candidate(s) is/are not Available during the Scheduled Time"})
def view(request):
    conn=msc.connect(host="localhost",user="root",password="aditya",database="icp")
    c=conn.cursor()
    c.execute("select * from interview")
    d=c.fetchall()
    l=[]
    for i in d:
        l.append(i)
    return render(request,"view.html",{"details":l})
def ed(request):
    conn=msc.connect(host="localhost",user="root",password="aditya",database="icp")
    c=conn.cursor()
    c.execute("select * from interview")
    d=c.fetchall()
    l=[]
    for i in d:
        l.append(i)
    return render(request,"edit.html",{"details":l})
def delete(request):
    conn=msc.connect(host="localhost",user="root",password="aditya",database="icp")
    c=conn.cursor()
    pid=request.GET.get("pid")
    c.execute("delete from interview where iid='{}'".format(pid))
    conn.commit()
    c.execute("select * from interview")
    d=c.fetchall()
    l=[]
    for i in d:
        l.append(i)
    return render(request,"edit.html",{"details":l})
    conn.commit()
    conn.close()
def edit(request):
    conn=msc.connect(host="localhost",user="root",password="aditya",database="icp")
    c=conn.cursor()
    pid=request.GET.get("pid")
    c.execute("select * from interview where iid='{}'".format(pid))
    f=c.fetchall()[0]
    c.execute("select cname from candidates")
    d=c.fetchall()
    conn.commit()
    a=list(f[4].split(","))
    print(a)
    l=[]
    for i in d:
        l.append(i[0])
    return render(request,"edit.html",{"info":f,"can":l,"req":a})
def editc(request):
    conn=msc.connect(host="localhost",user="root",password="aditya",database="icp")
    c=conn.cursor()
    id=request.GET.get("id")
    name=request.GET.get("name")
    st=request.GET.get("st")
    et=request.GET.get("et")
    d=request.GET.dict()
    del d['id']
    del d['name']
    del d['st']
    del d['et']
    l=[]
    for i in d.keys():
        l.append(i)
    c.execute("select cname from candidates")
    e=c.fetchall()
    can=[]
    for i in e:
        can.append(i[0])
    c.execute("select i_name,st,et,cand from interview where iid!={}".format(id))
    g=c.fetchall()
    c.execute("select * from interview where iid={}".format(id))
    o=c.fetchall()[0]
    a=list(o[4].split(","))
    p=0
    for i in g:
        if name.upper()==i[0].upper():
            p=1
    if(len(l)<=2):
        return render(request,"edit.html",{"info":o,"e1":"Select More than 2 Candidates","can":can,"req":a})
    if p==1:
        return render(request,"edit.html",{"info":o,"e1":"Meeting Name Cannot be Same as Previous","can":can,"req":a})
    if(st>=et):
        return render(request,"edit.html",{"info":o,"e1":"Select Proper Time Interval","can":can,"req":a})
    k1=[]
    for i in e:
        k1.append(i[0])
    f=0
    if g!=[]:
        for i in g:
            l1=i[3].split(",")
            for j in l1:
                if j in k1:
                    if (st<i[1] and et>i[1]) or (st<i[2] and et>i[2]):
                        f=1
    if f==0 or g==[]:
        z=",".join(l)
        c.execute("delete from interview where iid={}".format(id))
        conn.commit()
        c.execute("insert into interview value('{}','{}','{}','{}','{}')".format(id,name,st,et,z))
        conn.commit()
        conn.close()
        return redirect("/ed")
    elif f==1 and g!=[]:
        return render(request,"edit.html",{"info":o,"e1":"Selected Candidate(s) is/are not Available during the Scheduled Time","can":can,"req":a})
def AID(table):
    conn=msc.connect(host="localhost",user="root",password="aditya",database="icp")
    c=conn.cursor()
    c.execute("select * from {}".format(table))
    a=c.fetchall()
    conn.commit()
    if a==[]:
        return 1
    else:
        return a[len(a)-1][0]+1