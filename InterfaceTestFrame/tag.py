# -*-coding:utf-8-*-

from base_api import BaseApi


class Tag(BaseApi):

    def __init__(self):
        super().__init__()
        self.group_id = None
        self.tag_id = None

    def add_tag(self, group_name, tag, **kwargs):
        data = {
            "method": "post",
            "url": f'{self.base_url}/externalcontact/add_corp_tag',
            "params": {"access_token": self.access_token},
            "json": {"group_name": group_name,
                     "tag": tag,
                     **kwargs
                     }}
        r = self.send(data)
        res_dict = r.json()
        if r.status_code == 200 and res_dict['errcode'] == 0:
            self.group_id = res_dict['tag_group']['group_id']
            self.tag_id = res_dict['tag_group']['tag'][0]['id']

        return r

    def update_tag(self, tag_id, name=None, order=None):
        data = {
            "method": "post",
            "url": f'{self.base_url}/externalcontact/edit_corp_tag',
            "params": {"access_token": self.access_token},
            "json": {
                'id': tag_id,
                'name': name,
                'order': order
            }}
        r = self.send(data)
        return r

    def list_tag(self):
        data = {
            "method": "post",
            "url": f'{self.base_url}/externalcontact/get_corp_tag_list',
            "params": {"access_token": self.access_token},
        }
        r = self.send(data)
        return r

    def del_tag(self, tag_ids=None, group_ids=None):
        data = {
            "method": "post",
            "url": f'{self.base_url}/externalcontact/del_corp_tag',
            "params": {"access_token": self.access_token},
            'json': {
                'tag_id': tag_ids,
                'group_id': group_ids
            }
        }
        r = self.send(data)
        return r
