<template>
  <el-container >
  <el-main class="dashboard"> 
      <ul v-for="(item,index) in list" :key="index">
          <li>
              <el-card class="box-card" shadow="hover">
                  <div class="flex flex6" > 
                     <p style="flex-grow:13"><strong style="font-size:20x">{{item.author}}</strong> <span>申请加入</span><strong style="font-size:20x">{{item.team}}</strong></p>
                     <el-button style="flex-grow:1" plain @click="argee(item.id)">同意</el-button>
                     <el-button style="flex-grow:1" type="danger" plain  @click="refuse(item.id)">拒绝</el-button>
                  </div>
              </el-card>
          </li>
      </ul> 
  </el-main> 
  <el-aside>
       <info :info="infoo"></info>
  </el-aside>
</el-container>
</template>

<script>
// @ is an alias to /src
import info from '@/components/info'
export default {
  name: "TeamRemind",
  components: {
      info
  },
  data(){
      return{
        list:[
            {id:1231,author:"XXX",team:"sdas",},
            {id:1231,author:"XXXcsx",team:"sdas",},
            {id:1231,author:"XXXwqe",team:"sdas",}
        ]
      }
  },
  mounted(){
  },
  methods:{
      argee(id){
          this.aa=id
      },
      refuse(id){
           this.aa=id
      }
  }
};
</script>
<style scoped>
</style>
