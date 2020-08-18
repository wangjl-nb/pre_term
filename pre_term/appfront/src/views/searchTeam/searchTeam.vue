<template>
	<div>
		<el-row>
			<el-col :span="24" class="grid-content"></el-col>
			<el-col :span="3" class="grid-content"></el-col>
			<el-col :span="18" class="grid-content">
				<el-col :span="24" class="grid-content">
					<div style="text-align: center">
						<h2 style="font-size: 2rem">寻找你感兴趣的团队。</h2>
					</div>
				</el-col>
				<el-col :span="24" class="grid-content">
					<el-form ref="searchTeam" label-width="100px">

						<el-form-item label="关键字">
							<el-col :span="18">
								<el-input v-model="searchTeam.keyword" placeholder="请输入关键字，如团队名称"></el-input>
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

		<el-row :gutter="20" style="margin-top: 2rem; margin-right: 2rem">
			<el-col :span="6"
							class="grid-content"
							v-for="(item, index) in teams"
							:key="index"
							style="margin-bottom: 3rem">
				<a :href="'/diamond/dashboard/team/'+item.id">
					<el-card :body-style="{ padding: '0px' }" style="height: 16rem">
						<div style="text-align: center">
<!--							<img :src="item.icon" class="image" style="width: 50px; height: 50px">-->
							<h2 style="color: #aa67aa;margin-top:14px">{{item.name}}</h2>
							<h3 >团队人数：{{item.number}}</h3>
							<div style="padding:15px">
								<p class="teamDescription" style="font-family: 隶书">{{item.description}}</p>
							</div>
							
						</div>
					</el-card>
				</a>
			</el-col>
		</el-row>
	</div>
</template>

<script>
	export default {
		name: "SearchTeam",
		data() {
			return {
				searchTeam: {
					keyword: '',
				},
				teams: [
				],
			}
		},
		methods: {
			onSubmit() {
				var that = this
        console.log('submit')
				that.$axios.post('/app/team_search/',
				this.qs.stringify({key: this.searchTeam.keyword}),
						{headers: {'Content-Type':'application/x-www-form-urlencoded'}})
				.then(res => {
          console.log(res)
					this.teams = res.data.list
				})
        // this.$router.go(0)
			},

		},
		mounted() {
			// var that = this
			// console.log(that.$route.params.flag)
		}
	}
</script>

<style scoped>
	.grid-content {
		border-radius: 4px;
		min-height: 36px;
	}

  .teamDescription {
    font-size: 1.3rem;
    display: inline-block;
    overflow:hidden;
    text-overflow:ellipsis;
    display:-webkit-box;
    -webkit-line-clamp:3;
    -webkit-box-orient:vertical;
}
</style>