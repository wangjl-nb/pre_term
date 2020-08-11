<template>
  <el-container>
  <el-main class="dashboard">
    <el-row>
          <el-col :span="24"><div class="grid-content bg-purple-dark"></div></el-col>
    </el-row>
  </el-main>
</el-container>
</template>

<script>
// @ is an alias to /src


export default {
  name: "Desktop",
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
