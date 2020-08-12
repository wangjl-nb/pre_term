<template>
  <div style="width:80%">
    <el-row :gutter="40" >
  <el-col :span="6" v-for="(o, index) in 11" :key="index" style="margin-top:30px">
    <el-card :body-style="{ padding: '0px' }">
    <div class="demo-image__preview">
  <el-image 
    src="https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg" 
        style="width:100%;height:150px" 
    :preview-src-list="srcList">
  </el-image>
</div>
      
      <div style="padding: 14px;">
        <span><a href="/docoment/123">模板名字</a></span>
        <div class="bottom clearfix">
          <p>
              <el-rate
  v-model="value"
  disabled
  show-score
  text-color="#ff9900"
  score-template="{value}">
</el-rate>
          </p>
          <p style="color:gray;font-size:13px">已经被101位作者采纳</p>
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
          value:3.7,
             srcList: [
          'https://fuss10.elemecdn.com/8/27/f01c15bb73e1ef3793e64e6b7bbccjpeg.jpeg',
        ]
      }
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