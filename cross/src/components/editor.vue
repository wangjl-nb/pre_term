<template>

  <el-container style="position:relative">
      <el-drawer
      
      :visible.sync="drawer"
      :with-header="false"
      :direction="direction"> 
    <div style="height:700px">
       <h1 style="margin-left:100px">
        <svg class="icon" aria-hidden="true" style="width:3em;height:3em">
          <use xlink:href="#icon-quanxian"></use>
        </svg>
        <span style="margin-top:15px;margin-left:20px;position:absolute">协作权限管理</span>
      </h1>
      <div style="margin-top: 15px;">
        <el-input placeholder="输入 邮箱/用户名 添加协作权限" v-model="search">
          <template slot="prepend">
             <el-popover
  placement="bottom-start"
  width="400"
  trigger="click">
  <div v-if="searchItem.length>0">
 <ul v-for="(item,index) in searchItem" :key="index">
    <li style="position:relative">
      <el-avatar size="medium" :src="item.u_icon"></el-avatar>
      <span style="font-size:17px;position:absolute;margin-top:-5px;margin-left:20px">
        {{item.u_username}}
        <el-button type="text" @click="dialogVisible = true;inviteId=item.id"> 
           <i class="el-icon-circle-plus-outline" style="font-size:20px"></i> 
        </el-button>
       
        </span>
    </li>
  </ul>
  </div>
   <div v-else> 
      <pre style="color:#gray;font-size:15px;font-weight:normal">                 当前搜索结果为0</pre>
    </div>
      <el-button slot="reference" @click="searchUser(search)"> 
         <svg class="icon" aria-hidden="true" style="width:2em;height:2em">
             <use xlink:href="#icon-sousuo"></use>
         </svg>
      </el-button>
        </el-popover>
          </template>
        </el-input>
        <!--协作者列表卡片-->
        <div>
          <el-card class="box-card" shadow="never">
            <div slot="header" class="clearfix">
              <span style="font-size:17px;position:absolute;margin-top:-5px;margin-left:20px">协作者</span>
            </div>
            <div>
              <div>
                <ul v-for="(item,index) in userItem" :key="index">
                  <li style="position:relative">
                    <svg class="icon" aria-hidden="true" style="width:2em;height:2em">
                      <use xlink:href="#icon-renwu2"></use>
                    </svg>
                    <el-avatar size="medium" :src="item.u_icon" class="img"></el-avatar>
                    <span class="user_name">
                     {{item.u_username}}
                    </span>
                     <p style="positon:relative;margin-left:70px">
            <el-button v-show="item.comment==1" @click="changePower(index,item.id,0,item.change)">享有评论权限</el-button>
            <el-button v-show="item.comment==0" @click="changePower(index,item.id,1,item.change)">无评论权限</el-button>
            <el-button v-show="item.change==1" @click="changePower(index,item.id,item.comment,0)">享有修改权限</el-button>
            <el-button v-show="item.change==0" @click="changePower(index,item.id,item.comment,0)">无修改权限</el-button>
        </p>
                  </li>
                </ul>
              </div>
            </div>
          </el-card>
        </div>
        <!--管理者列表卡片-->
        <div>
          <el-card class="box-card" shadow="never">
            <div slot="header" class="clearfix">
              <span style="font-size:17px;position:absolute;margin-top:-5px;margin-left:20px">管理者</span>
            </div>
            <div>
              <div style="position:relative;margin-left:40px">
                <svg class="icon" aria-hidden="true" style="width:2em;height:2em">
                  <use xlink:href="#icon-renwu1"></use>
                </svg>
                <el-avatar size="medium" :src="author.img" class="img"></el-avatar>
                <span class="user_name">
                  {{author.name}}
                </span>
              </div>
            </div>
          </el-card>
        </div>
      </div>
    </div>
     
    </el-drawer>
<el-dialog
  title="发送协作者邀请"
  :visible.sync="dialogVisible"
  width="30%"
  :before-close="handleClose">
  <el-input
  type="textarea"
  autosize
  placeholder="请输入内容"
  v-model="reason">
