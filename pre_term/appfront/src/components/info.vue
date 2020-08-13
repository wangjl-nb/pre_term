<template>
    <div>
          <ul v-for="(item,index) in info" :key="index">
             <li>
                 <el-card shadow="hover">
                     {{item}}
                 </el-card>
            </li> 
          </ul>
    </div>
</template>
<script>
export default {
  name: "Info",
   props: {
    info:{
         default:[
             "您已加入XXX团队",
             "您已被踢出XXX团队",
             "您已退出XXX团队"
         ]
    } 
   
    }
    ,
  data(){
      return{
      }
  },
  mounted:{

  },
  methods:{
  }
}; 
</script>
<style scoped>
</style>
