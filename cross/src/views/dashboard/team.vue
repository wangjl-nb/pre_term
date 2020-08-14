<template>
  <el-container >
  <el-main class="dashboard">
    <el-row>
          <el-col :span="24" v-for="(item,index) in teams" :key="index">
               <el-divider></el-divider>
              <div class="flex flex7">
                   <div style="margin-top:-10px;flex-grow: 1;">  
                        <svg class="icon" aria-hidden="true" style="width:3em;height:3em">
                            <use :xlink:href="item.icon" ></use>
                        </svg>
                  </div> 
                    <div style="margin-left:0px;margin-top:-14px;flex-grow:32;"  >
                 <a style="font-size:18px" :href="'team/'+item.id">{{item.name}}</a>
                <el-card shadow="never" style="margin-top:10px" > 
                <p style="margin:-6px 0">{{item.description}}</p>
               </el-card>

                        
                    </div>
               </div>
          </el-col>
    </el-row>
  </el-main>
</el-container>
</template>

<script>
// @ is an alias to /src


export default {
  name: "Team",
  data(){
      return{
          owner:"#icon-guanli ",
          people:"#icon-zhanghaoguanli",
          teams:[
              {icon:"#icon-guanli",name:"sddfhdsss",context:"团队描述",id:234},
              {icon:"#icon-zhanghaoguanli",name:"sddsdfgdss",context:"团队描述",id:3463345}
          ]
      }
  },
  mounted() {
    this.$axios.post('/app/my_teams', )
            .then(res => {
      this.teams = res.data.teams;
      for(let i = 0;i < this.teams.length;i++){
        if(this.teams[i].level === 1){
          this.teams[i]['icon'] = this.people
        }
        else{
          this.teams[i]['icon'] = this.owner
        }
      }
    })
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
