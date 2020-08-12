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
                        <a style="font-size:18px" :href="'document/'+item.id">{{item.name}}</a>
                        <p style="color:gray;font-size:13px">于{{item.create}}  {{item.author}}创建    您上一次编辑于{{item.edit}}</p>
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
        [{name:"jack",id:123,author:"mala",create:"2020/2/2",edit:"2020/2/4"},
        {name:"jacasdk",id:12322,author:"masla",create:"2020/2/2",edit:"2020/2/4"},
        {name:"jacsdak",id:12332,author:"malsa",create:"2020/2/2",edit:"2020/2/4"}
        ]
    },
  data() {
    return {
 
    };
  },
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