from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
        #return HttpResponse('my_to_do_app first page')
        return render(request, 'my_to_do_app/index.html')


def createTodo(request):
        user_input_str = request.POST['todoContent']
        return HttpResponse("create Todo를 할 거야!! " + user_input_str)