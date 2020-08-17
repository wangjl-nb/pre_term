<template>
<div style="background:black;height:800px">
    <div class="text" :style="backgroundDiv" style="font-size:30px;">
    <p style="padding-top:200px">对不起</p>
    <p>您没有查看该文档或团队所需要的权限</p>
    <p>或此文档已经被删除！</p>
    <p>页面将在{{counter}}秒内自动返回</p>
</div>
</div>
    
</template>
<script>
export default {
     data(){
      return{
        backgroundDiv: {
backgroundImage:'url(' + require('../assets/logo/giphy.gif') + ')',
backgroundRepeat:'no-repeat',
backgroundSize:'100% 100%'
    },
    counter: 5,

      }
  },
    mounted() {
    setInterval(() => {
      this.counter--;
      if(this.counter <= 0){
        this.$router.go(-2)
      }
    }, 1000)
  },
}
</script>
<style scoped>
main {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}
.text {
  background-size: contain;
  background-position: top left;
  -webkit-background-clip: text;
  color: transparent;
  font-size: 10rem;
  font-weight: bold;
  font-family: sans-serif;
  text-align: center
}
</style>