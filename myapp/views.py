from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
from . import server


def update_score(request):
    if request.method == 'POST':
        r,s = server.input_user_score(request.body)
        return HttpResponse(r)
    return HttpResponse('hello world')


def get_score_rank(request, rank_begin, rank_end,user_name):
    ret = server.get_user_score_rank(request, rank_begin, rank_end,user_name)
    return HttpResponse(ret)