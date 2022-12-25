from django import forms
from lib.models import addbookF,addStudent,issueBook,bookDetail,gallery
class addbookForms(forms.ModelForm):
    class Meta:
        model=addbookF
        fields="__all__"


class addstudentForms(forms.ModelForm):
    class Meta:
        model=addStudent
        fields="__all__"



class issuebookForms(forms.ModelForm):
    class Meta:
        model=issueBook
        #issuedate: forms.dateField(attrs={ 'id': 'from' })
        fields="__all__"

class bookDetailForm(forms.ModelForm):
    class Meta:
        model=bookDetail
        fields="__all__"

class galleryForm(forms.ModelForm):
    class Meta:
        model=gallery
        fields="__all__"

