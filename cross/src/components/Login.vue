<template>
  <div clss = "login">
    <el-row :gutter="20">
      <el-col :span="24"><div class="grid-content"></div></el-col>
      <el-col :span="24"><div class="grid-content"></div></el-col>
      <el-col :span="24"><div class="grid-content"></div></el-col>
      <el-col :span="24"><div class="grid-content"></div></el-col>
      <el-col :span="12" :offset="6">
        <div class="grid-content">
            <!--card-->
            <el-card class="box-card" style="margin:0px auto; top:50%">
              <div slot="header" class="clearfix">
                <span>登录</span>
              </div>
              <!--form-->
              <div>
                <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="70px" class="demo-ruleForm">
                  <el-form-item label="用户名" prop="username">
                    <el-input v-model.number="ruleForm.username" placeholder="请输入用户名"></el-input>
                  </el-form-item>
                  <el-form :model="dynamicValidateForm" ref="dynamicValidateForm" label-width="70px" class="demo-dynamic">
                    <el-form-item
                      :model="dynamicValidateForm"
                      ref="dynamicValidateForm"
                      prop="email"
                      label="邮箱"
                      :rules="[{ required: false, message: '请输入邮箱地址', trigger: 'blur' },
                              { type: 'email', message: '请输入正确的邮箱地址', trigger: ['blur', 'change'] }]">
                      <el-input v-model="dynamicValidateForm.email" placeholder="请输入邮箱"></el-input>
                    </el-form-item>
                  </el-form>
                  <el-form-item label="密码" prop="pass">
                    <el-input type="password" v-model="ruleForm.pass" autocomplete="off" placeholder="请输入密码"></el-input>
                  </el-form-item>
                  <el-form-item>
                    <el-button type="primary" @click="submitForm('ruleForm')">提交</el-button>
                    <el-link><a href="/register">请先注册</a></el-link>
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
    data() {
      var checkEmail = (rule, value, callback) => {
        if (!value) {
          return callback(new Error('邮箱不能为空'));
        }
      };
      var checkUsername = (rule, value, callback) => {
        if (!value) {
          return callback(new Error('用户名不能为空'));
        }
      };
      var validatePass = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请输入密码'));
        } else {
          if (this.ruleForm.checkPass !== '') {
            this.$refs.ruleForm.validateField('checkPass');
          }
          callback();
        }
      };
      return {
        //邮箱
        dynamicValidateForm: {
          domains: [{
            value: ''
          }],
          email: ''
        },
        ruleForm: {
          email: '',
          username: '',
          pass:""
        },
        rules: {
          email: [
            { validator: checkEmail, trigger: 'blur' }
          ],
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
        this.$refs[formName].validate((valid) => {
          if (valid) {
            alert('submit!');
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

