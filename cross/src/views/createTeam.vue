<template>
<div>
 <el-card shadow="hover" style="width:70%;position:relative;margin-top:10%"> 
      <div>
 <el-form :model="ruleForm" label-position="top" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
  <el-form-item label="" prop="name" >
    <p class="change-color"><i>团队名称</i></p>
    <el-input v-model="ruleForm.name"></el-input>
  </el-form-item>
  <el-form-item label="" prop="desc">
      <p class="change-color"><i>团队描述</i></p> 
    <el-input type="textarea"  autosize v-model="ruleForm.desc"></el-input>
  </el-form-item>
  <el-form-item>
    <el-button type="primary" @click="submitForm('ruleForm')">立即创建</el-button>
  </el-form-item>
</el-form>
</div> 
    </el-card>
</div>
</template>

<script>
// @ is an alias to /src

export default {
  name: "CreateTeam",
  data(){
      return{
        team_id:0,
            ruleForm: {
          name: '',
          desc: ''
        },
        rules: {
          name: [
            { required: true, message: '请输入团队名称', trigger: 'blur' },
          ],
          desc: [
            { required: true, message: '请填写团队描述', trigger: 'blur' }
          ]
        }
      }
  },
  mounted(){

  },
     methods: {
      submitForm(formName) {
        var that=this
        this.$refs[formName].validate((valid) => {
          if (valid) {
                  //21 创建团队
     this.$axios.post('/app/create_team/',
              this.qs.stringify({
                name:this.ruleForm.name,
                discribe:this.ruleForm.desc,
                icon:"https://p1.ssl.qhimgs1.com/sdr/400__/t0160546366d509d2eb.jpg" 
              }),
              {headers: {'Content-Type': 'application/x-www-form-urlencoded'}})
              .then(res => {
                console.log(res)
                if(res.data.status==0)
                   that.$router.push({path:"/diamond/dashboard/team/"+res.data.id})
                else{
                    this.$message.error('创建团队失败');
                }
              })
          } else {
            console.log('error submit!!');
            return false;
          }
        });
      }
    }
};
</script>
<style scope>
</style>
