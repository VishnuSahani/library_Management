#from django.shortcuts import render
from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import addbookF,addStudent,issueBook,bookDetail,gallery
from .forms import addbookForms,addstudentForms,issuebookForms


# Create your views here.
def index(request):
    ob = bookDetail.objects.all()

    return render(request, 'index.html', {'ob': ob})

def gallery1(request):

    ob1 = gallery.objects.all()

    return render(request,'gallery.html', {'ob1': ob1})

   #return render(request,'admin.html')

def issuebookfunction(request,isbn):
    #print(id)
    if request.method=='POST' :
        formissu = issuebookForms(request.POST)
        #print('vis=',formissu)
        if formissu.is_valid():
            try:
                formissu.save()
                form = addbookF.objects.get(isbn=isbn)
                form.delete()
                messages.info(request, ' Book Issue Successfully ! ')

                return render(request,"searchbook.html")
            except:
                pass
        else:
            print("not save")

        #print("hi5")
        messages.info(request, 'Error! Try Again Data Are Not correct ! ')

        return render(request, "searchbook.html")

    else:
        messages.info(request, ' Action error! ')

        #form = addstudentForms()
        return render(request, 'searchbook.html')


def sighup(request):
    return render(request,'sighup.html')


def register(request):
    if request.method=='POST' :
        first_name=request.POST['firstName']
        last_name=request.POST['lastName']
        username=request.POST['userName']
        email=request.POST['email']
        password1=request.POST['password']
        password2 = request.POST['cpassword']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'User Name Already Exist Please try another userName')
                return redirect('sighup')

            elif User.objects.filter(email=email).exists():
                messages.info(request,'Eamil has already registerd with us')
                return redirect('sighup')
            else:
                user=User.objects.create_user(username=username,password=password1,first_name=first_name,last_name=last_name,email=email)
                user.save()

                messages.success(request,'Registered Successfully')

                return redirect('sighup')
        else:
            messages.info(request,'Confirm Password does not match')
          #  print("Confirm Password does not match")
            return redirect('sighup')
    else:
        return render(request, 'index.html')



def about(request):
    return render(request,'about.html')



def login(request):
    if request.method=='POST' :

        username=request.POST['userName']
        password1=request.POST['password']
        user=auth.authenticate(username=username,password=password1)
        if user is not None:
            auth.login(request,user)
            return render(request, 'admin.html',{'username':username})
        else:
           messages.info(request,'Either user name or password is incoreect! ')
           return render(request,'index.html')
    else:
        messages.info(request, 'Does Not Get user name or password ! ')

        return render(request, 'index.html')



def addbook(request):
    form=addbookForms()
    return render(request, 'addbook.html', {'form': form})

