from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def function_view(request):
    return HttpResponse('Response :)')


class ExampleClassBased(View):
	def get(self, request):
		return HttpResponse('response from class based view')


def Example_template(request):
	print('Hello')
	return render(request, 'Example.html')

def Example_template_Variable(request):
	return render(request, 'variable.html', {'my_variable': 'Текст'})

class GroupsView(View):
	def get(self, request):
		data = {
			'groups': [
				{'title': 'ИУ5-51', 'id' : '1'},
				{'title': 'ИУ5-52', 'id' : '2'}
			]
		}
		return render(request, 'groups.html', data)


class GroupView(View):
	def get(self, request, id):
		data = {
			'group': {
				'id': id
			}
		}
		return render(request, 'group.html', data)
