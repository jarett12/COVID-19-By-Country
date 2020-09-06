from django.shortcuts import render
import  requests


# Create your views here.
# process data
data = True
globalStats = None
countries = None
r = requests.get('https://api.covid19api.com/summary').json()
while(data):
    try:
        globalStats = r['Global']
        countries = r['Countries']

        data = False
    except:
        data = True

context = {
    'globalStats' : globalStats ,
    'countries' : countries
}

def home(request):
    return render(request , 'covid19/index.html' ,context)
