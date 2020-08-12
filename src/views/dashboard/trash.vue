<template>
  <el-container>
  <el-main class="dashboard">
    <el-row>
          <el-col :span="24">
            <div id="recycleBin">
              <div>
                <el-row :gutter="20">
                  <el-col :span="6" :offset="3"><div class="grid-content">
                    <span class="recycleTitle">回收站</span>
                  </div></el-col>
                  <el-col :span="12" ><div class="grid-content trashButton">
                    <el-button type="success" round>全部恢复</el-button>
                    <el-button type="danger" round>清空回收站</el-button>
                    <el-button type="success" round style="background-color: #42b983;">恢复已选中的部分</el-button>
                    <el-button type="danger" round style="background-color: blueviolet">清空已选中的部分</el-button>
                  </div></el-col>
                </el-row>
              </div>
<!--              :data="trashFile.slice((currentPage-1)*pageSize,currentPage*pageSize)-->
              <el-table
                      :data="trashFile"
                      ref="multipleTable"
                      style="width: 100%">
                <el-table-column
                        type="selection"
                        width="55">
                </el-table-column>
                <el-table-column
                        prop="name"
                        label="文件名"
                        width="200">
                </el-table-column>
                <el-table-column
                        prop="createDate"
                        label="创建时间"
                        width="300">
                </el-table-column>
                <el-table-column
                        prop="deleteDate"
                        label="删除时间"
                        width="300">
                </el-table-column>
                <el-table-column
                        label="操作"
                        width="300">
                  <template slot-scope="scope">
                    <el-button type="success"
                               size="small"
                               @click.native.prevent="deleteRow(scope.$index, trashFile)">恢复</el-button>
                    <el-button type="danger"
                               size="small"
                               @click.native.prevent="deleteRow(scope.$index, trashFile)">删除</el-button>
                  </template>
                </el-table-column>
              </el-table>

<!--              <el-pagination-->
<!--                      background-->
<!--                      layout="prev, pager, next"-->
<!--                      :total="trashFile.length"-->
<!--                      :page-size="pageSize"-->
<!--                      :current-page="currentPage"-->
<!--                      @current-change="handleCurrentChange">-->
<!--              </el-pagination>-->
              <el-button type="text" @click="nameSort('name')">按文件名排序</el-button>
              <el-button type="text" @click="createDateSort('createDate')">按创建日期排序</el-button>
              <el-button type="text" @click="deleteDateSort('deleteDate')">按删除日期排序</el-button>
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
            name: '4',
            createDate: '2020-08-07',
            deleteDate: '2020-08-11',
          },
          {
            name: '3',
            createDate: '2020-08-11',
            deleteDate: '2020-08-13',
          },
          {
            name: '2',
            createDate: '2020-08-02',
            deleteDate: '2020-08-08',
          },
          {
            name: '9',
            createDate: '2020-08-01',
            deleteDate: '2020-08-08',
          },
          {
            name: '10',
            createDate: '2020-08-09',
            deleteDate: '2020-08-17',
          },
          {
            name: '8',
            createDate: '2020-08-10',
            deleteDate: '2020-08-11',
          },
          {
            name: '5',
            createDate: '2020-08-01',
            deleteDate: '2020-08-14',
          },
          {
            name: '7',
            createDate: '2020-08-08',
            deleteDate: '2020-08-08',
          },
          {
            name: '6',
            createDate: '2020-08-07',
            deleteDate: '2020-08-08',
          },
        ],
        pageSize: 4,
        currentPage: 1,
        sortType: 'name',
        upName: true,
        upCreateDate: true,
        upDeleteDate: true,
      }
    },
    computed: {

    },
    methods: {
      nameSort(type) {
        this.upName = !this.upName;
        if(this.upName) {
          this.sort1(type);
        }
        else {
          this.sort2(type);
        }
      },
      createDateSort(type) {
        this.upCreateDate = !this.upCreateDate;
        if(this.upCreateDate) {
          this.sort1(type);
        }
        else {
          this.sort2(type);
        }
      },
      deleteDateSort(type) {
        this.upDeleteDate = !this.upDeleteDate;
        if(this.upDeleteDate) {
          this.sort1(type);
        }
        else {
          this.sort2(type);
        }
      },
      sort1(type) {
        this.sortType = type;
        this.trashFile.sort(this.compare1(type))
      },
      sort2(type) {
        this.sortType = type;
        this.trashFile.sort(this.compare2(type))
      },
      compare1(attr) {
        return function (a, b) {
          let val1 = new Date(a[attr]);
          let val2 = new Date(b[attr]);
          return val1 - val2;
        }
      },
      compare2(attr) {
        return function (a, b) {
          let val1 = new Date(a[attr]);
          let val2 = new Date(b[attr]);
          return val2 - val1;
        }
      },
      handleCurrentChange(val) {
        this.currentPage = val
      },
      deleteRow(index, rows) {
        rows.splice(index, 1);
        console.log(index)
      },
      // open(index, rows) {
      //   this.$confirm('此操作将永久删除该文件, 是否继续?', '提示', {
      //     confirmButtonText: '确定',
      //     cancelButtonText: '取消',
      //     type: 'warning'
      //   }).then(() => {
      //     rows.splice(index, 1)
      //     this.$message({
      //       type: 'success',
      //       message: '删除成功!'
      //     });
      //   }).catch(() => {
      //     this.$message({
      //       type: 'info',
      //       message: '已取消删除'
      //     });
      //   });
      // }
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
