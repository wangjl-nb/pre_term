<template>
  <el-container >
  <el-main class="dashboard">
      <ul v-for="(item,index) in list" :key="index">
          <li>
              <el-card class="box-card" shadow="hover">
                    <p style="flex-grow:13"><strong style="font-size:20x">{{item.author}}</strong> <span>于{{item.time}}时评论了</span><strong style="font-size:20x">{{item.document}}</strong>文档</p>
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
  name: "DocumentRemind",
  components: {
      info
  },
  data(){
      return{
        infoo:[
             "您已加入XXXsadsa团队",
             "您已被踢出XsdXX团队",
             "您已退出XddXX团队"
         ],
        list:[
            {author:"XXX",document:"sdas",time:"2020/1/1 12:00"},
            {author:"XXX",document:"sdas",time:"2020/1/1 12:00"},
            {author:"XXX",document:"sdas",time:"2020/1/1 12:00"},
        ]
      }
  },
  mounted(){
    this.$axios.post('').then(res => {
      //接收数据
      this.list = res.data.list;

    })
  },
  methods:{

  }
};
</script>
<style scoped>
</style>