</el-input>
  <span slot="footer" class="dialog-footer">
    <el-button type="primary" @click="invite(inviteId,reason)">确 定</el-button>
  </span>
</el-dialog>
    <!--头部导航栏-->
    <el-header>
       <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
          <div class="flex flex6" >
        <div style="">
          <svg class="icon" aria-hidden="true" style="width:4em;height:4em">
            <use xlink:href="#icon-wendang"></use>
          </svg>
        </div>
        <div style="margin-left:20px;margin-right:30px">
          <h1 class="change-color" style="font-weight:lighter ">{{document_type}}</h1>
        </div>
        <router-link :to="{path: '/changefile/', query: {fileId: fileId}}">
          <el-button type="primary" v-show="change_power==0&&allow_edit==0" plain>修改</el-button>
          <el-button type="danger" v-show="change_power==0&&allow_edit==1" plain disabled>当前有人正在修改 禁止修改</el-button>
           <el-button type="danger" v-show="change_power==1" plain disabled>您没有修改的权限</el-button>
        </router-link>
        <el-button type="primary" v-show="type==1&&is_team==1" plain @click="drawer = true" style="margin-left: 10px">协作</el-button> 
        <el-button type="primary" v-show="type==1&&allowShare==0" @click="set_allowShare(1)" plain >允许分享</el-button>
        <el-button type="primary" v-show="type==1&&allowShare==1" @click="set_allowShare(0)" plain >禁止分享</el-button>
        <input type="text" v-model="localURL" style="display: none">
        <el-button class="copyURL"
                   v-if="allowShare==0"
                   :data-clipboard-text="localURL"
                   type="primary"
                   @click="copy" plain style="margin-left: 10px">
                   分享</el-button>
          <el-button class="copyURL"
                   v-else
                   :data-clipboard-text="localURL"
                   type="primary"
                   @click="copy" plain style="margin-left: 10px" disabled>
                   分享
          </el-button>
        <el-button type="primary" v-show="type==1" @click="del()" plain >删除</el-button>
      </div>
        </el-menu> 
    <div style="position:relative">
       <div class="flex flex6" style="position:absolute;right:20px;top:-70px">
          <el-button type="text" icon="el-icon-star-off" v-show="star==1" @click="set_favorite(0)" style="color:gray;font-size:30px"></el-button>
           <el-button type="text" icon="el-icon-star-on" v-show="star==0" @click="set_favorite(1)" style="color:#ede159;font-size:30px"></el-button>
         <span style="color:gray;font-size:12px;margin-left:20px">{{creator}}创建于{{create_date}}</span>
         </div>
    </div>   
    </el-header>
    <!--drawer设置-->
  
    <!--中间文件内容-->
    <el-main> 
      <el-row>
        <el-col :span="3" class="grid-content"></el-col>
        <el-col :span="18">
          <h2>{{title}}</h2>
          <p>{{content}}</p>
        </el-col>
        <el-col :span="3" class="grid-content"></el-col>
      </el-row>
    </el-main>
    <!--底部评论区-->
    <el-footer>
      <el-row >
        <el-col :span="2" class="grid-content">
        </el-col>
        <el-col :span="20" style="position:relative">
           <div class="mengban" style="opacity: 0.5; background-color:#ededed"> 
           </div> 
           <div class="mengban"> 
             <p class="change-color" style="margin-top:70px;font-size:23px">您没有评论的权限</p>
           </div> 
          <el-form action="#" ref="commentTextarea" label-width="100px">
            <el-form-item label="评论">
              <el-input type="textarea" placeholder="请在此发表评论"></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="onSubmit(textarea)">提交</el-button>
            </el-form-item>
          </el-form>
         
        </el-col>
           
        <el-col :span="2" class="grid-content"></el-col>
      </el-row>
      <div style="text-align: center">
        <h2 style="font-size: 2rem">评论区</h2>
      </div>

      <el-row  v-for="(item, index) in comments" :key="index">
        <el-col :span="3" class="grid-content"></el-col>
        <el-col :span="19">
          <el-card shadow="always" style="margin-bottom: 1rem">
            <el-col :span="12"><span>用户名：{{item.u_username}}</span></el-col>
            <el-col :span="12"><span>评论时间：{{item.time}}</span></el-col>
            <el-col :span="24" class="grid-content"></el-col>
            <el-col :span="24" style="margin-bottom: 1rem"><span>{{item.content}}</span></el-col>
          </el-card>
        </el-col>
        <el-col :span="2" class="grid-content"></el-col>
      </el-row>
    </el-footer>
  </el-container>
