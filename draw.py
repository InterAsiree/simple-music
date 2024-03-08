from PIL import Image, ImageDraw

def create_rounded_rectangle(width, height, radius, color_fill=(255, 255, 255), color_border=(0, 0, 0)):
    # 创建一个新的空白图片
    img = Image.new('RGB', (width, height), color=color_fill)
    draw = ImageDraw.Draw(img)

    # 绘制圆角矩形
    draw.rectangle([(0, 0), (width, height)], fill=None, outline=color_border)
    draw.rectangle([(radius, radius), (width - radius, height - radius)], fill=color_fill, outline=color_border)

    # 绘制四个圆角
    for corner in [(0, 0), (width, 0), (width, height), (0, height)]:
        x, y = corner
        draw.ellipse([x, y, x + radius * 2, y + radius * 2], fill=color_fill)

    return img

# 使用函数创建圆角矩形并保存
img = create_rounded_rectangle(300, 200, 20)  # 宽度300像素，高度200像素，圆角半径20像素
img.save("rounded_rectangle.png")