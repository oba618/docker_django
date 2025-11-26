from django.shortcuts import render

from .models import Content


def index(request):
    latest_content_list = Content.objects.order_by("-pub_date")[:10]
    context = {"latest_content_list": latest_content_list}
    return render(request, "index/index.html", context)
