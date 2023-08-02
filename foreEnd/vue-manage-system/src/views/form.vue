<template>
    <div class="container">
        <div class="form-box">
            <el-form ref="formRef" :rules="rules" :model="form" label-width="80px">
                <el-form-item label="应用选择" prop="options">
                    <el-cascader :options="options" v-model="form.options"></el-cascader>
                </el-form-item>
                <el-form-item label="操作类型" prop="region">
                    <el-select v-model="form.region" placeholder="请选择">
                        <el-option key="绑定" label="绑定" value="绑定"></el-option>
                        <el-option key="解绑" label="解绑" value="解绑"></el-option>
                        <el-option key="换绑" label="换绑" value="换绑"></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item v-if="form.region === '解绑' || form.region === '换绑'" label="原有账号" prop="former">
                    <el-input v-model="form.former"></el-input>
                </el-form-item>
                <el-form-item v-if="form.region === '绑定' || form.region === '换绑'" label="新的账号" prop="later">
                    <el-input v-model="form.later"></el-input>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="onSubmit(formRef)">提交</el-button>
                    <el-button @click="onReset(formRef)">重置</el-button>
                </el-form-item>
            </el-form>
        </div>
    </div>
</template>

<script setup lang="ts" name="baseform">
import { reactive, ref } from 'vue';
import { ElMessage } from 'element-plus';
import type { FormInstance, FormRules } from 'element-plus';

const options = [
    {
        value: 'tencent',
        label: '腾讯',
        children: [
            {
                value: 'wechat',
                label: '微信',
            },
            {
                value: 'qq',
                label: 'QQ',
            },
        ],
    },
    {
        value: 'sina',
        label: '新浪',
        children: [
            {
                value: 'weibo',
                label: '微博',
            },
        ],
    },
    {
        value: 'bytedance',
        label: '字节跳动',
        children: [
            {
                value: 'tiktok',
                label: '抖音',
            },
        ],
    },
];
const rules: FormRules = {
    former: [{ required: true, message: '请输入原有账号', trigger: 'blur' }],
    later: [{ required: true, message: '请输入新的账号', trigger: 'blur' }],
};
const formRef = ref<FormInstance>();
const form = reactive({
    region: '',
    delivery: true,
    options: [],
    former: '',
    later: '',
});
// 提交
const onSubmit = (formEl: FormInstance | undefined) => {
    // 表单校验
    if (!formEl) return;
    formEl.validate((valid) => {
        if (valid) {
            console.log(form);
            ElMessage.success('提交成功！');
        } else {
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
