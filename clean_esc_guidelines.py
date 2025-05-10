import re

# 读取原始文件内容
with open("esc_guidelines_raw.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# 定义需要排除的关键词列表
exclude_keywords = [
    "Author", "AUTHORS", "author",
    "References", "REFERENCES", "references",
    "Footnote", "FOOTNOTE", "footnote",
    "Acknowledgements", "ACKNOWLEDGEMENTS", "acknowledgements",
    "Supplementary Material", "SUPPLEMENTARY MATERIAL", "supplementary material",
    "Table of Contents", "TABLE OF CONTENTS", "table of contents",
    "Index", "INDEX", "index",
    "ESC Guidelines" ,"Continued"
]

# 定义需要排除的正则表达式模式列表
exclude_patterns = [
    r"^Figure \d+",              # 图表，例如 "Figure 1"
    r"^Table \d+",               # 表格，例如 "Table 1"
    r"^\s*\d+\s*$",              # 仅包含数字的行
    r"^\s*–\s*.*",               # 破折号开头的行
    r"^\s*—\s*.*",               # 长破折号开头的行
    r"^\s*\*\s*.*",              # 星号开头的行
    r"^\s*·\s*.*",               # 圆点开头的行
    r"^\s*•\s*.*",               # 项目符号开头的行
    r"^\s*Continued\s.*",        # "Continued"开头的行
    r"^http.*",                  # "http"开头的行
    r"^\s*\d.*",                 # 以数字开头的行
]

# 清洗后的内容列表
cleaned_lines = []
skip_preamble = False
skip_evidence_tables = False
in_range = False  # 标志位，标记是否在 "1.Preamble" 和 "10.Evidencetables" 之间
preamble_count = 0  # 用于计数第几个 "1. Preamble" 被遇到
evidence_tables_count = 0  # 用于计数第几个 "10. Evidence tables" 被遇到

# 遍历每一行，进行清洗
for line in lines:
    stripped_line = line.strip()

    # 跳过空行
    if not stripped_line:
        continue

    # 检查是否进入了 "1.Preamble" 和 "10.Evidencetables" 之间的范围
    if re.match(r"^1\. Preamble", stripped_line):
        preamble_count += 1  # 遇到 "1. Preamble" 后增加计数器

        if preamble_count == 2:  # 第二个 "1. Preamble" 后开始清洗
            skip_preamble = True
            in_range = True  # 进入清洗范围
        continue

    # 跳过“10.Evidencetables”之后的所有内容
    if skip_evidence_tables:
        continue
    if re.match(r"^10\. Evidence tables", stripped_line):
        evidence_tables_count += 1  # 遇到 "10. Evidence tables" 后增加计数器

        if evidence_tables_count == 2:  # 第二个 "10. Evidence tables" 后跳过所有内容
            skip_evidence_tables = True
        continue


    # 如果不在范围内，跳过
    if not in_range:
        continue

    # 跳过包含排除关键词的行
    if any(keyword in stripped_line for keyword in exclude_keywords):
        continue

    # 跳过匹配排除模式的行
    if any(re.match(pattern, stripped_line) for pattern in exclude_patterns):
        continue

    # 保留其余行
    cleaned_lines.append(stripped_line)

# 将清洗后的内容写入新文件
with open("esc_guidelines.txt", "w", encoding="utf-8") as file:
    for line in cleaned_lines:
        file.write(line + "\n")

print("✅ 清洗完成，结果已保存至 esc_guidelines.txt 文件。")
