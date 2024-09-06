from django.shortcuts import render, redirect
from .models import Language, Level, Quiz, StudentProfile,UserMst
from . forms import languageform,levelform,quizform,studentform,userform
import pymysql


def indexview(request):
    return render(request,"index.html")

def home(request):
    return render(request, 'home.html')


def language_selection(request):    
    form=languageform(request.POST)
    languages = Language.objects.all()
    return render(request, 'language_selection.html', {'languages': languages})

def start_level(request, language_id):
    form=levelform(request.POST)
    language = Language.objects.get(id=language_id)
    levels = Level.objects.filter(language=language)
    return render(request, 'levels.html', {'levels': levels})

def quiz_view(request, level_id):
    form=quizform(request.POST)
    level = Level.objects.get(id=level_id)
    quizzes = Quiz.objects.filter(level=level)
    # Add quiz handling logic here
    return render(request, 'quiz.html', {'quizzes': quizzes})

def student_login(request):
    return render(request, "student_login.html")

def student_login1(request):
    if(request.method=="POST"):
        Username=request.POST['Username']
        Password=request.POST['Password']
        flag=0
        db=pymysql.connect(host="localhost",user="root",password="",database="codequest",port=3306)
        cursor=db.cursor()
        cursor.execute("select username, password from design_usermst")
        records = cursor.fetchall()
        for row in records:
            if(row[0]==Username and row[1]==Password):
                return redirect('user')
                flag=1
    
        if(flag==0):
            return redirect('index.html')
        


def Logintrans(request):
    return render(request, "userform.html")

def Logintrans1(request):
    if request.method == "POST":
        Name = request.POST['Name']
        Email = request.POST['Email']
        ContactNo = request.POST['ContactNo']
        Username = request.POST['Username']
        Password = request.POST['Password']
        
        db = pymysql.connect(host="localhost", user="root", password="", database="codequest", port=3306)
        cursor = db.cursor()
        cursor.execute("INSERT INTO design_UserMst (name, email, contactno, username, password) VALUES (%s, %s, %s, %s, %s)",
                       (Name, Email, ContactNo, Username, Password))
        db.commit()
        db.close()
        return redirect('user') 
    

    
def user(request):
    return render(request, "index1.html")

def topic(request):
    return render(request, "topic.html")

def strings(request):
    return render(request, "strings.html")

def strings2(request):
    return render(request, "strings2.html")

def strings3(request):
    return render(request, "strings3.html")

def strings4(request):
    return render(request, "strings4.html")

def strings5(request):
    return render(request, "strings5.html")

def strings6(request):
    return render(request, "strings6.html")

def quiz1(request):
    return render(request, "quiz1.html")

def quiz1(request):
    return render(request, "quiz1.html")

def quiz2(request):
    return render(request, "quiz2.html")

def quiz3(request):
    return render(request, "quiz3.html")

def quiz4(request):
    return render(request, "quiz4.html")

def quiz5(request):
    return render(request, "quiz5.html")