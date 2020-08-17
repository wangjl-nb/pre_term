<template>
  <div>
    <div style="text-align: center">
      <span style="font-weight: 700">当前处于预览状态</span>
      <span><el-button @click="this.$router.go(-1)"> < 返回 </el-button></span>
    </div>
    <div style="text-align: center; margin-top: 2rem">
      <h3>标题：{{title}}</h3>
    </div>
    <wang-enduit v-model="content"></wang-enduit>
  </div>
</template>

<script>
import wangEnduit from "@/components/wangEnduit";

export default {
  name: "TemplatePreview",
  components: {
    wangEnduit
  },
  data() {
    return {
      title: '',
      content: '',
    }
  },
  mounted() {
    this.$axios.get('/app/template_content/', {
      params: {
        id: this.$route.params.templateid,
      },
      headers: {'Content-Type': 'application/x-www-form-urlencoded'},
    }).then(res => {
      if(res.data.status === 0){
        this.title = res.data.title
        this.content = res.data.content
      }
    })
  }
}
</script>

<style scoped>

</style>