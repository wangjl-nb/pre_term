<template>
  <el-container >
  <el-main class="dashboard">
      <ul v-for="(item,index) in list" :key="index">
          <li>
              <el-card class="box-card" shadow="hover">
                     <div class="flex flex6" >
                        <p style="flex-grow:13"><strong style="font-size:20px">{{item.name}}</strong> <span>邀请您成为</span><strong style="font-size:20px">{{item.title}}</strong>文档的协作者</p>
                         <div style="flex-grow:1;margin-bottom:-30px" >
                            <button class="btn-7" style="margin-right:-5px" plain @click="argee(index,item.id)">同意</button>
                            <button class="btn-10"  type="danger" plain  @click="refuse(index,item.id)">拒绝</button>
                         </div>
                     </div>
                     <el-divider content-position="left">邀请理由</el-divider>
                     <div>
                       <el-row style="margin-bottom:-12px">
                        <el-col :span="2"><div class="grid-content"></div></el-col>
                        <el-col :span="20"><div class="grid-content"><p>{{item.reason}}</p></div></el-col>
                        <el-col :span="2"><div class="grid-content"></div></el-col>
                       </el-row>
                     </div>
              </el-card>
          </li>
      </ul>
  </el-main>
</el-container>
</template>

<script>
// @ is an alias to /src
import info from '@/components/info'
export default {
  name: "CollaboratorRemind",
  components: {
      info
  },
  data(){
      return{
        list:[
          {id:1,name: "xxx",reason: "你太厉害了！！！",title: "yyyy"},
          {id:2,name: "xxx",reason: "你太厉害了！！！",title: "yyyy"},
          {id:3,name: "xxx",reason: "你太厉害了！！！",title: "yyyy"},
          {id:4,name: "xxx",reason: "你太厉害了！！！",title: "yyyy"},
        ]
      }
  },
  mounted(){
    //接口文档48
    this.$axios.post('/app/coinvitation_list/', ).then(res => {
      //接收数据
      console.log(res);
      this.list = res.data.list;

    })
  },
  methods:{
    //接口文档49
    argee(index,id) {
      this.$axios.post('/app/process_coinvitation/',
        this.qs.stringify({
          id: id,
          type: 0
        }), {headers: {'Content-Type': 'application/x-www-form-urlencoded'}})
        .then(res => {
          if (res.data.status === 0) {
            alert('成为协作者成功！')
            this.list.splice(index,1)
          } else {
            this.$message.error("成为协作者失败！")
          }
        })
      // this.aa=id
    },
    refuse(index,id) {
      this.$axios.post('/app/process_coinvitation/',
        this.qs.stringify({
          id: id,
          type: 1,
        }), {headers: {'Content-Type': 'application/x-www-form-urlencoded'}})
        .then(res => {
          console.log(res)
          if (res.data.status === 0) {
            alert('拒绝成为协作者成功')
             this.list.splice(index,1)
          } else {
            this.$message.error("拒绝成为协作者失败！")
          }

        })
      // this.aa=id
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
