<template>
    <div>
        <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
            <el-form-item label="用户名" prop="username">
                <el-input v-model="ruleForm.username"></el-input>
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
        name: "ChangeUsername",
        data() {
            return {
                ruleForm: {
                    username: '',
                },
                rules: {
                    username: [
                        {required: true, message: '请输入用户名', trigger: 'blur'},
                        {min: 2, max: 8, message: '长度在 2 到 8 个字符', trigger: 'blur'}
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
                                console.log(res)
                                if (res.data.status === 0) {
                                    alert(res.data.msg)
                                } else {
                                    alert(res.data.msg)
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