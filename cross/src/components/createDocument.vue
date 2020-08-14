<template>
    <div>
          <p>
               <el-button plain @click="dialogVisible = true">新建文档</el-button>
<el-dialog
  title="新建文档"
  :visible.sync="dialogVisible"
  width="30%">
 <el-form ref="form" :model="form" label-width="80px">
  <el-form-item label="文档名称">
    <el-input v-model="form.name"></el-input>
  </el-form-item>
 </el-form>
  <span slot="footer" class="dialog-footer">
    <el-button @click="dialogVisible = false;form.name=''">取 消</el-button>
    <el-button type="primary" @click="newDocument(form.name,0)">确 定</el-button>
  </span>
</el-dialog>
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
      newDocument(name,template_id){
            //4 不基于模板创建文档
     this.$axios.post('/app/create_file/',
              this.qs.stringify({
                template_id:template_id,
                title:name,
                content:"",
                team_id:this.teamId
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
