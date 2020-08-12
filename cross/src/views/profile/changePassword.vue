<template>
	<div>
		<el-form :model="ruleForm" :rules="ruless" ref="ruleForm" label-width="100px" class="demo-ruleForm">
			<el-form-item label="请输入原密码" prop="oldPassword">
				<el-input v-model="ruleForm.oldPassword"></el-input>
			</el-form-item>
			<el-form-item label="请输入新密码" prop="password">
				<el-input v-model="ruleForm.password"></el-input>
			</el-form-item>
			<el-form-item label="请确认新密码" prop="checkPassword">
				<el-input v-model="ruleForm.checkPassword"></el-input>
			</el-form-item>
			<el-form-item>
				<el-button type="primary" @click="submitForm('ruleForm')">修改</el-button>
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
				ruless: {
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
						alert('修改成功');
					} else {
						console.log('修改失败');
						return false;
					}
				});
			},
		}
	}
</script>

<style scoped>

</style>