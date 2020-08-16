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
					<el-form ref="searchTeam" :model="searchTeam" label-width="100px">

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

		<el-row :gutter="20" style="margin-top: 2rem; margin-right: 2rem" v-if="isDisplay">
			<el-col :span="6"
							class="grid-content"
							v-for="(item,index) in teams"
							:key="index"
							style="margin-bottom: 1rem">
				<a :href="'/team/'+item.id">
					<el-card :body-style="{ padding: '0px' }">
						<div style="text-align: center">
							<img :src="item.icon" class="image" style="width: 50px; height: 50px">
							<h2>{{item.name}}</h2>
							<h3>团队人数：{{item.number_num}}</h3>
							<p>{{item.describe}}</p>
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
					{
						id: 234,
						name: '团队1',
						icon: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
						number_num: 10,
						describe: '团队介绍'
					},
					{
						id: 2,
						name: '团队2',
						icon: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
						number_num: 10,
						describe: '团队介绍'
					},
					{
						id: 3,
						name: '团队3',
						icon: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
						number_num: 10,
						describe: '团队介绍'
					},
					{
						id: 4,
						name: '团队4',
						icon: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
						number_num: 10,
						describe: '团队介绍'
					},
					{
						id: 5,
						name: '团队5',
						icon: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
						number_num: 10,
						describe: '团队介绍'
					},
				],
				isDisplay: false
			}
		},
		methods: {
			onSubmit() {
				this.isDisplay = true
				var that = this
				that.$axios.post('/app/team_search/',
				this.qs.stringify({key: this.searchTeam.keyword}),
						{headers: {'Content-Type':'application/x-www-form-urlencoded'}})
				.then(res => {
					this.team = res.data.list
				})
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
</style>