import datetime
import json
from . import models


def get_user_score_rank(request, rank_begin, rank_end, user_name):
    data = models.score.objects.all().order_by('-score')[rank_begin:rank_end]
    ret_dc = [
        {
            'index': rank_begin + index + 1,
            'score': d.score,
            'name': d.user_name
        }
        for index, d in enumerate(data)
    ]
    user_data = list(filter(lambda x: True if x['name'] == user_name else False, ret_dc))[0]
    ret_dc.append(
        {
            'index': user_data['index'],
            'score': user_data['score'],
            'name': user_data['name']
        }
    )
    return ret_dc


def input_user_score(body):
    data = json.loads(body)
    client_name = data.get('client_name')
    score = data.get('score')
    if not all([client_name, score]) or not isinstance(score, int) or 1 < score or score > 10000000:
        return {
                   'message': '参数不正确'
               }, 400
    models.score.objects.filter(user_name=client_name).delete()
    models.score.objects.create(**{
        'score': score,
        'user_name': client_name
    })
    return '成功', 200
