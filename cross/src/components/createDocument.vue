<template>
    <div>
          <p>
               <el-button plain @click="newDocument(0,teamId)">新建文档</el-button>
          </p>
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
        DocumentId:123,
        dialogVisible: false,
        form:{
          name:""
        }
      }
  },
  mounted:{

  },
  methods:{
      newDocument(template_id,teamId){
            //4 不基于模板创建文档
     this.$axios.post('/app/create_file/',
              this.qs.stringify({
                templete_id:template_id,
                team_id:teamId
              }),
              {headers: {'Content-Type': 'application/x-www-form-urlencoded'}})
              .then(res => {
                console.log(res)
                  this.$router.push({path:"/editor/"+res.data.id})
              })
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
