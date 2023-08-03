<template>
    <div>
        <div class="container">
            <div class="handle-box">
                <div style="margin-bottom: 20px">
                    <el-input v-model="searchQuery.Phone"
                              type="text"
                              placeholder="账号"
                              size="large"
                              @keyup.enter="phoneSearch"
                              clearable
                              @clear="phoneClear"
                              class="handle-input mr20"></el-input>
                    <el-button type="success" :icon="Search" @click="phoneSearch">搜索</el-button>
                    <span v-if="searchQuery.Phone.length===11" style="margin-left: 20px">
                        <el-button type="warning" :icon="RefreshLeft" @click="clearHistory">清空历史记录</el-button>
                    </span>
                </div>

                <el-select v-model="searchQuery.Superior"
                           placeholder="运营商"
                           clearable
                           @clear="searchQuery.Superior=''"
                           class="handle-select mr20">
                    <el-option key="1" label="Alibaba" value="Alibaba" align="center"></el-option>
                    <el-option key="2" label="Mihoyo" value="Mihoyo" align="center"></el-option>
                    <el-option key="3" label="ByteDance" value="ByteDance" align="center"></el-option>
                    <el-option key="4" label="Tencent" value="Tencent" align="center"></el-option>
                    <el-option key="5" label="NetEase" value="NetEase" align="center"></el-option>
                    <el-option key="6" label="buaa" value="buaa" align="center"></el-option>
                </el-select>
                <el-select v-model="searchQuery.App"
                           class="handle-select mr20"
                           clearable
                           placeholder="应用"
                           @clear="searchQuery.App=''">
                    <el-option-group label="Tencent">
                        <el-option key="1" label="weixin" value="weixin" align="center"></el-option>
                        <el-option key="2" label="QQ" value="QQ" align="center"></el-option>
                    </el-option-group>
                    <el-option-group label="Alibaba">
                        <el-option key="3" label="taobao" value="taobao" align="center"></el-option>
                        <el-option key="4" label="Alipay" value="Alipay" align="center"></el-option>
                    </el-option-group>
                    <el-option-group label="NetEase">
                        <el-option key="5" label="Musics" value="Musics" align="center"></el-option>
                    </el-option-group>
                    <el-option-group label="Mihoyo">
                        <el-option key="6" label="Genshin" value="Genshin" align="center"></el-option>
                    </el-option-group>
                    <el-option-group label="ByteDance">
                        <el-option key="7" label="Tiktok" value="Tiktok" align="center"></el-option>
                    </el-option-group>
                </el-select>
                <el-select v-model="searchQuery.Op"
                           placeholder="操作"
                           clearable
                           @clear="searchQuery.Op=''"
                           class="handle-select mr20">
                    <el-option key="1" label="注册" value="signup" align="center"></el-option>
                    <el-option key="2" label="变更" value="change" align="center"></el-option>
                    <el-option key="3" label="注销" value="cancel" align="center"></el-option>
                </el-select>

                <el-button type="primary" :icon="Search" @click="optionSearch">筛选</el-button>
                <el-button type="danger" :icon="Delete" @click="phoneSearch" round>清除</el-button>
            </div>

            <el-table :data="tableData" border class="table" ref="multipleTable" header-cell-class-name="table-header">
                <el-table-column prop="id" label="序号" width="55" align="center"></el-table-column>
                <el-table-column prop="Phone" label="账号" align="center"></el-table-column>
                <el-table-column prop="Superior" label="运营商" align="center"></el-table-column>
                <el-table-column prop="App" label="应用" align="center"></el-table-column>
                <el-table-column prop="Op" label="操作" align="center"></el-table-column>
                <el-table-column prop="TimeStamp" label="请求时间" width="250" align="center"></el-table-column>
            </el-table>
            <div class="pagination">
                <el-pagination
                    background
                    layout="total, prev, pager, next"
                    :current-page="query.pageIndex"
                    :page-size="query.pageSize"
                    :total="pageTotal"
                    @current-change="handlePageChange"
                ></el-pagination>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts" name="history">
import {ref, reactive} from 'vue';
import {Delete, Search, RefreshLeft} from '@element-plus/icons-vue';
import {requestData} from "../api";

interface TableItem {
    id: number
    Phone: string
    Superior: string
    App: string;
    Op: string;
    TimeStamp: string;
}

const query = reactive({
    pageIndex: 1,
    pageSize: 10
});
const searchQuery = reactive({
    Phone: '',
    Superior: '',
    App: '',
    Op: '',
});

const tableData = ref<TableItem[]>([]);
const tableDataCache = ref<TableItem[]>([]);
const pageTotal = ref(0);
const pageTotalCache = ref(0);
const request = reactive({
    url: '',
    method: 'get',
    query: {}
});

// 获取后台数据
const getData = () => {
    request.url='/get_history'
    request.query = {"Phone": searchQuery.Phone}
    requestData(request)!.then(res => {
        tableDataCache.value = res.data.list;
        pageTotalCache.value = res.data.pageTotal;
    });
};
getData()
// 搜索过程：清除筛选项目+获取后台数据
const phoneSearch = () => {
    searchQuery.Superior = '';
    searchQuery.App = '';
    searchQuery.Op = '';
    getData()
    tableData.value = tableDataCache.value
    pageTotal.value = pageTotalCache.value
}
// 清除搜索栏中的输入
const phoneClear = () => {
    searchQuery.Phone = '';
    searchQuery.Superior = '';
    searchQuery.App = '';
    searchQuery.Op = '';
    tableDataCache.value = []
    tableData.value = []
    pageTotal.value = 0
    pageTotalCache.value = 0
}
// 筛选操作
const optionSearch = () => {
    tableData.value = tableDataCache.value.filter(item => {
        const superiorMatch = item.Superior.includes(searchQuery.Superior);
        const appMatch = item.App.includes(searchQuery.App);
        const opMatch = item.Op.includes(searchQuery.Op);
        return superiorMatch && appMatch && opMatch;
    });
    pageTotal.value = tableData.value.length
};
const clearHistory = () => {
    request.url='/clear_history'
    request.query = {"Phone": searchQuery.Phone}
    requestData(request)!.then(res => {
        tableDataCache.value = res.data.list;
        pageTotalCache.value = res.data.pageTotal;
    });
    tableData.value = tableDataCache.value
    pageTotal.value = pageTotalCache.value
}
// 分页导航
const handlePageChange = (val: number) => {
    query.pageIndex = val;
    getData();
};


</script>

<style scoped>
.handle-box {
    margin-bottom: 20px;
}

.handle-select {
    width: 120px;
}

.handle-input {
    width: 150px;
}

.table {
    width: 100%;
    font-size: 14px;
}

.red {
    color: #F56C6C;
}

.mr20 {
    margin-right: 20px;
}

.table-td-thumb {
    display: block;
    margin: auto;
    width: 40px;
    height: 40px;
}
</style>
