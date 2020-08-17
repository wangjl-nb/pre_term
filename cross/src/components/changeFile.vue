<template>
  <el-row>

    <el-col :span="24">
      <div class="grid-content"></div>
    </el-col>
    <el-col :span="24">
      <el-col :span="2" class="grid-content"></el-col>
      <el-col :span="20" class="grid-content">
        <el-form
            :model="ruleForm"
            :rules="rules"
            ref="ruleForm"
            label-width="100px"
            class="demo-ruleForm">
          <el-form-item label="文件名" prop="title">
            <el-input v-model="ruleForm.title"></el-input>
          </el-form-item>
          <el-form-item label="内容">
            <!--            <div class="editor" v-model="ruleForm.content">-->
            <!--              <div ref="toolbar" class="toolbar">-->
            <!--              </div>-->
            <!--              <div ref="editor" class="text">-->
            <!--              </div>-->
            <!--            </div>-->
            <wang-enduit v-model="ruleForm.content"></wang-enduit>
          </el-form-item>
<!--          <el-form-item>-->
<!--            <el-button type="primary" @click="submitForm('ruleForm')">提交</el-button>-->
<!--          </el-form-item>-->
        </el-form>
      </el-col>
      <el-col :span="2" class="grid-content"></el-col>
    </el-col>


  </el-row>
</template>

<script>
import wangEnduit from "./wangEnduit";
import E from 'wangeditor';

export default {
  name: "ChangeFile",
  components: {
    wangEnduit
  },
  data() {
    return {
      // uploadPath,
      editor: null,
      info_: null,
      ruleForm: {
        title: '',
        content: '',
      },
      rules: {
        title: [{required: true, message: '文件名不能为空', trigger: 'change'}],
        content: [{required: true, message: '内容不能为空', trigger: 'change'}],
      },
      flag: false,
      url: '',
    }
  },
  beforeMount() {
    setInterval(() => {
      this.getContent()
    }, 1000)

  },
  mounted() {
    setInterval(() => {
      this.submitForm('ruleForm')
    }, 1000)

  },
  methods: {
    getContent() {
      this.$axios.get('/app/file_content/',
        {
          params: {
            id: this.$route.params.fileId,
          },
          headers: {'Content-Type': 'application/x-www-form-urlencoded'},
        }).then(res => {
      // console.log(res)
      if (res.data.status === 0) {
          this.ruleForm.title = res.data.title
          this.ruleForm.content = res.data.content
      }
    })
    },
    submitForm(formName) {
      console.log('2222')
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.$axios.post('/app/change_file/',
              this.qs.stringify({
                id: this.$route.params.fileId,
                title: this.ruleForm.title,
                content: this.ruleForm.content,
              }),
              {
                headers: {'Content-Type': 'application/x-www-form-urlencoded'}
              }).then(res => {
                // console.log(res)
                // this.$message(res.data.msg)
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
.editor {
  width: 100%;
  margin: 0 auto;
  position: relative;
  z-index: 0;
}

.toolbar {
  border: 1px solid #ccc;
}

.text {
  border: 1px solid #ccc;
  min-height: 500px;
}

.el-row {
  margin-bottom: 20px;

&
:last-child {
  margin-bottom: 0;
}

}
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