</template>

<script>
    export default {
        name: "editor",
      data() {
        return {
          allow_edit:1,
          dialogVisible: false,
          inviteId:-1,
          reason:"",
          document_type:"个人文档",
          type:0,
          change_power:0,
          comment_power:1,
          is_team:1,
          team_id:3242,
          title:"今天的交互",
          content:"sdas",
          creator:"ZZZ飘",
          create_date:"2020/1/1",
          allowShare:1,
          star:1,
          textarea:"",
          //悬浮框
          visible: false,
          isComment: false,
          localURL: '',
          value: '',
          //查找协作者
          search:"",
          searchItem:[
           {id:123,u_icon:'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',u_username:"sadasd"}   ,
          ],
          author: {id:123,img:'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',name:"sadasd"}
          ,
          //uploadPath,
          editor: null,
          info_: null,
          //title
          activeIndex: '1',
          activeIndex2: '1',
          //drawer
          drawer: false,
          direction: 'rtl',
          comments: [
            {u_username: '用户1', content: '评论内容1', time: '2020-08-10',id:123},
          ],
          fileId: 123,
          userItem:[
           {id:12443,u_icon:'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',u_username:"sadasewrwrwrwed",
            change:0, comment:0,
           },
           {id:12443,u_icon:'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',u_username:"sadasewrwrwrwed",
            change:1, comment:0,
           },
       ],
        }
      },
      mounted() {
        this.fileId=this.$route.params.documentId
        this.getURL()
             //35 获取文档信息
     this.$axios.post('',
              this.qs.stringify({
                id:this.fileId
              }),
              {headers: {'Content-Type': 'application/x-www-form-urlencoded'}})
              .then(res => {
                console.log(res)
                this.type=res.data.type
                if(this.type==-1&&this.allowShare==1){
                   this.$router.push({path:"/error"})
                }
                else if(this.type==-2){
                  this.$router.push({path:"/login"})
                }
                this.change_power=res.data.change,
                this.comment_power=res.data.comment,
                this.is_team=res.data.is_team
                if (this.is_team==0){
                  this.document_type="团队文档"
                }
                else{
                  this.document_type="个人文档"
                }
                this.team_id=res.data.team_id,
                this.title=res.data.title,
                this.content=res.data.content,
                this.comment=res.data.comments,
                this.allowShare=res.data.allowShare,
                this.star=res.data.star,
                this.userItem=res.data.list
              })
          //定时器 数据库轮询 查看是否可以修改文档
          self.setInterval(       
          function(){
            //37 数据库轮询 查看是否可以修改文档
     this.$axios.post('',
              this.qs.stringify({
                id:this.fileId
              }),
              {headers: {'Content-Type': 'application/x-www-form-urlencoded'}})
              .then(res => {
                console.log(res)
                this.allow_edit=res.data.status
              })
          },1000);
      },
      methods: {
        handleClick() {
          alert('button click');
        },
        handleSelect(key, keyPath) {
          console.log(key, keyPath);
        },
        goBack() {
          console.log('go back');
        },
        onSubmit(content) {
           //45 评论文档
     this.$axios.post('',
              this.qs.stringify({
                id:this.fileId,
                content:content
              }),
              {headers: {'Content-Type': 'application/x-www-form-urlencoded'}})
              .then(res => {
                console.log(res)
                if(res.data.status==0){
                  this.textarea=""
                  var com={id:res.data.id,time:res.data.time,u_username:res.data.u_username,content:content}
                  this.comments.push(com)
                }
                else{
                  this.$message.error('评论失败');
                }
              })
        },
        copy() {
          let clipboard = new this.Clipboard('.copyURL');
          clipboard.on('success', e => {
            this.$message({
              type: 'success',
              message: '链接已复制到剪贴板'
            });
            this.aa=e
            clipboard.destroy()
          })
        },
        getURL() {
          this.localURL = location.href
        },
        set_favorite(type){
            //40 收藏文档
     this.$axios.post('/app/deal_collect/',
              this.qs.stringify({
                id:this.fileId,
                type:type
              }),
              {headers: {'Content-Type': 'application/x-www-form-urlencoded'}})
              .then(res => {
                console.log(res)
                if(res.data.status==0){
                  this.star=type
                }
                else{
                  if(type==0)
                  this.$message.error('收藏失败');
                  else{
                     this.$message.error('取消收藏失败');
                  }
                }
              })
        },
        del(){
//40 删除文档
     this.$axios.post('/app/delete_file/',
              this.qs.stringify({
                id:this.fileId
              }),
              {headers: {'Content-Type': 'application/x-www-form-urlencoded'}})
              .then(res => {
                console.log(res)
                if(res.data.status==0){
                  this.$router.push({path:"/diamond/dashboard/desktop"})
                }
                else{
                  this.$message.error('删除文档失败');
                }
              })
        },
          changePower(index,id,comment,change){
         //15 分配个人文档权限
     this.$axios.post('/app/grant_power/',
              this.qs.stringify({
                u_id:id,
                id:this.teamId,
                comment:comment,
                change:change
              }),
              {headers: {'Content-Type': 'application/x-www-form-urlencoded'}})
              .then(res => {
                console.log(res)
                    if(res.data.status==0){
                      this.userItem[index].change=change
                      this.userItem[index].comment=comment
                    }
              })
    },
    searchUser(search){
      //13 搜索用户
     this.$axios.post('/app/search_person/',
              this.qs.stringify({
                key:search,
              }),
              {headers: {'Content-Type': 'application/x-www-form-urlencoded'}})
              .then(res => {
                console.log(res)
                    this.searchItem=res.data.list
              })
    },
        invite(id,reason){
         //47 邀请加入协作者
     this.$axios.post('/app/cooperate_invitation/',
              this.qs.stringify({
                id:this.fileId,
                u_id:id,
                reason:reason
              }),
              {headers: {'Content-Type': 'application/x-www-form-urlencoded'}})
              .then(res => {
                console.log(res)
                 if (res.data.status === 0) {
                     //更新数据
                 }else{
                   this.$message.error("邀请失败，请检查是否存在网络问题");
                 }
              })
      this.reason=""
      this.dialogVisible = false
    },
    handleClose(done) {
        done();
        this.reason="" 
    },
    set_allowShare(allowShare){
       this.allowShare=allowShare
        //38 设置分享权限
     this.$axios.post('/app/set_is_share/',
              this.qs.stringify({
                id:this.fileId,
                type:allowShare
              }),
              {headers: {'Content-Type': 'application/x-www-form-urlencoded'}})
              .then(res => {
                console.log(res)
                 if (res.data.status === 0) {
                     this.allowShare=allowShare
                 }else{
                   this.$message.error("邀请失败，请检查是否存在网络问题");
                 }
              })
    }
    }
}
</script>

<style>
.mengban{
  position:absolute;height:170px;text-align:center;width:100%;margin-left:3%;;margin-top:-20px;z-index:100
}
  .editor {
    width: 100%;
    margin: 0 auto;
    position: relative;
    z-index: 0;
  }
  .toolbar {
    border: 1px solid #ccc;
  }
  .text {
    border: 1px solid #ccc;
    min-height: 500px;
  }
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
