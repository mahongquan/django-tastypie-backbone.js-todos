from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from mysite.ncsdd.models import Todo

class TodoResource(ModelResource):
	class Meta:
		queryset = Todo.objects.all()
		authorization = Authorization()
