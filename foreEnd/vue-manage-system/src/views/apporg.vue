<template>
    <div>
        <div class="container">
            <div class="handle-box">
                <div style="margin-bottom: 20px">
                    <el-button type="success"
                               :icon="Search"
                               size="large"
                               @click="phoneSearch">数据查询/刷新
                    </el-button>
                </div>
                <el-input v-model="searchQuery.Phone"
                          type="text"
                          placeholder="账号"
                          :prefix-icon="Search"
                          clearable
                          @clear="searchQuery.Phone=''"
                          class="handle-input mr20">
                </el-input>
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
                           clearable
                           @clear="searchQuery.Superior=''"
                           class="mr20"
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
                           clearable
                           @clear="searchQuery.App=''"
                           class="mr20"
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
                <el-select v-model="searchQuery.Op"
                           placeholder="操作"
                           clearable
                           @clear="searchQuery.Op=''"
                           class="handle-select mr20">
                    <el-option key="1" label="注册" value="signup" align="center"></el-option>
                    <el-option key="2" label="变更" value="change" align="center"></el-option>
                    <el-option key="3" label="注销" value="cancel" align="center"></el-option>
                </el-select>
                <el-select v-model="searchQuery.State"
                           placeholder="状态"
                           clearable
                           @clear="searchQuery.State=''"
                           class="handle-select mr20">
                    <el-option key="1" label="成功" value="success" align="center"></el-option>
                    <el-option key="2" label="失败" value="error" align="center"></el-option>
                    <el-option key="3" label="待处理" value="pending" align="center"></el-option>
                </el-select>
                <el-button type="primary" :icon="Search" @click="optionSearch">筛选</el-button>
                <el-button type="danger" :icon="Delete" @click="phoneSearch">清除</el-button>
            </div>

            <el-table :data="tableData"
                      border
                      stripe
                      class="table"
                      ref="multipleTable"
                      header-cell-class-name="table-header">
                <el-table-column prop="id" label="序号" width="60" align="center"></el-table-column>
                <el-table-column prop="HashID" label="哈希索引" width="250" align="center"></el-table-column>
                <el-table-column prop="Phone" label="账号" align="center"></el-table-column>
                <el-table-column prop="Superior" label="运营商" align="center"></el-table-column>
                <el-table-column prop="App" label="应用" align="center"></el-table-column>
                <el-table-column prop="Op" label="操作" align="center"></el-table-column>
                <el-table-column label="状态" align="center">
                    <template #default="scope">
                        <el-tag
                            v-if="scope.row.State === 'success'"
                            :type="'success'"
                            size="large"
                            round
                        >
                            {{ "success" }}
                        </el-tag>
                        <el-tag
                            v-else-if="scope.row.State === 'pending'"
                            round
                            size="large"
                        >
                            {{ "pending" }}
                        </el-tag>
                        <el-tag
                            size="large"
                            v-else
                            :type="'danger'"
                            round
                        >
                            {{ "error" }}
                        </el-tag>
                    </template>
                </el-table-column>
                <el-table-column prop="TimeStamp" label="时间戳" width=250 align="center"></el-table-column>
                <el-table-column label="操作" width="220" align="center">
                    <template #default="scope">
                        <el-button type="danger"
                                   :icon="Edit"
                                   size="small"
                                   plain
                                   round
                                   @click.="handleEdit(scope.$index)"
                        >
                            反馈处理
                        </el-button>
                    </template>
                </el-table-column>
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

        <!-- 编辑弹出框 -->
        <el-dialog title="编辑" v-model="editVisible" width="30%" center @closed="getData">
            <template #header="{ close, titleId, titleClass }">
                <div class="my-header">
                    <h1 :id="titleId" :class="titleClass">请更改操作状态</h1>
                </div>
            </template>
            <div class="state-form">
                <el-form label-width="10%" :label-position="'right'">
                    <el-form-item label="状态" size="large">
                        <el-radio-group
                            v-model="formState"
                            size="large"
                        >
                            <el-radio label="success" border>成功</el-radio>
                            <el-radio label="error" border>失败</el-radio>
                        </el-radio-group>
                    </el-form-item>
                </el-form>
            </div>
            <template #footer>
                <span class="dialog-footer">
                  <el-button type="danger" @click="editVisible = false" size="large">取 消</el-button>
                  <el-button type="primary" @click="saveEdit" size="large">确 定</el-button>
                </span>
            </template>
        </el-dialog>
    </div>
