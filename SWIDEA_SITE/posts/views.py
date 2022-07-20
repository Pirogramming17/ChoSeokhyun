from django.shortcuts import redirect, render
from .models import Idea, DevTool

# Create your views here.
def ideaHome(request):
    sort = request.GET.get('sort', '')
    if sort == '':
        posts = Idea.objects.all()
    else:
        posts = Idea.objects.all().order_by(sort)

    context = {
        'posts' : posts
    }

    return render(request, template_name="posts/idea_home.html", context=context)

def ideaCreate(request):
    if request.method == "POST":
        title = request.POST["title"]
        image = request.FILES.get("image")
        content = request.POST["content"]
        interest = request.POST["interest"]
        tool_name = request.POST["dev_tool"]

        dev_tool = DevTool.objects.get(name = tool_name)
        new = Idea.objects.create(title=title, image=image, content=content, interest=interest, dev_tool=dev_tool)
        return redirect(f"/idea_detail/{new.id}")
    else:
        tools = DevTool.objects.all()
        context = {
            'tools' : tools
        }
        return render(request, template_name="posts/idea_create.html", context=context)

def ideaDetail(request, id):
    idea = Idea.objects.get(id=id)
    context = {
        'idea' : idea
    }

    return render(request, template_name='posts/idea_detail.html', context=context)

def ideaUpdate(request,id):
    if request.method == "POST":
        title = request.POST["title"]
        if request.FILES.get('file') is not None:
            image= request.FILES.get('file')
        else:
            image = Idea.objects.get(id=id).image
        content = request.POST["content"]
        interest = request.POST["interest"]
        tool_name = request.POST["dev_tool"]
        dev_tool = DevTool.objects.get(name = tool_name)
        Idea.objects.filter(id=id).update(title=title, image=image, content=content, interest=interest, dev_tool=dev_tool)
        return redirect(f"/idea_detail/{id}")
    else:
        idea = Idea.objects.get(id=id)
        tools = DevTool.objects.all()
        context = {
            "idea" : idea,
            "tools" : tools
        }
        return render(request, template_name="posts/idea_update.html", context=context)

def ideaDelete(request, id):
    if request.method == "POST":
        Idea.objects.filter(id=id).delete()
    return redirect("/")

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