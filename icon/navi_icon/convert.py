import os
import re


def convert_android_vector_to_svg(xml_content):
    """将 Android Vector XML 内容转换为标准的 SVG 格式的内容，仅替换必要的颜色属性。"""
    # 使用正则表达式替换 vector 标签为 svg，并设置合适的命名空间
    svg_content = re.sub(
        r'<vector[^>]*>',
        '<svg xmlns="http://www.w3.org/2000/svg" width="48px" height="48px"> ',
        xml_content
    )
    svg_content = svg_content.replace('android: fillColor = "?attr/navigationTextColorTertiary"', 'fill="#FFFFFF"')
    svg_content = svg_content.replace('android:fillColor="@color/directionBackground"', 'fill="#FFFFFF"')
    svg_content = svg_content.replace('android:pathData="', 'd="')
    svg_content = svg_content.replace('android:fillColor="@color/directionBackground"', 'fill="#FFFFFF"')

    # 替换颜色引用为白色

    # 确保所有 vector 结束标签都被替换为 svg 结束标签
    svg_content = svg_content.replace('</vector>', '</svg>')

    return svg_content


def process_files(base_path, numbers):
    svg_folder = "svg"
    png_folder = "png"
    os.makedirs(svg_folder, exist_ok=True)
    os.makedirs(png_folder, exist_ok=True)

    for number in numbers:
        file_path = os.path.join(base_path, f"{number}.xml")
        output_svg_path = os.path.join(svg_folder, f"{number}.svg")
        output_png_path = os.path.join(png_folder, f"{number}.png")

        try:
            import cairosvg
            cairosvg.svg2png(url=output_svg_path, write_to=output_png_path, output_width=150, output_height=150)
            print(f"Processed file {number} successfully.")
        except Exception as e:
            print(f"Failed to process file {number}: {e}")


def main():
    base_path = "./xml"
    numbers = list(range(0, 39))
    process_files(base_path, numbers)


if __name__ == "__main__":
    main()
