from PIL import Image
import os

def create_favicon(input_path, output_dir):
    # 确保输出目录存在
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 打开原始图片
    try:
        original = Image.open(input_path)
        
        # 定义需要的尺寸
        sizes = {
            'favicon.ico': (32, 32),
            'favicon-32x32.png': (32, 32),
            'favicon-16x16.png': (16, 16),
            'apple-touch-icon.png': (180, 180)
        }
        
        # 为每个尺寸创建图标
        for filename, size in sizes.items():
            # 创建一个副本并调整大小
            img_copy = original.copy()
            img_copy = img_copy.resize(size, Image.Resampling.LANCZOS)
            
            # 保存文件
            output_path = os.path.join(output_dir, filename)
            
            # 如果是.ico文件，需要特殊处理
            if filename.endswith('.ico'):
                img_copy.save(output_path, format='ICO', sizes=[(size[0], size[1])])
            else:
                img_copy.save(output_path, format='PNG')
            
            print(f'已生成 {filename}')
            
    except Exception as e:
        print(f'处理图片时出错: {str(e)}')

if __name__ == '__main__':
    # 设置输入和输出路径
    input_image = '/Users/caojie/Documents/Projects/JieJayCao.github.io/images/logo.png'
    output_directory = '/Users/caojie/Documents/Projects/JieJayCao.github.io/images/new_logo'
    
    create_favicon(input_image, output_directory)
