import datetime

from django.core.paginator import Paginator
from django.db.models import Count
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt

from manage_system.models import User

def show_manage(request):
   login = request.session.get('login')
   print('login',login)
   return render(request, 'manage_system/持明法洲管理界面.html',{"login":login})


@cache_page(timeout=10,key_prefix="cacheRedis")    # timeout 缓存时效(秒)
def show_userlist(request):
    '''
    用户信息列表,展示每页的用户信息
    :param request:
    :return:
    '''
    '''
    接收rows(每页展示的用户条数),page(第几页)
    构建分页器,得到分页对象
    根据数据格式,构造data
    返回
    '''
    def mydefault(u):
        if isinstance(u,User):
            return {"id":u.id,"username":u.username,"phone":u.phone,"sex":u.sex,"create_time":str(u.create_time),"province":u.province,"addr":u.addr,"rank":u.rank,"status":(lambda x:"激活" if x==1 else "冻结")(u.status),"pic":str(u.pic)}
    rows = request.GET.get('rows')
    page_num = request.GET.get("page")
    pagtor = Paginator(User.objects.all(),rows)
    page = pagtor.page(page_num)
    data = {
        "page":page_num,
        "total":pagtor.num_pages,
        "records":pagtor.count,
        "rows":list(page)
    }
    return JsonResponse(data=data,safe=False,json_dumps_params={"default":mydefault})

@csrf_exempt
def update(request):
    id = request.POST.get('id')
    status = request.POST.get('status')
    u = User.objects.get(id=id)
    u.status = int(status)
    u.save()
    return HttpResponse('ok')

@csrf_exempt
@cache_page(timeout=10,key_prefix="cacheRedis")    # timeout 缓存时效(秒)
def bar_list(request):
    u = User.objects.values("province").annotate(Count('province'))
    print('分组查询结果',u)
    res = []
    now = datetime.datetime.now()
    for i in range(7,36,7):
        delta = datetime.timedelta(days=i)
        delta1 = datetime.timedelta(days=i-7)
        count = len(list(User.objects.filter(create_time__gt=(now - delta).strftime("%Y-%m-%d"), create_time__lte=(now - delta1).strftime("%Y-%m-%d"))))
        res.append(count)
    else:
        count = len(list(User.objects.filter(create_time__gt=(now - datetime.timedelta(days=35)).strftime("%Y-%m-%d"))))
        res.append(count)
    return JsonResponse(data={"result":res})

@cache_page(timeout=10,key_prefix="cacheRedis")    # timeout 缓存时效(秒)
def map_data(request):
    data = []
    u = list(User.objects.values("province").annotate(Count('province')))
    for i in range(len(u)):
        print('分组查询结果', u[i]["province"])
        print('分组查询结果', u[i]["province__count"])
        data.append({"name":u[i]["province"],"value":u[i]["province__count"]})
    return JsonResponse(data={"result":data})

