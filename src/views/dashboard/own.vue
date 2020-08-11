<template>
  <el-container>
  <el-main class="dashboard"> 
      <show-documents :list="list"></show-documents>
  </el-main>
</el-container>
</template>

<script>
// @ is an alias to /src
import showDocuments from "@/components/showDocuments";

export default {
  name: "Own",
  components: {
    showDocuments
  },
  data(){
      return{
        list:  [{name:"jackff",id:123,author:"mala",create:"2020/2/2",edit:"2020/2/4"},
        {name:"jacasdk66",id:12322666,author:"masla",create:"2020/2/2",edit:"2020/2/4"},
        {name:"jacsdawek",id:1223432,author:"malsa",create:"2020/2/2",edit:"2020/2/4"}
        ]  
      }
  },
  mounted:{

  }
};
</script>
<style scoped>
</style>
