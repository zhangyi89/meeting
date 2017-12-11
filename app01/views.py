from django.shortcuts import render, redirect, HttpResponse
import json

from app01 import models


# Create your views here.


def login(request):
    username = request.POST.get("username")
    pwd = request.POST.get("pwd")
    user_obj = models.UserInfo.objects.filter(name=username, pwd=pwd)
    if user_obj:
        request.session['user'] = {'username': username, "uid": user_obj[0].id}
        return redirect("/meeting_list/")
    return render(request, "login.html")


def meeting_list(request):
    time_list = {2: "8：00", 3: "9:00", 4: "10:00", 5: "11:00", 6: "12:00", 7: "13:00",
                 8: "14:00", 9: "15:00", 10: "16:00", 11: "17:00", 12: "18:00", 13: "19:00",
                 14: "20:00"}
    room_list = models.MeetingList.objects.all()
    reserve_list = models.Reserve.objects.all()
    if request.method == "POST":
        # print(json.loads(request.body.decode("utf8")))
        data = json.loads(request.body.decode("utf8"))
        user_id = request.session['user']['uid']

        room = data['meeting_room']
        room_obj = models.MeetingList.objects.filter(name=room)[0]
        time = time_list[data['times'][0]]
        print(user_id, room, time)
        models.Reserve.objects.create(person_id=user_id, room=room_obj, reserve_time=time, reserve_date="2017-12-10")
        return HttpResponse("ok")

    return render(request, "meeting_list.html", locals())
