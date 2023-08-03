<template>
    <div>
        <div class="container">
            <div class="handle-box">
                <div style="margin-bottom: 20px">
                    <el-button type="success"
                               :icon="Search"
                               size="large"
                               @click="phoneSearch">一键查询
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
                <el-table-column prop="TimeStamp" label="时间戳" width=250 align="center"></el-table-column>
                <el-table-column label="操作" width="220" align="center">
                    <template #default="scope">
                        <el-button text :icon="Edit" @click="handleEdit(scope.$index, scope.row)" v-permiss="15">
                            编辑
                        </el-button>
                        <el-button text :icon="Delete" class="red" @click="handleDelete(scope.$index)" v-permiss="16">
                            删除
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
        <el-dialog title="编辑" v-model="editVisible" width="30%">
            <el-form label-width="70px">
                <el-form-item label="状态">
                    <el-radio-group v-model="form.state">
                        <el-radio-button label="success">成功</el-radio-button>
                        <el-radio-button label="error">失败</el-radio-button>
                    </el-radio-group>
                </el-form-item>
            </el-form>
            <template #footer>
    <span class="dialog-footer">
      <el-button @click="editVisible = false">取 消</el-button>
      <el-button type="primary" @click="saveEdit">确 定</el-button>
    </span>
            </template>
        </el-dialog>
    </div>
</template>

<script setup lang="ts" name="basetable">
import {reactive, ref} from 'vue';
import {ElMessage, ElMessageBox} from 'element-plus';
import {Delete, Edit, Search} from '@element-plus/icons-vue';
import Data from "./DB.json";
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
    url: '/get_all',
    method: 'get',
    query: {}
})// 获取后台数据
const getData = () => {
    request.query = {"Phone": searchQuery.Phone}
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

// 删除操作
const handleDelete = (index: number) => {
    // 二次确认删除
    ElMessageBox.confirm('确定要删除吗？', '提示', {
        type: 'warning'
    })
        .then(() => {
            ElMessage.success('删除成功');
            tableData.value.splice(index, 1);
        })
        .catch(() => {
        });
};

// 表格编辑时弹窗和保存
const editVisible = ref(false);
let form = reactive({
    state: '',
    timestamp: ''
});
let idx: number = -1;
const handleEdit = (index: number, row: any) => {
    idx = index;
    form.state = row.state;
    form.timestamp = row.timestamp;
    editVisible.value = true;
};
const saveEdit = () => {
    editVisible.value = false;
    const now = new Date();
    const days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thus', 'Fri', 'Sat'];
    const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
    form.timestamp = `${days[now.getDay()]}-${months[now.getMonth()]}-${now.getDate()}-${now.getHours()}:${now.getMinutes()}:${now.getSeconds()}-${now.getFullYear()}`;
    ElMessage.success(`操作成功`);
    tableData.value[idx].State = form.state;
    tableData.value[idx].TimeStamp = form.timestamp;
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
    width: 200px;
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