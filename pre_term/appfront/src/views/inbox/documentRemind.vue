<template>
  <el-container >
  <el-main class="dashboard">
      <ul v-for="(item,index) in list" :key="index">
          <li>
              <el-card class="box-card" shadow="hover">
                <div class="flex flex6">
                  <p style="flex-grow:13"><strong style="font-size:20px">{{item.u_username}}</strong> <span>于{{item.date}}时评论了</span><strong style="font-size:20px">{{item.title}}</strong>文档</p>
                  <button class="btn-10" style="flex-grow:1"  plain @click="read(index,item.id)">已阅</button>
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
    //接口文档26
    this.$axios.post('/app/comment_reminder/').then(res => {
      //接收数据
      console.log(res);
      this.list = res.data.list;

    })
  },
  methods:{
    read(index,id){
      //接口文档27.5
      this.$axios.get('/app/delete_comment_reminder/',{
        params:{
          id: id
        },
        headers: {'Content-Type': 'application/x-www-form-urlencoded'}
      }).then(res =>{
          console.log(res);
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
