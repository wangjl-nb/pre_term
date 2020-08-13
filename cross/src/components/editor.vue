<template>

  <el-container>
    <!--头部导航栏-->
    <el-header>
      <div class="flex flex6" >
        <div style="">
          <svg class="icon" aria-hidden="true" style="width:4em;height:4em">
            <use xlink:href="#icon-wendang"></use>
          </svg>
        </div>
        <div style="margin-left:20px;margin-right:30px">
          <h1 class="change-color" style="font-weight:lighter "><li>个人文档</li></h1>
        </div>
        <router-link :to="{path: 'changefile/', query: {fileId: fileId}}">
          <el-button type="primary" plain>修改</el-button>
        </router-link>
        <el-button type="primary" plain @click="drawer = true" style="margin-left: 10px">协作</el-button>
        <input type="text" v-model="localURL" style="display: none">
        <el-button class="copyURL"
                   :data-clipboard-text="localURL"
                   type="primary"
                   @click="copy" plain style="margin-left: 10px">
          分享</el-button>
        <el-button type="primary" plain >收藏</el-button>
        <el-button type="primary" plain >删除</el-button>
      </div>
    </el-header>
    <!--drawer设置-->
    <el-drawer
      :visible.sync="drawer"
      :with-header="false"
      :direction="direction">
      <h1 style="margin-left:100px">
        <svg class="icon" aria-hidden="true" style="width:3em;height:3em">
          <use xlink:href="#icon-quanxian"></use>
        </svg>
        <span style="margin-top:15px;margin-left:20px;position:absolute">协作权限管理</span>
      </h1>
      <div style="margin-top: 15px;">
        <el-input placeholder="输入 邮箱/用户名 添加协作权限" v-model="search">
          <template slot="prepend">
            <el-button slot="reference">
              <svg class="icon" aria-hidden="true" style="width:2em;height:2em">
                <use xlink:href="#icon-sousuo"></use>
              </svg>
            </el-button>
          </template>
        </el-input>
        <!--协作者列表卡片-->
        <div>
          <el-card class="box-card" shadow="never">
            <div slot="header" class="clearfix">
              <span style="font-size:17px;position:absolute;margin-top:-5px;margin-left:20px">协作者</span>
              <el-popover
                placement="bottom"
                width="200"
                trigger="click"
                style="float: right">
                <el-button slot="reference" style="float: right; padding: 3px 0" type="text">
                  添加协作者
                  <i class="el-icon-circle-plus-outline"></i>
                </el-button>
                <div v-if="searchItem.length>0">
                  <ul v-for="(item,index) in searchItem" :key="index">
                    <li style="position:relative">
                      <!--头像-->
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
              </el-popover>
            </div>
            <div>
              <div>
                <ul v-for="(item,index) in searchItem" :key="index">
                  <li style="position:relative">
                    <svg class="icon" aria-hidden="true" style="width:2em;height:2em">
                      <use xlink:href="#icon-renwu2"></use>
                    </svg>
                    <el-avatar size="medium" :src="item.img" class="img"></el-avatar>
                    <span class="user_name">
                     {{item.name}}
                    </span>
                    <template>
                      <el-select v-model="value" placeholder="请选择权限" style="float: right; padding: 3px 0" type="text">
                        <el-option
                          v-for="item in options"
                          :key="item.value"
                          :label="item.label"
                          :value="item.value">
                        </el-option>
                      </el-select>
                    </template>
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
    </el-drawer>
    <!--中间文件内容-->
    <el-main>
