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
									<div class="block" style="text-align: center"><el-avatar :size="100" :src="icon"></el-avatar></div>
									<el-button type="text" @click="$router.push({name: 'ChangeIcon'})">修改头像</el-button>
									<el-row :gutter="20">
										<el-col :span="24"><div class="grid-content">
											<span>用户名：</span>
											<span style="font-weight: 700; margin-right: 1rem">{{username}}</span>
											<el-button type="text" @click="$router.push({name: 'ChangeUsername'})">修改用户名</el-button>
										</div></el-col>
										<el-col :span="24"><div class="grid-content">
											<span>密码：</span>
											<el-button type="text" @click="$router.push({name: 'ChangePassword'})">修改密码</el-button>
										</div></el-col>
										<el-col :span="24"><div class="grid-content" style="margin-top: 0.4rem">
											<span>邮箱：</span>
											<span style="font-weight: 700">{{email}}</span>
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
				icon: '',
				username: '',
				password: '',
				email: ''
			};
		},

		mounted(){
			var that=this
			this.$axios({
				url:'/app/user_info/',
				method:"post",
			}).then(res=>{
					// console.log(res);
					that.icon = '/media/' + res.data.u_icon
					that.username = res.data.u_username
					that.password = res.data.u_password
					that.email = res.data.u_email
			})

			// this.$axios({
			// 	url:'/app/user_info/',
			// 	method:"post",
			// 	responseType: 'blob',
			// }).then(res=>{
			// 	console.log(res);
			// 	that.icon = window.URL.createObjectURL(res.data.u_icon)
			// })
		},
		methods: {
			//图片上传之前检验
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
