# -*-coding:utf-8-*-
import json

import requests


class BaseApi:

    def __init__(self):
        self.base_url = 'https://qyapi.weixin.qq.com/cgi-bin'
        self.access_token = self.get_token()

    def get_token(self):
        corp_id = ''
        corp_secret = ''
        params = {
            'corpid': corp_id,
            'corpsecret': corp_secret
        }
        r = requests.get(self.base_url + '/gettoken', params=params)
        response_dict = r.json()
        if r.status_code == 200 and response_dict['errcode'] == 0:
            access_token = response_dict['access_token']
            return access_token
        return r

    @staticmethod
    def send(kwargs):
        r = requests.request(**kwargs)
        print(f'url: {r.url}')
        print(f'params: {kwargs["params"]}')
        if 'json' in kwargs:
            print(f'json: {kwargs["json"]}')
        print(json.dumps(r.json(), ensure_ascii=False, indent=4))
        return r
