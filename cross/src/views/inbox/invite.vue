<template>
  <el-container >
  <el-main class="dashboard"> 
      <ul v-for="(item,index) in list" :key="index">
          <li>
              <el-card class="box-card" shadow="hover">
                     <div class="flex flex6" > 
                        <p style="flex-grow:13"><strong style="font-size:20px">{{item.author}}</strong> <span>邀请您加入</span><strong style="font-size:20x">{{item.team}}</strong></p>
                        <el-button style="flex-grow:1" plain @click="argee(item.id)">同意</el-button>
                        <el-button style="flex-grow:1" type="danger" plain  @click="refuse(item.id)">拒绝</el-button>
                     </div>
                     <el-divider content-position="left">邀请理由</el-divider>
                  <div>
                      <el-row>
  <el-col :span="2"><div class="grid-content"></div></el-col> 
  <el-col :span="20"><div class="grid-content"><p>{{item.reason}}</p></div></el-col>
  <el-col :span="2"><div class="grid-content"></div></el-col>
</el-row>
                  </div>
              </el-card>
          </li>
      </ul> 
  </el-main> 
  <el-aside>
       <info :info="infoo"></info>
  </el-aside>
</el-container>
</template>

<script>
// @ is an alias to /src
import info from '@/components/info'
export default {
  name: "Invite",
  components: {
      info
  },
  data(){
      return{
        list:[
            {id:1231,author:"XXX",team:"sdas",reason:"你太厉害了！！！"},
            {id:1231,author:"XXXcsx",team:"sdas",reason:"你太厉害了！！！"},
            {id:1231,author:"XXXwqe",team:"sdas",reason:"你太厉害了！！！"}
        ]
      }
  },
  mounted(){
  },
  methods:{
      argee(id){
          this.aa=id
      },
      refuse(id){
           this.aa=id
      }
  }
};
</script>
<style scoped>
 .el-row {
    margin-bottom: 20px;
    &:last-child {
      margin-bottom: 0;
    }
  }
  .el-col {
    border-radius: 4px;
  }
  .bg-purple-dark {
    background: #99a9bf;
  }
  .bg-purple {
    background: #d3dce6;
  }
  .bg-purple-light {
    background: #e5e9f2;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }
</style>
