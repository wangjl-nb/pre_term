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
                <el-form ref="form" :model="form" label-width="80px">
                  <el-form-item label="邮箱">
                    <el-input v-model="form.email" placeholder="请输入邮箱"></el-input>
                  </el-form-item>
                  <el-form-item label="密码">
                    <el-input v-model="form.password" placeholder="请输入密码"></el-input>
                  </el-form-item>
                  <el-form-item>
                    <el-button type="primary" @click="onSubmit">登录</el-button>
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
      return {
        form: {
          email: '',
          password: ''
        }
      }
    },
    methods: {
      onSubmit() {
        console.log('submit!');
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

