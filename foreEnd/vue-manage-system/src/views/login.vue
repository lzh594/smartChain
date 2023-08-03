<template>
    <div class="login-wrap">
        <div class="ms-login">
            <div class="ms-title">跨应用账号管理系统</div>
            <el-form :model="param" :rules="rules" ref="login" label-width="0px" class="ms-content">
                <el-form-item prop="username" class="form-item">
                    <el-divider content-position="center" font-size="30px">请输入用户名和密码</el-divider>
                    <el-input v-model="param.username" placeholder="username" class="input-field">
                        <template #prepend>
                            <el-button icon="User" disabled></el-button>
                        </template>
                    </el-input>
                </el-form-item>
                <el-form-item prop="password" class="form-item">
                    <el-input
                        type=text
                        show-password
                        placeholder="password"
                        v-model="param.password"
                        @keyup.enter="submitForm(login)"
                        class="input-field"
                    >
                        <template #prepend>
                            <el-button icon="Lock" disabled></el-button>
                        </template>
                    </el-input>
                </el-form-item>
                <el-divider content-position="center">请选择身份</el-divider>
                <el-form-item class="form-item">
                    <el-radio-group v-model="param.identity" size="big" class="identity-group" align="center">
                        <el-radio label="用户" border size="large" align="center">用户
                        </el-radio>
<!--                        <el-divider direction="vertical"></el-divider>-->
                        <el-radio label="运营商" border size="large" >运营商</el-radio>
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
            </el-form>
            <p class="login-tips">Tips : 请正确填写用户名和密码，并选择你的身份。</p>
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
    margin-left: 40px;
    height: 60px; /* adjust as needed */
    width: 400px;
}

.identity-group /deep/ {
    display: block;
    font-size: 25px;
    font-weight: bold;
    justify-content: center;
    margin-left: 140px;
    margin-top: 10px;
    margin-bottom: 10px;
}

.login-button {
    font-size: 24px; /* adjust as needed */
}

.login-wrap {
    position: absolute;
    width: 100%;
    height: 100%;
    background-image: url(../assets/img/login-bg.jpg);
    background-position: center center;
    background-size: 100%;
}

.ms-title {
    width: 100%;
    line-height: 80px;
    text-align: center;
    font-size: 36px;
    font-weight: bold;
    color:dodgerblue;
    border-bottom: 2px solid grey;
}

.ms-login {
    position: relative;
    text-align: center;
    left: 43%;
    top: 40%;
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
    width: 50%;
    height: 40px;
    margin-top: 10px;
    margin-bottom: 20px;
}

.login-tips {
    font-size: 18px;
    margin-bottom: 20px;
    color: #000;
}

</style>
