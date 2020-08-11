<template>
  <el-container class="router">
       <el-header style="background:#fafbfc;height:150px;padding-top:30px" >
                <div class="flex flex6" >
                   <div style="">  
                        <svg class="icon" aria-hidden="true" style="width:4em;height:4em">
                            <use xlink:href="#icon-project"></use>
                        </svg> 
                  </div> 
                    <div style="margin-left:20px">       
                        <h1 class="change-color" style="font-weight:lighter "><i>团队名字</i></h1> 
                    </div>
                    <el-button type="danger" plain>解散团队</el-button>
               </div>
        
       </el-header>
  <el-main > 
      cd
  </el-main>
   <el-aside width="200px">Aside</el-aside>
   <el-footer>
       <el-card class="box-card">
  <div slot="header" class="clearfix">
    <span>卡片名称</span>
    <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>
  </div>
  <div v-for="o in 4" :key="o" class="text item">
    {{'列表内容 ' + o }}
  </div>
</el-card>

   </el-footer>
</el-container>
</template>

<script>
// @ is an alias to /src

export default {
  name: "TeamInfo",
 
  data(){
      return{
        list:  [{name:"jac324kff",id:123243,author:"mala",create:"2020/2/2",edit:"2020/2/4"},
        {name:"jac432asdk",id:12322342,author:"masla",create:"2020/2/2",edit:"2020/2/4"},
        {name:"jac423sdak",id:12324332,author:"malsa",create:"2020/2/2",edit:"2020/2/4"}
        ]  
      }
  },
  mounted:{

  }
};
</script>
<style scoped>
</style>
