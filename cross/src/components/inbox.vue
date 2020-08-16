<template>
  <div class="router">
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect"   router>
      <el-menu-item index="/diamond/inbox/invite"><span slot="title">团队邀请信息</span></el-menu-item>
      <el-menu-item index="/diamond/inbox/kickOutRemind"><span slot="title">团队退出提醒</span></el-menu-item>
      <el-menu-item index="/diamond/inbox/documentRemind"><span slot="title">文档评论提醒</span></el-menu-item>
      <el-menu-item index="/diamond/inbox/collaboratorRemind"><span slot="title">协作者邀请提醒</span></el-menu-item>
  </el-menu>
 <router-view></router-view>
  </div>
</template>

<script>
/* eslint-disable */
  export default {
    name: "Inbox",
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
