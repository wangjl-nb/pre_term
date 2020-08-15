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
        list:  [{title:"jac324kff",id:123243,creator:"mala",create_date:"2020/2/2",change_date:"2020/2/4",u_username:"222xs"},
          {title:"jac432asdk",id:12322342,creator:"masla",create_date:"2020/2/2",change_date:"2020/2/4",u_username:"222xs"},
          {title:"jac423sdak",id:12324332,creator:"malsa",create_date:"2020/2/2",change_date:"2020/2/4",u_username:"222xs"}
        ]
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
