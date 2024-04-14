<template>
  <div class="header-temp-container">
    <div class="nav-links">
      <div class="platformIcon">井盖隐患检测系统</div>
      <el-menu
        :default-active="activeIndex"
        class="nav-menu"
        mode="horizontal"
        @select="handleMenuSelect"
      >
        <el-menu-item index="home">首页</el-menu-item>
      </el-menu>
    </div>
    <div class="userInfo">
      <el-image :src="require('@/assets/admin.jpg')" class="eImage"></el-image>
      <el-dropdown @command="handleLogout">
        <div class="detail user-link">
          <span>阿瑾瑾瑾</span>
          <span>admin</span>
          <i class="el-icon--right"></i>
        </div>
        <template #dropdown>
          <el-dropdown-menu>
            <el-dropdown-item command="logout">退出</el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>
    </div>
  </div>
</template>

<script>
import { Message } from "element-ui"
export default {
  name: "header-temp-container",
  data() {
    return {
      userInfo: JSON.parse(window.localStorage.getItem("userInfo")),
      activeIndex: "home", // 默认选中首页
    }
  },
  methods: {
    // 退出登录
    handleLogout(key) {
      if (key == "logout") {
        window.localStorage.removeItem("userInfo")
        Message({
          type: "success",
          message: "退出登录",
          showClose: true,
          duration: 3000,
        })
        this.$router.replace({ path: "/login" })
      }
    },
    // 处理菜单选择
    handleMenuSelect(index) {
      this.activeIndex = index
      switch (index) {
        case "home":
          this.$router.push("/index")
          break
        case "grading":
          this.$router.push("/grading/index")
          break
        case "about":
          this.$router.push("/about/index")
          break
        default:
          break
      }
    },
  },
}
</script>

<style scoped>
.header-temp-container {
  border-bottom: 1px solid #ddd;
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  height: 60px;
}
.userInfo {
  display: flex;
  flex-direction: row;
  align-items: center;
  margin-right: 20px;
}
.eImage {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  margin-right: 10px;
}
.detail {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: space-around;
}
.nav-links {
  display: flex;
  flex-direction: row;
  margin-right: 20px;
}
.platformIcon {
  align-content: center;
  align-items: center;
  margin-left: 20px;
  margin-right: 40px;
}
.nav-menu {
  background-color: transparent;
}
</style>
