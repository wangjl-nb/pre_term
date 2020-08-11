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
  name: "Favorites",
  components: {
    showDocuments
  },
  data(){
      return{
        list:  [{name:"jac324kff",id:34123,author:"mala",create:"2020/2/2",edit:"2020/2/4"},
        {name:"jaca324sdk",id:134322,author:"masla",create:"2020/2/2",edit:"2020/2/4"},
        {name:"jacsda423k",id:1234332,author:"malsa",create:"2020/2/2",edit:"2020/2/4"}
        ]  
      }
  },
  mounted:{

  }
};
</script>
<style scoped>
</style>
