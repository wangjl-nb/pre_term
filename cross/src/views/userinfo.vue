<template>
  <div>
    <el-container>
      <el-header>
        <el-row style="margin-top: 3rem; margin-bottom: 6rem">
          <el-col :span="24" class="grid-content" style="margin-bottom: 1rem">
            <el-button style="margin-left: 3rem" @click="$router.go(-1)"> < 返回 </el-button>
          </el-col>
          <el-col :span="24" class="grid-content" style="margin-bottom: 1rem">
            <div style="text-align: center"><img :src="u_icon" alt=""></div>
          </el-col>
          <el-col :span="24" class="grid-content" style="margin-bottom: 1rem">
            <div style="text-align: center"><h1 style="font-size: 2rem">{{ this.u_username }}</h1></div>
          </el-col>
          <el-col :span="24" class="grid-content">
            <div style="text-align: center"><h2 style="font-size: 2rem">{{ this.u_email }}</h2></div>
          </el-col>
        </el-row>

        <el-main>
          <div style="text-align: center"><h2>TA创建的团队</h2></div>
          <el-row v-for="(item,index) in teams" :key="index">
            <el-col :span="3" class="grid-content"></el-col>
            <el-col :span="18">
            <el-divider></el-divider>
            <div class="flex flex7">
              <!--                   <div style="margin-top:-10px;flex-grow: 1;">-->
              <!--                        <svg class="icon" aria-hidden="true" style="width:3em;height:3em">-->
              <!--                            <use :xlink:href="  item.icon" ></use>-->
              <!--                        </svg>-->
              <!--                  </div>-->
              <div style="margin-left:0px;margin-top:-14px;flex-grow:32;">
                <a style="font-size:18px" :href="'/diamond/dashboard/team/'+item.id">{{ item.name }}</a>
                <el-card shadow="never" style="margin-top:10px">
                  <p style="margin:-6px 0">{{ item.description }}</p>
                </el-card>
              </div>
            </div>
          </el-col>
            <el-col :span="3" class="grid-content"></el-col>
          </el-row>
        </el-main>

      </el-header>
    </el-container>
  </div>
</template>

<script>
export default {
  name: "Userinfo",
  data() {
    return {
      u_icon: '',
      u_username: '',
      u_email: '',
      teams: [],
    }
  },
  mounted() {
    this.getUserInfo()
  },
  methods: {
    getUserInfo() {
      this.$axios.get('/app/user_info/', {
        params: {
          id: this.$route.params.userId,
        },
        headers: {'Content-Type': 'application/x-www-form-urlencoded'},
      }).then(res => {
        this.u_icon = '/media/' + res.data.u_icon
        this.u_username = res.data.u_username
        this.u_email = res.data.u_email
        this.teams = res.data.teams
      })
    }
  },
}
</script>

<style scoped>
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
</style>