<template>
	<div>
		<el-container>
			<el-main class="dashboard">
				<el-row>
					<el-col :span="5"><div class="grid-content"></div></el-col>
<!--					<el-col :span="5"><div class="grid-content"></div></el-col>-->
					<el-col :span="8" style="background:white">
						<el-container>
							<el-main>
								<div class="center">
									<div class="block" style="text-align: center"><el-avatar :size="100" :src="circleUrl"></el-avatar></div>
									<el-button type="text" @click="$router.push('/diamond/profile/changeicon')">修改头像</el-button>
									<el-row :gutter="20">
										<el-col :span="24"><div class="grid-content">
											<span>用户名：</span>
											<span style="font-weight: 700; margin-right: 1rem">用户名</span>
											<el-button type="text" @click="$router.push('/diamond/profile/changeusername')">修改用户名</el-button>
										</div></el-col>
										<el-col :span="24"><div class="grid-content">
											<span>密码：</span>
											<el-button type="text" @click="$router.push({name: 'ChangePassword', params: {oldpwd: oldpwd}})">修改密码</el-button>
										</div></el-col>
										<el-col :span="24"><div class="grid-content" style="margin-top: 0.4rem">
											<span>邮箱：</span>
											<span style="font-weight: 700">用户邮箱</span>
										</div></el-col>
									</el-row>
								</div>
								<router-view></router-view>
							</el-main>
							<el-footer></el-footer>
						</el-container>
					</el-col>
				</el-row>
			</el-main>
		</el-container>
	</div>

</template>

<script>
	export default {
		name: 'Profile',
		data() {
			return {
				dialogImageUrl: "",
				oldpwd: '12345',
				circleUrl: "https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png",
				upload_url: 'upload/pic',
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
					that.oldpwd = res.data.password
					that.ruleForm.email=res.data.email
				}
			})
		},
		methods: {
			//图片上传之前检验
			submitForm(formName) {
				this.$refs[formName].validate(valid => {
					if (valid) {
						var that=this
						this.$axios({
							url:'user/user_info',
							method:'POST',
							data: {
								icon:that.ruleForm.jpg[0].url,
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
