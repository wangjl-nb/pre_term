<template>
  <div>
    <el-row :gutter="20">
      <el-col :span="24">
        <img :src="img" />  
      </el-col> 
      <el-col :span="4"><div class="grid-content"></div></el-col>
      <el-col :span="16"> <img alt="Vue logo" style="width:920px;height:230px" src="http://www.diyiziti.com/Res/Images//Temp/119/3fac3f9573a04bc28c4d5525ca1a7097.PNG" /></el-col> 
      <el-col :span="4"><div class="grid-content"></div></el-col>
      <el-col :span="12" :offset="6">
        <div class="grid-content">
            <!--card-->
            <el-card class="box-card" style="margin:0px auto; top:50%">
              <div slot="header" class="clearfix">
                <span>登录</span>
              </div>
              <!--form-->
              <div>
                <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="70px" class="demo-ruleForm">
                  <el-form-item label="用户名" prop="username">
                    <el-input v-model="ruleForm.username" placeholder="请输入用户名"></el-input>
                  </el-form-item>
                  <el-form-item label="密码" prop="pass">
                    <el-input type="password" v-model="ruleForm.pass" autocomplete="off" placeholder="请输入密码"></el-input>
                  </el-form-item>
                  <el-form-item>
                    <el-button type="primary" @click="submitForm('ruleForm')">提交</el-button>
                    <el-link style="float: right"><a href="/register" >请先注册</a></el-link>
                  </el-form-item>
                </el-form>
              </div>
            </el-card>
        </div>
      </el-col>
    </el-row>
  </div>
</template>
<script>
  export default { 
    name:"Login",
    data() {
      // var checkEmail = (rule, value, callback) => {
      //   if (!value) {
      //     return callback(new Error('邮箱不能为空'));
      //   }
      // };
      let checkUsername = (rule, value, callback) => {
        if (!value) {
          callback(new Error('用户名不能为空'));
        }
        else{
          callback()
        }
      };
      let validatePass = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请输入密码'));
        }
        else{
          callback()
        }
        // else {
        //   if (this.ruleForm.checkPass !== '') {
        //     this.$refs.ruleForm.validateField('checkPass');
        //   }
        //   callback();
        // }
      };
      return {
        // //邮箱
        // dynamicValidateForm: {
        //   domains: [{
        //     value: ''
        //   }],
        //   email: ''
        // },
        ruleForm: {
          // email: '',
          username: '',
          pass:''
        },
        rules: {
          // email: [
          //   { validator: checkEmail, trigger: 'blur' }
          // ],
          username: [
            { validator: checkUsername, trigger: 'blur' }
          ],
          pass: [
            { validator: validatePass, trigger: 'blur' }
          ]
        },
      }
    },
    methods: {
      // submit button
      submitForm(formName) {
        console.log('submit')
        this.$refs[formName].validate((valid) => {
          if (valid) {
            console.log('legal')
                // this.$router.push({path:"/diamond/dashboard/desktop"})
            this.$axios.post('/app/login/',
              this.qs.stringify({
                username: this.ruleForm.username,
                password: this.ruleForm.pass}),
              {headers: {'Content-Type': 'application/x-www-form-urlencoded'}})
              .then(res => {
                alert(res.data.msg)
                 if (res.data.msg === '登陆成功') {
                  this.$router.push({path:"/diamond/dashboard/desktop"})
                 }
              })
          } else {
            console.log('error submit!!');
            return false;
          }
        });
      },
    }
  }
</script>
<style>
  .text {
    font-size: 14px;
  }

  .item {
    margin-bottom: 18px;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }
  .clearfix:after {
    clear: both
  }

  .box-card {
    width: 480px;
  }
  /*.el-row {*/
  /*  margin-bottom: 20px;*/
  /*  &:last-child {*/
  /*     margin-bottom: 0;*/
  /*   }*/
  /*}*/
  .el-col {
    border-radius: 4px;
  }
  .bg-purple-dark {
    background: #99a9bf;
  }
  .bg-purple {
    background: #d3dce6;
  }
  .bg-purple-light {
    background: #e5e9f2;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }
</style>

