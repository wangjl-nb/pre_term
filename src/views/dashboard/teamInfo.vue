<template>
  <el-container class="router">
       <el-header style="background:#fafbfc;height:150px;padding-top:30px" >
                <div class="flex flex6" >
                   <div style="">  
                        <svg class="icon" aria-hidden="true" style="width:4em;height:4em">
                            <use xlink:href="#icon-project"></use> 
                        </svg> 
                  </div>  
                    <div style="margin-left:20px;margin-right:30px">       
                        <h1 class="change-color" style="font-weight:lighter "><i>{{name}}</i></h1> 
                    </div>
                     <el-button plain @click="drawer = true">管理成员</el-button> 
                     <el-button plain @click="setpower()">设置团队权限</el-button>
                    <el-button type="danger" plain @click="dispose()">解散团队</el-button>
                    <el-button plain @click="join()">加入团队</el-button>
                    <el-button type="danger" plain @click="out()">退出团队</el-button>
               </div>
        
       </el-header>
        <el-container>
        <el-container>  
  <el-main >  
      <show-documents :list="list"></show-documents>
  </el-main>
    <el-aside width="200px">
       <create-document :teamId="teamId"></create-document>
    </el-aside>
      </el-container>
   <el-footer>
       <el-card class="box-card">
  <div slot="header" class="clearfix">
    <span>README</span>
    <el-button style="float: right; padding: 3px 0" type="text" @click="dialogTableVisible=true">修改</el-button>
  <el-dialog  title="修改团队信息" :visible.sync="dialogTableVisible" center :append-to-body='true' :lock-scroll="false" width="50%" @closed="handleClose">
    <el-input
  type="textarea"
  :rows="5"
  autosize
  placeholder="请输入内容"
  v-model="editTeamInfo"> 
</el-input>
 <el-button  class="medium" style="margin-left:40%;position:relative;margin-top:30px" plain @click="submitedit(editTeamInfo)">提交修改</el-button>
      </el-dialog>
  </div> 
  <pre style="font-size:20px"> 
    这里是团队信息
    写下想说的话
    {{teamInfo}}
  </pre>
</el-card>

   </el-footer>
</el-container>
  <el-drawer
    title="我是标题"
  :visible.sync="drawer"
  direction="rtl"
   :with-header="false">
  <h1 style="margin-left:100px">
    <svg class="icon" aria-hidden="true" style="width:3em;height:3em">
  <use xlink:href="#icon-shuangsechangyongtubiao-
"></use> 
</svg>
<span style="margin-top:15px;margin-left:20px;position:absolute">团队成员</span>
  </h1>
  <div style="margin-top: 15px;">

  <el-input placeholder="请输入内容" v-model="search">
    <template slot="prepend">
       <el-popover
  placement="bottom-start"
  width="400"
  trigger="click">
  <div v-if="searchItem.length>0">
 <ul v-for="(item,index) in searchItem" :key="index">
    <li style="position:relative">
      <el-avatar size="medium" :src="item.img"></el-avatar>
      <span style="font-size:17px;position:absolute;margin-top:-5px;margin-left:20px">
        {{item.name}}
        <el-button type="text" @click="invite(item.id)"> 
           <i class="el-icon-circle-plus-outline" style="font-size:20px"></i> 
        </el-button>
       
        </span>
    </li>
  </ul>
  </div>
   <div v-else> 
      <pre style="color:#gray;font-size:15px;font-weight:normal">                 当前搜索结果为0</pre>
    </div>
      <el-button slot="reference">
         <svg class="icon" aria-hidden="true" style="width:2em;height:2em">
             <use xlink:href="#icon-shuangsechangyongtubiao-1"></use>
         </svg>
      </el-button>
        </el-popover>
    </template>
  </el-input>

</div>
<div>
  <div style="position:relative;margin-left:40px">  
      <svg class="icon" aria-hidden="true" style="width:2em;height:2em">
      <use xlink:href="#icon-gerenguanli"></use>
      </svg>
      <el-avatar size="medium" :src="author.img" class="img"></el-avatar>
      <span class="user_name">
        {{author.name}}       
        </span>
  </div>
  <div>
     <ul v-for="(item,index) in searchItem" :key="index">
    <li style="position:relative">
      <svg class="icon" aria-hidden="true" style="width:2em;height:2em">
      <use xlink:href="#icon-zhanghaoguanli"></use>
      </svg>
      <el-avatar size="medium" :src="item.img" class="img"></el-avatar>
      <span class="user_name">
        {{item.name}}       
        </span>
    </li>
  </ul>
  </div>
  
</div>
</el-drawer>
  </el-container>
</template>

<script>
// @ is an alias to /src
import showDocuments from "@/components/showDocuments";
import createDocument from "@/components/createDocument";
export default {
  name: "TeamInfo",
  components: {
    showDocuments,
    createDocument
  },
  data(){
      return{
        teamId:134,
        name:"团队名字哈哈",
        editTeamInfo:"",
        teamInfo:"希望一直加油",
        dialogTableVisible: false,
        author: {id:123,img:'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',name:"sadasd"}   
        ,
        searchItem:[
           {id:123,img:'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',name:"sadasd"}   ,
            {id:123,img:'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',name:"sadasd"}   ,
             {id:123,img:'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',name:"sadasd"}   
       ],
        drawer: false,
        search:"",
        list:  [{name:"jac324kff",id:123243,author:"mala",create:"2020/2/2",edit:"2020/2/4"},
        {name:"jac432asdk",id:12322342,author:"masla",create:"2020/2/2",edit:"2020/2/4"},
        {name:"jac423sdak",id:12324332,author:"malsa",create:"2020/2/2",edit:"2020/2/4"}
        ]  
      } 
  },
  mounted(){
    var that=this
    that.teamId=that.$route.params.teamId
  },
  methods:{
     handleClose () {
       this.editTeamInfo=""
      this.dialogTableVisible=false
    },
    dispose(){
    },
    join(){

    },
    out(){

    },
    setpower(){

    },
    invite(id){
      this.aa=id
    },
    submitedit(text){
      this.dialogTableVisible=false
      this.teamInfo=text
    }
  }
};
</script>
<style scoped>
.img{
  position:relative;left:10px;top:3px
}
.user_name{
  font-size:18px;
  position:absolute;
  margin-top:6px;
  margin-left:20px
}
</style>
