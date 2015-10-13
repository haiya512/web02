# Create your views here.
#encoding=utf-8
from django.shortcuts import render_to_response
import datetime
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from web.models import *
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from web.backend import MultiRunCounter
from web.backend import *
import json
import os
Working_dir = '/home/limian/py_web/web'
def index(request):
        return render_to_response('index.html')
def monitor(request):
	file = '/home/limian/py_web/static/monitor'
        get_images = os.listdir(file)
        return render_to_response('monitor.html',{"get_images":get_images })
def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><body>当前时间 %s.</body></html>" % now
	return HttpResponse(html)
# Create your views here.
def index(request):
        return render_to_response('index.html')
def upload(request):
        return render_to_response('upload.html')
def server_manager(request):
        group_list = {}
        for group in  Group.objects.all(): #get all the groups
                group_list[ group.name ] = ( IP.objects.filter(group__name=group.name))
        remote_user_list = TriaquaeUser.objects.get(user__username=request.user).remoteuser.all()

        #groups = Group.objects.all() #get all the groups
        return render_to_response('server_manager.html',
                {'group_list':group_list,
                'user':request.user,
                'remote_user_list':remote_user_list,}
                )
def dashboard(request):
        return render_to_response('dashboard.html',{'user':request.user})
def account_login(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username,password=password) #mapping the user and passoword
    if user is not None:
        auth.login(request,user) #auth for user
        return HttpResponseRedirect("/dashboard/")
    else:
        return render_to_response('index.html',{'login_err':'Wrong username or password!'})
def get_ip_list(request):
        g_name = request.GET['Name']
        print g_name
        ip_list = IP.objects.filter(group__name = g_name).values()
        ip_dic = {}
        for host in ip_list:
                ip_dic[host['hostname']] = host

        return HttpResponse(json.dumps(ip_dic))
def runCmd(request):
        print request.POST
	track_mark = MultiRunCounter.AddNumber()
	user_input = request.POST['cmd']
	user_account = request.POST['SelectUser']
	SelectedIPs = []
	GroupList = Group.objects.all()
	for g_name in  GroupList:
		if g_name.name in request.POST.keys():
			print "selected group:",g_name.name
			for selected_ip in IP.objects.filter(group__name = g_name.name):		
				SelectedIPs.append(selected_ip.ip)
	print request.POST.get('command')
	cmd = "python %s/backend/multiprocessing_runCMD2.py %s '%s' '%s' %s & " %(Working_dir,track_mark,''.join(set(SelectedIPs)),user_input,user_account)
	os.system(cmd)
	return HttpResponse(track_mark)
def getCmdResult(request):
	track_mark=request.GET['TrackMark']
	print track_mark
	cmd_result_record = OpsLog.objects.get(track_mark=track_mark)
	total_task = cmd_result_record.total_task
	success_num = cmd_result_record.success_num
	failed_num = cmd_result_record.failed_num
	cmd_feedback = OpsLogTemp.objects.filter(track_mark=track_mark).values('event_log','ip','result')
	#print cmd_feedback
	def result():
		data_dic={}
		for i in cmd_feedback:
			print i['ip']
			data_dic[i['ip']] = i
		print data_dic
		return data_dic
	return HttpResponse(json.dumps(result()))
