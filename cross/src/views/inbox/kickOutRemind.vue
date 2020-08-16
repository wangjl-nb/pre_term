<template>
  <el-container >
  <el-main class="dashboard">
      <ul v-for="(item,index) in list" :key="index">
          <li>
              <el-card class="box-card" shadow="hover">
                    <p style="flex-grow:13">你收到一条团队踢出提醒：<strong style="font-size:20x">{{item.message}}</strong> </p>
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
          {id:"1",message: "zzz1"},
          {id:"2",message: "zzz2"},
          {id:"3",message: "zzz3"},
        ]
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

  }
};
</script>
<style scoped>
</style>
