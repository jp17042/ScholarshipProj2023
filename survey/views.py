from django.shortcuts import render, redirect
from .forms import SurveyForm
from signup.views import signup, User
from django.contrib import auth

import sqlite3
# Create your views here.
def surveys(request):
    user_id = request.user.id
    global q_N
    global q_T
    global q_q
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():

            q_N = form.cleaned_data['S_name']
            q_T = form.cleaned_data['Q_options']
            q_q = form.cleaned_data['S_question']
       
            add_data_user(user_id)
            return redirect('/survey')
        
            
        else: form = SurveyForm()
    return render(request, 'survey/survey.html' )
def add_data_user(user_id):
    conn = sqlite3.connect('/Users/jacobptak/Documents/GitHub/ScholarshipProj2023/database.sqlite3')
    cursor = conn.cursor()
     
    cursor.execute('INSERT INTO user_{}_data (Survey_Name, Survey_Type, Survey_Question) VALUES (?, ?, ?)'.format(user_id), (q_N, q_T, q_q))
    conn.commit()
    conn.close()


