# -*-coding:utf-8-*-
import time

from tag import Tag


class TestTag:

    def setup_class(self):
        self.tag = Tag()

    def test_del_tmp_groups(self):
        # 清理之前自动化创建的标签组
        for group in self.tag.list_tag().json()['tag_group']:
            if 'tmp_group' in group['group_name']:
                self.tag.del_tag(group_ids=[group['group_id']])

    def test_add_tag(self):
        time_now = time.strftime('%Y%m%d%H%M%S', time.localtime())
        group_name = f'tmp_group{time_now}'
        tag = [{
            'name': f'tmp_tag{time_now}',
        }]
        r = self.tag.add_tag(group_name, tag)
        assert r.status_code == 200 and r.json()['errcode'] == 0

    def test_update_tag(self):
        r = self.tag.update_tag(self.tag.tag_id, name='new_tag_name')
        assert r.status_code == 200 and r.json()['errcode'] == 0

    def test_list_tag(self):
        r = self.tag.list_tag()
        assert r.status_code == 200 and r.json()['errcode'] == 0

    def test_del_tag(self):
        group_ids = [self.tag.group_id]
        tag_ids = [self.tag.tag_id]
        r = self.tag.del_tag(group_ids=group_ids, tag_ids=tag_ids)
        assert r.status_code == 200 and r.json()['errcode'] == 0
