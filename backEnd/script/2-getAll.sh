#!/bin/bash

# 进入test-network
cd /Users/lzh/Documents/workSpace/vscode/go/fabric-2.4.9/fabric-samples/test-network

# 配置peer环境变量
export PATH=${PWD}/../bin:$PATH
# 配置config环境变量
export FABRIC_CFG_PATH=$PWD/../config/

# 配置环境变量，使Org1做为peer操作者
# Environment variables for Org1
export CORE_PEER_TLS_ENABLED=true
export CORE_PEER_LOCALMSPID="Org1MSP"
export CORE_PEER_TLS_ROOTCERT_FILE=${PWD}/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt
export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org1.example.com/users/Admin@org1.example.com/msp
export CORE_PEER_ADDRESS=localhost:7051

# 启动链码调用GetAllAssets函数查询全部资产信息
peer chaincode query -C mychannel -n basic -c '{"Args":["GetAllAssets"]}'
