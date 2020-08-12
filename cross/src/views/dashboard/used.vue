<template>
  <el-container >
  <el-main class="dashboard"> 
      <show-documents :list="list"></show-documents>
  </el-main>
   <el-aside>
    <create-document></create-document>
  </el-aside>
</el-container>
</template>
 
<script>
// @ is an alias to /src
import showDocuments from "@/components/showDocuments";
import createDocument from "@/components/createDocument";
export default {
  name: "Used",
  components: {
    showDocuments,
    createDocument
  },
  data(){
      return{
        list:  [{name:"jackffgf",id:123432,author:"mala",create:"2020/2/2",edit:"2020/2/4",user:"222xs"},
        {name:"jaca324sdk",id:1232432,author:"masla",create:"2020/2/2",edit:"2020/2/4",user:"222xs"},
        {name:"jacs234dak",id:123345672,author:"malsa",create:"2020/2/2",edit:"2020/2/4",user:"222xs"}
        ]  
      }
  },
  mounted:{

  }
};
</script>
<style scoped>
</style>
