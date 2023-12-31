import time

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from .models import UsrData, History
from .ssh import *


# Create your views here.
def index(request):
    # return render(request, 'index.html')
    return JsonResponse({"para1": "Test"})


# 检查是否需要覆写
def check(data, t, state="pending"):
    # 计算hash值，得到id
    cmd = " ".join([data["Phone"], data["Superior"], data["App"], data["Op"], state, t])
    hashid = command_SSH(x_sh['getHash'] + f' \"{cmd}\"')
    # 查询是否存在旧数据
    d = UsrData.objects.filter(Phone=data["Phone"], App=data["App"])
    if len(d):
        if d[0].Op == data["Op"] and state == "pending":
            return 0
        cmd = " " + d[0].HashID
        command_SSH(x_sh['delete'] + cmd)
        # 创建新资产
        cmd = " " + " ".join([hashid, data['Phone'], data["Superior"], data["App"], data["Op"], state, f"\"{t}\""])
        command_SSH(x_sh['create'] + cmd)
        return 1
    # 创建新资产
    cmd = " " + " ".join([hashid, data['Phone'], data["Superior"], data["App"], data["Op"], state, f"\"{t}\""])
    command_SSH(x_sh['create'] + cmd)
    return 2


# 从fabric上更新数据到usrdata
def update():
    # 获取所有最新数据
    data_all = command_SSH(x_sh['getAll'])
    # 删除全部数据
    UsrData.objects.all().delete()
    # 将新数据加入数据库中
    for d in data_all:
        UsrData.objects.create(HashID=d["HashID"], Phone=d['Phone'], Superior=d['Superior'], App=d['App'], Op=d['Op'],
                               State=d['State'], TimeStamp=d["TimeStamp"])


@require_http_methods(['GET', 'POST'])
# 提交数据到fabric
def create(request):
    data = request.GET if request.method == "GET" else request.POST
    t = time.asctime().replace("  ", " ").replace(" ", "-")
    # 更新fabric数据端
    x, value = check(data, t), True
    if x == 2:
        s = "用户提交新申请，操作成功"
        # 将数据写入历史记录
        _ = History.objects.create(Phone=data['Phone'], Superior=data['Superior'], App=data['App'], Op=data['Op'],
                                   TimeStamp=t)
    elif x == 1:
        s = "检测到已有操作申请，修改成功"
        # 将数据写入历史记录
        _ = History.objects.create(Phone=data['Phone'], Superior=data['Superior'], App=data['App'], Op=data['Op'],
                                   TimeStamp=t)
    elif x == 0:
        s = "重复提交申请，操作失败"
        value = False
    else:
        s = "Error"
    return get_all(request)


# 换绑请求
@require_http_methods(['GET', 'POST'])
def change(request):
    data = request.GET if request.method == "GET" else request.POST
    t = time.asctime().replace("  ", " ").replace(" ", "-")
    d = UsrData.objects.filter(Phone=data["OldPhone"], App=data["App"])
    if len(d):
        # 删除旧注册
        cmd = " " + d[0].HashID
        command_SSH(x_sh['delete'] + cmd)
        # 计算hash值，得到id
        cmd = " ".join([data["Phone"], data["Superior"], data["App"], "change", "pending", t])
        hashid = command_SSH(x_sh['getHash'] + f' \"{cmd}\"')
        # 创建新资产
        cmd = " " + " ".join([hashid, data['Phone'], data["Superior"], data["App"], "change", "pending", f"\"{t}\""])
        command_SSH(x_sh['create'] + cmd)
        _ = History.objects.create(Phone=data['OldPhone'], Superior=data['Superior'], App=data['App'], Op="change",
                                   TimeStamp=t)
    return get_all(request)


# 查询特定手机号数据
@require_http_methods(['GET', 'POST'])
def query(request):
    # 更新数据库
    update()
    data = request.GET if request.method == "GET" else request.POST
    all_data = UsrData.objects.filter(Phone=data['Phone'], State="success").exclude(Op="cancel")
    query_data, cnt = {"list": [], "pageTotal": 0}, 0
    for q in all_data:
        query_data["list"].append({"id": cnt + 1, "HashID": q.HashID, "Phone": data["Phone"], "Superior": q.Superior,
                                   "App": q.App, "Op": q.Op, "State": "success", "TimeStamp": q.TimeStamp})
        cnt += 1
    query_data["pageTotal"] = cnt
    return JsonResponse(query_data)


# 查询某(Phone)历史记录
@require_http_methods(['GET', 'POST'])
def get_history(request):
    data = request.GET if request.method == "GET" else request.POST
    # 查询出相关历史记录
    aim = History.objects.filter(Phone=data['Phone'])
    history_data = {"list": [], "pageTotal": 0}
    cnt = 0
    for i in aim:
        history_data["list"].append(
            {"id": cnt + 1, "Phone": data['Phone'], "Superior": i.Superior, "App": i.App, "Op": i.Op,
             "TimeStamp": i.TimeStamp})
        cnt += 1
    history_data["pageTotal"] = cnt
    return JsonResponse(history_data)


# 删除历史记录
@require_http_methods(['GET', 'POST'])
def clear_history(request):
    History.objects.all().delete()
    return get_history(request)


"""
厂商操作
"""


# 查询数据库(Usrdata)所有数据
@require_http_methods(['GET', 'POST'])
def get_all(request):
    # 先对数据库进行更新
    update()
    all_data = UsrData.objects.all()
    usrdata = {"list": [], "pageTotal": 0}
    cnt = 0
    for e in all_data:
        usrdata["list"].append(
            {"id": cnt + 1, "HashID": e.HashID, "Phone": e.Phone, "Superior": e.Superior, "App": e.App, "Op": e.Op,
             "State": e.State, "TimeStamp": e.TimeStamp})
        cnt += 1
    usrdata["pageTotal"] = cnt
    return JsonResponse(usrdata)


# 运营商编辑操作
@require_http_methods(['GET', 'POST'])
def edit(request):
    data = request.GET if request.method == "GET" else request.POST
    t = time.asctime().replace("  ", " ").replace(" ", "-")

    # 查询是否存在旧数据
    d = UsrData.objects.filter(Phone=data["Phone"], App=data["App"])
    if len(d):
        # 删除旧数据
        cmd = " " + d[0].HashID
        command_SSH(x_sh['delete'] + cmd)
        # 计算hash值，得到id
        cmd = " ".join([data["Phone"], data["Superior"], data["App"], data["Op"], data["State"], t])
        hashid = command_SSH(x_sh['getHash'] + f' \"{cmd}\"')
        # 创建新资产
        cmd = " " + " ".join([hashid, data['Phone'], data["Superior"], data["App"], data["Op"], data["State"], f"\"{t}\""])
        command_SSH(x_sh['create'] + cmd)
    return get_all(request)
