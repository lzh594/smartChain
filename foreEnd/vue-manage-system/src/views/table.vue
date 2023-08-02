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
                </div>
                <el-input v-model="searchQuery.HashID"
                          style="width: 350px"
                          :prefix-icon="Search"
                          class="mr20"
                          clearable
                          @clear="searchQuery.HashID=''"
                          placeholder="哈希索引">

                </el-input>
                <el-select v-model="searchQuery.Superior"
                           placeholder="运营商"
                           class="mr20"
                           clearable
                           @clear="searchQuery.Superior=''"
                           style="width: 88px">
                    <el-option key="1" label="Alibaba" value="Alibaba" align="center"></el-option>
                    <el-option key="2" label="Mihoyo" value="Mihoyo" align="center"></el-option>
                    <el-option key="3" label="ByteDance" value="ByteDance" align="center"></el-option>
                    <el-option key="4" label="Tencent" value="Tencent" align="center"></el-option>
                    <el-option key="5" label="NetEase" value="NetEase" align="center"></el-option>
                    <el-option key="6" label="buaa" value="buaa" align="center"></el-option>
                </el-select>
                <el-select v-model="searchQuery.App"
                           placeholder="应用"
                           class="mr20"
                           clearable
                           @clear="searchQuery.App=''"
                           style="width: 88px">
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
                <el-button type="primary" :icon="Search" @click="optionSearch">筛选</el-button>
                <el-button type="danger" :icon="Delete" @click="phoneSearch">清除</el-button>
            </div>
            <el-table :data="tableData" border class="table" ref="multipleTable" header-cell-class-name="table-header">
                <el-table-column prop="id" label="序号" width="55" align="center"></el-table-column>
                <el-table-column prop="HashID" label="哈希索引" width="220" align="center"></el-table-column>
                <el-table-column prop="Phone" label="账号" align="center"></el-table-column>
                <el-table-column prop="Superior" label="运营商" align="center"></el-table-column>
                <el-table-column prop="App" label="应用" align="center"></el-table-column>
                <el-table-column prop="Op" label="操作" align="center"></el-table-column>
                <el-table-column label="状态" align="center">
                    <template #default="scope">
                        <el-tag
                            v-if="scope.row.State === 'success'"
                            :type="'success'"
                            round
                        >
                            {{ "success" }}
                        </el-tag>
                        <el-tag
                            v-else-if="scope.row.State === 'pending'"
                            round
                        >
                            {{ "pending" }}
                        </el-tag>
                        <el-tag
                            v-else
                            :type="'danger'"
                            round
                        >
                            {{ "error" }}
                        </el-tag>
                    </template>
                </el-table-column>
                <el-table-column prop="TimeStamp" label="处理时间" width="250" align="center"></el-table-column>

            </el-table>
            <div class="pagination">
                <el-pagination
                    background
                    layout="total, prev, pager, next"
                    :current-page="pageQuery.pageIndex"
                    :page-size="pageQuery.pageSize"
                    :total="pageTotal"
                    @current-change="handlePageChange"
                ></el-pagination>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts" name="basetable">
import {ref, reactive} from 'vue';
import {requestData} from '../api';
import {Delete, Search} from "@element-plus/icons-vue";

interface TableItem {
    id: number
    HashID: string;
    Phone: string
    Superior: string
    App: string;
    Op: string;
    State: string;
    TimeStamp: string;
}

const searchQuery = reactive({
    Phone: '',
    HashID: '',
    Superior: '',
    App: '',
});
const pageQuery = reactive({
    pageIndex: 1,
    pageSize: 10
});
const tableData = ref<TableItem[]>([]);
const tableDataCache = ref<TableItem[]>([]);
const pageTotal = ref(0);
const pageTotalCache = ref(0);
const request = reactive({
    url: '/query',
    method: 'get',
    query: {}
})
// 获取表格数据
const getData = () => {
    request.query = {"Phone": searchQuery.Phone}
    requestData(request)!.then(res => {
        tableDataCache.value = res.data.list;
        pageTotalCache.value = res.data.pageTotal;
    });
};
getData();
const phoneSearch = () => {
    searchQuery.HashID = '';
    searchQuery.Superior = '';
    searchQuery.App = '';
    getData();
    tableData.value = tableDataCache.value;
    pageTotal.value = pageTotalCache.value;
}
// 清除搜索栏中的输入
const phoneClear = () => {
    searchQuery.Phone = '';
    searchQuery.HashID = '';
    searchQuery.Superior = '';
    searchQuery.App = '';
    tableDataCache.value = []
    tableData.value = []
    pageTotal.value = 0
    pageTotalCache.value = 0
}
// 筛选操作
const optionSearch = () => {
    pageQuery.pageIndex = 1;
    tableData.value = tableDataCache.value.filter(item => {
        const superiorMatch = item.Superior.includes(searchQuery.Superior);
        const appMatch = item.App.includes(searchQuery.App);
        const hashIDMatch = item.HashID.includes(searchQuery.HashID);
        return superiorMatch && appMatch && hashIDMatch;
    });
    pageTotal.value = tableData.value.length
};

// 分页导航
const handlePageChange = (val: number) => {
    pageQuery.pageIndex = val;
    getData();
};

</script>

<style scoped>
.handle-box {
    margin-bottom: 20px;
    margin-left: 10px;
}

.handle-select {
    width: 120px;
}

.handle-input {
    width: 300px;
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

