<template>
    <div class="sidebar">
        <el-menu
            class="sidebar-el-menu"
            :default-active="onRoutes"
            :collapse="sidebar.collapse"
            background-color="#324157"
            text-color="#bfcbd9"
            active-text-color="#20a0ff"
            unique-opened
            router
        >
            <template v-for="(item, index) in items">
                <template
                    v-if="identity === '1' && (item.index === '/dashboard' || item.index === '/table' || item.index === '/form' || item.index === '/history') || identity === '0' && (item.index === '/dashboard' || item.index === '/apporg')">
                    <el-menu-item :index="item.index" :key="item.index" v-permiss="item.permiss">
                        <el-icon>
                            <component :is="item.icon"></component>
                        </el-icon>
                        <template #title class="side-font">{{ item.title }}</template>
                    </el-menu-item>
                </template>
            </template>
        </el-menu>
    </div>
</template>

<script setup lang="ts">
import {computed} from 'vue';
import {useSidebarStore} from '../store/sidebar';
import {useRoute} from 'vue-router';

const items = [
    {
        icon: 'Odometer',
        index: '/dashboard',
        title: '系统首页',
        permiss: '1',
    },
    {
        icon: 'User',
        index: '/table',
        title: '账号信息',
        permiss: '2',
    },
    {
        icon: 'Calendar',
        index: '/history',
        title: '历史记录',
        permiss: '6',
    },
    {
        icon: 'Edit',
        index: '/form',
        title: '账号管理',
        permiss: '1',
    },
    {
        icon: 'Goods',
        index: '/apporg',
        title: '数据管理',
        permiss: '2',
    },
];

const route = useRoute();
const onRoutes = computed(() => {
    return route.path;
});

const sidebar = useSidebarStore();
// const identity = computed(() => window.userIdentity || 0); // 从全局变量读取用户身份
const identity = localStorage.getItem('ms_identity')
</script>

<style scoped>
.side-font{
    display: block;
    font-size: 100px;
}
.sidebar {
    display: block;
    position: absolute;
    left: 0;
    top: 70px;
    bottom: 0;
    overflow-y: scroll;
    font-size: 20px;
}

.sidebar::-webkit-scrollbar {
    width: 0;
}
li {
    font-size: large;
    font-weight: bolder;
    text-align: center;
}
.sidebar-el-menu:not(.el-menu--collapse) {
    width: 250px;
    font-size: 30px;
}

.sidebar > ul {
    height: 100%;
}
</style>