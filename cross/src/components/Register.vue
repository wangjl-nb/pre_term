<template>
  <div class="login">
    <el-header style="height: 110px"></el-header>
    <el-main>
      <el-row :gutter="20">
        <el-col :span="10" style="height: 18em;text-align: right">
          <img src="../assets/logo/logo01.png" style="width:35em;height:25em">
        </el-col>
      <el-col :span="12" >
        <div class="grid-content">
          <!--card-->
          <el-card class="box-card" style="margin:0px auto; top:50%">
            <div slot="header" class="clearfix">
              <div>
                <h1 class="change-color" style="font-weight:lighter ">
                  <li>
                    <svg class="icon" aria-hidden="true" style="width:2em;height:2em">
                      <use xlink:href="#icon-rengongzhinengjiqiren"></use>
                    </svg>
                    注册
                  </li>
                </h1>
              </div>
            </div>
            <!--form-->
            <div>
              <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="70px" class="demo-ruleForm">
                 
                <el-form-item label="用户名" prop="username">
                  <el-input v-model.number="ruleForm.username" placeholder="请输入用户名"></el-input>
                </el-form-item>
                <el-form-item
                  prop="email"
                  label="邮箱"
                  :rules="[{ required: true, message: '请输入邮箱地址', trigger: 'blur' },
                            { type: 'email', message: '请输入正确的邮箱地址', trigger: ['blur', 'change'] }]">
                  <el-input v-model="ruleForm.email" placeholder="请输入邮箱"></el-input>
                </el-form-item>
                <input type="password" style="width: 1px; height: 1px; position: absolute; border: 0px; padding: 0px;">
                <el-form-item label="密码" prop="pass">
                  <el-input type="password" v-model="ruleForm.pass" autocomplete="new-password" placeholder="请输入密码" show-password></el-input>
                </el-form-item>
                <el-form-item label="确认密码" prop="checkPass">
                  <el-input type="password" v-model="ruleForm.checkPass" autocomplete="off" placeholder="请再次输入密码" show-password></el-input>
                </el-form-item>
                <el-form-item>
                  <button class="btn-7" @click="submitForm('ruleForm')">提交</button>
                  <el-link style="float: right"><a href="/login">已有账号？点我登陆</a></el-link>
                </el-form-item>
              </el-form>
            </div>
          </el-card>
        </div>
      </el-col>
      </el-row>
    </el-main>
    <el-footer></el-footer>
  </div>
</template>
 
<script>
  export default {
    data() {

      var checkUsername = (rule, value, callback) => {
        if (!value) {
          callback(new Error('用户名不能为空'));
        }
        else {
          callback();
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
      var validatePass2 = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请再次输入密码'));
        } else if (value !== this.ruleForm.pass) {
          callback(new Error('两次输入密码不一致!'));
        } else {
          callback();
        }
      };
      return {
        i:"",
        p:"",
        imageUrl: '',
        ruleForm: {
          pass: '',
          checkPass: '',
          username: '',
          email: ''
        },
        rules: {
          pass: [
            { validator: validatePass, trigger: 'blur' }
          ],
          checkPass: [
            { validator: validatePass2, trigger: 'blur' }
          ],
          username: [
            { validator: checkUsername, trigger: 'blur' }
          ],
        }
      }
    },
    methods: {
      // submit button
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            this.$axios.post('/app/register/',
              this.qs.stringify({
                u_username: this.ruleForm.username,
                u_password: this.ruleForm.pass,
                u_email: this.ruleForm.email
              }), {headers: {'Content-Type': 'application/x-www-form-urlencoded'}})
            .then(res => {
              console.log(res)
              if(res.data.status === 0){
                this.$message({
                  message: '注册成功',
                  type: 'success'
                })
                this.$router.push({path: '/login'})
              }
              else {
                this.$message.error('注册失败')
              }
            })
              // this.$router.push({path:"/login"})
          } else {
            console.log('error submit!!');
            return false;
          }
        });
      },
      // update picture button
      handleAvatarSuccess(res, file) {
        this.imageUrl = URL.createObjectURL(file.raw);
      },
      beforeAvatarUpload(file) {
        const isJPG = file.type === 'image/jpeg';
        const isLt2M = file.size / 1024 / 1024 < 2;

        if (!isJPG) {
          this.$message.error('上传头像图片只能是 JPG 格式!');
        }
        if (!isLt2M) {
          this.$message.error('上传头像图片大小不能超过 2MB!');
        }
        return isJPG && isLt2M;
      }
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
  /*&:last-child {*/
  /*   margin-bottom: 0;*/
  /* }*/
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
  .avatar-uploader .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
  }
  .avatar-uploader .el-upload:hover {
    border-color: #409EFF;
  }
  .avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 178px;
    height: 178px;
    line-height: 178px;
    text-align: center;
  }
  .avatar {
    width: 178px;
    height: 178px;
    display: block;
  }
</style>