def addbookFunction(request):
    if request.method=='POST' :
        form = addbookForms(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.info(request, 'Book Add Successfully ! ')

                return redirect("addbook")
            except:
                messages.info(request, 'Book Does not Add Please Try Again ! ')
                return redirect("addbook")



        else:
            messages.info(request, 'Book Does not Add Please Try Again ! ')
            return redirect("addbook")

            #print("not save")

        #print("hi5")

        #return render(request, "admin.html")

    else:
        messages.info(request, 'Book Does not Add Please Try Again ! ')

        form = addbookForms()
        return render(request, 'addbook.html', {'form': form})

def showbook(request):
    form = addbookF.objects.all()
    return render(request, 'showbook.html', {'form': form})

def bookdelete(request,id):
    form = addbookF.objects.get(id=id)
    form.delete()
    messages.info(request, 'Book Delete Successfully ! ')

    return redirect("/showbook")

def bookedit1(request,id):
    data = addbookF.objects.get(id=id)
    return render(request,'bookedit.html', {'data': data})


def bookupdate(request,id):
    student = addbookF.objects.get(id=id)
    form = addbookForms(request.POST, instance=student)

    if form.is_valid():
        form.save()
        messages.info(request, 'Your Book Update Successfully! ')

        return redirect("/showbook")
    else:
        print(form.errors)

    return render(request, "bookedit.html", {'data': student})

def addstudent(request):
    form=addstudentForms()
    return render(request, 'addstudent.html', {'form': form})


def addstudentfunction(request):
    if request.method=='POST' :
        form2 = addstudentForms(request.POST)
        if form2.is_valid():
            try:
                form2.save()
                messages.info(request, 'Student Registration successfully ! ')

                return redirect("addstudent")
            except:
                pass

        else:
            messages.info(request, 'Please Try Again Because Information Does Not Valid ! ')
            return redirect("addstudent")

            #print("not save")

        #print("hi5")

        return render(request, "admin.html")

    else:
        messages.info(request, 'Please Try Again ! ')

        form = addstudentForms()
        return render(request, 'addstudent.html', {'form': form})

def showstudent(request):
    form = addStudent.objects.all()
    return render(request, 'showstudent.html', {'form': form})

def studentdelete(request,id):
    form = addStudent.objects.get(id=id)
    form.delete()
    messages.info(request, 'Student Data Delete Successfully ! ')

    return redirect("/showstudent")

def studentedit(request,id):
    data = addStudent.objects.get(id=id)
    return render(request,'studentedit.html', {'data': data})


def studentupdate(request,id):
    student = addStudent.objects.get(id=id)
    form = addstudentForms(request.POST, instance=student)

    if form.is_valid():
        form.save()
        messages.info(request, 'Student Data Update Successfully ! ')

        return redirect("/showstudent")
    else:
        print(form.errors)

    return render(request, "studentedit.html", {'data': student})

def search(request):
    return render(request,"searchbook.html")



def searchbook(request):
    if request.method=='POST' :
        book_name= request.POST.get('search')
        print(book_name)
        try:
            #for status in addbookF.objects.filter(bookname=book_name): #jab ek data lala ho
             #   print()

            status = addbookF.objects.filter(bookname=book_name)

            #print('vvv=',status)
            #print("search ho gaya")
        except addbookF.DoesNotExist:
            #print("search nhiiiiiiiiii")

            status = None
        #data2 = issuebookForms()
        #print("vis test-",status)

        messages.info(request, 'Book Search successfully ! ')

        return render(request, "searchbook.html",{"books":status})
    else:
        #print("search nhi ho gaya")

        return render(request, "admin.html")



## Logout
def logout(request):
    auth.logout(request)
    return redirect("/")

def dashboad(request):
   return render(request,'admin.html')

def issuebook1(request,id):
    data = addbookF.objects.get(id=id)
    #data2 = issuebookForms()

    return render(request, 'issuebook.html', {'book': data})



def showissueStData(request):
    form = issueBook.objects.all()
    return render(request, 'showissueData.html', {'form': form})

##################################################


def returnbook(request):
    return render(request, "returnbook.html")


def searchstudent(request):
    if request.method == 'POST':
        studentid = request.POST.get('searchid')
        try:

            status = issueBook.objects.filter(sid=studentid)

            print('vvv=',status)
            # print("search ho gaya")

        except issueBook.DoesNotExist:
            # print("search nhiiiiiiiiii")

            status = None
        messages.info(request, 'Search Successfully ! ')

        return render(request, "returnbook.html", {"books": status})
    else:
        # print("search nhi ho gaya")

        return render(request, "admin.html")


'''def returnbookFun(request,isbn):

    form2 = addbookForms(request.POST)
    #form2 = addbookForms(request.POST)

    #form2 = addbookForms(request.POST)
    dell2 = issueBook.objects.get(isbn=isbn)
    print(form2)
    #print(dell2)
    if form2.is_valid():
        form2.save()

        dell2.delete()
        #return redirect("/searchbook")

        return render(request, 'returnbook.html')


    else:
        print("nhi hua")
        print(form2.errors)
        return render(request, 'admin.html')
'''

def returnbookFun(request,isbn):
    data = issueBook.objects.get(isbn=isbn)
    # data2 = issuebookForms()

    return render(request, 'returnbook.html', {'book': data})



def addbook_Return(request,isbn):
    if request.method=='POST' :
        form = addbookForms(request.POST)
        if form.is_valid():
            try:
                form.save()
                form = issueBook.objects.get(isbn=isbn)
                form.delete()
                messages.info(request, 'Book Return Successfully ! ')

                return redirect("returnbook")
            except:
                pass



        else:
            messages.info(request, 'Book Does not Return Please Try Again ! ')
            return redirect("returnbook")

            #print("not save")

        #print("hi5")

        #return render(request, "admin.html")

    else:
        messages.info(request, 'Book Does not Return Please Try Again ! ')
        return redirect("returnbook")


