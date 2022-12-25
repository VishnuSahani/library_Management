from django.db import models

# Create your models here.
class addbookF(models.Model):
    bookname = models.CharField(max_length=150)
    authorname = models.CharField(max_length=150)
    publication = models.CharField(max_length=150)
    isbn = models.IntegerField()
    #quantity = models.CharField(max_length=150)


    language_choice= (
        ('English','English'),
        ('Hindi','Hindi'),
        ('Urdu', 'Urdu'),

    )
    language=models.CharField(max_length=111,choices=language_choice)

    Category_choice = (
        ('programming', 'programming'),
        ('Drama', 'Drama'),
        ('Poetry', 'Poetry'),
        ('Drama', 'Drama'),
        ('Comic', 'Comic'),
        ('Novel', 'Novel'),
        ('Historical', 'Historical'),
        ('Horror', 'Horror'),
        ('Science Fiction', 'Science Fiction'),
        ('Short Story', 'Short Story'),
        ('Other Book', 'Other Book'),

    )
    category = models.CharField(max_length=111, choices=Category_choice)


    class Meta:
        db_table="book_info"


class addStudent(models.Model):
    sid = models.CharField(max_length=150)
    studentname = models.CharField(max_length=150)
    #branch = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    mobile=models.IntegerField()
    branch_choice = (
        ('Computer Science & Engineering', 'Computer Science & Engineering'),
        ('Mechanical Production', 'Mechanical Production'),
        ('Mechanical Cad', 'Mechanical Cad'),
        ('Electronic','Electronic'),
        ('Civil','Civil'),
        ('Electrical Engineering','Electrical Engineering'),
    )
    branch = models.CharField(max_length=111, choices=branch_choice)

    year_choice = (
        ('First Year', 'First Year'),
        ('Second Year', 'Second Year'),
        ('Last Year','Last Year'),
    )
    year = models.CharField(max_length=111, choices=year_choice)

    gender_choice= (
        ('Male','Male'),
        ('Female','Female'),
    )
    gender=models.CharField(max_length=111,choices=gender_choice)


    class Meta:
        db_table="student_info"



class issueBook(models.Model):
    sid = models.CharField(max_length=150)
    studentname = models.CharField(max_length=150)
    branch = models.CharField(max_length=150)
    year = models.CharField(max_length=150)

    mobile=models.IntegerField()
    bookname = models.CharField(max_length=150)
    isbn = models.IntegerField()
    authorname = models.CharField(max_length=150)
    publication = models.CharField(max_length=150)
    language = models.CharField(max_length=150)
    category = models.CharField(max_length=150)
    issuedate = models.DateField(auto_now_add=False,auto_now=False, blank=True)
    returndate = models.DateField(auto_now_add=False,auto_now=False, blank=True)


    '''language_choice = (
        ('English', 'English'),
        ('Hindi', 'Hindi'),
        ('Urdu', 'Urdu'),

    )
    language = models.CharField(max_length=111, choices=language_choice)

    Category_choice = (
        ('programming', 'programming'),
        ('Drama', 'Drama'),
        ('Poetry', 'Poetry'),
        ('Drama', 'Drama'),
        ('Comic', 'Comic'),
        ('Novel', 'Novel'),
        ('Historical', 'Historical'),
        ('Horror', 'Horror'),
        ('Science Fiction', 'Science Fiction'),
        ('Short Story', 'Short Story'),

    )
    category = models.CharField(max_length=111, choices=Category_choice)'''

    class Meta:
        db_table = "bookissue_info"




class bookDetail(models.Model):
    name=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    class Meta:
        db_table="bookDetail"


class gallery(models.Model):
    title=models.CharField(max_length=100)
    g_img=models.ImageField(upload_to='gall')
    class Meta:
        db_table="gallery_img"


