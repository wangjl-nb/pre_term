<template>
	<div>
		<el-form
						:model="ruleForm"
						:rules="rules"
						ref="ruleForm"
						label-width="100px"
						class="demo-ruleForm"
		>
			<!--              修改头像-->
				<el-form-item label="头像" prop="dialogImage">
					<el-upload
									action="https://jsonplaceholder.typicode.com/posts/"
									list-type="picture-card"
									:limit="1"
									:file-list="ruleForm.icon"
									:on-remove="handleRemove"
									:on-preview="handlePictureCardPreview"
									:before-upload="beforeImageUpload"
									:http-request="uploadImage"
									:on-exceed="handleExceed"
									:auto-upload="true"
					>
						<i class="el-icon-plus"></i>
					</el-upload>
				</el-form-item>
				<h3 style="color: darkorange; text-align: center">上传的图片不能超过2MB</h3>
				<el-form-item>
					<el-button type="primary" @click="submitForm('ruleForm')">上传</el-button>
				</el-form-item>

<!--				<el-button index="/profile">返回个人信息页面</el-button>-->
		</el-form>
	</div>
</template>

<script>
	export default {
		name: "ChangeIcon",
		data() {
			return {
				dialogVisible: false,
				ruleForm: {
					dialogImage: false,
					icon: [],
				},
				rules: {
					dialogImage: { required: true, message: "请上传头像", trigger: "change" }
				}
			}
		},
		methods: {
			//图片上传之前检验
			beforeImageUpload(file) {
				let testmsg=file.name.substring(file.name.lastIndexOf('.')+1)
				const isJpg = testmsg === 'jpg' || testmsg === 'png'
				if (!isJpg) {
					this.$message.error('上传图片只能是 jpg 或 png 格式!')
					return false
				}
				const isLt2M = file.size / 1024 / 1024 < 2
				if (!isLt2M) {
					this.$message.error('上传图片大小不能超过 2MB!')
					return false
				}
				this.dialogImage = true;
				return true
				// return false // (返回false不会自动上传)
			},
			handlePictureCardPreview(file) {
				this.dialogImage = true
				this.dialogVisible = true
			},
			handleRemove(file, fileList) {
				for(var i = 0; i < this.ruleForm.icon.length; i++){
					if(this.ruleForm.icon[i].url === file.url){
						//      deleteImageReport(this.fileList[i].id).then(res =>{
						//       this.$message.success('删除图片成功')
						//      })
						this.ruleForm.icon.splice(i, 1)
					}
				}
			},
//上传图片
			uploadImage(image){
				var that=this
				this.$axios({
					url:"/upload/pic",
					method:"get",
					params:{
						icon:image.file
					}
				}).then(res =>{
					// that.ruleForm.icon.push({name:"头像",url:res.data.url})
				})
			},
			handleExceed: function () {
				this.$alert('请先删除选择的图片，再上传  。最多上传一张', '提示', {
					type: 'warning'
				});
			},
			submitForm(formName) {
				this.$refs[formName].validate((valid) => {
					if (valid && this.dialogImage) {
						alert('修改成功');
					} else {
						alert('请上传头像');
						return false;
					}
				});
			},
		}
	}
</script>

<style scoped>

</style>