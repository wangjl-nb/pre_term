<template>
  <div style="text-align: center">
    <h1>对不起，您没有查看该文档或团队所需要的权限，或查看的文档已经被删除！</h1>
    <h2>页面将在{{counter}}秒内自动返回</h2>
  </div>
</template>

<script>
export default {
  name: "Error",
  data() {
    return {
      counter: 5,
    }
  },
  mounted() {
    setInterval(() => {
      this.counter--;
      if(this.counter === 0){
        this.$router.go(-2)
      }
    }, 1000)
  },
}
</script>

<style scoped>

</style>