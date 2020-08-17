<template>
  <el-container>
    <el-main class="dashboard">
      <ul v-for="(item,index) in list" :key="index">
        <li>
          <el-card class="box-card" shadow="hover">
            <div class="flex flex6">
              <p style="flex-grow:11"><strong style="font-size:20px">{{ item.u_username }}</strong>
                <span>邀请您加入</span><strong style="font-size:20px">{{ item.name }}</strong></p>
              <div style="flex-grow:1;margin-bottom:-30px" >
                <button class="btn-7" style="margin-right:-5px" @click="argee(index,item.invitation_id)">同意</button>
                <button class="btn-10"  @click="refuse(index,item.invitation_id)">拒绝</button>
              </div> 
            </div>
            <el-divider content-position="left">邀请理由</el-divider>
            <div>
              <el-row style="margin-bottom:-12px">
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
    </el-main>
    <!--  <el-aside>-->
    <!--       <info :info="infoo"></info>-->
    <!--  </el-aside>-->
  </el-container>
</template>

<script>
// @ is an alias to /src
import info from '@/components/info'

export default {
  name: "Invite",
  components: {
    info
  },
  data() {
    return {
      list: [
        {id: 1231, author: "XXX", team: "sdas", reason: "你太厉害了！！！"},
        {id: 1231, author: "XXXcsx", team: "sdas", reason: "你太厉害了！！！"},
        {id: 1231, author: "XXXwqe", team: "sdas", reason: "你太厉害了！！！"}
      ]
    }
  },
  mounted() {
    this.$axios.post('/app/invitation_list/',).then(res => {
      //接收数据
      console.log(res)
      this.list = res.data.list;

    })
  },
  methods: {
    argee(index,id) {
      this.$axios.post('/app/process_invitation/',
          this.qs.stringify({
            id: id,
            type: 0
          }), {headers: {'Content-Type': 'application/x-www-form-urlencoded'}})
          .then(res => {
        if (res.data.status === 0) {
          alert('加入团队成功')
           this.list.splice(index,1)
        } else {
          this.$message.error("加入团队失败！")
        }
      })
      // this.aa=id
    },
    refuse(index,id) {
      this.$axios.post('/app/process_invitation/',
          this.qs.stringify({
            id: id,
            type: 1,
          }), {headers: {'Content-Type': 'application/x-www-form-urlencoded'}})
          .then(res => {
            console.log(res)
            if (res.data.status === 0) {
              alert('拒绝加入成功')
               this.list.splice(index,1)
            } else {
              this.$message.error("拒绝加入失败！")
            }

          })
      // this.aa=id
    }
  }
};
</script>
<style scoped>
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
