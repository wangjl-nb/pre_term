<template>
  <el-container>
  <el-main class="dashboard">
    <el-row>
          <el-col :span="24">
            <div id="recycleBin">
              <div>
                <el-row :gutter="20">
                  <el-col :span="6" :offset="3"><div class="grid-content bg-purple">
                    <span class="recycleTitle">回收站</span>
                  </div></el-col>
                  <el-col :span="12" ><div class="grid-content bg-purple trashButton">
                    <el-button type="success" round>全部恢复</el-button>
                    <el-button type="danger" round>清空回收站</el-button>
                    <el-button type="success" round style="background-color: #42b983;">恢复已选中的部分</el-button>
                    <el-button type="danger" round style="background-color: blueviolet">清空已选中的部分</el-button>
                  </div></el-col>
                </el-row>
              </div>
              <el-table
                      :data="trashFile"
                      ref="multipleTable"
                      :default-sort="{prop: 'createDate', order: 'descending'}"
                      style="width: 100%">
                <el-table-column
                        type="selection"
                        width="55">
                </el-table-column>
                <el-table-column
                        prop="name"
                        label="文件名"
                        sortable
                        width="200">
                </el-table-column>
                <el-table-column
                        prop="createDate"
                        label="创建时间"
                        sortable
                        width="300">
                </el-table-column>
                <el-table-column
                        prop="deleteDate"
                        label="删除时间"
                        sortable
                        width="300">
                </el-table-column>
                <el-table-column
                        label="操作"
                        width="300">
                  <template slot-scope="scope">
                    <el-button type="success" size="small">恢复</el-button>
                    <el-button type="danger" size="small">删除</el-button>
                  </template>
                </el-table-column>
              </el-table>
            </div>
    </el-col>
    </el-row>
  </el-main>
</el-container>
</template>

<script>
  export default {
    name: "RecycleBin",
    data() {
      return {
        trashFile: [
          {
            name: '1',
            createDate: '2020-08-09',
            deleteDate: '2020-08-12',
          },
          {
            name: '2',
            createDate: '2020-08-07',
            deleteDate: '2020-08-11',
          },
          {
            name: '3',
            createDate: '2020-08-11',
            deleteDate: '2020-08-13',
          },
          {
            name: '4',
            createDate: '2020-08-02',
            deleteDate: '2020-08-08',
          },
        ],
      }
    }
  }
</script>

<style scoped>
  .recycleTitle {
    font-size: 2rem;
    font-weight: bold;
    color: #42b983;
    vertical-align: middle;
  }
</style>
