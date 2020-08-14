<template>
  <div style="width:80%">
    <el-row :gutter="40" >
  <el-col :span="6" v-for="(item, index) in list" :key="index" style="margin-top:30px">
    <el-card :body-style="{ padding: '0px' }">
    <div class="demo-image__preview">
  <el-image 
    :src="item.jpg" 
        style="width:100%;height:150px" 
    :preview-src-list="item.srcList">
  </el-image>
</div>
      <div style="padding: 14px;">
        <span>
          <el-button type="text" style="color:black" plain @click="dialogVisible = true">{{item.name}}</el-button>
          <el-dialog
  title="新建文档"
  :visible.sync="dialogVisible"
  width="30%">
 <el-form ref="form" :model="form" label-width="80px">
  <el-form-item label="文档名称">
    <el-input v-model="form.name"></el-input>
  </el-form-item>
 </el-form>
  <span slot="footer" class="dialog-footer">
    <el-button @click="dialogVisible = false;form.name=''">取 消</el-button>
    <el-button type="primary" @click="newDocument(form.name,item.id)">确 定</el-button>
  </span>
</el-dialog>
        </span>
        <div class="bottom clearfix">
          <div class="flex flex6">
            <div> 
              <el-rate
  v-model="item.value"
  disabled
  show-score
  text-color="#ff9900"
  score-template="{value}">
</el-rate>
            </div>
            <div style="margin-left:10px">
              <el-popover
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
          <p style="color:gray;font-size:13px">已经被{{item.number}}位作者采纳</p>
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
        form:{
          name:""
        },
        visible:false,
        list:[ 
          {id:123,jpg:'https://fuss10.elemecdn.com/8/27/f01c15bb73e1ef3793e64e6b7bbccjpeg.jpeg',name:"模板名字",value:3.45,value2:null,number:11,srcList:["https://fuss10.elemecdn.com/8/27/f01c15bb73e1ef3793e64e6b7bbccjpeg.jpeg"]},
           {id:123,jpg:'https://fuss10.elemecdn.com/8/27/f01c15bb73e1ef3793e64e6b7bbccjpeg.jpeg',name:"模板名字",value:3.45,value2:null,number:11,srcList:["https://fuss10.elemecdn.com/8/27/f01c15bb73e1ef3793e64e6b7bbccjpeg.jpeg"]},
            {id:123,jpg:'https://fuss10.elemecdn.com/8/27/f01c15bb73e1ef3793e64e6b7bbccjpeg.jpeg',name:"模板名字",value:3.45,value2:null,number:11,srcList:["https://fuss10.elemecdn.com/8/27/f01c15bb73e1ef3793e64e6b7bbccjpeg.jpeg"]},
             {id:123,jpg:'https://fuss10.elemecdn.com/8/27/f01c15bb73e1ef3793e64e6b7bbccjpeg.jpeg',name:"模板名字",value:3.45,value2:null,number:11,srcList:["https://fuss10.elemecdn.com/8/27/f01c15bb73e1ef3793e64e6b7bbccjpeg.jpeg"]},
              {id:123,jpg:'https://fuss10.elemecdn.com/8/27/f01c15bb73e1ef3793e64e6b7bbccjpeg.jpeg',name:"模板名字",value:3.45,value2:null,number:11,srcList:["https://fuss10.elemecdn.com/8/27/f01c15bb73e1ef3793e64e6b7bbccjpeg.jpeg"]},
               {id:123,jpg:'https://fuss10.elemecdn.com/8/27/f01c15bb73e1ef3793e64e6b7bbccjpeg.jpeg',name:"模板名字",value:3.45,value2:null,number:11,srcList:["https://fuss10.elemecdn.com/8/27/f01c15bb73e1ef3793e64e6b7bbccjpeg.jpeg"]},
                {id:123,jpg:'https://fuss10.elemecdn.com/8/27/f01c15bb73e1ef3793e64e6b7bbccjpeg.jpeg',name:"模板名字",value:3.45,value2:null,number:11,srcList:["https://fuss10.elemecdn.com/8/27/f01c15bb73e1ef3793e64e6b7bbccjpeg.jpeg"]},
                 {id:123,jpg:'https://fuss10.elemecdn.com/8/27/f01c15bb73e1ef3793e64e6b7bbccjpeg.jpeg',name:"模板名字",value:3.45,value2:null,number:11,srcList:["https://fuss10.elemecdn.com/8/27/f01c15bb73e1ef3793e64e6b7bbccjpeg.jpeg"]},
                  {id:123,jpg:'https://fuss10.elemecdn.com/8/27/f01c15bb73e1ef3793e64e6b7bbccjpeg.jpeg',name:"模板名字",value:3.45,value2:null,number:11,srcList:["https://fuss10.elemecdn.com/8/27/f01c15bb73e1ef3793e64e6b7bbccjpeg.jpeg"]}
                  , {id:123,jpg:'https://fuss10.elemecdn.com/8/27/f01c15bb73e1ef3793e64e6b7bbccjpeg.jpeg',name:"模板名字",value:3.45,value2:null,number:11,srcList:["https://fuss10.elemecdn.com/8/27/f01c15bb73e1ef3793e64e6b7bbccjpeg.jpeg"]}
        ]
      }
  },
  methods:{
      newDocument(name,template_id){
          this.aa=name
           this.aa=template_id
           var document_id=123
           this.$router.push({path:"/editor/"+document_id})
      },
    pingfen(id,value){
      this.aa=id
      this.aa=value
      this.visible=false
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