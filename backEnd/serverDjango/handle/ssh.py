# _*_ coding: utf-8 _*_
"""
Time:     2023/5/14 14:28
Author:   刘征昊(£·)
Version:  V 1.1
File:     ssh.py
Describe: 
"""
import ast

import paramiko

fabric_path = "/Users/lzh/Documents/workSpace/github/smartChain/backEnd/script"

# 脚本文件命令字典
x_sh = {
    "start": f"cd {fabric_path};./0-startNet.sh",
    "init": f"cd {fabric_path};./1-initLedger.sh",
    "getAll": f"cd {fabric_path};./2-getAll.sh",
    "getHash": f"cd {fabric_path};./3-getHash.sh",
    "create": f"cd {fabric_path};./4-create.sh",
    "delete": f"cd {fabric_path};./5-delete.sh",
    "end": f"cd {fabric_path};./6-endNet.sh",
}


def set_SSH():
    """
    设置SSH连接
    :return ssh:ssh对象
    """
    # 进行对paramiko方法下的SSHclient进行实例化
    ssh = paramiko.SSHClient()
    # 保存服务器密钥
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 输入服务器地址，账户名，密码
    ssh.connect(hostname='10.192.53.11', port=22, username='lzh', password='Lzh20020909~')
    return ssh


def command_SSH(command):
    """
    SSH调用fabric脚本文件
    :param command: 执行脚本文件所需命令
    :return out: 执行命令的返回值
    """
    myssh = set_SSH()
    # 导入环境变量（很重要）
    cmd = "source /etc/profile;source ~/.bash_profile;"
    cmd += command
    # 返回了三个数据，第一个是输入命令，第2个是命令返回的结果，第3个是命令错误时返回的结果
    stdin, stdout, stderr = myssh.exec_command(cmd)
    out = stdout.read().decode('utf-8').strip("\n")
    if command == x_sh["getAll"]:
        # getALl下的out返回值为字典的列表:[dict1,dict2,...]
        # read下的out返回值为字典dict
        out = ast.literal_eval(out)
    print(out)
    # 返回了当前的路径结果，如果错误则返回为空
    err = stderr.read().decode('utf-8')
    if err != "":
        print(err)
    # 返回错误的执行结果，如果正确则返回为空
    myssh.close()
    return out


def start_fabric():
    """
    启动并初始化fabric
    :return:
    """
    command_SSH(x_sh["start"])
    command_SSH(x_sh["init"])


if __name__ == "__main__":
    # start_fabric()
    # command_SSH(x_sh["start"])
    # command_SSH(x_sh["init"])
    # command_SSH(x_sh["getAll"])
    # command_SSH(x_sh["create"]+" asset5 158xxxx0701 org2 timi change error")
    # command_SSH(x_sh["delete"]+" asset5")
    command_SSH(x_sh["end"])

    # t1 = time.asctime().replace("  ", " ").replace(" ","-")
    # c = " ".join(["lzh20230603", "BUAA", "Genshin", "signup", "pending", t1])
    # # print(x_sh['getHash'] + f' \"{c}\"')
    # h = command_SSH(x_sh['getHash'] + f' \"{c}\"')
    # # print("h",h)
    # cmd1 = " " + " ".join([h, "lzh20230603", "BUAA", "Genshin", "signup", "pending", f"\"{t1}\""])
    # print(cmd1)
    # command_SSH(x_sh['create'] + cmd1)
