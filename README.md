1. 获取原始指南文本
get_acc_guidelines.py：提取 ACC 指南的文本并保存为 acc_guidelines.txt。
get_esc_guidelines.py：提取 ESC 指南的文本并保存为 esc_guidelines_raw.txt。

2. 清洗 ESC 指南文本
clean_esc_guidelines.py：对 esc_guidelines_raw.txt 中的内容进行清洗，去除：
作者、参考文献等无关内容页码、标题符号、网址等干扰性文本

3. 清洗后的结果保存在 esc_guidelines.txt 中，便于后续分析或知识抽取。
