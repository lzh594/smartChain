<template>
    <div>
        <el-row :gutter="20">
            <el-col :span="8">
                <el-card shadow="hover" class="mgb20" style="height: 252px">
                    <div class="user-info">
                        <el-avatar v-if="identity==='1'" class="user-avator" :size="30" :src="userImg"/>
                        <el-avatar v-else class="user-avator" :size="120" :src="orgImg"/>
                        <div class="user-info-cont">
                            <div class="user-info-name">{{ username }}</div>
                            <div>{{ role }}</div>
                        </div>
                    </div>
                    <div class="user-info-list">
                        上次登录时间：
                        <span>2023-08-02</span>
                    </div>
                    <div class="user-info-list">
                        上次登录地点：
                        <span>北京</span>
                    </div>
                </el-card>
                <el-row :gutter="20" class="mgb20">
                    <el-col :span="12">
                        <el-card shadow="hover">
                            <div class="grid-content grid-con-1">
                                <el-icon class="grid-con-icon">
                                    <User/>
                                </el-icon>
                                <div class="grid-cont-right">
                                    <div class="grid-num">39</div>
                                    <div>用户访问量</div>
                                </div>
                            </div>
                        </el-card>
                    </el-col>
                    <el-col :span="12">
                        <el-card shadow="hover">
                            <div class="grid-content grid-con-2">
                                <el-icon class="grid-con-icon">
                                    <ChatDotRound/>
                                </el-icon>
                                <div class="grid-cont-right">
                                    <div class="grid-num">21</div>
                                    <div>系统消息</div>
                                </div>
                            </div>
                        </el-card>
                    </el-col>
                    <el-col :span="12">
                        <el-card shadow="hover">
                            <div class="grid-content grid-con-3">
                                <el-icon class="grid-con-icon">
                                    <Goods/>
                                </el-icon>
                                <div class="grid-cont-right">
                                    <div class="grid-num">50</div>
                                    <div>厂商数量</div>
                                </div>
                            </div>
                        </el-card>
                    </el-col>
                    <el-col :span="12">
                        <el-card shadow="hover">
                            <div class="grid-content grid-con-4">
                                <el-icon class="grid-con-icon">
                                    <Calendar/>
                                </el-icon>
                                <div class="grid-cont-right">
                                    <div class="grid-num">25</div>
                                    <div>已绑定账号</div>
                                </div>
                            </div>
                        </el-card>
                    </el-col>
                </el-row>
            </el-col>
            <el-col :span="16">
                <el-card shadow="hover" style="height: 600px">
                    <template #header>
                        <div class="function">
                            <span>功能介绍</span>
                        </div>
                    </template>
                    <div class="intro" style="line-height: 60px;">
                        <span>本系统基于Web3.0的思想，是一个以联盟链为基础的跨应用的账号管理系统。</span>
                        <br>
                        <span>本系统旨在便于用户直接管理自己的账号信息，解决了统一认证存在的安全、效率等方面的问题。</span>
                    </div>
                    <div class="character">
                        <span>本系统具有以下特点：</span>
                    </div>
                    <div class="chara1" style="line-height: 60px;">
                        <span>——跨应用的账号管理：跨越应用平台限制，一键管理所有账号。</span>
                    </div>
                    <div class="chara2" style="line-height: 60px;">
                        <span>——兼顾隐私与安全：使用多项国密技术，提供安全隐私保护。</span>
                    </div>
                    <div class="chara3" style="line-height: 60px;">
                        <span>——项目技术高度先进：采用异步Dory共识，方案具备性能优势。</span>
                    </div>
                    <div class="advertise"
                         style="line-height: 60px; text-align: center; font-family: '华文行楷',serif;">
                        <span>应用账号？告别依赖平台，实现自主管理！</span>
                    </div>
                </el-card>
            </el-col>
        </el-row>
    </div>
</template>

<script setup lang="ts" name="dashboard">
import imgurl from './../assets/img/user.jpg';
import {Calendar, ChatDotRound, Goods} from "@element-plus/icons-vue";
import userImg from "../assets/img/user.jpg";
import orgImg from "../assets/img/org.jpg";

const identity = localStorage.getItem('ms_identity');
const username = localStorage.getItem('ms_username');
const role: string = identity === '0' ? '运营商' : '普通用户';


</script>

<style scoped>

.user-info {
    display: flex;
    align-items: center;
    padding-bottom: 20px;
    border-bottom: 2px solid #ccc;
    margin-bottom: 20px;
}

.user-info-cont {
    padding-left: 50px;
    flex: 1;
    font-size: 14px;
    color: #999;
}

.user-info-cont div:first-child {
    font-size: 30px;
    color: #222;
}

.user-info-list {
    font-size: 14px;
    color: #999;
    line-height: 25px;
}

.user-info-list span {
    margin-left: 70px;
}

.mgb20 {
    margin-bottom: 20px;
}

.function {
    font-size: 28px;
    font-weight: bold;
    text-align: center;
}

.intro {
    font-size: 20px;
    line-height: 80px;
    font-family: 宋体, serif;
}

.character {
    font-size: 24px;
    line-height: 100px;
    color: black;
    font-family: 方正小标宋简体, serif;
}

.chara1 {
    font-size: 24px;
    line-height: 100px;
    color: chocolate;
    font-family: 楷体, serif;
}

.chara2 {
    font-size: 24px;
    line-height: 100px;
    color: blueviolet;
    font-family: 楷体, serif;
}

.chara3 {
    font-size: 24px;
    line-height: 100px;
    color: indigo;
    font-family: 楷体, serif;
}

.advertise {
    font-size: 30px;
    font-weight: bold;
    text-align: center;
    font-family: "华文行楷", serif;
    color: olivedrab;
}

.grid-content {
    display: flex;
    align-items: center;
    height: 100px;
}

.grid-cont-right {
    flex: 1;
    text-align: center;
    font-size: 14px;
    color: #999;
}

.grid-num {
    font-size: 30px;
    font-weight: bold;
}

.grid-con-icon {
    font-size: 50px;
    width: 100px;
    height: 100px;
    text-align: center;
    line-height: 100px;
    color: #fff;
}

.grid-con-1 .grid-con-icon {
    background: rgb(45, 140, 240);
}

.grid-con-1 .grid-num {
    color: rgb(45, 140, 240);
}

.grid-con-2 .grid-con-icon {
    background: rgb(100, 213, 114);
}

.grid-con-2 .grid-num {
    color: rgb(100, 213, 114);
}

.grid-con-3 .grid-con-icon {
    background: rgb(242, 94, 67);
}

.grid-con-3 .grid-num {
    color: rgb(242, 94, 67);
}

.grid-con-4 .grid-con-icon {
    background: rgb(250, 200, 25);
}

.grid-con-4 .grid-num {
    color: rgb(250, 200, 25);
}
</style>