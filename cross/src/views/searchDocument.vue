<template>
	<div>
		<el-row>
			<el-col :span="24" class="grid-content"></el-col>
			<el-col :span="3" class="grid-content"></el-col>
			<el-col :span="18" class="grid-content">
				<el-col :span="24" class="grid-content">
					<div style="text-align: center">
						<h2 style="font-size: 2rem">发现你的文件。</h2>
					</div>
				</el-col>
				<el-col :span="24" class="grid-content">
					<el-form ref="searchTeam" :model="searchDocument" label-width="100px">

						<el-form-item label="关键字">
							<el-col :span="18">
								<el-input v-model="searchDocument.keyword" placeholder="请输入关键字，如文档名称"></el-input>
							</el-col>
							<el-col :span="6">
									<el-button type="primary" @click="onSubmit" icon="el-icon-search" style="display: inline-block">搜索</el-button>
							</el-col>
						</el-form-item>
					</el-form>
				</el-col>
			</el-col>
			<el-col :span="3" class="grid-content"></el-col>
		</el-row>

		<el-row  style="margin-top: 2rem; margin-right: 2rem" :span="24" :gutter="20" v-for="(item,index) in searchDocument.list" :key="index">
        <el-col :span="18">
           <el-card shadow="hover" >
               <div class="flex flex6">
                   <div style="margin-top:0px">  
                        <i class="iconfont icon-wenjian" style="font-size:40px"></i> 
                  </div> 
                    <div style="margin-left:20px;margin-top:0px">  
                        <a style="font-size:18px" :href="'/editor/'+item.id">{{item.name}}</a>
                        <p style="color:gray;font-size:13px">于{{item.create}}  {{item.author}}创建   最后一次更新为{{item.user}}编辑于{{item.edit}} 时</p>
                    </div>
               </div>
                  
           </el-card>
        </el-col> 
		</el-row>
	</div>
</template>

<script>
	export default {
        name: "SearchDocument",
		data() {
			return {
				searchDocument: {
                    keyword: '',
                     list:  [{name:"jackffgf",id:123432,author:"mala",create:"2020/2/2",edit:"2020/2/4",user:"222xs"},
        {name:"jaca324sdk",id:1232432,author:"masla",create:"2020/2/2",edit:"2020/2/4",user:"222xs"},
        {name:"jacs234dak",id:123345672,author:"malsa",create:"2020/2/2",edit:"2020/2/4",user:"222xs"}
        ]  
			   }	
            }
        },
		methods: {
			onSubmit() {
				var that = this
        //         this.searchDocument.list= [{name:"j",id:123432,author:"mala",create:"2020/2/2",edit:"2020/2/4",user:"222xs"},
        // {name:"jaca",id:1232432,author:"masla",create:"2020/2/2",edit:"2020/2/4",user:"222xs"},
        // {name:"jac",id:123345672,author:"malsa",create:"2020/2/2",edit:"2020/2/4",user:"222xs"}
        // ]
				that.$axios.post('',
						this.qs.stringify({keyword: that.searchDocument.keyword}),
						{headers: {'Content-Type': 'application/x-www-form-urlencoded'}})
						.then(res => {
							this.searchDocument.list = res.data.list
						})
			},

		},
		mounted() {
			var that = this
			console.log(that.$route.params.flag)

		}
	}
</script>

<style scoped>
	.grid-content {
		border-radius: 4px;
		min-height: 36px;
	}
</style>