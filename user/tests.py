# Create your tests here.

from django.test import TestCase
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wcb_project.settings")
django.setup()
from manage_system.models import User
from datetime import datetime
import datetime
def add():
# #     User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time=datetime.now().strftime('%Y-%m-%d'),province='山东省',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
# #     User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time=datetime.now().strftime('%Y-%m-%d'),province='山东省',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
# #     User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time=datetime.now().strftime('%Y-%m-%d'),province='山东省',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
# #     User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time=datetime.now().strftime('%Y-%m-%d'),province='山东省',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
# #     User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time=datetime.now().strftime('%Y-%m-%d'),province='山东省',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
# #     User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time=datetime.now().strftime('%Y-%m-%d'),province='山东省',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
# #     User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time=datetime.now().strftime('%Y-%m-%d'),province='山东省',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
#     User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-28",province='山东省',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
#     User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-28",province='山东省',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
#     User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-28",province='山东省',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
#     User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-25",province='山东省',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
#     User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-25",province='山东省',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
#     User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-21",province='山东省',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
#     User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-21",province='山东省',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
#     User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-21",province='山东省',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
#     User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-21",province='山东省',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
#     User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-21",province='山东省',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
#     User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-21",province='山东省',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
#     User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-13",province='山东省',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
#     User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-13",province='山东省',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
#     User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-13",province='山东省',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
#     User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-13",province='山东省',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
#     User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-13",province='山东省',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
#     User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='山东省',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
#     User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='山东省',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
#     User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='山东省',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='北京',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='北京',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='北京',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='天津',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='天津',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='上海',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='上海',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='上海',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='重庆',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='重庆',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='河北',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='河北',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='河北',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='河北',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='河北',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='河南',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='河南',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='云南',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='云南',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='云南',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='辽宁',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='辽宁',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='湖南',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='湖南',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='安徽',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='安徽',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='安徽',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='新疆',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='新疆',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='新疆',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='新疆',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='新疆',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='江苏',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='江苏',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='浙江',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='浙江',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='浙江',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='江西',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='江西',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='江西',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='江西',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='湖北',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='湖北',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='广西',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='甘肃',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='甘肃',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='山西',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='陕西',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='吉林',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='吉林',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='吉林',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='福建',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='福建',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='广州',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='广州',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='广东',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='广东',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='广东',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='广东',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='青海',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='青海',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='青海',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='西藏',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='西藏',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='四川',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='四川',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='宁夏',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='宁夏',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='宁夏',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='宁夏',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='宁夏',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='宁夏',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='宁夏',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='海南',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='海南',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='海南',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='海南',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='海南',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='海南',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='台湾',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='台湾',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='台湾',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='台湾',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='台湾',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='台湾',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='台湾',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='香港',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='香港',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='香港',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='香港',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='香港',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='澳门',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='澳门',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='澳门',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='澳门',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='澳门',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
    User.objects.create(username='zz',password='123456',phone='11111111111',sex='男',create_time="2020-2-1",province='新疆',addr='山东省青岛市城阳区红岛街道',rank="大师",status=0,pic='pic',sinature='这个人很懒,什么都没有留下')
# #
add()

# d = datetime.datetime.now()
# d1 = datetime.timedelta(days=7)
# res = (d-d1).strftime("%Y-%m-%d")
#
# u = User.objects.filter(create_time__gt=res)
# print(u)