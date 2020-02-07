import random
import unittest
import requests

# Create your tests here.
class TestDemo(unittest.TestCase):

    def test_update_score(self,client_name):
        url = 'http://127.0.0.1:8000/update_score'
        data = {
            'client_name':client_name,
            'score': random.randint(0,10000000)
        }
        response = requests.post(url,json=data)
        print(response.text)

    def test_get_score_rank(self,cilent_name = '客户端1'):
        index_begin = 0
        index_end = 10
        url = 'http://127.0.0.1:8000/score_rank/%s/%s/%s'
        url = url%(index_begin,index_end,cilent_name)
        response = requests.get(url)
        print(response.text)


    def test_do_update_score(self):
        st = '客户端%s'
        for i in range(10):
            name = st%i
            self.test_update_score(name)