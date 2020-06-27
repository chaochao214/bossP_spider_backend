# Create your views here.


from django.http import HttpResponse, JsonResponse

from bossP.models import Zhilian, Lagou, Zhipin


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def search(request, searchName):
    zhilianList = Zhilian.objects.all().filter(job__contains=searchName)
    lagouList = Lagou.objects.all().filter(job__contains=searchName)
    zhipinList = Zhipin.objects.all().filter(job__contains=searchName)
    d = []

    if zhilianList is not None:
        for res in lagouList:
            print(res.company)
            # d.append(res.company)
            d.append({'id': res.id, 'company': res.company, 'job': res.job, 'city': res.city, 'site': res.city,
                      'salary': res.salary,
                      'url': res.url})

    if zhilianList is not None:
        for res in zhilianList:
            print(res.company)
            # d.append(res.company)
            d.append({'id': res.id, 'company': res.company, 'job': res.job, 'city': res.city, 'site': "",
                      'salary': res.salary,
                      'url': res.url})

    if zhipinList is not None:
        for res in zhipinList:
            print(res.company)
            # d.append(res.company)
            d.append({'id': res.id, 'company': res.company, 'job': res.job, 'city': res.city, 'site': "",
                      'salary': res.salary,
                      'url': res.url})

    # 和前端约定的返回格式
    result = {"resCode": '0', "message": 'success', "data": d}

    return JsonResponse(result, safe=False)


def search1(request):
    zhilianList = Zhilian.objects.all()
    lagouList = Lagou.objects.all()
    zhipinList = Zhipin.objects.all()
    d = []

    if zhilianList is not None:
        for res in lagouList:
            print(res.company)
            # d.append(res.company)
            d.append({'id': res.id, 'company': res.company, 'job': res.job, 'city': res.city, 'site': res.city,
                      'salary': res.salary,
                      'url': res.url})

    if zhilianList is not None:
        for res in zhilianList:
            print(res.company)
            # d.append(res.company)
            d.append({'id': res.id, 'company': res.company, 'job': res.job, 'city': res.city, 'site': "",
                      'salary': res.salary,
                      'url': res.url})

    if zhipinList is not None:
        for res in zhipinList:
            print(res.company)
            # d.append(res.company)
            d.append({'id': res.id, 'company': res.company, 'job': res.job, 'city': res.city, 'site': "",
                      'salary': res.salary,
                      'url': res.url})

    # 和前端约定的返回格式
    result = {"resCode": '0', "message": 'success', "data": d}

    return JsonResponse(result, safe=False)
