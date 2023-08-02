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

# 测试样例
# ./sh/4-create.sh id phone org app op
# ./sh/4-create.sh hashid 158xxxx0701 org2 timi signup pending time 
var="{\"function\":\"CreateAsset\",\"Args\":[\"$1\",\"$2\",\"$3\",\"$4\",\"$5\",\"$6\",\"$7\"]}"
echo $var
# 启动链码调用CreateAsset，创建一条新的资产信息（phone,superior,app,op）
peer chaincode invoke -o localhost:7050 --ordererTLSHostnameOverride orderer.example.com --tls --cafile "${PWD}/organizations/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem" -C mychannel -n basic --peerAddresses localhost:7051 --tlsRootCertFiles "${PWD}/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt" --peerAddresses localhost:9051 --tlsRootCertFiles "${PWD}/organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt" -c $var
