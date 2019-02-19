import requests

username = input("用户名：")
password = input("密码：")
ac_id = input("台式机请输入：25\r\n笔记本等其他设备输入:13\r\n:")

post_addr="http://202.113.5.133/include/auth_action.php"

post_header={
 'Host': '202.113.5.133',
 'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0',
 'Accept': '*/*',
 'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
 'Accept-Encoding': 'gzip, deflate',
 'Content-Type': 'application/x-www-form-urlencoded',
 'X-Requested-With':'XMLHttpRequest',
 'Referer':'http://202.113.5.133/srun_portal_pc.php?wlanuserip=&wlanacname=&ac_id=' + repr(ac_id),
 'Connection':'keep-alive',
}


form_data=[
    ('action','login'),
    ('username',username),
    ('password',password),
    ('ac_id',ac_id),
#    ('user_ip','172.23.116.27'),
#    ('nas_ip','172.23.0.1'),
#    ('user_mac','30:85:A9:9b:46:25'),
    ('save_me','1'),
    ('ajax','1'),
 ]

z=requests.post(post_addr,data=form_data,headers=post_header)
print(z)
if 'login_ok' in z.text:
    print("登陆成功！")
else:
    print("登陆失败！")

input("按任意键结束")
