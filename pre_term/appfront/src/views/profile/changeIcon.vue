<template>
 <div>
  <el-form :model="form">
   <el-form-item label="上传图片" :label-width="formLabelWidth">
    <el-upload
        ref="upload"
        action="http://127.0.0.1:8000/"
        accept="image/png,image/gif,image/jpg,image/jpeg"
        list-type="picture-card"
        :limit=limitNum
        :http-request="uploadFile"
        :auto-upload="false"
        :on-exceed="handleExceed"
        :before-upload="handleBeforeUpload"
        :on-preview="handlePictureCardPreview"
        :on-remove="handleRemove">
     <i class="el-icon-plus"></i>
    </el-upload>
   </el-form-item>
<!--   <el-form-item>-->
<!--    <el-button size="small" type="primary" @click="uploadFile">立即上传</el-button>-->
<!--   </el-form-item>-->
  </el-form>
 </div>
</template>

<script>
 export default {
  name: "ChangeIcon",
  data() {
   return{
    formLabelWidth: '80px',
    limitNum: 1,
    form: {}
   }
  },
  methods: {
   // 上传文件之前的钩子
   handleBeforeUpload(file){
    console.log('before')
    let size = file.size / 1024 / 1024 / 2
    if(!(file.type === 'image/png' || file.type === 'image/gif' || file.type === 'image/jpg' || file.type === 'image/jpeg')) {
     this.$notify.warning({
      title: '警告',
      message: '请上传格式为image/png, image/gif, image/jpg, image/jpeg的图片'
     })
    }

    if(size > 2) {
     this.$notify.warning({
      title: '警告',
      message: '图片大小必须小于2M'
     })
    }
   },
   // 文件超出个数限制时的钩子
   handleExceed(files, fileList) {

   },
   // 文件列表移除文件时的钩子
   handleRemove(file, fileList) {
    console.log(file, fileList);
   },
   // 点击文件列表中已上传的文件时的钩子
   handlePictureCardPreview(file) {
    this.dialogImageUrl = file.url;
    this.dialogVisible = true;
   },
   uploadFile(fileObj) {
    let formData = new FormData()
    formData.append('icon', fileObj.file)
    console.log(formData.get("icon"))
    this.$axios.post('/app/change_icon/', {
     formData
    }, {
     headers: {"Content-type": "multipart/form-data"},
    }).then(res => {
     console.log(res)
    })
   }
  }
 }
</script>

<style scoped>

</style>