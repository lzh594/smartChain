<template>
    <div class="login-wrap">
        <div class="ms-login">
            <div class="ms-title">跨应用账号管理系统</div>
            <el-form :model="param" :rules="rules" ref="login" label-width="0px" class="ms-content">
                <el-form-item prop="username" class="form-item">
                    <el-divider content-position="center" font-size="30px">请输入用户名和密码</el-divider>
                    <el-input v-model="param.username" placeholder="username" class="input-field">
                        <template #prepend>
                            <el-button icon="User" size="12px"></el-button>
                        </template>
                    </el-input>
                </el-form-item>
                <el-form-item prop="password" class="form-item">
                    <el-input
                        type="password"
                        placeholder="password"
                        v-model="param.password"
                        @keyup.enter="submitForm(login)"
                        class="input-field"
                    >
                        <template #prepend>
                            <el-button icon="Lock" size="16px"></el-button>
                        </template>
                    </el-input>
                </el-form-item>
                <el-divider content-position="center">请选择身份</el-divider>
                <el-form-item class="form-item">
                    <el-radio-group v-model="param.identity" size="big" class="identity-group" align="center">
                        <el-radio-button label="用户" border size="large" align="center">用户
                        </el-radio-button>
                        <el-divider direction="vertical"></el-divider>
                        <el-radio-button label="运营商" border size="large" >运营商</el-radio-button>
                    </el-radio-group>
                    <!--      <el-row>-->
                    <!--          <el-button round>圆角按钮</el-button>-->
                    <!--          <el-button type="primary" round>主要按钮</el-button>-->
                    <!--          <el-button type="success" round>成功按钮</el-button>-->
                    <!--          <el-button type="info" round>信息按钮</el-button>-->
                    <!--          <el-button type="warning" round>警告按钮</el-button>-->
                    <!--          <el-button type="danger" round>危险按钮</el-button>-->
                    <!--      </el-row>-->
                </el-form-item>
                <div class="login-btn">
                    <el-button round type="primary" @click="submitForm(login)" class="login-button">登 录</el-button>
                </div>
                <p class="login-tips">Tips : 请正确填写用户名和密码，并选择你的身份。</p>
            </el-form>
        </div>
    </div>
</template>

<script setup lang="ts">
import {ref, reactive} from 'vue';
import {useTagsStore} from '../store/tags';
import {usePermissStore} from '../store/permiss';
import {useRouter} from 'vue-router';
import {ElMessage} from 'element-plus';
import type {FormInstance, FormRules} from 'element-plus';
import {Lock, User} from '@element-plus/icons-vue';
import user from "./user.vue";


interface LoginInfo {
    username: string;
    password: string;
    identity: string;
}

const router = useRouter();
const param = reactive<LoginInfo>({
    username: '',
    password: '',
    identity: '用户'
});

const rules: FormRules = {
    username: [
        {
            required: true,
            message: '请输入用户名',
            trigger: 'blur'
        }
    ],
    password: [{required: true, message: '请输入密码', trigger: 'blur'}],
    identity: [{required: true, message: '请选择身份', trigger: 'blur'}]
};
const permiss = usePermissStore();
const login = ref<FormInstance>();
const submitForm = (formEl: FormInstance | undefined) => {
    if (!formEl) return;
    formEl.validate((valid: boolean) => {
        if (valid) {
            ElMessage.success('登录成功');
            localStorage.setItem('ms_username', param.username);
            const keys = permiss.defaultList[param.identity == '用户' ? 'admin' : 'user'];
            permiss.handleSet(keys);
            localStorage.setItem('ms_keys', JSON.stringify(keys));
            // window.userIdentity = param.identity === '用户' ? 1 : 0;
            localStorage.setItem('ms_identity', param.identity === '用户' ? '1' : '0');
            router.push('/');
        } else {
            ElMessage.error('登录失败');
            return false;
        }
    });
};

const tags = useTagsStore();
tags.clearTags();
</script>

<style scoped>
.form-item {
    font-size: 40px; /* adjust as needed */
}

.input-field {
    height: 50px; /* adjust as needed */
}

.identity-group /deep/ {
    display: block;
    font-size: 25px;
    font-weight: bold;
    justify-content: center;
    margin-left: 165px;
}

.login-button {
    font-size: 22px; /* adjust as needed */
}

.login-wrap {
    position: relative;
    width: 100%;
    height: 100%;
    background-image: url(../assets/img/login-bg.jpg);
    background-size: 100%;
}

.ms-title {
    width: 100%;
    line-height: 50px;
    text-align: center;
    font-size: 30px;
    color: midnightblue;
    border-bottom: 1px solid #18518d;
}

.ms-login {
    position: absolute;
    left: 43%;
    top: 45%;
    width: 600px;
    margin: -190px 0 0 -175px;
    border-radius: 5px;
    background: ghostwhite;
    overflow: hidden;
}

.ms-content {
    padding: 50px 60px;
}

.login-btn {
    font-size: 24px;
    text-align: center;
}

.login-btn button {
    width: 100%;
    height: 36px;
    margin-bottom: 20px;
}

.login-tips {
    font-size: 15px;
    line-height: 30px;
    color: #000;
}

</style>
