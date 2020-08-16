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
  name: "Own",
  components: {
    showDocuments,
    createDocument
  },
  data(){
      return{
        list:  []
      }
  },
  mounted(){
    this.$axios.get('/app/my_files_list/', {
      params: {
        type: 2,
        page: 1,
        perpage: 5,
      },
      // headers: {'Content-Type': 'application/x-www-form-urlencoded'}
    })
        .then(res => {
          console.log(res)
      this.list = res.data.documentList
    })
  }
};
</script>
<style scoped>
</style>
