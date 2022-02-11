from django.shortcuts import render
import http.client, urllib.parse


# Create your views here.
def home(request):
    return render(request, 'home.html')

def news(request):
    conn = http.client.HTTPSConnection('api.thenewsapi.com')

    params = urllib.parse.urlencode({
        'api_token': 'AYtAStyVMqv1p6H2y7OpXrQ0ITWs0KUw0ZPtzdQG',
        # 'categories': 'business,tech',
        'limit': 5,
        'search' : 'london',
        })

    conn.request('GET', '/v1/news/all?{}'.format(params))

    res = conn.getresponse()
    data = res.read()

    print(data.decode('utf-8'))
    return render(request, 'news.html')

def weather(request):
    return render(request, 'weather.html')
