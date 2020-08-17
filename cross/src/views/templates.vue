<template>
  <div style="width:80%">
    <el-row :gutter="40" >
  <el-col :span="6" v-for="(item, index) in list" :key="index" style="margin-top:30px">
    <el-card :body-style="{ padding: '0px' }">
    <div class="demo-image__preview">
  <el-image 
    :src="'/media/'+item.img" 
        style="width:100%;height:150px" 
    :preview-src-list="[item.img]">
  </el-image>
</div>
      <div style="padding: 14px;">
        <span>
          <el-button type="text" style="color:black" plain @click="dialogVisible = true">{{item.title}}</el-button>
          <el-dialog
  title="新建文档"
  :visible.sync="dialogVisible"
  width="30%">
    <el-button @click="dialogVisible = false;">取 消</el-button>
    <el-button @click="$router.push({path: '/templatepreview/'+item.id})">预 览</el-button>
    <el-button type="primary" @click="newDocument(item.id,team_id)">确 定新建</el-button>
</el-dialog>
        </span>
        <div class="bottom clearfix">
          <div class="flex flex6">
            <div> 
              <el-rate
  v-model="item.score"
  disabled
  show-score
  text-color="#ff9900"
  score-template="{value}">
</el-rate>
            </div>
              <div style="margin-left:10px" >
              <el-popover
  v-show="item.myscore==-1" 
  trigger="click"
  placement="bottom"
  width="250"
>
  <div class="flex flex6">
  <el-rate
    v-model="item.value2"
    :colors="colors">
  </el-rate>
    <el-button plain  @click="pingfen(item.id,item.value2)">发布</el-button>
</div>
  <el-button type="text" slot="reference">评分</el-button>
</el-popover>
            </div> 
          </div>
          <div v-show="item.myscore!=-1" class="flex flex6">
<el-rate 
  v-model="item.myscore"
  disabled
  show-score
  text-color="#ff9900"
  score-template="{value}">
</el-rate>
<span style="font-size:12px;color:gray;margin-left:7px">个人评分</span>
          </div>
          <p style="color:gray;font-size:13px">已经被{{item.accept_num}}位作者采纳</p>
       
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
  name: "Templates ",
  data(){
      return{
           dialogVisible: false,
           team_id:0,
        visible:false,
           list:[]
      }
  },
  mounted(){
    this.team_id=this.$route.params.teamId
//15 初始化模板信息
     this.$axios.post('/app/get_templetes/',
              {headers: {'Content-Type': 'application/x-www-form-urlencoded'}})
              .then(res => {
                console.log(res)
                this.list=res.data.templetes_list
              })
  },
  methods:{
    newDocument(templete_id,team_id){
                  //4 不基于模板创建文档
      this.$axios.post('/app/create_file/',
              this.qs.stringify({
                templete_id:templete_id,
                team_id:team_id
              }),
              {headers: {'Content-Type': 'application/x-www-form-urlencoded'}})
              .then(res => {
                console.log(res)
                  this.$router.push({path:"/editor/"+res.data.id})
              })
      },
    pingfen(id,value){
         //6 给模板评分
     this.$axios.post('/app/grade_templetes/',
              this.qs.stringify({
                id:id,
                score:value
              }),
              {headers: {'Content-Type': 'application/x-www-form-urlencoded'}})
              .then(res => {
                console.log(res)
                if(res.data.status==0){
                 this.$router.go(0);
                   this.$message({
          message: '评分成功',
          type: 'success'
        });
                }else{
                   this.$message.error('您已经评分过了');
                }
              })
      this.visible=false
    },
  }
};
</script>

<style scoped>
  .time {
    font-size: 13px;
    color: #999;
  }
    .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }

  .image {
    width: 100%;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }
  
  .clearfix:after {
      clear: both
  }
</style>