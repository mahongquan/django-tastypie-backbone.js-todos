from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
        (r'^$','mysite.ncsdd.views.index'),
        #
	(r'^register/','mysite.ncsdd.views.register'),
	(r'^saveuser/','mysite.ncsdd.views.saveuser'),	                       
	(r'^login/','mysite.ncsdd.views.mylogin'),	
	(r'^logout/','mysite.ncsdd.views.mylogout'),
	(r'^afterlogin/','mysite.ncsdd.views.afterlogin'),
	(r'^loginpage/','mysite.ncsdd.views.loginpage'),
         #
	(r'^editcontact/','mysite.ncsdd.views.editcontact'),
	(r'^newcontact/','mysite.ncsdd.views.newcontact'),
	(r'^savecontact/','mysite.ncsdd.views.savecontact'),
	(r'^printcontact/','mysite.ncsdd.views.printcontact'),
	(r'^deletecontact/','mysite.ncsdd.views.deletecontact'),                       
	(r'^finishcontact/','mysite.ncsdd.views.finishcontact'),  

	(r'^server_processing/','mysite.ncsdd.views.server_processing'),
    (r'^ajax/','mysite.ncsdd.views.ajax'),       
    (r'^post/','mysite.ncsdd.views.post'),           
         #
    (r'^gedit/','mysite.ncsdd.views.gedit'),
    (r'^infinite/','mysite.ncsdd.views.infinite'),
    (r'^gserver/','mysite.ncsdd.views.gserver'),
)
