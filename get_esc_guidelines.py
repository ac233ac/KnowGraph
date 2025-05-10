import requests
import fitz  # PyMuPDF
import io

# PDF 文件的直接链接
pdf_url = "https://alicliimg.clewm.net/300/942/1942300/1724992588430638fe11ddc74ce988321055c2dd7c90f1724992585.pdf"

# 发送请求获取 PDF 内容
response = requests.get(pdf_url)
pdf_bytes = response.content

# 使用 PyMuPDF 打开 PDF
with fitz.open(stream=pdf_bytes, filetype="pdf") as doc:
    full_text = ""
    for page in doc:
        text = page.get_text()
        full_text += text + "\n"

# 分割文本为段落
paragraphs = full_text.split('\n')

# 定义要排除的关键词
exclude_keywords = []

# 过滤掉包含排除关键词的段落
filtered_paragraphs = [para for para in paragraphs if not any(keyword in para for keyword in exclude_keywords)]

# 合并过滤后的段落
filtered_text = '\n'.join(filtered_paragraphs)

# 将提取的正文内容保存到 esc_guidelines_raw.txt 文件
with open("esc_guidelines_raw.txt", "w", encoding="utf-8") as f:
    f.write(filtered_text)

print("✅ 正文内容已成功提取并保存到 esc_guidelines_raw.txt 文件中。")
