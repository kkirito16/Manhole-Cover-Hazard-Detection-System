<template>
	<div class="login-wrapper">
		<div class="modal">
			<el-form :model="user" status-icon :rules="rules" ref="userForm">
				<div class="title">欢迎登录</div>
				<el-form-item prop="username">
					<el-input type="text" prefix-icon="el-icon-user" placeholder="请输入用户名" v-model="user.username" />
				</el-form-item>
				<el-form-item prop="password">
					<el-input type="password" prefix-icon="el-icon-view" placeholder="请输入密码" v-model="user.password" />
				</el-form-item>
				<el-form-item>
					<el-button type="primary" class="btn-login" @click="login">登录</el-button>
				</el-form-item>
				<el-form-item>
					<el-button type="primary" class="btn-register" @click="register">注册</el-button>
				</el-form-item>
			</el-form>
		</div>
	</div>
</template>
<script>
import dynamicUser from "../../mock"
import { Message } from "element-ui"

export default {
	name: 'login',
	data() {
		return {
			user: {
				username: "",
				password: ""
			},
			rules: {
				username: [
					{ required: true, message: '请输入用户名', trigger: 'blur' }
				],
				password: [
					{ required: true, message: '请输入密码', trigger: 'blur' }
				]
			}
		}
	},
	methods: {
		login() {
			this.$refs.userForm.validate(( valid ) => {
			    if(valid) {
					let flag = !1
					window.localStorage.removeItem("userInfo")
					dynamicUser.forEach(item => {
						if(item["username"] == this.user['username'] && item["password"] == this.user['password']) {
							flag = !0
							Message({ type: 'success', message: "登录成功", showClose: true, duration: 3000 })
							window.localStorage.setItem("userInfo", JSON.stringify(item))
							this.$router.replace({ path: "/" })
						}
					})
					if(!flag) Message({ type: 'warning', message: "账号密码错误，请重试!", showClose: true, duration: 3000 })
			    } else return false
			})
		},
		register() {

		}
	}
}
</script>
<style scoped>
.login-wrapper {
	display: flex;
	flex-direction: row;
	align-items: center;
	background-image: url('../../assets/login-background.png');
	background-size: cover;
	background-position: center;
	width: 100vw;
	height: 100vh;
}
.modal {
	width: 360px;
	height: 380px;
	box-shadow: 0 3px 6px -4px #0000001f, 0 6px 16px #00000014, 0 9px 28px 8px #0000000d;
	background-color: #fff;
	padding: 50px;
	border-radius: 5px;
	margin-left: auto;
	margin-right: 6vw;
}
.title {
	width: 100%;
	text-align: center;
	line-height: 1.5;
	font-size: 50px;
	margin-bottom: 30px;
}
.btn-login {
	margin-top: 20px;
	width: 100%;
	border-color: rgb(0,0,0,0.1);
}
.btn-register{
	width: 100%;
	background: #cacdcf;
	border-color: rgb(0,0,0,0.1);
}
.toast{
	width: 100%;
	display: flex;
	flex-direction: row;
	align-items: center;
	justify-content: space-between;
	height: 50px;
}
</style>