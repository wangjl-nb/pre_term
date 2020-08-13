<template>
    <div>
          <p><el-button plain @click="newDocument()">新建文档</el-button></p>
          <p><el-button type="dark" plain @click="withDocument()">模板库</el-button> </p> 
    </div>
</template>
<script>
export default {
  name: "CreateDocument",
   props: {
    teamId:{
         default:0
    } 
   
    }
    ,
  data(){
      return{
        list:  [{name:"jackff",id:123,author:"mala",create:"2020/2/2",edit:"2020/2/4"},
        {name:"jacasdk66",id:12322666,author:"masla",create:"2020/2/2",edit:"2020/2/4"},
        {name:"jacsdawek",id:1223432,author:"malsa",create:"2020/2/2",edit:"2020/2/4"}
        ]  ,
        DocumentId:123,
      }
  },
  mounted:{

  },
  methods:{
      newDocument(){
          var that=this
        this.$router.push({
        path:"/Document/"+that.DocumentId+"/"+that.teamId 
      });
      },
      withDocument(){
           var that=this
          this.$router.push({
        path:"/diamond/templates/"+that.teamId 
      });
      }
  }
}; 
</script>
<style scoped>
</style>
