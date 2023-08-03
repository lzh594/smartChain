<template>
    <div class="container">
        <div class="form-box">
            <el-form ref="formRef"
                     :rules="rules"
                     :model="form"
                     label-width="100px"
                     size="large"
                     label-position="top">
                <el-form-item label="运营商选择" prop="Superior">
                    <el-select v-model="form.Superior"
                               placeholder="运营商"
                               class="handle-select mr10"
                               clearable
                               @clear="form.Superior=''"
                    >
                        <el-option key="1" label="阿里巴巴" value="Alibaba" align="center"></el-option>
                        <el-option key="2" label="米哈游" value="Mihoyo" align="center"></el-option>
                        <el-option key="3" label="字节跳动" value="ByteDance" align="center"></el-option>
                        <el-option key="4" label="腾讯" value="Tencent" align="center"></el-option>
                        <el-option key="5" label="网易" value="NetEase" align="center"></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="应用选择" prop="App">
                    <el-select v-model="form.App"
                               placeholder="应用"
                               clearable
                               @clear="form.App=''"
                               class="handle-select mr10"
                    >
                        <el-option-group label="腾讯">
                            <el-option key="1" label="微信" value="weixin"></el-option>
                            <el-option key="2" label="QQ" value="QQ"></el-option>
                        </el-option-group>
                        <el-option-group label="阿里巴巴">
                            <el-option key="3" label="淘宝" value="taobao"></el-option>
                            <el-option key="4" label="支付宝" value="Alipay"></el-option>
                        </el-option-group>
                        <el-option-group label="网易">
                            <el-option key="5" label="网易云音乐" value="Musics"></el-option>
                        </el-option-group>
                        <el-option-group label="米哈游">
                            <el-option key="6" label="原神" value="Genshin"></el-option>
                        </el-option-group>
                        <el-option-group label="字节跳动">
                            <el-option key="7" label="抖音" value="Tiktok"></el-option>
                        </el-option-group>
                    </el-select>
                </el-form-item>
                <el-form-item label="操作类型" prop="Op">
                    <el-select v-model="form.Op"
                               class="handle-select mr10"
                               clearable
                               @clear="form.Op=''"
                               placeholder="请选择">
                        <el-option key="注册" label="注册" value="signup"></el-option>
                        <el-option key="变更" label="变更" value="change"></el-option>
                        <el-option key="注销" label="注销" value="cancel"></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item v-if="form.Op === 'cancel' || form.Op === 'change'" label="原有账号" prop="Former">
                    <el-input v-model="form.Former"></el-input>
                </el-form-item>
                <el-form-item v-if="form.Op === 'signup' || form.Op === 'change'" label="新的账号" prop="Later">
                    <el-input v-model="form.Later"></el-input>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="onSubmit(formRef)">提 交</el-button>
                    <el-button @click="onReset(formRef)">重 置</el-button>
                </el-form-item>
            </el-form>
        </div>
    </div>
</template>

<script setup lang="ts" name="baseform">
import {reactive, ref} from 'vue';
import {ElMessage} from 'element-plus';
import type {FormInstance, FormRules} from 'element-plus';
import {requestData} from "../api";

const rules: FormRules = {
    Superior: [{required: true, message: '请选择需要操作的运营商', trigger: 'blur'}],
    App: [{required: true, message: '请选择需要操作的应用', trigger: 'blur'}],
    Op: [{required: true, message: '请选择需要进行的操作', trigger: 'blur'}],
    Former: [{required: true, message: '请输入原有账号', trigger: 'blur'}],
    Later: [{required: true, message: '请输入新的账号', trigger: 'blur'}],
};

const formRef = ref<FormInstance>();
const form = reactive({
    Superior: '',
    Op: '',
    App: '',
    Former: '',
    Later: '',
});
const submit = reactive({
    Phone: '',
    OldPhone: '',
    Superior: '',
    App: '',
    Op: '',
})
const request = reactive({
    url: '',
    method: 'get',
    query: {}
})
const handleSubmit = () => {
    submit.Op = form.Op
    submit.Superior = form.Superior
    submit.App = form.App
    if (form.Op === 'signup') {
        submit.Phone = form.Later;
        createData()
    } else if (form.Op === 'change') {
        submit.Phone = form.Later;
        submit.OldPhone = form.Former;
        changeData()
    } else {
        submit.Phone = form.Former;
        createData()
    }
}
// 获取后台数据
const createData = () => {
    request.url = '/create';
    request.query = submit;
    requestData(request)!.then(res => {

    });
};
const changeData = () => {
    request.url = '/change';
    request.query = submit;
    requestData(request)!.then(res => {

    });
};

const optionClear=() =>{
    form.Former=''
    form.Superior=''
    form.App=''
    form.Later=''
    form.Op=''
    submit.Phone=''
    submit.Superior=''
    submit.App=''
    submit.OldPhone=''
    submit.Op=''
}
// 提交
const onSubmit = (formEl: FormInstance | undefined) => {
    // 表单校验
    if (!formEl) return;
    formEl.validate((valid) => {
        if (valid) {
            handleSubmit()
            console.log(form);
            ElMessage.success('提交成功！');
            optionClear()
        } else {
            ElMessage.error('出错啦！请重新提交！');
            return false;
        }
    });
};
// 重置
const onReset = (formEl: FormInstance | undefined) => {
    if (!formEl) return;
    formEl.resetFields();
};
</script>
<style scoped>
.handle-select {
    width: 300px;
}

</style>