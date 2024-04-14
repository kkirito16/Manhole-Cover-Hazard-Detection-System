from ultralytics import YOLO
from PIL import Image
from io import BytesIO
import io
import base64

# 导入 Flask
from flask import Flask, jsonify, request
# 导入 CORS
from flask_cors import CORS

# 创建一个 Flask 应用实例
app = Flask(__name__)
# 并允许来自所有域的请求
CORS(app)

# Load a model
# model = YOLO('runs/detect/yolov8_train4/weights/best.pt')  # pretrained YOLOv8n model
model = YOLO('best.pt')


def process_image(base64_image):
    # 解码 base64 图片数据
    image_data = base64.b64decode(base64_image.split(',')[1])
    # 将数据转换为图像格式
    img = Image.open(BytesIO(image_data))
    # 调整图像大小或其他预处理操作
    # 在这里可以添加你的预处理逻辑
    return img


@app.route('/api/upload/image', methods=['POST'])
def upload_image():
    # 初始化计数变量
    count0 = 0
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0

    # 从请求体中获取传递过来的 base64 图片数据
    base64_image = request.json.get('image')

    # 处理接收到的图片数据
    img = process_image(base64_image)

    # 在这里调用 YOLO 模型进行物体检测等操作
    results = model(img)
    for result in results:
        boxes = result.boxes  # Boxes object for bounding box outputs
        masks = result.masks  # Masks object for segmentation masks outputs
        class_ids = result.boxes.cls.int().tolist()  # Class IDs
        keypoints = result.keypoints  # Keypoints object for pose outputs
        probs = result.probs  # Probs object for classification outputs

        # 更新计数变量
        for class_id in class_ids:
            if class_id == 0:
                count0 += 1
            if class_id == 1:
                count1 += 1
            elif class_id == 2:
                count2 += 1
            elif class_id == 3:
                count3 += 1
            elif class_id == 4:
                count4 += 1

        # 将图片保存为临时文件
        for i, result in enumerate(results):
            # 将结果保存为本地图片
            result.save(f"result_{i}.jpg")
            # 将保存的本地图片转换为base64格式
            with open(f"result_{i}.jpg", "rb") as image_file:
                base64_img = base64.b64encode(image_file.read()).decode()
                base64_img = 'data:image/jpeg;base64,' + base64_img

    # 返回一个响应，告诉前端图片上传成功，同时返回base64格式的图片和各类别的计数
    return jsonify({'message': 'Image uploaded successfully!!',
                    'image': base64_img,
                    'count0': count0,
                    'count1': count1,
                    'count2': count2,
                    'count3': count3,
                    'count4': count4,})

# 如果作为主程序运行，启动应用
if __name__ == '__main__':
    app.run(debug=True)
