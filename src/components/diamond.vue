<template>
  <div class="Manage">
    <el-col :span="4"> 
      <el-menu
        :default-active="activeIndex"
        class="el-menu-vertical-demo"
        @select="handleSelect"
        router
        background-color="#ffffff "
        text-color="#24292e" 
      >
        <el-menu-item-group >
          <template slot="title"> 
            <span>
               <el-image
                        style="width: 70px; height: 70px; border-radius: 50%;"
                        :src="jpg"
                        :fit="fits">
                    </el-image>
            </span>
            </template
          >
          <el-menu-item index="/diamond/dashboard/desktop">
            <span slot="title">工作台</span>
          </el-menu-item>
            <el-menu-item index="/diamond/createTeam">
            <span slot="title">创建团队</span>
          </el-menu-item>
           <el-menu-item index="/diamond/inbox">
            <span slot="title">消息通知</span>
          </el-menu-item>
          <el-menu-item index="/diamond/profile">
            <span slot="title">个人信息</span>
          </el-menu-item>
        </el-menu-item-group>
      </el-menu>
    </el-col>
    <el-col :span="20">
      <router-view></router-view>
    </el-col>
  </div>
</template> 

<script>
/* eslint-disable */
  export default {
    name: "Diamond",
    data(){
      return{
        jpg:'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
        activeIndex: this.$route.path,
      }
    },
    mounted(){
      this.init()
    },
    methods: {
      init(){

      },
      handleSelect(key, keyPath) {
        console.log(this.$route.path)
        console.log(key, keyPath);
      },
    }
  }
</script>

<style scoped>
.el-menu-item.is-active {
  position:relative; 
  left:'-20px';
　　text-color:#aa67aa  !important; 
   background-image: linear-gradient(to right, #aa67aa, #1682dc) !important;
        -webkit-background-clip: text;
        color: transparent;
}

  .el-menu-item-group>>>.el-menu-item-group__title{
    padding: 5px 45px !important;
  }
  .el-menu{
    width: 150px;
  }
  .el-menu-item, .el-submenu__title {
    text-align: center;
  }
</style>