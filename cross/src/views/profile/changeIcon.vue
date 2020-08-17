<template>
	<div style="text-align: center">
		<el-form :model="form">
			<el-form-item :label-width="formLabelWidth"
										ref="uploadElement">
				<el-upload ref="upload"
									 action="#"
									 accept="image/png,image/gif,image/jpg,image/jpeg"
									 list-type="picture-card"
									 :limit=limitNum
									 :auto-upload="false"
									 :on-exceed="handleExceed"
									 :before-upload="handleBeforeUpload"
									 :on-preview="handlePictureCardPreview"
									 :on-remove="handleRemove"
									 :on-change="imgChange">
					<i class="el-icon-plus"></i>
				</el-upload>
			</el-form-item>
			<el-form-item>
			  <button class="btn-7" size="small" type="primary" @click="uploadFile">上传</button>
				
			</el-form-item>
		</el-form>
	</div>
</template>

<script>
	export default {
		data () {
			return {
				formLabelWidth: '80px',
				limitNum: 1,
				form: {},
			}
		},
		methods: {
			// 上传文件之前的钩子
			handleBeforeUpload (file) {
				if (!(file.type === 'image/png' || file.type === 'image/gif' || file.type === 'image/jpg' || file.type === 'image/jpeg')) {
					this.$notify.warning({
						title: '警告',
						message: '请上传格式为image/png, image/gif, image/jpg, image/jpeg的图片'
					})
				}
				let size = file.size / 1024 / 1024 / 2
				if (size > 2) {
					this.$notify.warning({
						title: '警告',
						message: '图片大小必须小于2M'
					})
				}
				let fd = new FormData();//通过form数据格式来传
				fd.append("u_icon", file); //传文件
				console.log(fd.get('u_icon'));
				this.$axios({
					url: '/app/change_icon/',
					method: "post",
					data: fd,
					headers: {
						'Content-Type': 'multipart/form-data'
					}
				}).then((res) => {
					if (res.data.status === 0) {
                        this.$message("修改成功")
                        this.$router.push({
                            path:"/diamond/profile/"
                        });
                    }
                    else{
                        this.$message.error('修改用户名失败，请检查网络配置');
                    }
				})
			},
			// 文件超出个数限制时的钩子
			handleExceed (files, fileList) {

			},
			// 文件列表移除文件时的钩子
			handleRemove (file, fileList) {
				this.hideUpload = fileList.length >= this.limitNum;

			},
			// 点击文件列表中已上传的文件时的钩子
			handlePictureCardPreview (file) {
				this.dialogImageUrl = file.url;
				this.dialogVisible = true;
			},
			uploadFile () {
				this.$refs.upload.submit()
        this.$router.go(0)
			},
			imgChange (files, fileList) {
				this.hideUpload = fileList.length >= this.limitNum;
				if (fileList) {
					this.$refs.uploadElement.clearValidate();
				}
			},
		}
	}
</script>

<style scoped>

</style>