<!--      <div class="editor">-->
<!--        <div ref="toolbar" class="toolbar">-->
<!--        </div>-->
<!--        <div ref="editor" class="text">-->
<!--        </div>-->
<!--      </div>-->
      <h2>标题</h2>
      <h3>创建者：xxx 创建时间：xxx</h3>
      <p>文档内容</p>
    </el-main>
    <!--底部评论区-->
    <el-footer>
      <el-col :span="24" v-if="">
        <el-col :span="2" class="grid-content"></el-col>
        <el-col :span="20">
          <el-form action="#" ref="commentTextarea" label-width="100px">
            <el-form-item label="评论">
              <el-input type="textarea" placeholder="请在此发表评论"></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="onSubmit">提交</el-button>
            </el-form-item>
          </el-form>
        </el-col>
        <el-col :span="2" class="grid-content"></el-col>
      </el-col>

      <div style="text-align: center">
        <h2 style="font-size: 2rem">评论区</h2>
      </div>

      <el-row  v-for="(item, index) in comment" :key="index">
        <el-col :span="3" class="grid-content"></el-col>
        <el-col :span="19">
          <el-card shadow="always" style="margin-bottom: 1rem">
            <el-col :span="12"><span>用户名：{{item.userName}}</span></el-col>
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
  import wangEnduit from "./wangEnduit";
  import E from 'wangeditor';
    export default {
        name: "editor",
        components:{
          wangEnduit
        },
      data() {
        return {
          //悬浮框
          visible: false,
          isComment: false,
          localURL: '',
          //权限下拉显示框
          options: [{
            value: '选项1',
            label: '只能阅读'
          }, {
            value: '选项2',
            label: '只能阅读和评论'
          }, {
            value: '选项3',
            label: '可以编辑'
          }],
          value: '',
          //查找协作者
          search:"",
          searchItem:[
            {id:123,img:'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',name:"sadasd"},
            {id:123,img:'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',name:"sadasd"},
            {id:123,img:'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',name:"sadasd"}
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
          comment: [
            {userName: '用户1', content: '评论内容1', time: '2020-08-10'},
            {userName: '用户2', content: '评论内容2', time: '2020-08-13'},
            {userName: '用户3', content: '评论内容3', time: '2020-08-12'},
            {userName: '用户4', content: '评论内容4', time: '2020-08-15'},
            {userName: '用户5', content: '评论内容5', time: '2020-08-09'},
          ],
          fileId: 123,
        }
      },
      model: {
        // prop: 'value',
        // event: 'change'
      },
      props: {
        // value: {
        //   type: String,
        //   default: ''
        // },
        // isClear: {
        //   type: Boolean,
        //   default: false
        // }
      },
      watch: {
        // isClear(val) {
        //   // 触发清除文本域内容
        //   if (val) {
        //     this.editor.txt.clear()
        //     this.info_ = null
        //   }
        // },
        // value: function(value) {
        //   if (value !== this.editor.txt.html()) {
        //     this.editor.txt.html(this.value)
        //   }
        // }
        //value为编辑框输入的内容，这里我监听了一下值，当父组件调用得时候，如果给value赋值了，子组件将会显示父组件赋给的值
      },
      mounted() {
        // this.seteditor()
        // this.editor.txt.html(this.value)
        this.getURL()
      },
      methods: {
        handleClick() {
          alert('button click');
        },
        handleClose(done) {
          this.$confirm('确认关闭？')
            .then(_ => {
              done();
            })
            .catch(_ => {});
        },
        handleSelect(key, keyPath) {
          console.log(key, keyPath);
        },
        goBack() {
          console.log('go back');
        },
        // seteditor() {
        //   // http://192.168.2.125:8080/admin/storage/create
        //   this.editor = new E(this.$refs.toolbar, this.$refs.editor)
        //   this.editor.customConfig.uploadImgShowBase64 = false // base 64 存储图片
        //   this.editor.customConfig.uploadImgServer = 'http://otp.cdinfotech.top/file/upload_images'// 配置服务器端地址
        //   this.editor.customConfig.uploadImgHeaders = { }// 自定义 header
        //   this.editor.customConfig.uploadFileName = 'file' // 后端接受上传文件的参数名
        //   this.editor.customConfig.uploadImgMaxSize = 2 * 1024 * 1024 // 将图片大小限制为 2M
        //   this.editor.customConfig.uploadImgMaxLength = 6 // 限制一次最多上传 3 张图片
        //   this.editor.customConfig.uploadImgTimeout = 3 * 60 * 1000 // 设置超时时间
        //
        //   // 配置菜单
        //   this.editor.customConfig.menus = [
        //     'head', // 标题
        //     'bold', // 粗体
        //     'fontSize', // 字号
        //     'fontName', // 字体
        //     'italic', // 斜体
        //     'underline', // 下划线
        //     'strikeThrough', // 删除线
        //     'foreColor', // 文字颜色
        //     'backColor', // 背景颜色
        //     'link', // 插入链接
        //     'list', // 列表
        //     'justify', // 对齐方式
        //     'quote', // 引用
        //     'emoticon', // 表情
        //     'image', // 插入图片
        //     'table', // 表格
        //     'video', // 插入视频
        //     'code', // 插入代码
        //     'undo', // 撤销
        //     'redo', // 重复
        //     'fullscreen' // 全屏
        //   ]
        //
        //   this.editor.customConfig.uploadImgHooks = {
        //     fail: (xhr, editor, result) => {
        //       // 插入图片失败回调
        //     },
        //     success: (xhr, editor, result) => {
        //       // 图片上传成功回调
        //     },
        //     timeout: (xhr, editor) => {
        //       // 网络超时的回调
        //     },
        //     error: (xhr, editor) => {
        //       // 图片上传错误的回调
        //     },
        //     customInsert: (insertImg, result, editor) => {
        //       // 图片上传成功，插入图片的回调
        //       //result为上传图片成功的时候返回的数据，这里我打印了一下发现后台返回的是data：[{url:"路径的形式"},...]
        //       // console.log(result.data[0].url)
        //       //insertImg()为插入图片的函数
        //       //循环插入图片
        //       // for (let i = 0; i < 1; i++) {
        //       // console.log(result)
        //       let url = "http://otp.cdinfotech.top"+result.url
        //       insertImg(url)
        //       // }
        //     }
        //   }
        //   this.editor.customConfig.onchange = (html) => {
        //     this.info_ = html // 绑定当前逐渐地值
        //     this.$emit('change', this.info_) // 将内容同步到父组件中
        //   }
        //   // 创建富文本编辑器
        //   this.editor.create()
        // },
        onSubmit() {
          alert('评论成功')
        },
        copy() {
          let clipboard = new this.Clipboard('.copyURL');
          clipboard.on('success', e => {
            this.$message({
              type: 'success',
              message: '链接已复制到剪贴板'
            });
            clipboard.destroy()
          })
        },
        getURL() {
          this.localURL = location.href
        },
      }
    }
</script>

<style>
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
