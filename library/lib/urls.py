from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .import views

urlpatterns = [
     path('', views.index, name='index'),
     path('gallery1', views.gallery1, name='gallery1'),
     path('login', views.login, name='login'),
     path('logout', views.logout, name='logout'),
     path('dashboad', views.dashboad, name='dashboad'),

     path('sighup', views.sighup, name='sighup'),
     path('about', views.about, name='about'),

     path('register', views.register, name='register'),
     path('addbook', views.addbook, name='addbook'),
     path('addbookFunction', views.addbookFunction, name='addbookFunction'),
     path('showbook', views.showbook, name='showbook'),
     path('bookdelete/<int:id>', views.bookdelete, name='bookdelete'),
     path('bookedit1/<int:id>', views.bookedit1, name='bookedit1'),
     path('bookupdate/<int:id>', views.bookupdate, name='bookupdate'),
     path('addstudent', views.addstudent, name='addstudent'),
     path('addstudentfunction', views.addstudentfunction, name='addstudentfunction'),
     path('showstudent', views.showstudent, name='showstudent'),
     path('studentdelete/<int:id>', views.studentdelete, name='studentdelete'),
     path('studentedit/<int:id>', views.studentedit, name='studentedit'),
     path('studentupdate/<int:id>', views.studentupdate, name='studentupdate'),

     path('search', views.search, name='search'),
     path('searchbook', views.searchbook, name='searchbook'),
     path('issuebook1/<int:id>',views.issuebook1, name='issuebook1'),
     #path('issuebook_2', views.issuebook_2, name='issuebook_2'),

     path('showissueStData', views.showissueStData, name='showissueStData'),
     path('returnbook', views.returnbook, name='returnbook'),
     path('searchstudent', views.searchstudent, name='searchstudent'),
     path('returnbookFun/<int:isbn>', views.returnbookFun, name='returnbookFun'),
     path('issuebookfunction/<int:isbn>', views.issuebookfunction, name='issuebookfunction'),
     path('addbook_Return/<int:isbn>', views.addbook_Return, name='addbook_Return'),



]


urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)