<template>
	<div>
		<el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
			<el-form-item label="请输入原密码" prop="oldPassword">
				<el-input v-model="ruleForm.oldPassword" show-password></el-input>
			</el-form-item>
			<el-form-item label="请输入新密码" prop="password">
				<el-input v-model="ruleForm.password" show-password></el-input>
			</el-form-item>
			<el-form-item label="请确认新密码" prop="checkPassword">
				<el-input v-model="ruleForm.checkPassword" show-password></el-input>
			</el-form-item>
			<el-form-item>
				<button class="btn-7" @click="submitForm('ruleForm')">修改</button>
<!--				<el-button index="/profile">返回个人信息页面</el-button>-->
			</el-form-item>
		</el-form>
	</div>
</template>

<script>
	export default {
		name: "ChangePassword",
		data() {
			let validateOldPassword = (rule, value, callback) => {
				if (value === '') {
					callback(new Error('请输入原密码'));
				}
				// else if (value !== this.oldpwd) {
				// 	callback(new Error('原密码错误'))
				// }
				else {
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
					callback(new Error('请确认新密码'));
				} else if (value !== this.ruleForm.password) {
					callback(new Error('两次输入密码不一致!'));
				} else {
					callback();
				}
			};
			return {
				oldpwd: '',
				ruleForm: {
					oldPassword: '',
					password: '',
					checkPassword: '',
				},
				rules: {
					oldPassword: [
						{ validator: validateOldPassword, trigger: 'blur' }
					],
					password: [
						{ validator: validatePass, trigger: 'blur' }
					],
					checkPassword: [
						{ validator: validatePass2, trigger: 'blur' }
					],
				}
			}
		},
		created() {
			this.oldpwd = this.$route.params.oldpwd
			console.log(this.$route.params.oldpwd)
		},
		methods: {
			submitForm(formName) {
				this.$refs[formName].validate((valid) => {
					if (valid) {
						this.$axios.post('/app/change_password/',
								this.qs.stringify({
									old_password: this.ruleForm.oldPassword,
									new_password: this.ruleForm.password,
								}),
								{headers: {'Content-Type':'application/x-www-form-urlencoded'}})
								.then(res => {
								if (res.data.status === 0) {
                                     this.$message(res.data.msg)
                                     this.$router.push({
                                     path:"/diamond/profile/"
                                     });
                                }
                                else{
                                    this.$message.error('修改用户名失败，请检查网络配置');
                                }
								})
					} else {
						return false;
					}
				});
			},
		}
	}
</script>

<style scoped>

</style>