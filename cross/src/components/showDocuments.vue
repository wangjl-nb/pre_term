<template>
<div>
      <el-row :span="24" :gutter="20" v-for="(item,index) in list" :key="index">  
        <el-col :span="18">
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
</template>
  <script>
// @ is an alias to /src

export default {
      props: {
    list: {
      default:
        [{title:"jack",id:123,creator:"mala",create_date:"2020/2/2",change_date:"2020/2/4",u_username:"222xs"},
        {title:"jacasdk",id:12322,creator:"masla",create_date:"2020/2/2",change_date:"2020/2/4",u_username:"222xs"},
        {title:"jacsdak",id:12332,creator:"malsa",create_date:"2020/2/2",change_date:"2020/2/4",u_username:"222xs"}
        ]
    },
 
  },
  data() {
    return {
    }
  },
  methods: {

  
}};
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
 .flex6 {
            display: flex;
            flex-wrap: wrap;
              align-items: center;
        }


</style>