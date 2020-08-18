<template>
    <div>
        <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
            <el-form-item label="用户名" prop="username">
                <el-input v-model="ruleForm.username"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button class="btn-7"  @click="submitForm('ruleForm')">修改</el-button>
                <!--				<el-button index="/profile">返回个人信息页面</el-button>-->
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
    export default {
        name: "ChangeUsername",
        inject: ['reload'],
        data() {
            return {
                ruleForm: {
                    username: '',
                },
                rules: {
                    username: [
                        {required: true, message: '请输入用户名', trigger: 'blur'},
                    ],
                }
            }
        },
        methods: {
            submitForm(formName) {
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        console.log('legal')
                        this.$axios.post('/app/change_name/',
                                this.qs.stringify({u_username: this.ruleForm.username}),
                            {headers: {'Content-Type': 'application/x-www-form-urlencoded'}})
                            .then(res => {
                                if (res.data.status === 0) {
                                   this.$message(res.data.msg)
                                   setTimeout(() => {
                                     this.$router.push({
                                      path:"/diamond/profile/"
                                     });
                                   }, 500)
                                }
                                else{
                                    this.$message.error('修改用户名失败，用户名已存在');
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