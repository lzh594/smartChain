<template>
    <div>
        <div class="container">
            <div class="handle-box">
                <el-select v-model="searchQuery.App" placeholder="应用" class="handle-select mr10">
                    <el-option-group label="腾讯">
                        <el-option key="1" label="微信" value="weixin" align="center"></el-option>
                        <el-option key="2" label="QQ" value="QQ" align="center"></el-option>
                    </el-option-group>
                    <el-option-group label="阿里巴巴">
                        <el-option key="3" label="淘宝" value="taobao" align="center"></el-option>
                        <el-option key="4" label="支付宝" value="Alipay" align="center"></el-option>
                    </el-option-group>
                    <el-option-group label="网易">
                        <el-option key="5" label="网易云音乐" value="Musics" align="center"></el-option>
                    </el-option-group>
                    <el-option-group label="米哈游">
                        <el-option key="6" label="原神" value="Genshin" align="center"></el-option>
                    </el-option-group>
                    <el-option-group label="字节跳动">
                        <el-option key="7" label="抖音" value="Tiktok" align="center"></el-option>
                    </el-option-group>
                </el-select>
                <el-input v-model="searchQuery.Phone" placeholder="账号" class="handle-input mr10"></el-input>
                <el-select v-model="searchQuery.Op" placeholder="操作" class="handle-select mr10">
                    <el-option key="1" label="变更" value="change" align="center"></el-option>
                    <el-option key="2" label="注册" value="signup" align="center"></el-option>
                    <el-option key="3" label="注销" value="cancel" align="center"></el-option>
                </el-select>
                <el-select v-model="searchQuery.State" placeholder="状态" class="handle-select mr10">
                    <el-option key="1" label="成功" value="success" align="center"></el-option>
                    <el-option key="2" label="失败" value="error" align="center"></el-option>
                    <el-option key="3" label="待处理" value="pending" align="center"></el-option>
                </el-select>
                <el-button type="primary" :icon="Search" @click="handleSearch">搜索</el-button>
                <el-button type="text" :icon="Delete" @click="handleClear">清除</el-button>
            </div>

            <el-table :data="tableData" border class="table" ref="multipleTable" header-cell-class-name="table-header">
                <el-table-column prop="id" label="序号" width="55" align="center"></el-table-column>
                <el-table-column prop="HashID" label="哈希" align="center"></el-table-column>
                <el-table-column prop="Phone" label="账号" align="center"></el-table-column>
                <el-table-column prop="Superior" label="运营商" align="center"></el-table-column>
                <el-table-column prop="App" label="应用" align="center"></el-table-column>
                <el-table-column prop="Op" label="操作" align="center"></el-table-column>
                <el-table-column prop="state" label="状态" align="center">
                    <template #default="scope">
                        <el-tag
                            :type="scope.row.state === 'success' ? 'success' : scope.row.state === 'error' ? 'danger' : ''"
                        >
                            {{ scope.row.state }}
                        </el-tag>
                    </template>
                </el-table-column>

                <el-table-column prop="TimeStamp" label="时间" width=190 align="center"></el-table-column>
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
                    :current-page="query.pageIndex"
                    :page-size="query.pageSize"
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


interface TableItem {
    id: number
    HashID: string;
    Phone: string
    Superior: string
    App: string;
    Op: string;
    state: string;
    TimeStamp: string;
}

const query = reactive({
    Phone: '',
    App: '',
    Op: '',
    pageIndex: 1,
    pageSize: 10
});
const tableData = ref<TableItem[]>(Data.list);
const pageTotal = ref(Data.pageTotal || 50);

// 获取表格数据
const getData = () => {
    tableData.value = Data.list;
    pageTotal.value = Data.pageTotal || 50;
};

const searchQuery = reactive({
    App: '',
    Phone: '',
    Op: '',
    State: ''
});

// 查询操作
const handleSearch = () => {
    query.pageIndex = 1;
    getData();
    tableData.value = Data.list.filter(item => {
        const appMatch = item.App.includes(searchQuery.App);
        const phoneMatch = item.Phone.includes(searchQuery.Phone);
        const opMatch = item.Op.includes(searchQuery.Op);
        const stateMatch = item.state.includes(searchQuery.State);
        return appMatch && phoneMatch && opMatch && stateMatch;
    });
};

// 清除搜索栏中的输入
const handleClear = () => {
    searchQuery.App = '';
    searchQuery.Phone = '';
    searchQuery.Op = '';
    searchQuery.State = '';
    getData();
};
// 分页导航
const handlePageChange = (val: number) => {
    query.pageIndex = val;
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
    tableData.value[idx].state = form.state;
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
    width: 300px;
}

.table {
    width: 100%;
    font-size: 14px;
}

.red {
    color: #F56C6C;
}

.mr10 {
    margin-right: 10px;
}

.table-td-thumb {
    display: block;
    margin: auto;
    width: 40px;
    height: 40px;
}
</style>