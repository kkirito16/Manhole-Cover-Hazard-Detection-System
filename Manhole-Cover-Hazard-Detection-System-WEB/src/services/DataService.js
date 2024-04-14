// 导入 axios
import axios from 'axios';
// 创建一个 axios 实例，用于发送请求
const apiClient = axios.create({
  // 设置后端 API 的基础 URL
  baseURL: 'http://localhost:5000/api',
  // 设置请求头
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json',
  },
});

// 定义一个用于获取数据的函数
export default {
  sendImage(base64Image) {
    // 向 '/upload/image' 路由发送 POST 请求，传递 base64 图片数据
    return apiClient.post('/upload/image', { image: base64Image });
  },
};
