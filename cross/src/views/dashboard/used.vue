<template>
  <el-container>
  <el-main class="dashboard" > 
    <div style="height:550px">
       <el-row :span="24" :gutter="20" v-for="(item,index) in list" :key="index">  
        <el-col :span="18" >
           <el-card shadow="hover" >
               <div class="flex flex6">
                   <div style="margin-top:0px">  
                        <i class="iconfont icon-wenjian" style="font-size:40px"></i> 
                  </div> 
                    <div style="margin-left:20px;margin-top:0px">   
                        <a style="font-size:18px" :href="'/editor/'+item.id">
                          <h3>{{item.title}}</h3>
                          <p style="color:gray;font-size:13px">于{{item.create_date}}  {{item.creator}}创建   最后一次更新为{{item.u_username}}编辑于{{item.change_date}}</p>
                        </a>
                    </div>
               </div>
                  
           </el-card>
        </el-col> 
    </el-row>
    </div> 
      <el-row>
  <el-col :span="2"><div class="grid-content "></div></el-col>
  <el-col :span="16">
    <div class="grid-content ">
      <el-button type="text" v-for="(item,index) in pages" :key="index" style="margin-right:30px" @click="goto(index+1)">
        <svg class="icon" aria-hidden="true" style="font-size:20px">
            <use :xlink:href="'#icon-icon-test'+indexs[index]"></use>
        </svg>
      </el-button>
    </div>
  </el-col>
  <el-col :span="4"><div class="grid-content"></div></el-col>
</el-row>
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
        type:1,
        indexs:['',1,2,3,4,5,6,7,8],
        pages:1,
        list:  []  ,
        perpage:5
      }
  },
  mounted(){
    this.$axios.get('/app/my_files_list/', {
      params: {
        type:this.type,
        page: 1,
        perpage: this.perpage,
      },
      // headers: {'Content-Type': 'application/x-www-form-urlencoded'}
    })
        .then(res => {
      this.list = res.data.documentList,
      this.pages=res.data.pages
      if(this.pages==1&&this.list.length==0)
      this.pages=0
    })
  },
  methods:{
    goto(index){
       this.$axios.get('/app/my_files_list/', {
      params: {
        type: this.type,
        page: index,
        perpage: this.perpage,
      },
      // headers: {'Content-Type': 'application/x-www-form-urlencoded'}
    })
        .then(res => {
      this.list = res.data.documentList
    })
    }
  }
};
</script>
<style scoped>
 .el-row {
    margin-bottom: 20px;
    &:last-child {
      margin-bottom: 0;
    }
  }
  .el-col {
    border-radius: 4px;
  }
  .bg-purple-dark {
    background: #99a9bf;
  }
  .bg-purple {
    background: #d3dce6;
  }
  .bg-purple-light {
    background: #e5e9f2;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }
</style>
