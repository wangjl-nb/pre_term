<template>
  <el-container>
    <el-main class="dashboard">
      <el-row>
        <el-col :span="24">
          <div id="recycleBin">
            <div>
              <el-row :gutter="20">
                <el-col :span="6" :offset="3">
                  <div class="grid-content">
                    <span class="recycleTitle">回收站</span>
                  </div>
                </el-col>
                <el-col :span="12">
                  <div class="grid-content trashButton">
                    <el-button type="success" round @click="recoverAll">全部恢复</el-button>
                    <el-button type="danger" round @click="deleteAll">清空回收站</el-button>
                    <el-button type="success" round
                               style="background-color: #42b983;" @click="recoverSelection">恢复已选中的部分
                    </el-button>
                    <el-button type="danger" round
                               style="background-color: blueviolet" @click="deleteSelection">清空已选中的部分
                    </el-button>
                  </div>
                </el-col>
              </el-row>
            </div>
            <!--              :data="trashFile.slice((currentPage-1)*pageSize,currentPage*pageSize)-->
            <el-table
                :data="trashFile"
                ref="trashFile"
                style="width: 100%">
              <el-table-column
                  type="selection"
                  width="55">
              </el-table-column>
              <el-table-column
                  prop="title"
                  label="文件名"
                  width="200">
              </el-table-column>
              <el-table-column
                  prop="create_date"
                  label="创建时间"
                  width="300">
              </el-table-column>
              <el-table-column
                  prop="delete_date"
                  label="删除时间"
                  width="300">
              </el-table-column>
              <el-table-column
                  label="操作"
                  width="300">
                <template slot-scope="scope">
                  <el-button type="success"
                             size="small"
                             @click.native.prevent="recoverOne(scope.$index, trashFile)">恢复
                  </el-button>
                  <el-button type="danger"
                             size="small"
                             @click.native.prevent="deleteOne(scope.$index, trashFile)">删除
                  </el-button>
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
            <el-button type="text" @click="titleSort('title')">按文件名排序</el-button>
            <el-button type="text" @click="createDateSort('create_date')">按创建日期排序</el-button>
            <el-button type="text" @click="deleteDateSort('delete_date')">按删除日期排序</el-button>
          </div>
        </el-col>
      </el-row>
    </el-main>
  </el-container>
</template>

<script>
export default {
  name: "Trash",
  data() {
    return {
      trashFile: [{
        title: 1,
        create_date: '2020-01-02',
        delete_date: '2020-01-03',
      }, {
        title: 2,
        create_date: '2020-01-01',
        delete_date: '2020-01-04',
      }, ],
      ids: [],
      pageSize: 4,
      currentPage: 1,
      sortType: 'title',
      upName: true,
      upCreateDate: true,
      upDeleteDate: true,
    }
  },
  mounted() {
    this.$axios.post('/app/personal_delete_files/')
        .then(res => {
          console.log(res)
          this.trashFile = res.data.list
        })
  },

  methods: {
    recoverOne(index, row) {
      this.$confirm('此操作将恢复已删除的文件，是否继续？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
      }).then(() => {
        this.ids = []
        this.ids.push(row[index].id)
        this.$axios.post('/app/recover_file/', {
          //key(接口):value
          ids: this.ids
        }).then(res => {
          if (res.data.status === 0) {
            this.$message({
              message: '恢复成功',
              type: 'success',
            })
            this.$router.go(0)
          }
        })
      }).catch(() => {
        this.$message({
          message: '已取消恢复操作',
          type: 'info',
        })
      })
    },


    deleteOne(index, row) {
      this.$confirm('此操作将彻底删除该文件，是否继续？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
      }).then(() => {
        this.ids = []
        this.ids.push(row[index].id)
        this.$axios.post('/app/destroy_file/', {
          ids: this.ids
        }).then(res => {
          if (res.data.status === 0) {
            this.$message({
              message: '删除成功',
              type: 'success',
            })
            this.$router.go(0)
          }
        })
      }).catch(() => {
        this.$message({
          message: '已取消删除操作',
          type: 'info',
        })
      })
    },


    recoverAll() {
      this.$confirm('此操作将恢复已删除的文件，是否继续？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
      }).then(() => {
        this.ids = []
        for (let i = 0; i < this.trashFile.length; i++) {
          this.ids.push(this.trashFile[i].id)
        }
        this.$axios.post('/app/recover_file/', {
          ids: this.ids
        }).then(res => {
          if (res.data.status === 0) {
            this.$message({
              message: '恢复成功',
              type: 'success',
            })
            this.$router.go(0)
          }
        })
      }).catch(() => {
        this.$message({
          message: '已取消恢复操作',
          type: 'info',
        })
      })
    },


    deleteAll() {
      this.$confirm('此操作将彻底删除该文件，是否继续？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
      }).then(() => {
        this.ids = []
        for (let i = 0; i < this.trashFile.length; i++) {
          this.ids.push(this.trashFile[i].id)
        }
        this.$axios.post('/app/destroy_file/', {
          ids: this.ids
        }).then(res => {
          if (res.data.status === 0) {
            this.$message({
              message: '删除成功',
              type: 'success',
            })
            this.$router.go(0)
          }
        })
      }).catch(() => {
        this.$message({
          message: '已取消删除操作',
          type: 'info',
        })
      })
    },


    recoverSelection() {
      this.$confirm('此操作将恢复已删除的文件，是否继续？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
      }).then(() => {
        let selectData = this.$refs.trashFile.selection;
        this.ids = []
        for (let i = 0; i < selectData.length; i++) {
          this.ids.push(selectData[i].id)
        }
        this.$axios.post('/app/recover_file/', {
          ids: this.ids
        }).then(res => {
          if (res.data.status === 0) {
            this.$message({
              message: '恢复成功',
              type: 'success',
            })
            this.$router.go(0)
          }
        })
      }).catch(() => {
        this.$message({
          message: '已取消恢复操作',
          type: 'info',
        })
      })

    },
    deleteSelection() {
      var that = this
      this.$confirm('此操作将彻底删除该文件，是否继续？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
      }).then(() => {
        let selectData = this.$refs.trashFile.selection;
        this.ids = []
        for (let i = 0; i < selectData.length; i++) {
          this.ids.push(selectData[i].id)
        }
        this.$axios.post('/app/destroy_file/', {
          ids: this.ids
        }).then(res => {
          if (res.data.status === 0) {
            this.$message({
              message: '删除成功',
              type: 'success',
            })
            this.$router.go(0)
          }
        })
      }).catch(() => {
        this.$message({
          message: '已取消删除操作',
          type: 'info',
        })
      })
    },


    titleSort(type) {
      this.upName = !this.upName;
      if (this.upName) {
        this.sort1(type);
      } else {
        this.sort2(type);
      }
    },
    createDateSort(type) {
      this.upCreateDate = !this.upCreateDate;
      if (this.upCreateDate) {
        this.sort1(type);
      } else {
        this.sort2(type);
      }
    },
    deleteDateSort(type) {
      this.upDeleteDate = !this.upDeleteDate;
      if (this.upDeleteDate) {
        this.sort1(type);
      } else {
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
        console.log(val1)
        let val2 = new Date(b[attr]);
        console.log(val2)
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
