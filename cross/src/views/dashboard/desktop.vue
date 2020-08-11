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
  name: "Desktop",
  components: {
    showDocuments,
    createDocument
  },
  data(){
      return{
        list:  [{name:"jac324kff",id:123243,author:"mala",create:"2020/2/2",edit:"2020/2/4"},
        {name:"jac432asdk",id:12322342,author:"masla",create:"2020/2/2",edit:"2020/2/4"},
        {name:"jac423sdak",id:12324332,author:"malsa",create:"2020/2/2",edit:"2020/2/4"}
        ]  
      }
  },
  mounted(){

  }
};
</script>
<style scoped>
</style>
