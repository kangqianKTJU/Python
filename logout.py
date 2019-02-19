import requests

post_addr="http://202.113.5.133/srun_portal_pc_succeed.php"

post_header={
 'Host': '202.113.5.133',
 'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0',
 'Accept': '*/*',
 'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
 'Accept-Encoding': 'gzip, deflate',
 'Content-Type': 'application/x-www-form-urlencoded',
 'X-Requested-With':'XMLHttpRequest',
 'Referer':'http://202.113.5.133/srun_portal_pc_succeed.php',
 'Connection':'keep-alive',
}


form_data=[
    ('action','auto_logout'),
#    ('user_ip','172.23.116.27'),
#    ('nas_ip','172.23.0.1'),
#    ('user_mac','30:85:A9:9b:46:25'),
 ]

z=requests.post(post_addr,data=form_data,headers=post_header)
print(z)
print("ok")
input("按任意键结束")
