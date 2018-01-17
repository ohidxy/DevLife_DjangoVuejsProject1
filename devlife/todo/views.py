from django.shortcuts import render

# Create your views here.
def todo_page(request):
    if request.user.is_authenticated():
        if request.method == 'GET':
          return render(request,'todo/todo.html')
    else:
        return redirect('/login')