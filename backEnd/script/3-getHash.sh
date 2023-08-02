#!/bin/bash

# 计算hash
echo -n $1 | gmssl sm3 -bin > hash.sm3
# base64表示
base64 -i hash.sm3
# 删除中间文件
rm hash.sm3