import os
import time
import requests
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from admins import models
from admins.sessions import verify_permission


def index(request):

    if request.method == 'POST':
        user = request.POST.get('username','')
        pwd = request.POST.get('password','')
        try:
            admin = models.Admins.objects.get(username=user)
        except:
            return HttpResponse('error')
        if admin.pwd == pwd:
            request.session['username'] = user
            request.session.set_expiry(0)
            return render(request, "index.html")
        else:
            err = '密码或用户名不正确'
            return render(request, "login.html", locals())
    return render(request, "index.html")


@verify_permission
def welcome(request,*args):
    times = time.strftime('%Y-%m-%d %H:%M')
    trains = train()
    return render(request, "welcome.html", locals())


def login(request):
    return render(request, "login.html")






def member(request):
    return render(request, "member-list.html")


def city_path(request):
    return render(request, "order-list.html")


def country_path(request):
    return render(request, "order-list1.html")


def process(request):
    return render(request, "cate.html")


def contract(request):
    return render(request, "city.html")


def meet(request):
    return render(request, "city.html")



def train():
    url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station=LYT&leftTicketDTO.to_station=SYT&purpose_codes=ADULT'
    headers = {
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
              'Accept-Encoding': 'gzip, deflate, br',
              'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
              'Cookie': 'JSESSIONID=FCEF19F8DA5313B99D1C153A0C291F91; RAIL_EXPIRATION=1591578008458; RAIL_DEVICEID=I39EJMOQUfW8b6OM1wqHnbttUXpR8cejm4BLgxwfO2vxVCzaUZwG2eHLTPEGOdYbSMTvT2wn_4r4QywUBBvCf5dVx_N5ltTvCFDVSUDlsQVU0F682IErlU_t7VB5ESxC0ipXVNSFpdQzfM8E245zU4UfyvtKjY1-; _jc_save_fromStation=%u8FBD%u9633%2CLYT; _jc_save_toStation=%u6C88%u9633%2CSYT; _jc_save_fromDate=2020-06-10; _jc_save_toDate=2020-06-04; _jc_save_wfdc_flag=dc; route=495c805987d0f5c8c84b14f60212447d; BIGipServerotn=1574502666.64545.0000',
              'Host': 'kyfw.12306.cn',
              'Upgrade-Insecure-Requests':	'1',
              'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0',
              'Connection': 'keep-alive'
               }
    date = time.strftime("%Y-%m-%d")
    #print(date)
    res = requests.get(url=url.format(date), headers=headers)
    res.encoding = 'utf-8'
    html = res.json()
    re_list = []
    for re in html['data']['result']:
        re = re.split('|')
        re_dict = {}
        #for i in range(len(re)):
         #   re_dict[i] = re[i]
        #print(re_dict)
        re_dict['num'] = re[3]
        re_dict['time_str'] = re[8]+'---'+re[9]
        re_dict['business_spe'] = re[25] + re[32]
        re_dict['one'] = re[31]
        re_dict['two'] = re[30]
        re_dict['three'] = re[29]
        re_dict['stand'] = re[26]
        re_list.append(re_dict)
    #print(re_list)
    return re_list

