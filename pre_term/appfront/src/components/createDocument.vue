<template>
    <div>
          <p style="margin-bottom:-40px">
          <button class="btn-6" plain @click="newDocument(0,teamId)">新建文档</button>
          </p>
         <p><button class="btn-7" style="margin-left:30px" type="dark" plain @click="withDocument()">模板库</button> </p> 
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
