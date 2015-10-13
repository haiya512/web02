from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class IP(models.Model):
        hostname = models.CharField(max_length=50,unique=True)
        ip = models.IPAddressField(unique=True)
        group = models.ManyToManyField('Group',null=True,blank=True)
        port = models.IntegerField(default='22')
        os = models.CharField(max_length=20,default='linux',verbose_name='Operating System')
        def __unicode__(self):
                return self.hostname
class Group(models.Model):
        name = models.CharField(max_length=50,unique=True)
        def __unicode__(self):
                return self.name
class RemoteUser(models.Model):
        name = models.CharField(max_length=50,unique=True)
        def __unicode__(self):
                return self.name
class TriaquaeUser(models.Model):
        user = models.ForeignKey(User,null=True)
        email = models.EmailField()
        remoteuser = models.ManyToManyField(RemoteUser,null=True,blank=True)
        group = models.ManyToManyField(Group,null=True,blank=True)
        ip = models.ManyToManyField(IP,null=True,blank=True)
        def __unicode__(self):
                return '%s' % self.user
'''
class IpGroup(models.Model):
        group_name = models.CharField(max_length=30)
        def __unicode__(self):
                return self.group_name
'''
class AuthByIpAndRemoteUser(models.Model):
        password = models.CharField(max_length=1024,verbose_name="Password or SSH_KEY")
        AUTH_CHOICES = (('ssh','ssh-password'),('ssh-key','ssh-key'))
        authtype = models.CharField(max_length=100,choices=AUTH_CHOICES)
        ip = models.ForeignKey(IP,null=True,blank=True)
        remoteUser = models.ForeignKey(RemoteUser,null=True,blank=True)
        def __unicode__(self):
                return '%s\t%s' % (self.ip,self.remoteUser)
        class Meta:
                unique_together = (('ip','remoteUser'),)

class ServerStatus(models.Model):
        host = models.IPAddressField(primary_key=True)
        host_status = models.CharField(max_length=10,default='Unkown')
        ping_status = models.CharField(max_length=100,default='Unkown')
        last_check = models.DateTimeField(auto_now_add=True)
        host_uptime = models.CharField(max_length=50,default='Unkown')
        attempt_count = models.CharField(max_length=25,null=True,blank=True)
        def __unicode__(self):
                return self.host
class OpsLog(models.Model):
        start_date = models.DateTimeField(auto_now_add=True)
        finish_date = models.DateTimeField(null=True,blank=True)
        log_type = models.CharField(max_length=50)
        tri_user = models.CharField(max_length=30)
        run_user = models.CharField(max_length=30)
        cmd = models.TextField()
        total_task = models.IntegerField()
        success_num = models.IntegerField()
        failed_num = models.IntegerField()
        track_mark = models.IntegerField(unique=True)
        note = models.CharField(max_length=100,blank=True,null=True)
        def __unicode__(self):
                return self.cmd

class OpsLogTemp(models.Model):
        date = models.DateTimeField(auto_now_add=True)
        user = models.CharField(max_length=30)
        ip = models.IPAddressField()
        event_type = models.CharField(max_length=50)
        cmd = models.TextField()
        event_log = models.TextField()
        result = models.CharField(max_length=30,default='unknown')
        track_mark = models.IntegerField(blank=True)
        note = models.CharField(max_length=100,blank=True)
        def __unicode__(self):
		return self.ip

class UploadFile(models.Model):
    	username=models.CharField(max_length=50)
    	uploadfile=models.FileField(upload_to='./upload/')
    
    	def __unicode__(self):
        	return username                
