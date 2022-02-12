from django.shortcuts import render, HttpResponse
import http.client, urllib.parse
import json

from matplotlib.pyplot import title

from jpconnect.forms import SearchForm
from .models import Employees

from jpconnect.forms import SearchForm
from django.views.generic import ListView

# Create your views here.
def home(request):
    employees = Employees.objects.all()
    return render(request, 'home.html', {'employees': employees})

def news(request):
    # conn = http.client.HTTPSConnection('api.thenewsapi.com')

    # params = urllib.parse.urlencode({
    #     'api_token': 'AYtAStyVMqv1p6H2y7OpXrQ0ITWs0KUw0ZPtzdQG',
    #     "domains" : "bbc.co.uk",
    #     "language" : "en",
    #     'limit': 5,
    #     'search' : 'Glasgow',
    #     "categories" : "general,politics"
    #     })

    # conn.request('GET', '/v1/news/all?{}'.format(params))

    # res = conn.getresponse()
    # data = res.read()
    data= '{"meta": {"found": 901, "returned": 5, "limit": 5, "page": 1}, "data": [{"uuid": "b3801a14-a8ac-429c-96c2-83fdf308a39c", "title": "Pro14: Glasgow v Ospreys (Fri)", "description": "Team news and preview for Ospreys Friday night visit to Glasgow in Pro14.", "keywords": "", "snippet": "Last updated on .From the section Rugby Union Reuben Morgan Williams scores Ospreys opening try in Octobers 23-15 Pro14 victory over Glasgow at Liberty Stadi...", "url": "https://www.bbc.co.uk/sport/rugby-union/56357903", "image_url": "https://ichef.bbci.co.uk/live-experience/cps/624/cpsprodpb/585F/production/_117532622_cdf_240121_connacht_v_ospreys_50.jpg", "language": "en", "published_at": "2021-03-11T12:19:46.000000Z", "source": "bbc.co.uk", "categories": ["sports", "general"], "relevance_score": 22.681335}, {"uuid": "377bf009-ae61-4be8-b343-8c6a609c6ea7", "title": "Pro14: Dragons v Glasgow (Sun)", "description": "Team news and preview for Dragons Pro14 match against Glasgow at the Principality Stadium.", "keywords": "", "snippet": "Last updated on .From the section Rugby Union Ross Moriarty has won 45 caps for Wales since his international debut in 2015 Pro14: Dragons v Glasgow Warriors ...", "url": "https://www.bbc.co.uk/sport/rugby-union/56456082", "image_url": "https://ichef.bbci.co.uk/live-experience/cps/624/cpsprodpb/71B9/production/_117631192_ospreys_v_dragons_18.jpg", "language": "en", "published_at": "2021-03-19T12:29:30.000000Z", "source": "bbc.co.uk", "categories": ["sports", "general"], "relevance_score": 22.489006}, {"uuid": "459f60ee-eaf9-4b0c-8569-962f4d038858", "title": "COP26: How will road closures affect Glasgow?", "description": "Travel in Glasgow will be significantly impacted by road closures, congestion and demonstrations during the summit.", "keywords": "", "snippet": "COP26: How will road closures affect Glasgow? Published 21 minutes ago Image source, Getty Images Image caption, The summit is based at the SEC campus in Glasg...", "url": "https://www.bbc.co.uk/news/uk-scotland-58809709?at_medium=RSS&at_campaign=KARANGA", "image_url": "https://ichef.bbci.co.uk/news/1024/branded_news/3821/production/_121096341_gettyimages-1346381038.jpg", "language": "en", "published_at": "2021-10-15T21:57:55.000000Z", "source": "bbc.co.uk", "categories": ["general"], "relevance_score": 22.2052}, {"uuid": "b3619e6b-e0af-490e-b7a5-c6ed468b9138", "title": "Shuggie Bain mural unveiled in Glasgow", "description": "The tribute to Douglas Stuarts Booker Prize-winning novel is unveiled at the Barrowland Ballroom.", "keywords": "", "snippet": "Stuart, who was born in Glasgow but now lives in New York, said: It is beyond my wildest dreams to see my words adorning the city that inspired them. Glasgow, ...", "url": "https://www.bbc.co.uk/news/uk-scotland-glasgow-west-56618043", "image_url": "https://ichef.bbci.co.uk/news/1024/branded_news/F76E/production/_117824336_shuggiepa.jpg", "language": "en", "published_at": "2021-04-02T15:39:03.000000Z", "source": "bbc.co.uk", "categories": ["general"], "relevance_score": 22.186462}, {"uuid": "29e14967-189b-48b5-9f38-d8bf6c1a887b", "title": "Glasgow Pride Mardi Gla march returns", "description": "Pride celebrations have returned to Glasgow following its cancellation last year due to Covid.", "keywords": "", "snippet": "Pride celebrations have returned to Glasgow following its cancellation last year due to Covid. Thousands of people turned out for the Pride Mardi Gla march fro...", "url": "https://www.bbc.co.uk/news/av/uk-scotland-58450443?at_medium=RSS&at_campaign=KARANGA", "image_url": "https://ichef.bbci.co.uk/news/1024/branded_news/1816D/production/_120396689_gettyimages-1338274260.jpg", "language": "en", "published_at": "2021-09-04T16:20:40.000000Z", "source": "bbc.co.uk", "categories": ["general"], "relevance_score": 22.186462}]}'

    # Opening JSON file
    my_dict=json.loads(data)

    context_dict = {}

    # print (my_dict['data'][x]['title'])
    # what the actual fuck is this
    title1=my_dict['data'][0]['title']
    title2=my_dict['data'][1]['title']
    title3=my_dict['data'][2]['title']
    title4=my_dict['data'][3]['title']
    title5=my_dict['data'][4]['title']

    description1=my_dict['data'][0]['description']
    description2=my_dict['data'][1]['description']
    description3=my_dict['data'][2]['description']
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
    conn = http.client.HTTPSConnection('api.weatherapi.com')
    params = urllib.parse.urlencode({
        'key': '0bdcd5c3dd934722a2c185317221102',
        "q" : "Glasgow",
        })

    conn.request('GET', '/v1/current.json?{}'.format(params))

    res = conn.getresponse()
    data = res.read()

    # Opening JSON file
    my_dict=json.loads(data)
    temp_c = my_dict['current']['temp_c']
    temp_f = my_dict['current']['temp_f']
    condition = my_dict['current']['condition']['text']
    img = my_dict['current']['condition']['icon']
    speed_kph = my_dict['current']['wind_kph']
    speed_mph = my_dict['current']['wind_mph']
    context_dict = {}
    context_dict['temp_c'] = temp_c
    context_dict['temp_f'] = temp_f
    context_dict['condition'] = condition
    context_dict['img'] = img
    context_dict['speed_kph'] = speed_kph
    context_dict['speed_mph'] = speed_mph
    return render(request, 'weather.html', context_dict)


