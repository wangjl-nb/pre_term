<template>
  <div class="router">    
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect"   router>
  <el-submenu index="2">
    <template slot="title">我的文档</template>
    <el-menu-item index="/diamond/dashboard/desktop">我的桌面<span slot="title"></span></el-menu-item>
      <el-menu-item index="/diamond/dashboard/used"><span slot="title">最近使用</span></el-menu-item>
    <el-menu-item index="/diamond/dashboard/own"><span slot="title">我创建的</span></el-menu-item>
      <el-menu-item index="/diamond/dashboard/favorites"><span slot="title">我收藏的</span></el-menu-item>
  </el-submenu>
  <el-menu-item index="/diamond/dashboard/team"><span slot="title">我的团队</span></el-menu-item> 
  <el-menu-item index="/diamond/dashboard/trash"><span slot="title">回收站</span></el-menu-item>
  </el-menu>
 <router-view></router-view>
  </div>
</template>

<script>
/* eslint-disable */
  export default {
    name: "Dashboard",
    data(){
      return{
          activeIndex: '1',
      }
    },
    mounted(){
      this.init()
    },
    methods: {
      init(){

      },
        handleSelect(key, keyPath) {
        console.log(key, keyPath);
      }
    }
  }
</script>

<style scoped>
  
</style>