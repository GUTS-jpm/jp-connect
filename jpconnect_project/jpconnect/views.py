from django.shortcuts import render, HttpResponse
import http.client, urllib.parse
import json

from matplotlib.pyplot import title
from .models import Employees


# Create your views here.
def home(request):
    employees = Employees.objects.all()
    return render(request, 'home.html', {'employees': employees})

def news(request):
    # conn = http.client.HTTPSConnection('api.thenewsapi.com')

    # params = urllib.parse.urlencode({
    #     'api_token': 'AYtAStyVMqv1p6H2y7OpXrQ0ITWs0KUw0ZPtzdQG',
    #     "id" : "bbc.co.uk",
    #     "source" : "bbc.co.uk",
    #     "language" : "en",
    #     'limit': 5,
    #     'search' : 'Glasgow',
    #     "categories" : "general,politics"
    #     })

    # conn.request('GET', '/v1/news/all?{}'.format(params))

    # res = conn.getresponse()
    # data = res.read()
    data='{"meta": {"found": 35989, "returned": 5, "limit": 5, "page": 1}, "data": [{"uuid": "bb3e6be4-6395-45e3-9924-4b3bd086e2c6", "title": "THE GLASGOW CLIMATE CONFERENCE", "description": "The Glasgow Climate Change Conference is about to begin as 30,000 spongers descend on the city. My Glasgow office tells me Glaswegians are not well pleased at t...", "keywords": "", "snippet": "The Glasgow Climate Change Conference is about to begin as 30,000 spongers descend on the city. My Glasgow office tells me Glaswegians are not well pleased at t...", "url": "https://nopunchespulled.com/2021/10/21/the-glasgow-climate-conference/", "image_url": "https://s0.wp.com/i/blank.jpg", "language": "en", "published_at": "2021-10-20T20:10:26.000000Z", "source": "nopunchespulled.com", "categories": ["politics", "general"], "relevance_score": 23.406437}, {"uuid": "8011dd0b-433a-4320-b6b4-033a9a385e68", "title": "New Glasgow apartment evacuated during fire", "description": "An apartment was evacuated as crews tackled a fire in downtown New Glasgow at the corner of MacLean and Provost streets Sunday morning.", "keywords": "", "snippet": "An apartment was evacuated as crews tackled a fire in downtown New Glasgow on Sunday morning.Around 7 a.m., fire departments from New Glasgow, Stellarton, Tre...", "url": "https://www.cbc.ca/news/canada/nova-scotia/new-glasgow-business-apartment-building-evacuated-during-fire-1.5983231?cmp=rss", "image_url": "https://i.cbc.ca/1.5983233.1618148396!/fileImage/httpImage/image.jpg_gen/derivatives/16x9_620/new-glasgow-fire.jpg", "language": "en", "published_at": "2021-04-11T14:49:59.000000Z", "source": "cbc.ca", "categories": ["general"], "relevance_score": 23.186863}, {"uuid": "35bf9a4d-4947-41fc-a387-886e40dca0ae", "title": "Glasgow and Guyana", "description": "Dear Editor, A week after the conclusion of the Glasgow summit where an agreement was reached on carbon emission reduction, will nations honour the agreement? G...", "keywords": "", "snippet": "Glasgow and Guyana Dear Editor, week after the conclusion of the Glasgow summit where an agreement was reached on carbon emission reduction, will nations ho...", "url": "https://www.kaieteurnewsonline.com/2021/11/22/glasgow-and-guyana/", "image_url": "https://www.kaieteurnewsonline.com/images/2017/12/letters-2-150x150.jpg", "language": "en", "published_at": "2021-11-22T04:02:05.000000Z", "source": "kaieteurnewsonline.com", "categories": ["general"], "relevance_score": 22.834278}, {"uuid": "0e1fc424-f0e9-4eea-a8f4-c6dfb9cc0906", "title": "Rhodes goes to Glasgow", "description": "", "keywords": "", "snippet": "This week, Ben calls in from the COP26 climate summit in Glasgow where he’s traveling with President Obama. In this episode Ben and Tommy cover the latest new...", "url": "https://crooked.com/podcast/rhodes-goes-to-glasgow/", "image_url": "https://res.cloudinary.com/crooked-media/image/upload/f_auto,q_auto/v1636501677/crooked/pstw-episode-generic-hero-twitter-487780-7SDc8RBy.jpg", "language": "en", "published_at": "2021-11-10T05:01:55.000000Z", "source": "crooked.com", "categories": ["politics", "general"], "relevance_score": 22.784126}, {"uuid": "b1610588-2f7b-4bc3-b80d-e028db24db50", "title": "glasgow: Five things you need to know about the Glasgow Climate Pact", "description": "UK News: LONDON: The COP26 UN climate talks in Glasgow have finished and the gavel has come down on the Glasgow Climate Pact agreed by all 197 countries.", "keywords": "paris agreement, ndc, glasgow loss and damage facility, Glasgow Climate Pact, glasgow climate, glasgow", "snippet": "LONDON: The COP26 UN climate talks in Glasgow have finished and the gavel has come down on the Glasgow Climate Pact agreed by all 197 countries.If the 2015 Pari...", "url": "https://timesofindia.indiatimes.com/world/uk/five-things-you-need-to-know-about-the-glasgow-climate-pact/articleshow/87678435.cms", "image_url": "https://static.toiimg.com/thumb/msid-87694125,width-1070,height-580,imgsize-166868,resizemode-75,overlay-toi_sw,pt-32,y_pad-40/photo.jpg", "language": "en", "published_at": "2021-11-14T07:33:06.000000Z", "source": "timesofindia.indiatimes.com", "categories": ["general"], "relevance_score": 22.72462}]}'


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

    description1=my_dict['data'][0]['snippet']
    description2=my_dict['data'][1]['snippet']
    description3=my_dict['data'][2]['snippet']
    description4=my_dict['data'][3]['snippet']
    description5=my_dict['data'][4]['snippet']

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
    print(employee.location.split()[0])
    conn.request('GET', '/v1/current.json?{}'.format(params))
    res = conn.getresponse()
    data = res.read()
    my_dict=json.loads(data)
    context_dict['img'] = my_dict['current']['condition']['icon']
    context_dict['temp_c'] = my_dict['current']['temp_c'] 
    
    # NEWS API
    data='{"meta": {"found": 35989, "returned": 5, "limit": 5, "page": 1}, "data": [{"uuid": "bb3e6be4-6395-45e3-9924-4b3bd086e2c6", "title": "THE GLASGOW CLIMATE CONFERENCE", "description": "The Glasgow Climate Change Conference is about to begin as 30,000 spongers descend on the city. My Glasgow office tells me Glaswegians are not well pleased at t...", "keywords": "", "snippet": "The Glasgow Climate Change Conference is about to begin as 30,000 spongers descend on the city. My Glasgow office tells me Glaswegians are not well pleased at t...", "url": "https://nopunchespulled.com/2021/10/21/the-glasgow-climate-conference/", "image_url": "https://s0.wp.com/i/blank.jpg", "language": "en", "published_at": "2021-10-20T20:10:26.000000Z", "source": "nopunchespulled.com", "categories": ["politics", "general"], "relevance_score": 23.406437}, {"uuid": "8011dd0b-433a-4320-b6b4-033a9a385e68", "title": "New Glasgow apartment evacuated during fire", "description": "An apartment was evacuated as crews tackled a fire in downtown New Glasgow at the corner of MacLean and Provost streets Sunday morning.", "keywords": "", "snippet": "An apartment was evacuated as crews tackled a fire in downtown New Glasgow on Sunday morning.Around 7 a.m., fire departments from New Glasgow, Stellarton, Tre...", "url": "https://www.cbc.ca/news/canada/nova-scotia/new-glasgow-business-apartment-building-evacuated-during-fire-1.5983231?cmp=rss", "image_url": "https://i.cbc.ca/1.5983233.1618148396!/fileImage/httpImage/image.jpg_gen/derivatives/16x9_620/new-glasgow-fire.jpg", "language": "en", "published_at": "2021-04-11T14:49:59.000000Z", "source": "cbc.ca", "categories": ["general"], "relevance_score": 23.186863}, {"uuid": "35bf9a4d-4947-41fc-a387-886e40dca0ae", "title": "Glasgow and Guyana", "description": "Dear Editor, A week after the conclusion of the Glasgow summit where an agreement was reached on carbon emission reduction, will nations honour the agreement? G...", "keywords": "", "snippet": "Glasgow and Guyana Dear Editor, week after the conclusion of the Glasgow summit where an agreement was reached on carbon emission reduction, will nations ho...", "url": "https://www.kaieteurnewsonline.com/2021/11/22/glasgow-and-guyana/", "image_url": "https://www.kaieteurnewsonline.com/images/2017/12/letters-2-150x150.jpg", "language": "en", "published_at": "2021-11-22T04:02:05.000000Z", "source": "kaieteurnewsonline.com", "categories": ["general"], "relevance_score": 22.834278}, {"uuid": "0e1fc424-f0e9-4eea-a8f4-c6dfb9cc0906", "title": "Rhodes goes to Glasgow", "description": "", "keywords": "", "snippet": "This week, Ben calls in from the COP26 climate summit in Glasgow where he’s traveling with President Obama. In this episode Ben and Tommy cover the latest new...", "url": "https://crooked.com/podcast/rhodes-goes-to-glasgow/", "image_url": "https://res.cloudinary.com/crooked-media/image/upload/f_auto,q_auto/v1636501677/crooked/pstw-episode-generic-hero-twitter-487780-7SDc8RBy.jpg", "language": "en", "published_at": "2021-11-10T05:01:55.000000Z", "source": "crooked.com", "categories": ["politics", "general"], "relevance_score": 22.784126}, {"uuid": "b1610588-2f7b-4bc3-b80d-e028db24db50", "title": "glasgow: Five things you need to know about the Glasgow Climate Pact", "description": "UK News: LONDON: The COP26 UN climate talks in Glasgow have finished and the gavel has come down on the Glasgow Climate Pact agreed by all 197 countries.", "keywords": "paris agreement, ndc, glasgow loss and damage facility, Glasgow Climate Pact, glasgow climate, glasgow", "snippet": "LONDON: The COP26 UN climate talks in Glasgow have finished and the gavel has come down on the Glasgow Climate Pact agreed by all 197 countries.If the 2015 Pari...", "url": "https://timesofindia.indiatimes.com/world/uk/five-things-you-need-to-know-about-the-glasgow-climate-pact/articleshow/87678435.cms", "image_url": "https://static.toiimg.com/thumb/msid-87694125,width-1070,height-580,imgsize-166868,resizemode-75,overlay-toi_sw,pt-32,y_pad-40/photo.jpg", "language": "en", "published_at": "2021-11-14T07:33:06.000000Z", "source": "timesofindia.indiatimes.com", "categories": ["general"], "relevance_score": 22.72462}]}'
    my_dict=json.loads(data)

    articles=[]
    for i in range(5):
        articles.append({"title": my_dict['data'][i]['title'], "desc": my_dict['data'][i]['snippet'], 
                    "url":my_dict['data'][i]['url'], "img":my_dict['data'][i]['image_url']})
    context_dict["articles"] = articles

    return render(request, 'employee.html', context=context_dict)
        
