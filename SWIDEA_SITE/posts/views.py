from django.shortcuts import redirect, render
from .models import Idea, DevTool

# Create your views here.
def ideaHome(request):
    posts = Idea.objects.all()
    context = {
        'posts' : posts
    }

    return render(request, template_name="posts/idea_home.html", context=context)

def ideaCreate(request):
    if request.method == "POST":
        title = request.POST["title"]
        image = request.FILE["photo"]
        content = request.POST["content"]
        interest = request.POST["interest"]
        dev_tool = request.POST["dev_tool"]

        new = Idea.objects.create(title=title, image=image, content=content, interest=interest, dev_tool=dev_tool)

        return redirect(f"/idea_detail/{new.id}")
    else:
        tools = DevTool.objects.all()
        context = {
            'tools' : tools
        }
        return render(request, template_name="posts/idea_create.html", context=context)

def ideaDetail(request):
    pass

def ideaUpdate(request):
    pass

def ideaDelete(request):
    pass

def devHome(request):
    pass

def devCreate(request):
    pass

def devDetail(request):
    pass

def devUpdate(request):
    pass

def devDelete(request):
    pass