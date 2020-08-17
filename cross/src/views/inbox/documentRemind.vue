<template>
  <el-container >
  <el-main class="dashboard">
      <ul v-for="(item,index) in list" :key="index">
          <li>
              <el-card class="box-card" shadow="hover">
                <p style="flex-grow:13"><strong style="font-size:20px">{{item.u_username}}</strong> <span>于{{item.date}}时评论了</span><strong style="font-size:20px">{{item.title}}</strong>文档</p>
                <el-button type="danger" plain @click="read(item.id)">阅读</el-button>
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
        list:[
          {id:"1",u_username:"xxx",date:"2020/1/1 12:00",title:"YYYY"},
          {id:"2",u_username:"xxx",date:"2020/1/1 12:00",title:"YYYY"},
          {id:"3",u_username:"xxx",date:"2020/1/1 12:00",title:"YYYY"},
          {id:"4",u_username:"xxx",date:"2020/1/1 12:00",title:"YYYY"},
        ]
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
    read(id){
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
          this.$router.go(0)
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