def show_name(request, name_slug):
    context_dict = {}
    try:
        employee = Employees.objects.get(id=name_slug)
        context_dict['employee'] = employee
    except Employees.DoesNotExist:
        context_dict['employee'] = None
        return render(request, 'employee.html', context=context_dict)

    # WEATHER API
    conn = http.client.HTTPSConnection('api.weatherapi.com')
    params = urllib.parse.urlencode({
        'key': '0bdcd5c3dd934722a2c185317221102',
        "q" : employee.location.split()[0],
        })
    conn.request('GET', '/v1/current.json?{}'.format(params))
    res = conn.getresponse()
    data = res.read()
    my_dict=json.loads(data)
    context_dict['img'] = my_dict['current']['condition']['icon']
    context_dict['temp_c'] = my_dict['current']['temp_c']

    # NEWS API
    # data= '{"meta": {"found": 901, "returned": 5, "limit": 5, "page": 1}, "data": [{"uuid": "b3801a14-a8ac-429c-96c2-83fdf308a39c", "title": "Pro14: Glasgow v Ospreys (Fri)", "description": "Team news and preview for Ospreys Friday night visit to Glasgow in Pro14.", "keywords": "", "snippet": "Last updated on .From the section Rugby Union Reuben Morgan Williams scores Ospreys opening try in Octobers 23-15 Pro14 victory over Glasgow at Liberty Stadi...", "url": "https://www.bbc.co.uk/sport/rugby-union/56357903", "image_url": "https://ichef.bbci.co.uk/live-experience/cps/624/cpsprodpb/585F/production/_117532622_cdf_240121_connacht_v_ospreys_50.jpg", "language": "en", "published_at": "2021-03-11T12:19:46.000000Z", "source": "bbc.co.uk", "categories": ["sports", "general"], "relevance_score": 22.681335}, {"uuid": "377bf009-ae61-4be8-b343-8c6a609c6ea7", "title": "Pro14: Dragons v Glasgow (Sun)", "description": "Team news and preview for Dragons Pro14 match against Glasgow at the Principality Stadium.", "keywords": "", "snippet": "Last updated on .From the section Rugby Union Ross Moriarty has won 45 caps for Wales since his international debut in 2015 Pro14: Dragons v Glasgow Warriors ...", "url": "https://www.bbc.co.uk/sport/rugby-union/56456082", "image_url": "https://ichef.bbci.co.uk/live-experience/cps/624/cpsprodpb/71B9/production/_117631192_ospreys_v_dragons_18.jpg", "language": "en", "published_at": "2021-03-19T12:29:30.000000Z", "source": "bbc.co.uk", "categories": ["sports", "general"], "relevance_score": 22.489006}, {"uuid": "459f60ee-eaf9-4b0c-8569-962f4d038858", "title": "COP26: How will road closures affect Glasgow?", "description": "Travel in Glasgow will be significantly impacted by road closures, congestion and demonstrations during the summit.", "keywords": "", "snippet": "COP26: How will road closures affect Glasgow? Published 21 minutes ago Image source, Getty Images Image caption, The summit is based at the SEC campus in Glasg...", "url": "https://www.bbc.co.uk/news/uk-scotland-58809709?at_medium=RSS&at_campaign=KARANGA", "image_url": "https://ichef.bbci.co.uk/news/1024/branded_news/3821/production/_121096341_gettyimages-1346381038.jpg", "language": "en", "published_at": "2021-10-15T21:57:55.000000Z", "source": "bbc.co.uk", "categories": ["general"], "relevance_score": 22.2052}, {"uuid": "b3619e6b-e0af-490e-b7a5-c6ed468b9138", "title": "Shuggie Bain mural unveiled in Glasgow", "description": "The tribute to Douglas Stuarts Booker Prize-winning novel is unveiled at the Barrowland Ballroom.", "keywords": "", "snippet": "Stuart, who was born in Glasgow but now lives in New York, said: It is beyond my wildest dreams to see my words adorning the city that inspired them. Glasgow, ...", "url": "https://www.bbc.co.uk/news/uk-scotland-glasgow-west-56618043", "image_url": "https://ichef.bbci.co.uk/news/1024/branded_news/F76E/production/_117824336_shuggiepa.jpg", "language": "en", "published_at": "2021-04-02T15:39:03.000000Z", "source": "bbc.co.uk", "categories": ["general"], "relevance_score": 22.186462}, {"uuid": "29e14967-189b-48b5-9f38-d8bf6c1a887b", "title": "Glasgow Pride Mardi Gla march returns", "description": "Pride celebrations have returned to Glasgow following its cancellation last year due to Covid.", "keywords": "", "snippet": "Pride celebrations have returned to Glasgow following its cancellation last year due to Covid. Thousands of people turned out for the Pride Mardi Gla march fro...", "url": "https://www.bbc.co.uk/news/av/uk-scotland-58450443?at_medium=RSS&at_campaign=KARANGA", "image_url": "https://ichef.bbci.co.uk/news/1024/branded_news/1816D/production/_120396689_gettyimages-1338274260.jpg", "language": "en", "published_at": "2021-09-04T16:20:40.000000Z", "source": "bbc.co.uk", "categories": ["general"], "relevance_score": 22.186462}]}'
    conn = http.client.HTTPSConnection('api.thenewsapi.com')

    params = urllib.parse.urlencode({
        'api_token': 'AYtAStyVMqv1p6H2y7OpXrQ0ITWs0KUw0ZPtzdQG',
        "domains" : "bbc.co.uk",
        "language" : "en",
        'limit': 5,
        'search' : employee.location,
        "categories" : "general,politics"
        })

    conn.request('GET', '/v1/news/all?{}'.format(params))

    res = conn.getresponse()
    data = res.read()
    my_dict=json.loads(data)
    print(my_dict)
    articles=[]
    for i in range(5):
        articles.append({"title": my_dict['data'][i]['title'], "desc": my_dict['data'][i]['snippet'],
                    "url":my_dict['data'][i]['url'], "img":my_dict['data'][i]['image_url']})
    context_dict["articles"] = articles

    return render(request, 'employee.html', context=context_dict)
    
def Search(request):
    context_dict = {}
    if request.method == 'POST':
        query = request.POST['q'].strip()
        if query:
            object_list = Employees.objects.filter(last_name__icontains=query)
            context_dict["search_employees"] = object_list
    return render(request, 'search.html', context=context_dict)
