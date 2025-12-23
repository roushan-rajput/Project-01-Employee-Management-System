from django.shortcuts import render
from .models import employee
# from django.shortcuts import get_object_or_404

# Create your views here.
def landing(req):
    return render(req,'landing.html')

def login(req):
    return render(req,'login.html')

def add_emp(req):
    return render(req,'add_emp.html')

def login_data(req):
    if req.method=='POST':
        e=req.POST.get('email')
        p=req.POST.get('pass')
        print(e,p)

        if e=='roushanrajput12362@gmail.com' and p=='12362':
            return render(req,'admindashboard.html')
        else:
         return render(req,'empdashboard.html')

def emp_data(req):
    if (req.method=='POST'):
        e=req.POST.get('empid')
        n=req.POST.get('empname')
        em=req.POST.get('empemail')
        p=req.POST.get('empposition')
        c=req.POST.get('empcontact')
        s=req.POST.get('empsalary')
        print(e,n,em,p,c,s)
        user=employee.objects.filter(email=em)
        userid=employee.objects.filter(empid=e)
        if user or userid:
            msg='E-mail Already Exists!'
            return render(req,'add_emp.html',{'msg':msg})
        else:
            employee.objects.create(empid=e,name=n,email=em,contact=c,position=p,salary=s)
            return render(req,'admindashboard.html')
    else:
        return render(req,'add_emp.html')
    
def show_emp(req):
    emp=employee.objects.all()
    data=[]
    for i in emp:
        data.append({
            'empid':i.empid,
            'name':i.name,
            'email':i.email,
            'contact':i.contact,
            'position':i.position,
            'salary':i.salary,
        })
    return render(req,'showemp.html', {'emp': emp})

# def emp(req):
#     employee=employee.objects.all().order_by('-id')
#     return render(req, 'showemp.html',{'emp':emp})

def edit_employee(req,pk):
    print(pk)
    userdata = employee.objects.get(id=pk)
    
    data={
        'id':userdata.empid,
        'name':userdata.name,
        'email':userdata.email,
        'contact':userdata.contact,
        'position':userdata.position,
        'salary':userdata.salary,
    }
    return render(req,'add_emp.html',{'data':data})

def update_data(req,pk):
    if (req.method=='POST'):
        e=req.POST.get('empid')
        n=req.POST.get('empname')
        em=req.POST.get('empemail')
        p=req.POST.get('empposition')
        c=req.POST.get('empcontact')
        s=req.POST.get('empsalary')
        data = employee.objects.get(empid=pk)

        data.empid=e
        data.name=n
        data.email=em
        data.contact=c
        data.position=p
        data.salary=s
        data.save()
        return render(req,'admindashboard.html')

def del_employee(req,pk):
        userdata=employee.objects.get(id=pk)
        userdata.delete()
        return render(req,'showemp.html')

def admin_logout(req):
    if req.session.get('admin'):
        req.session.flush()
    return render(req,'login.html')