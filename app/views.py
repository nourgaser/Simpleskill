from re import M
from django.shortcuts import redirect, render
from .models import *
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q


@login_required
def dashboard(request, fid=-1):
    onGoingSimpleskills = []
    availableSimpleskills = []
    user = request.user

    registered = user.registered_simpleskills.all()
    interests = user.interests.all()
    seen = set()
    if fid == -1:
        for tag in Tag.objects.all():
            for ss in tag.simpleskills.all():
                if ss not in seen:
                    if ss in registered:
                        onGoingSimpleskills.append(ss)
                    elif tag.category in interests and ss not in user.finished_simpleskills.all():
                        availableSimpleskills.append(ss)
                    seen.add(ss)
    else:
        for tag in Tag.objects.all():
            if tag.category in interests and tag.category.id == fid:
                for ss in tag.simpleskills.all():
                    if ss not in seen:
                        if ss in registered:
                            onGoingSimpleskills.append(ss)
                        elif ss not in user.finished_simpleskills.all():
                            availableSimpleskills.append(ss)
                        seen.add(ss)

    context = {
        "user": user,
        "ongoing_simpleskills": onGoingSimpleskills,
        "available_simpleskills": availableSimpleskills
    }
    return render(request, 'app/dashboard.html', context=context)


@login_required
def configure(request):
    return render(request, 'app/user_config/configure.html', context={"user": request.user})


@login_required
def configure_interests(request):
    interests_ids = []
    for i in request.user.interests.all():
        interests_ids.append(i.id)
    if request.method == 'GET':
        return render(request, "app/user_config/interests.html", context={
            "user": request.user,
            "fields": Category.objects.all(), "interests_ids": interests_ids})
    elif request.method == 'POST':
        user = request.user
        interests = []
        for x in request.POST:
            if str(x) != "csrfmiddlewaretoken":
                interests.append(Category.objects.get(id=x))
        user.interests.set(interests)
        user.save()
        return redirect("/app/configure/interest_level")


@login_required
def interest_level(request):
    if request.method == 'GET':
        return render(request, "app/user_config/interest_levels.html", context={"user": request.user, "interests": UserInterest.objects.filter(user=request.user)})
    elif request.method == 'POST':
        for x in request.POST.keys():
            if str(x) != "csrfmiddlewaretoken":
                interest = UserInterest.objects.get(id=x)
                interest.interest_level = request.POST[x]
                interest.save()
        return redirect("/app/configure/experience_level")


@login_required
def experience_level(request):
    if request.method == 'GET':
        return render(request, "app/user_config/experience_levels.html", context={"user": request.user, "interests": UserInterest.objects.filter(user=request.user)})
    elif request.method == 'POST':
        for x in request.POST.keys():
            if str(x) != "csrfmiddlewaretoken":
                interest = UserInterest.objects.get(id=x)
                interest.experience_level = request.POST[x]
                interest.save()
        return redirect("/app")


@login_required
def learn(request, ssid):
    user = request.user
    ss = Simpleskill.objects.get(id=ssid)
    if ss not in user.registered_simpleskills.all() and ss not in user.finished_simpleskills.all():
        request.user.registered_simpleskills.add(ss)

    context = {
        "user": user,
        "ss": ss,
        "rss": RegisteredSimpleskill.objects.get(user=user, simpleskill=ss)
    }
    return render(request, 'app/learn.html', context=context)


@login_required
def unlearn(request, ssid):
    user = request.user
    ss = Simpleskill.objects.get(id=ssid)
    if ss in user.registered_simpleskills.all():
        RegisteredSimpleskill.objects.get(user=user, simpleskill=ss).delete()
        # user.registered_simpleskills.remove(ss)
    return redirect("/app")


@login_required
def finish(request, ssid):
    user = request.user
    ss = Simpleskill.objects.get(id=ssid)
    if ss in user.registered_simpleskills.all():
        user.finished_simpleskills.add(ss)
        user.registered_simpleskills.remove(ss)
    return redirect("/app/finished/%d" % ss.tags.all()[0].category.id)


@login_required
def unfinish(request, ssid):
    user = request.user
    ss = Simpleskill.objects.get(id=ssid)
    if ss in user.finished_simpleskills.all():
        user.finished_simpleskills.remove(ss)
        user.registered_simpleskills.add(ss)
    return redirect("/app/learn/%d" % ssid)


@login_required
def finished(request, fid=-1):
    finishedSimpleskills = []
    user = request.user

    seen = set()
    if fid == -1:
        finishedSimpleskills = user.finished_simpleskills.all()
    else:
        for ss in user.finished_simpleskills.all():
            for tag in ss.tags.all():
                if tag.category.id == fid:
                    finishedSimpleskills.append(ss)
                    break
            seen.add(ss)
    context = {
        "user": user,
        "finished_simpleskills": finishedSimpleskills,
    }
    return render(request, 'app/finished.html', context=context)


@login_required
def finish_material(request, rssid, mid):
    user = request.user
    rss = RegisteredSimpleskill.objects.get(id=rssid)
    mat = Material.objects.get(id=mid)
    if rss.simpleskill in user.registered_simpleskills.all():
        rss.finished_materials.add(mat)
    return redirect("/app/learn/%d" % rss.simpleskill.id)

@login_required
def unfinish_material(request, rssid, mid):
    user = request.user
    rss = RegisteredSimpleskill.objects.get(id=rssid)
    mat = Material.objects.get(id=mid)
    if rss.simpleskill in user.registered_simpleskills.all():
        rss.finished_materials.remove(mat)
    return redirect("/app/learn/%d" % rss.simpleskill.id)


@login_required
def explore(request):
    return HttpResponse("Hello from app:explore!")
