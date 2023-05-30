from django.http import HttpResponse, JsonResponse, Http404
# from .models import User, Diary
from django.forms.models import model_to_dict
from django.shortcuts import render
from sqlcommon.models import Customer


# 先定义好HTML模板
html_template = '''
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
table {
    border-collapse: collapse;
}
th, td {
    padding: 8px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}
</style>
</head>
    <body>
        <table>
        <tr>
        <th>id</th>
        <th>姓名</th>
        <th>电话号码</th>
        <th>地址</th>
        <th>QQ<th>
        </tr>

        %s


        </table>
    </body>
</html>
'''

# 接收请求数据返回字符串响应。http://127.0.0.1:8000/app1/
def listcustomers(request):

    # 每条表记录都是是一个dict对象，
    # key 是字段名，value 是 字段值
    # 定义返回字符串
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    qs = Customer.objects.values()
    # 检查url中是否有参数phonenumber
    ph = request.GET.get('phonenumber', None)
    # 如果有，添加过滤条件
    if ph:
        qs = qs.filter(phonenumber=ph)

    tableContent = ''
    for customer in qs:
        tableContent += '<tr>'
        for name, value in customer.items():
            tableContent += f'<td>{value}</td>'

        # <br> 表示换行
        tableContent += '<br>'

    return HttpResponse(html_template%tableContent)

# # 返回字典或json字符串
# def finduser(request):
#     try:
#         userid = request.GET.get("userid", None)  # 读取数据
#         users = User.objects.filter(id=userid)  # 获取一个用户，返回QuerySet
#         user = users[0]  # 获取第一个user对象
#         user_dict1 = model_to_dict(user)  # 将对象转化为字典
#         return JsonResponse(user_dict1)  # 返回前端字典
#     except:
#         raise Http404("用户不存在")

