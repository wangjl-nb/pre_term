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
            <wang-enduit v-model="ruleForm.content"></wang-enduit>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="quitChange">退出修改</el-button>
          </el-form-item>
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
      changeFileInterval: 0,
    }
  },
  beforeMount() {
    this.getContent()
  },
  mounted() {
    alert('修改文档时会自动保存，且他人不会在您修改时修改文档，请在修改之后点击下方的“返回修改”按钮，便于他人继续修改')
    this.changeFileInterval = setInterval(() => {
      this.submitForm('ruleForm')
    }, 1000)
  },
  beforeDestroy() {
    clearInterval(this.changeFileInterval)
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
    quitChange() {
      this.$confirm('确定退出修改吗？','提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
      }).then(() => {
        this.$axios.get('/app/abandon_change_power/',
          {
            params: {
              id: this.$route.params.fileId
            },
            headers: {'Content-Type': 'application/x-www-form-urlencoded'},
          }).then(res => {
          console.log(res)
            if(res.data.status === 0){
              alert('退出修改成功')
              this.$router.go(-1)
            }
            else{
              alert('退出修改失败')
            }
        })
      })

    }
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
