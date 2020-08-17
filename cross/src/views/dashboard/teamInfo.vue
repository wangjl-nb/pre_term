<template>
  <el-container class="router" style="position:relative">
        <el-dialog
        title="发送团队邀请"
        :visible.sync="dialogVisible"
        width="30%"
        :before-close="handleClose2">
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
      <el-dialog
        title="发送团队申请"
        :visible.sync="dialogVisible1"
        width="30%"
        :before-close="handleClose1">
      <el-input
          type="textarea"
          autosize
          placeholder="请输入内容"
          v-model="reason1">
      </el-input>
      <span slot="footer" class="dialog-footer">
    <el-button type="primary" @click="join(reason1)">确 定</el-button>
  </span>
    </el-dialog>
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
                <ul v-for="(item, index) in searchItem" :key="index">
                  <li style="position:relative">
                    <el-avatar size="medium" :src="'/media/'+item.u_icon"></el-avatar>
                    <span style="font-size:17px;position:absolute;margin-top:-5px;margin-left:20px">
        {{ item.u_username }}
        <el-button type="text" @click="dialogVisible = true;inviteId=item.id"> 
           <i class="el-icon-circle-plus-outline" style="font-size:20px"></i> 
        </el-button>
       
        </span>
                  </li>
                </ul>
              </div>
              <div v-else>
                <pre style="color:gray;font-size:15px;font-weight:normal">                 当前搜索结果为0</pre>
              </div>
              <el-button slot="reference" @click="searchUser(search)">
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
        {{ author.name }}
        </span>
        </div>
        <div>
          <ul v-for="(item,index) in userItem" :key="index">
            <li style="position:relative">
              <svg class="icon" aria-hidden="true" style="width:2em;height:2em">
                <use xlink:href="#icon-zhanghaoguanli"></use>
              </svg>
              <el-avatar size="medium" :src="'/media/'+item.u_icon" class="img"></el-avatar>
              <span class="user_name">
        {{ item.u_username }}
        </span>
              <p style="positon:relative;margin-left:90px">
                <el-button v-show="item.comment==1" @click="changePower(index,item.id,0,item.change)">享有评论权限</el-button>
                <el-button v-show="item.comment==0" @click="changePower(index,item.id,1,item.change)">无评论权限</el-button>
                <el-button v-show="item.change==1" @click="changePower(index,item.id,item.comment,0)">享有修改权限</el-button>
                <el-button v-show="item.change==0" @click="changePower(index,item.id,item.comment,1)">无修改权限</el-button>
                <el-button type="text" @click="tichu(item.id,index)"
                           style="position:absolute;margin-top:-10px;margin-left:10px">
                  <svg class="icon" aria-hidden="true" style="color:red;width:2em;height:2em">
                    <use xlink:href="#icon-tiren"></use>
                  </svg>
                </el-button>
              </p>
            </li>
          </ul>
        </div>

      </div>
    </el-drawer>
    <el-header style="background:#fafbfc;height:150px;padding-top:30px;position:relative">
      <div v-show="type==0" style="position:absolute;top:10px;z-index:100;width:40%;right:0px">
        <ul v-for="(item,index) in teamRemind" :key="index">
          <li>
            <el-card class="box-card" shadow="hover">
              <div>
                <p style="flex-grow:13"><strong style="font-size:20px">{{ item.u_username }}</strong>
                  <span>申请加入团队</span></p>
              </div>
              <div>

              </div>
              <el-divider content-position="right">
                申请理由
                <el-button style="flex-grow:1;margin-left:20px" plain
                           @click="manageTeamRemind(index,item.application_id,0)">同意
                </el-button>
                <el-button style="flex-grow:1" type="danger" plain
                           @click="manageTeamRemind(index,item.application_id,1)">拒绝
                </el-button>
              </el-divider>
              <div>
                <el-row style="margin-bottom:-10px;margin-top:-10px">
                  <el-col :span="2">
                    <div class="grid-content"></div>
                  </el-col>
                  <el-col :span="20">
                    <div class="grid-content"><p>{{ item.reason }}</p></div>
                  </el-col>
                  <el-col :span="2">
                    <div class="grid-content"></div>
                  </el-col>
                </el-row>
              </div>
            </el-card>
          </li>
        </ul>
      </div>
      <div class="flex flex6">
        <div style="">
          <el-image
              style="width: 70px; height: 70px; border-radius: 50%;"
              :src="jpg"
              :fit="fits">
          </el-image>
        </div>
        <div style="margin-left:20px;margin-right:30px">
          <h1 class="change-color" style="font-weight:lighter "><i>{{ name }}</i></h1>
        </div>
        <el-button plain v-show="type==0" @click="drawer = true">管理成员</el-button>
        <el-button type="danger" plain v-show="type==0" @click="dispose()">解散团队</el-button>
        <el-button plain v-show="type==2" @click="dialogVisible1=true">加入团队</el-button>
        <el-button type="danger" v-show="type==1" plain @click="out()">退出团队</el-button>
        <el-button type="primary" v-show="type==0" plain @click="changeTeamIcon()">修改团队头像</el-button>
        <el-button type="warning" v-show="type==0" plain @click="changeTeamName()">修改团队名称</el-button>
        <el-button type="primary" v-show="type==0" plain @click="dialogTableVisible=true"
                   style="background-color: #ffc107;">修改团队描述
        </el-button>
      </div>

    </el-header>
    <el-container>
      <el-container>
        <el-main>
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
            <el-dialog title="修改团队描述" :visible.sync="dialogTableVisible" center :append-to-body='true'
                       :lock-scroll="false" width="50%" @closed="handleClose">
              <el-input
                  type="textarea"
                  :rows="5"
                  autosize
                  placeholder="请输入内容"
                  v-model="editTeamInfo">
              </el-input>
              <el-button class="medium" style="margin-left:40%;position:relative;margin-top:30px" plain
                         @click="submitedit(editTeamInfo)">提交修改
              </el-button>
            </el-dialog>

            <el-dialog title="修改团队头像" :visible.sync="isChangeTeamIcon" center :append-to-body='true'
                       :lock-scroll="false" width="50%" @closed="teamIconClose">
              <el-upload ref="upload"
                         action="#"
                         accept="image/png,image/gif,image/jpg,image/jpeg"
                         list-type="picture-card"
                         :limit=1
                         :auto-upload="false"
                         :on-exceed="handleExceed"
                         :before-upload="handleBeforeUpload"
                         :on-preview="handlePictureCardPreview"
                         :on-remove="handleRemove"
                         :on-change="imgChange">
                <i class="el-icon-plus"></i>
              </el-upload>
              <el-button class="medium" style="margin-left:40%;position:relative;margin-top:30px" plain
                         @click="uploadFile">提交修改
              </el-button>
            </el-dialog>

            <el-dialog title="修改团队名称" :visible.sync="isChangeTeamName" center :append-to-body='true'
                       :lock-scroll="false" width="50%" @closed="teamNameClose">
              <el-input
                  type="textarea"
                  :rows="5"
                  autosize
                  placeholder="请输入内容"
                  v-model="newName">
              </el-input>
              <el-button class="medium" style="margin-left:40%;position:relative;margin-top:30px" plain
                         @click="submitName(newName)">提交修改
              </el-button>
            </el-dialog>
          </div>
          <pre style="font-size:20px">
    这里是团队信息
    写下想说的话
    {{ teamInfo }}
  </pre>
        </el-card>

      </el-footer>
    </el-container>
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
  data() {
    return {
      dialogVisible: false,
      inviteId: -1,
      reason: "",
      dialogVisible1: false,
      reason1: "",
      img: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
      teamId: 134,
      name: "团队名字哈哈",
      newName: '',
      type: 2,
      doucument_ids: [],
      isChangeTeamIcon: false,
      isChangeTeamName: false,
      editTeamInfo: "",
      teamInfo: "希望一直加油",
      dialogTableVisible: false,
      author: {id: 123, img: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg', name: "sadasd"}
      ,
      searchItem: [ {id: 123, img: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg', name: "sadasd"}],
      userItem: [],
      drawer: false,
      search: "",
      list: [],
      teamRemind: [
        {application_id: 12331, u_username: "你太厉害", reason: "你太厉害了！！！"},
        {application_id: 12331, u_username: "叽叽喳喳害", reason: "你太厉害了！！！"},
        {application_id: 1231, u_username: "话害", reason: "你太厉害了！！！"},
      ]
    }
  },
  mounted() {
    var that = this
    that.teamId = that.$route.params.teamId
    /// 获取团队信息
    this.$axios.get('/app/team_info/',
        {
          params: {
            team_id: that.teamId,
          },
          headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        }).then(res => {
      console.log(res)
      that.name = res.data.name
      that.jpg = '/media/' + res.data.icon
      that.type = res.data.type
      that.teamInfo = res.data.describe
      that.author.id = res.data.u_id
      that.author.img = '/media/' + res.data.u_icon
      that.author.name = res.data.u_username
      that.userItem = res.data.list
      //权限按钮显示？？？
      that.create_date = res.data.create_date
      //    this.$router.push({path:"/diamond/dashboard/desktop"})
    })
    //获取团队文档信息
    this.$axios.get('/app/team_files_list', {
          params: {
            team_id: that.teamId,
          }
        },
        {headers: {'Content-Type': 'application/x-www-form-urlencoded'}})
        .then(res => {
          console.log(res)
          that.list = []
          for (var i = 0; i < res.data.documentList.length; i++) {
            var di = res.data.documentList[i]
            var document = {
              title: di.title,
              id: di.id,
              creator: di.creator,
              create_date: di.create_date,
              change_date: di.change_date,
              u_username: di.u_username
            }
            that.list.push(document)
          }
        })
    //24.5 获取团队申请信息
    this.$axios.get('/app/application_list/', {
          params: {
            team_id: that.teamId,
          }
        },
        {headers: {'Content-Type': 'application/x-www-form-urlencoded'}})
        .then(res => {
          console.log(res)
          this.teamRemind = res.data.list
        })
  },
  methods: {
    handleClose() {
      this.editTeamInfo = ""
      this.dialogTableVisible = false
    },
    handleClose1() {
      this.reason1 = ""
      this.dialogVisible1 = false
    },
    handleClose2() {
      this.reason = ""
      this.dialogVisible = false
    },
    changeTeamIcon() {
      //11 修改团队头像
      this.isChangeTeamIcon = true
    },
    teamIconClose() {
      this.isChangeTeamIcon = false
    },
    changeTeamName() {
      //12 修改团队名称
      this.isChangeTeamName = true
    },
    teamNameClose() {
      this.isChangeTeamName = false
    },
    dispose() {
      //18
      ///解散团队
      var that = this
      this.$axios.post('/app/dismiss_team/',
          this.qs.stringify({
            id: that.teamId,
          }),
          {headers: {'Content-Type': 'application/x-www-form-urlencoded'}})
          .then(res => {
            console.log(res)
            if (res.data.status === 0) {
              this.$router.push({path: "/diamond/dashboard/desktop"})
            } else {
              this.$message.error("解散团队失败");
            }
          })

    },
    join(reason) {
      //19 申请加入团队
      var that = this
      this.$axios.post('/app/team_application/',
          this.qs.stringify({
            id: that.teamId,
            reason:reason
          }),
          {headers: {'Content-Type': 'application/x-www-form-urlencoded'}})
          .then(res => {
            console.log(res)
            if (res.data.status === 0) {
              this.$message({
                message: "申请加入团队成功，请等待对方反馈",
                type: 'success'
              });
            } else {
              this.$message.error("申请加入团队失败，您的申请正在被处理或者您已经是团队成员，请刷新界面");
            }
            this.reason1 = ""
      this.dialogVisible1 = false
          })
    },
    out() {
      //20 退出团队
      var that = this
      this.$axios.post('/app/exit_team/',
          this.qs.stringify({
            id: that.teamId,
          }),
          {headers: {'Content-Type': 'application/x-www-form-urlencoded'}})
          .then(res => {
            console.log(res)
            if (res.data.status === 0) {
              this.$router.push({path: "/diamond/dashboard/desktop"})
            } else {
              this.$message.error("退出团队失败，请检查是否存在网络问题");
            }
          })
    },
    invite(id,reason) {
      //14 邀请加入团队
      var that = this
      this.$axios.post('/app/team_invitation/',
          this.qs.stringify({
            team_id: that.teamId,
            user_id:id,
            reason:reason
          }),
          {headers: {'Content-Type': 'application/x-www-form-urlencoded'}})
          .then(res => {
            console.log(res)
            if (res.data.status === 0) {
              this.$message({
                message: "邀请成功，请等待对方同意",
                type: 'success'
              });
            } else {
              this.$message.error("邀请失败,您之前发送的邀请还未被处理或者他已经是团队成员");
            }
            this.dialogVisible=false
            this.reason=""
          })
    },
    tichu(id, index) {
      // 踢出团队
      var that = this
      this.$axios.post('/app/kick/',
          this.qs.stringify({
            id: that.teamId,
            u_id: id
          }),
          {headers: {'Content-Type': 'application/x-www-form-urlencoded'}})
          .then(res => {
            console.log(res)
            if (res.data.status === 0) {
              this.$message({
                message: "踢人成功",
                type: 'success'
              });
              this.userItem.splice(index, 1)
            } else {
              this.$message.error("踢人失败，请检查是否存在网络问题");
            }
          })
    },
    submitedit(text) {
      this.dialogTableVisible = false
      //10 修改团队信息
      var that = this
      this.$axios.post('/app/change_team_describe/',
          this.qs.stringify({
            team_id: that.teamId,
            describe: text
          }),
          {headers: {'Content-Type': 'application/x-www-form-urlencoded'}})
          .then(res => {
            console.log(res)
            if (res.data.status === 0) {
              this.teamInfo = text
            } else {
              this.$message.error("修改团队信息失败，请检查是否存在网络问题");
            }
          })
    },
    searchUser(search) {
      //13 搜索用户
      this.$axios.post('/app/search_person/',
          this.qs.stringify({
            key: search,
          }),
          {headers: {'Content-Type': 'application/x-www-form-urlencoded'}})
          .then(res => {
            console.log(res)
            this.searchItem = res.data.list
          })
    },
    changePower(index, id, comment, change) {
      //15 分配团队文档权限
      this.$axios.get('/app/grant_team_power/', {
        params: {
          u_id: id,
          team_id: this.teamId,
          comment: comment,
          change: change
        },
        headers: {'Content-Type': 'application/x-www-form-urlencoded'}
      }).then(res => {
        console.log(res)
        if (res.data.status == 0) {
          this.userItem[index].change = change
          this.userItem[index].comment = comment
        }
      })
    },
    manageTeamRemind(index, id, type) {
      //25 管理团队申请信息
      this.$axios.post('/app/process_application/',
          this.qs.stringify({
            id: id,
            type: type
          }),
          {headers: {'Content-Type': 'application/x-www-form-urlencoded'}})
          .then(res => {
            console.log(res)
            if (res.data.status == 0) {
              this.teamRemind.splice(index, 1)
            }
          })
    },

    //上传头像所用
    handleBeforeUpload(file) {
      if (!(file.type === 'image/png' || file.type === 'image/gif' || file.type === 'image/jpg' || file.type === 'image/jpeg')) {
        this.$notify.warning({
          title: '警告',
          message: '请上传格式为image/png, image/gif, image/jpg, image/jpeg的图片'
        })
      }
      let size = file.size / 1024 / 1024 / 2
      if (size > 2) {
        this.$notify.warning({
          title: '警告',
          message: '图片大小必须小于2M'
        })
      }
      let fd = new FormData();//通过form数据格式来传
      fd.append("team_id", this.teamId)
      fd.append("icon", file); //传文件
      console.log(fd.get('icon'));
      this.$axios({
        url: '/app/change_team_icon/',
        method: "post",
        data: fd,
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }).then((res) => {
        this.$message(res.data.msg)
        console.log(res)
        if (res.data.status === 0) {
          this.$router.go(0)
        }
      })
    },
    handleExceed(files, fileList) {
      //防报错
      this.aa = files
      this.aa = fileList
    },
    handleRemove(file, fileList) {
      this.hideUpload = fileList.length >= this.limitNum;
      //防报错
      this.aa = file
      this.aa = fileList
    },
    handlePictureCardPreview(file) {
      //防报错
      this.aa = file
      // this.dialogImageUrl = file.url;
      // this.dialogVisible = true;
    },
    uploadFile() {
      this.$refs.upload.submit()
      this.isChangeTeamIcon = false
    },
    imgChange(files, fileList) {
      //防报错
      this.aa = files
      this.hideUpload = fileList.length >= this.limitNum;
      if (fileList) {
        this.$refs.uploadElement.clearValidate();
      }
    },

    //修改名称所用
    submitName(text) {
      this.isChangeTeamName = false
      var that = this
      this.$axios.post('/app/change_teamname/',
          this.qs.stringify({
            team_id: that.teamId,
            team_name: text
          }),
          {headers: {'Content-Type': 'application/x-www-form-urlencoded'}})
          .then(res => {
            console.log(res)
            this.$message(res.data.msg)
            if (res.data.status === 0) {
              this.name = text
            }
          })
    }
  }
};
</script>
<style scoped>

.img {
  position: relative;
  left: 10px;
  top: 3px
}

.user_name {
  font-size: 18px;
  position: absolute;
  margin-top: 6px;
  margin-left: 20px
}

.el-row {
  margin-bottom: 20px;

&
:last-child {
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
