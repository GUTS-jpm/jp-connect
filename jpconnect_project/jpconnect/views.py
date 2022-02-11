from django.shortcuts import render
import http.client, urllib.parse

from matplotlib.pyplot import title


# Create your views here.
def home(request):
    return render(request, 'home.html')

def news(request):
    import http.client, urllib.parse
    import json
    conn = http.client.HTTPSConnection('api.thenewsapi.com')

    params = urllib.parse.urlencode({
        'api_token': 'AYtAStyVMqv1p6H2y7OpXrQ0ITWs0KUw0ZPtzdQG',
        "id" : "bbc.co.uk",
        "source" : "bbc.co.uk",
        "language" : "en",
        # 'categories': 'business,tech',
        'limit': 5,
        'search' : 'Glasgow',
        "categories" : "general,politics"
        })

    conn.request('GET', '/v1/news/all?{}'.format(params))

    res = conn.getresponse()
    data = res.read()

    # Opening JSON file
    my_dict=json.loads(data)

    context_dict = {}
    
    # print (my_dict['data'][x]['title'])
    title1=my_dict['data'][0]['title']
    title2=my_dict['data'][1]['title']
    title3=my_dict['data'][2]['title']
    title4=my_dict['data'][3]['title']
    title5=my_dict['data'][4]['title']

    description1=my_dict['data'][0]['description']
    description2=my_dict['data'][1]['description']
    description3=my_dict['data'][2]['snippet']
    description4=my_dict['data'][3]['description']
    description5=my_dict['data'][4]['description']

    url1=my_dict['data'][0]['url']
    url2=my_dict['data'][1]['url']
    url3=my_dict['data'][2]['url']
    url4=my_dict['data'][3]['url']
    url5=my_dict['data'][4]['url']

    img1=my_dict['data'][0]['image_url']
    img2=my_dict['data'][1]['image_url']
    img3=my_dict['data'][2]['image_url']
    img4=my_dict['data'][3]['image_url']
    img5=my_dict['data'][4]['image_url']
    
    context_dict["title1"] = title1
    context_dict["title2"] = title2
    context_dict["title3"] = title3
    context_dict["title4"] = title4
    context_dict["title5"] = title5

    context_dict["description1"] = description1
    context_dict["description2"] = description2
    context_dict["description3"] = description3
    context_dict["description4"] = description4
    context_dict["description5"] = description5

    context_dict["url1"] = url1
    context_dict["url2"] = url2
    context_dict["url3"] = url3
    context_dict["url4"] = url4
    context_dict["url5"] = url5

    context_dict["img1"] = img1
    context_dict["img2"] = img2
    context_dict["img3"] = img3
    context_dict["img4"] = img4
    context_dict["img5"] = img5
    return render(request, 'news.html', context_dict)

def weather(request):
    return render(request, 'weather.html')
