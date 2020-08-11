<template>
	<div>
		<el-container>
			<el-main class="dashboard">
				<el-row>
<!--					<el-col :span="5"><div class="grid-content"></div></el-col>-->
					<el-col :span="14" style="background:white">
						<el-container>
							<el-main>
								<div class="center">
									<div class="block" style="text-align: center"><el-avatar :size="100" :src="circleUrl"></el-avatar></div>
									<el-button type="text" @click="$router.push('/profile/changeicon')">修改头像</el-button>
									<el-row :gutter="20">
										<el-col :span="8"><div class="grid-content">
											<span>用户名：</span>
											<span style="font-weight: 700; margin-right: 1rem">用户名</span>
											<el-button type="text" @click="$router.push('/profile/changeusername')">修改用户名</el-button>
										</div></el-col>
										<el-col :span="8"><div class="grid-content">
											<span>密码：</span>
											<el-button type="text" @click="$router.push('/profile/changepassword')">修改密码</el-button>
										</div></el-col>
										<el-col :span="8"><div class="grid-content" style="margin-top: 0.4rem">
											<span>邮箱：</span>
											<span style="font-weight: 700">用户邮箱</span>
										</div></el-col>
									</el-row>
								</div>
							</el-main>
							<el-footer></el-footer>
						</el-container>
					</el-col>
					<el-col :span="10"><div class="grid-content">
						<router-view></router-view>
					</div></el-col>
				</el-row>
			</el-main>
		</el-container>
	</div>

</template>

<script>
	export default {
		name: 'Profile',
		data() {
			let validateUsername = (rule, value, callback) => {
				if (value === '') {
					callback(new Error('请输入用户名'));
				} else {
					if (this.ruleForm.username !== '') {
						this.$refs.ruleForm.validateField('checkPass');
					}
					callback();
				}
			};
			let validateOldPassword = (rule, value, callback) => {
				if (value === '') {
					callback(new Error('请输入原密码'));
				} else if (value !== this.oldpwd) {
					callback(new Error('原密码错误'))
				} else {
					callback();
				}
			};
			let validatePass = (rule, value, callback) => {
				if (value === '') {
					callback(new Error('请输入新密码'));
				} else {
					if (this.ruleForm.checkPassword !== '') {
						this.$refs.ruleForm.validateField('checkPassword');
					}
					callback();
				}
			};
			let validatePass2 = (rule, value, callback) => {
				if (value === '') {
					callback(new Error('请再次输入密码'));
				} else if (value !== this.ruleForm.password) {
					callback(new Error('两次输入密码不一致!'));
				} else {
					callback();
				}
			};
			return {
				dialogImageUrl: "",
				imageVisible: false,
				usernameVisible: false,
				passwordVisible: false,
				oldpwd: '',
				circleUrl: "https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png",

				upload_url: 'upload/pic',
				ruleForm: {
					ad_url: '',//上传后的图片或视频URL
					username: '',//用户名
					image:[] ,
					oldPassword: '',
					password: '',
					checkPassword: '',
					email: '',
				},
				rules: {
					username: [
						{ validator: validateUsername, trigger: 'blur'}
					],
					oldPassword: [
						{ validator: validateOldPassword, trigger: 'blur' }
					],
					password: [
						{ validator: validatePass, trigger: 'blur' }
					],
					checkPassword: [
						{ validator: validatePass2, trigger: 'blur' }
					],
				},
			};
		},

		mounted(){
			var that=this
			this.$axios({
				url:"user/user_info",
				method:"get",
				params:{
					id:'123'
				}
			}).then(res=>{
				if(res.status==200){
					console.log(res);
					that.ruleForm.image.push({name:"头像",url:res.data.img});
					that.ruleForm.username=res.data.username
					this.ruleForm.password=res.data.password
					that.oldpwd = res.data.password
					that.ruleForm.email=res.data.email
				}
			})
		},
		methods: {
			//图片上传之前检验
			beforeImageUpload(file) {
				console.log(file)
				var testmsg=file.name.substring(file.name.lastIndexOf('.')+1)
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
				// return false // (返回false不会自动上传)
			},
			// handlePictureCardPreview(file) {
			//   this.dialogImageUrl = file.url
			//   this.dialogVisible = true
			// },
			handleRemove(file, fileList) {
				this.aa=fileList
				for(var i = 0; i < this.ruleForm.jpg.length; i++){
					if(this.ruleForm.image[i].url === file.url){
						//      deleteImageReport(this.fileList[i].id).then(res =>{
						//       this.$message.success('删除图片成功')
						//      })
						this.ruleForm.image.splice(i, 1)
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
						img:image.file
					}
				}).then(res=>{
					if(res.status == 200){
						if(res.data.status == 0)
							that.ruleForm.image.push({name:"头像",url:res.data.url})
					}
					else
						that.$message("上传失败")
				})
			},
			handleExceed: function () {
				this.$alert('请先删除选择的图片或视频，再上传  。最多上传一张', '提示', {
					type: 'warning'
				});
			},
			submitForm(formName) {
				this.$refs[formName].validate(valid => {
					if (valid) {
						var that=this
						this.$axios({
							url:'user/user_info',
							method:'POST',
							data: {
								img:that.ruleForm.jpg[0].url,
								username:that.ruleForm.username,
								password:that.ruleForm.password,
							}
						}).then(res=>{
							if(res.status==200){
								if(res.data.status==0)
									alert('修改成功')
								else
									alert('未知错误')
							}
						})
					} else {
						console.log("error submit!!");
						return false;
					}
				});
			},
			handleClose(done) {
				this.$confirm('确认关闭？')
						.then(_ => {
							done();
						})
						.catch(_ => {});
			}
			// 上传成功回调
			//  handleAvatarSuccess(res, file) {
			//    alert(this.ruleForm.jpg.length)
			//   this.ruleForm.jpg=file
			//  this.ruleForm.jpg.push( res.data.url)
//    },
			// 上传前格式和图片大小限制
		}}

</script>
<style>
	.el-row {
		margin-bottom: 20px;
	&:last-child {
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
	.avatar-uploader .el-upload {
		border: 1px dashed #d9d9d9;
		border-radius: 6px;
		cursor: pointer;
		position: relative;
		overflow: hidden;
	}
	.avatar-uploader .el-upload:hover {
		border-color: #409eff;
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

	.center {
		text-align: center;
	}
</style>
