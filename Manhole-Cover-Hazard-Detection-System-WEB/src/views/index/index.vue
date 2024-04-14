<template>
  <div class="home">
    <div class="title">
      井盖隐患检测系统
      <div class="upload-container">
      <el-upload
        class="upload-demo"
        action="#"
        :on-change="onChange"
        :before-upload="beforeUpload"
        accept="image/*"
        :show-file-list="false"
        :auto-upload="false"
      >
        <el-button type="primary" class="upload-demo">上传图片</el-button>
      </el-upload>
    </div>
    </div>
    <div class="main-content">
      <div class="image-container">
        <div class="image-container-title">原图</div>
        <div class="image-wrapper">
          <img
            :src="originalImageUrl"
            alt="Original Image"
            v-if="originalImageUrl"
            class="image"
          />
        </div>
      </div>
      <div class="image-container">
        <div class="image-container-title">处理后的图片</div>
        <div class="image-wrapper">
          <img
            :src="processedImageUrl"
            alt="Processed Image"
            v-if="processedImageUrl"
            class="image"
          />
        </div>
      </div>
      <div class="indicators">
        <p>井盖完好:{{ count0 }}</p>
        <p>井盖破损:{{ count1 }}</p>
        <p>井盖丢失:{{ count2 }}</p>
        <p>井盖未盖:{{ count3 }}</p>
        <p>井盖问题:{{ count4 }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import DataService from "../../services/DataService"
export default {
  data() {
    return {
      originalImageUrl: "",
      processedImageUrl: "",
      message: "",
      items: [],
      count0: 0,
      count1: 0,
      count2: 0,
      count3: 0,
      count4: 0,
    }
  },
  methods: {
    beforeUpload(file) {
      const isLt5M = file.size / 1024 / 1024 < 5
      if (!isLt5M) {
        this.$message.error("上传图片大小不能超过5MB!")
      }
      return isLt5M
    },
    onChange(file, fileList) {
      this.getBase64(file.raw)
        .then((base64Data) => {
          // 调用 DataService 发送图片数据到后端
          DataService.sendImage(base64Data)
            .then((response) => {
              // 处理发送成功后的逻辑，比如显示返回的消息等
              console.log(response.data)
              this.originalImageUrl = URL.createObjectURL(file.raw)
              this.processedImageUrl = response.data.image
              this.count0 = response.data.count0
              this.count1 = response.data.count1
              this.count2 = response.data.count2
              this.count3 = response.data.count3
              this.count4 = response.data.count4
            })
            .catch((error) => {
              // 处理发送失败的逻辑
              console.error(error)
            })
        })
        .catch((error) => {
          // 处理获取 base64 数据失败的逻辑
          console.error(error)
        })
    },

    getBase64(file) {
      return new Promise(function (resolve, reject) {
        let reader = new FileReader()
        let imgResult = ""
        reader.readAsDataURL(file)
        reader.onload = function () {
          imgResult = reader.result
        }
        reader.onerror = function (error) {
          reject(error)
        }
        reader.onloadend = function () {
          resolve(imgResult)
        }
      })
    },
  },
}
</script>

<style>
.title {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  text-align: center;
  font-size: 40px;
  font-weight: bold;
  margin-bottom: 30px;
}

.main-content {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

.image-container {
  margin-right: 50px; /* 右侧留出空白 */
}
.image-container-title {
  font-size: 30px;
  margin-bottom: 5px;
  margin-left: 5px;
  text-align: center;
}
.image {
  width: 320px;
  height: auto;
}
.image-wrapper {
  border: 2px dashed lightgray; /* 添加黑色的边框 */
  padding: 10px; /* 添加内边距 */
  margin-bottom: 20px; /* 底部留出空白 */
  width: 400px;
  height: 450px;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

.indicators {
  text-align: left; /* 将指标靠右对齐 */
  border: 2px dashed lightgray; /* 添加灰色的边框 */
  border-radius: 10px;
  height: 250px;
  width: 300px;
  align-content: center;
}

.indicators p {
  margin-left: 10px;
  font-size: 20px;
}

.upload-container {
  display: flex;
  left: 20px;
  bottom: 20px;
  margin-left: 40px;
}
</style>
