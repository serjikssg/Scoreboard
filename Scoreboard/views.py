from django.shortcuts import render
from django.http import HttpResponse
from .models import Scoreboard, ScoreboardTags
import requests, datetime
from django.utils import timezone
from datetime import timedelta


def api2db(request):
    b = requests.get('https://api.safisense.com/api/v1/devices/uptime?company_id=***&api_key=***')
    ma = {}

    for i in b.json()['data']:
        try:
            if i['computedLoadStates']['percentages']['online'] >= 0:
                ma[int(i['deviceid'].split('machine')[1])] = i['computedLoadStates']['percentages']['online']
        except:
            ...

    li = list(ma.keys())

    for m in sorted(li):
        scb = Scoreboard.objects.get(machine_id=m)
        scb.percentage = round(ma[m]*100)
        scb.running = ma[m] > 0
        scb.save()

    return HttpResponse("ok")


def scoreboard(request):
    time_test(request)
    now = datetime.datetime.now()
    ma_list = []
    xx = Scoreboard.objects.filter(display=True)

    for i in xx:
        ma_list.append([i.machine_id, i.tag_id.style, (0 if i.running else 1), i.percentage, i.tag_id.tag, i.update_at, now,])

    return render(request, 'scoreboard/scoreboard.html', {'items':ma_list})


def time_test(request):
    now = timezone.now()
    dbt = Scoreboard.objects.filter(display=True)[0].update_at
    
    td = now - dbt
    txt = "<hr>"
    
    txt += f"D: {dbt} <hr> N: {now} <hr> = {td}"
        
    if td > timedelta(minutes=3):
        txt += f"<hr> update"
        api2db(request)
    else:
        txt += f"<hr> no update"
            
    return HttpResponse(txt)


def tag_change(request, id):
    machine = Scoreboard.objects.filter(machine_id = id)[0]
    return render(request, 'scoreboard/tag_change.html', {'id':machine})
    # return HttpResponse(id)


def tag_update(request, id):
    if request.method == 'GET':
        t = request.GET.get('tag')

        machine = Scoreboard.objects.get(machine_id = id)
        tag = ScoreboardTags.objects.get(id = t)

        machine.tag_id = tag
        machine.save()

    return scoreboard(request)
    ...