</template>

<script setup lang="ts" name="basetable">
import {reactive, ref} from 'vue';
import {ElMessage} from 'element-plus';
import {Delete, Edit, Search} from '@element-plus/icons-vue';
import {requestData} from "../api";


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

const pageQuery = reactive({
    pageIndex: 1,
    pageSize: 10
});
const tableData = ref<TableItem[]>([]);
const tableDataCache = ref<TableItem[]>([]);
const pageTotal = ref(0);
const pageTotalCache = ref(0);

const searchQuery = reactive({
    HashID: '',
    Superior: '',
    Phone: '',
    App: '',
    Op: '',
    State: ''
});

const request = reactive({
    url: '',
    method: 'get',
    query: {}
})// 获取后台数据
const getData = () => {
    request.url = '/get_all'
    request.query = {}
    requestData(request)!.then(res => {
        tableDataCache.value = res.data.list;
        pageTotalCache.value = res.data.pageTotal;
    });
};
getData()

// 清除筛选项目
const optionClear = () => {
    searchQuery.HashID = '';
    searchQuery.Phone = '';
    searchQuery.Superior = '';
    searchQuery.App = '';
    searchQuery.Op = '';
    searchQuery.State = '';
}
// 搜索过程：清除筛选项目+获取后台数据
const phoneSearch = () => {
    optionClear()
    getData()
    tableData.value = tableDataCache.value
    pageTotal.value = pageTotalCache.value
}

// 筛选操作
const optionSearch = () => {
    pageQuery.pageIndex = 1;
    tableData.value = tableDataCache.value.filter(item => {
        const phoneMatch = item.Phone.includes(searchQuery.Phone);
        const hashIDMatch = item.HashID.includes(searchQuery.HashID);
        const superiorMatch = item.Superior.includes(searchQuery.Superior);
        const appMatch = item.App.includes(searchQuery.App);
        const opMatch = item.Op.includes(searchQuery.Op);
        const stateMatch = item.State.includes(searchQuery.State);
        return phoneMatch && hashIDMatch && superiorMatch && appMatch && opMatch && stateMatch;
    });
    pageTotal.value = tableData.value.length
};

// 分页导航
const handlePageChange = (val: number) => {
    pageQuery.pageIndex = val;
    getData();

};


// 表格编辑时弹窗和保存
let editVisible = ref(false);
const formState = ref("")
const submit = reactive({
    HashID: '',
    Phone: '',
    Superior: '',
    App: '',
    Op: '',
    State: '',
})
let idx: number = -1;

// 点击编辑处理
const handleEdit = (index: number) => {
    idx = index
    editVisible.value = true
}

// 发送编辑请求
const editRequest = () => {
    optionClear()
    request.url = "/edit"
    request.query = submit
    requestData(request)!.then(res => {
        tableDataCache.value = res.data.list;
        pageTotalCache.value = res.data.pageTotal;
    });
    tableData.value = tableDataCache.value
    pageTotal.value = pageTotalCache.value
}

// 确认编辑处理
const saveEdit = () => {
    submit.HashID = tableDataCache.value[idx].HashID
    submit.Phone = tableDataCache.value[idx].Phone
    submit.Superior = tableDataCache.value[idx].Superior
    submit.App = tableDataCache.value[idx].App
    submit.Op = tableDataCache.value[idx].Op
    submit.State = formState.value;
    editRequest()
    editVisible.value = false;
    ElMessage.success(`操作成功`);
};
</script>

<style scoped>
.handle-box {
    margin-bottom: 18px;
}

.handle-select {
    width: 120px;
}

.handle-input {
    width: 200px;
}

.table {
    width: 100%;
    font-size: 16px;
}


.mr20 {
    margin-right: 20px;
}


.my-header h1 {
    font-size: 26px;
    margin-top: 15px;
}

.state-form {
    font-size: 18px;
    margin-top: 10px;
    margin-left: 50px;
}
</style>