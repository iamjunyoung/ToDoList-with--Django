from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
from django.db.models import Q

# Create your views here.
def index(request):
        #return HttpResponse('my_to_do_app first page')
        #todos = Todo.objects.all()
        todos = Todo.objects.filter(isDone= False)
        content = {'todos' : todos}
        return render(request, 'my_to_do_app/index.html', content)
        #return render(request, 'my_to_do_app/index.html')


def createTodo(request):
        user_input_str = request.POST['todoContent']
        new_todo = Todo(content = user_input_str)
        new_todo.save()
        return HttpResponseRedirect(reverse('index'))
        #return HttpResponse("create Todo를 할 거야!! " + user_input_str)

def doneTodo(request):
        done_todo_id = request.GET['todoNum']
        print("완료한 todo의 id ", done_todo_id)
        todo = Todo.objects.get(id = done_todo_id)
        todo.isDone = True
        todo.save()
        # todo.delete()
        return HttpResponseRedirect(reverse('index'))