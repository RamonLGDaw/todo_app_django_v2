from django.shortcuts import redirect, render
from task_app.forms import CreateNewTask
from task_app.models import Task, Category

# By default, the filter type shows all completed and pending tasks. 
filter_type = 'all'


def index(request):
    
    task_list_all = Task.objects.all()
    task_list_pending = Task.objects.all().filter(done = False)
    task_list_completed = Task.objects.all().filter(done = True)

    if filter_type == 'all':
        task_list = task_list_all

    elif filter_type == 'completed':
        task_list = task_list_completed

    else:
        task_list = task_list_pending

    if len(task_list) < 10:
        return render(request,'index.html', {
                'form':CreateNewTask,
                'task_list':task_list,
                'filter_type':filter_type,
                'len_list_all':len(task_list_all),
                'len_list_pending':len(task_list_pending),
                'len_list_completed':len(task_list_completed)

            })
    else:
        return render(request, 'index.html', {
            'max_reached': True,
            'task_list':task_list
        })


def create_task(request):
    if request.method == 'GET':
        return render(request, 'index.html', {
            'form': CreateNewTask()
        })
    else:
        title = request.POST['title']
        category_id = request.POST['category']
        category_object = Category.objects.get(id=category_id)
        Task.objects.create(title=title, category=category_object)

        return redirect('index')


def delete_task(request, id):
    Task.objects.filter(id=id).delete()
    return redirect('index')


def update_task(request, id):
    updated_task_title = request.POST['update_task']

    task_to_update = Task.objects.get(id=id)
    task_to_update.title = updated_task_title
    task_to_update.save()

    return redirect('index')


def task_check_ok(request, id):

    task = Task.objects.get(id = id)
    task.done = True
    task.save()
    print(f'El check se ha pasado a {task.done}')

    return redirect('index')



def task_check_no(request, id):

    task = Task.objects.get(id = id)
    task.done = False
    task.save()
    return redirect('index')


def task_filter(request, type):
    global filter_type
    filter_type = type
    return redirect('index')


def category(request):

    category_list = Category.objects.all()
    len_category_list = len(category_list)
    return render(request, 'create_category.html',{
        'category_list':category_list,
        'len_category_list': len_category_list
    })


def create_category(request):

    category_name = request.POST.get('category_name', '').strip().upper()
    category_color = request.POST.get('category_color', '').strip()


    if not category_name:
        return render(request, 'create_category.html', {
            'error': 'Category name is empty.'
        })

    if Category.objects.filter(name__iexact=category_name).exists():
        return render(request, 'create_category.html', {
            'answer': category_name,
        })

    Category.objects.create(name=category_name, color=category_color)
    return redirect('index')



def delete_category(request, id):

    Category.objects.filter(id=id).delete()

    return redirect('category')