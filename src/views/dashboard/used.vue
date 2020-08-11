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
  name: "Used",
  components: {
    showDocuments
  },
  data(){
      return{
        list:  [{name:"jackffgf",id:123432,author:"mala",create:"2020/2/2",edit:"2020/2/4"},
        {name:"jaca324sdk",id:1232432,author:"masla",create:"2020/2/2",edit:"2020/2/4"},
        {name:"jacs234dak",id:123345672,author:"malsa",create:"2020/2/2",edit:"2020/2/4"}
        ]  
      }
  },
  mounted:{

  }
};
</script>
<style scoped>
</style>
