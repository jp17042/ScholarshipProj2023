from django.shortcuts import render

# Create your views here.
def csv(request):
  return render(request, 'csv/csv.html')
 
