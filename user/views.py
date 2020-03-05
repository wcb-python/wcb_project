import random
import re
import string

from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from redis import Redis

from tools.yunpian import YunPian
# Create your views here.

def get_redis_conn():
    return Redis(host=settings.HOST, port=settings.PORT)

def login(request):
    return render(request, "user/login.html")

def send_code(request):
    '''
    获取到手机号,判断手机号是否符合规则:
    符合:
        再进行进行判断此手机号在60s内是否已经获取过验证码
        获取过:返回空
        没获取:获取随机验证码,发送到对应手机,且将此验证码存入到redis中,设置有效期
    不符合:
        返回手机号不符合规则
    :param request:
    :return:
    '''
    phone = request.POST.get("phone")
    pattern = re.compile("^1[3456789]\d{9}$")
    result = pattern.findall(phone)
    if result:
        red = get_redis_conn()
        try:
            res = red.get(phone)
        except:
            res=""
        print('res',res)
        if res:
            return JsonResponse(data={"msg":"不可频繁发送验证码"},safe=False)
        else:
            code = "".join(random.sample(string.digits,4))
            print(code)
            y = YunPian(settings.APIKEY)
            res = y.send_message(code,phone)
            if "200" in res:
                red.setex(phone,120,code)
                return JsonResponse(data={"msg":"ok"},safe=False)
            else:
                red.setex(phone, 120, code)
                return JsonResponse(data={"msg": "您不可频繁发送验证码,请一小时后再进行操作"}, safe=False)
    else:
        return JsonResponse(data={"msg":'手机号不符合规范'},safe=False)

def loginlogic(request):
    # 获取手机号进行格式判断
    # 不正确:
        # 返回错误信息
    # 正确:
    #     再进行判断验证码是否还存在,没有过期
        # 过期了:返回错误信息
        # 没过期:进行判断验证码是否正确
        #     不正确:返回错误欣喜
        #    正确:跳转到首页
    phone = request.POST.get("phone")
    code = request.POST.get("code")
    print(phone)
    pattern = re.compile("^1[3456789]\d{9}$")
    result = pattern.findall(phone)
    if result:
        red = get_redis_conn()
        try:
            res = red.get(phone).decode()
        except:
            res = ""
        if res:
            if res== code:
                # 登陆之后,保存登录状态
                request.session['login']='ok'
                return redirect('manage_system:show_manage')
            else:
                return HttpResponse('验证码错误')
        else:
            return HttpResponse('验证码已过期')
    else:
        return HttpResponse('手机号不符合规范')