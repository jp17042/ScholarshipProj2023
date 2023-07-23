from django.shortcuts import render, redirect
from .forms import SurveyForm
from django.http import JsonResponse
from signup.views import signup, User
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt

import sqlite3

# View function to handle searching surveys for a specific user
def search_view(request, user_id):
    keyword = request.GET.get('keyword', '')
    
    # Connect to the SQLite database
    conn = sqlite3.connect('database.sqlite3')
    cursor = conn.cursor()
     
    # Insert data into the user's data table
    cursor.execute('INSERT INTO user_{}_data (Survey_Name, Survey_Type, Survey_Question) VALUES (?, ?, ?)'.format(user_id), (q_N, q_T, q_q))
    conn.commit()

    # Execute the query to search for surveys by name
    cursor.execute("SELECT Survey_Name FROM user_{}_data WHERE Survey_Name LIKE ?".format(user_id), ('%' + keyword + '%',))

    # Fetch all the rows containing the search results
    rows = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Prepare the results as a list of dictionaries
    results = []
    for row in rows:
        result = {'title': row[0]}  # Adjust the column index based on your database structure
        results.append(result)

    # Return the search results as a JSON response
    return JsonResponse(results, safe=False)

# View function to display surveys for the current user
def surveys(request):
    global user_id
    user_id = request.user.id

    # Connect to the SQLite database
    conn = sqlite3.connect('/Users/jacobptak/Documents/GitHub/ScholarshipProj2023/database.sqlite3')
    cursor = conn.cursor()

    # Retrieve data for surveys with Question_Number '1_question'
    cursor.execute("SELECT * FROM user_{}_data WHERE Question_Number LIKE '1_question'".format(user_id))
    rows = cursor.fetchall()

    # Close the database connection
    conn.close()

    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            # Process the submitted form data
            survey_name = form.cleaned_data['S_name']
            question_data = get_question_data(request.POST)
            save_question_data(user_id, question_data, survey_name)
            return redirect('/survey')
        
    else:
        form = SurveyForm()

    # Check if a search query was provided in the URL and display the search results
    keyword = request.GET.get('keyword')
    if keyword:
        return search_view(request)

    # Render the survey.html template with the survey data
    return render(request, 'survey/survey.html', {'rows': rows})

# A decorator to exempt this view from CSRF protection
@csrf_exempt
def get_question_data(post_data):
    question_data = []
    
    # Extract the question data from the POST data
    for key, value in post_data.items():
        if key.startswith('Q_options') and value:
            question_number = key.split('Q_options')[1]
            question_type = value
            question = post_data.get('S_question{}'.format(question_number), '_question')
            question_data.append({'question_number': question_number, 'question_type': question_type, 'question': question})
    
    return question_data

# Function to save the question data for a survey in the user's data table
def save_question_data(user_id, question_data, survey_name):
    conn = sqlite3.connect('/Users/jacobptak/Documents/GitHub/ScholarshipProj2023/database.sqlite3')  # Replace with the actual path to your SQLite database
    cursor = conn.cursor()
    
    # Insert the question data into the user's data table
    for question in question_data:
        question_number = question['question_number']
        question_type = question['question_type']
        question_text = question['question']
        
        cursor.execute('INSERT INTO user_{}_data (Survey_Name, Question_Number, Question_Type, Question_Text) VALUES (?, ?, ?, ?)'.format(user_id), (survey_name, question_number, question_type, question_text))
    
    conn.commit()
    conn.close()
