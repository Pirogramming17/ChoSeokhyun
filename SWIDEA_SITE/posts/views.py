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
    tools = DevTool.objects.all()
    context = {
        'tools' : tools
    }

    return render(request, template_name='posts/dev_home.html', context=context)

def devCreate(request):
    if request.method == "POST":
        name = request.POST["name"]
        kind = request.POST["kind"]
        content = request.POST["content"]
        
        new = DevTool.objects.create(name=name, kind=kind, content=content)

        return redirect(f"/dev_detail/{new.id}")
    else:
        
        context = {
            
        }
        return render(request, template_name="posts/dev_create.html", context=context)

def devDetail(request, id):
    tool = DevTool.objects.get(id=id)
    ideas = Idea.objects.filter(dev_tool = tool)
    context = {
        'tool' : tool,
        'ideas' : ideas
    }
    return render(request, template_name='posts/dev_detail.html', context=context)

def devUpdate(request, id):
    if request.method == "POST":
        name = request.POST["name"]
        kind = request.POST["kind"]
        content = request.POST["content"]
        
        DevTool.objects.filter(id=id).update(name=name, kind=kind, content=content)
        return redirect(f"/dev_detail/{id}")
    else:
        tool = DevTool.objects.get(id=id)
        context = {
            "tool" : tool
        }
        return render(request, template_name="posts/dev_update.html", context=context)

def devDelete(request, id):
    if request.method == "POST":
        DevTool.objects.filter(id=id).delete()
    return redirect("/dev_home")