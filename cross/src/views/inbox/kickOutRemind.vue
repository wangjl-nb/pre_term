<template>
  <el-container >
  <el-main class="dashboard">
      <ul v-for="(item,index) in list" :key="index">
          <li>
              <el-card class="box-card" shadow="hover" >
                <div class="flex flex6">
                    <p style="flex-grow:13">你收到一条团队提醒：<strong style="font-size:20px">{{item.message}}</strong> </p>
                    <button class="btn-10" style="flex-grow:1" type="danger" plain @click="read(index,item.id)">已阅</button>
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
  name: "DocumentRemind",
  components: {
      info
  },
  data(){
      return{
        list:[]
      }
  },
  mounted(){
    //接口文档27.3
    this.$axios.post('/app/message_list/').then(res => {
      //接收数据
      console.log(res);
      this.list = res.data.list;

    })
  },
  methods:{
    read(index,id){
      //接口文档27.5
      this.$axios.get('/app/delete_message/',{
        params:{
          id: id
        },
        headers: {'Content-Type': 'application/x-www-form-urlencoded'}
      }).then(res =>{
        if (res.data.status === 0) {
          alert('阅读完成并删除！')
           this.list.splice(index,1)
        } else {
          this.$message.error("阅读失败！")
        }
      })
    }
  }
};
</script>
<style scoped>
</style>
