#!/bin/bash

# 进入test-work目录
cd ./../../blockChain/fabric-samples/test-network

# 开启区块链网络并创建通道
./network.sh down
./network.sh up
./network.sh createChannel

