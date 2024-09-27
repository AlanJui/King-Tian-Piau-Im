chapters = [
    "法會因由分第一", 
    "善現啟請分第二", 
    "大乘正宗分第三", 
    "妙行無住分第四", 
    "如理實見分第五", 
    "正信希有分第六", 
    "無得無說分第七", 
    "依法出生分第八", 
    "一相無相分第九", 
    "莊嚴淨土分第十", 
    "無為福勝分第十一", 
    "尊重正教分第十二", 
    "如法受持分第十三", 
    "離相寂滅分第十四", 
    "持經功德分第十五", 
    "能淨業障分第十六", 
    "究竟無我分第十七", 
    "一體同觀分第十八", 
    "法界通化分第十九", 
    "離色離相分第二十", 
    "非說所說分第二十一", 
    "無法可得分第二十二", 
    "淨心善行分第二十三", 
    "福智無比分第二十四", 
    "化無所化分第二十五", 
    "法身非相分第二十六", 
    "無斷無滅分第二十七", 
    "不受不貪分第二十八", 
    "威儀寂靜分第二十九", 
    "一合理相分第三十", 
    "知見不生分第三十一", 
    "應化非真分第三十二", 
]

# 生成每個章節的 HTML 檔案
for i, chapter in enumerate(chapters):
    with open(f"金剛般若波羅蜜經{str(i+1).zfill(3)}.html", "w", encoding="utf-8") as f:
        prev_link = f'金剛般若波羅蜜經{str(i).zfill(3)}.html' if i > 0 else "#"
        next_link = f'金剛般若波羅蜜經{str(i+2).zfill(3)}.html' if i < len(chapters) - 1 else "#"
        f.write(f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta property="og:image" content="https://alanjui.github.io/Piau-Im/assets/picts/king_tian.png" />
    <title>{chapter} - 金剛般若波羅蜜經</title>
    <link rel="stylesheet" href="./assets/styles/styles.css">
</head>
<body>
    <!-- 頁首 -->
    <header id="header">
        <img src="./assets/picts/king_tian.png" width="300" height="200" alt="四晝五經">
        <h1>金剛般若波羅蜜經</h1>
    </header><!-- /#header -->
    <h1>{chapter}</h1>
    <p>（這裡是該章節的內容）</p>
    <nav>
        <a href="{prev_link}">上一頁</a> | 
        <a href="index.html">回首頁</a> | 
        <a href="{next_link}">下一頁</a>
    </nav>
</body>
</html>
""")

print("Generating index.html...")

# 生成 index.html 檔案，將章節以 table 形式顯示，每行三個章節
with open("index.html", "w", encoding="utf-8") as index_file:
    index_file.write("""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta property="og:image" content="https://alanjui.github.io/Piau-Im/assets/picts/king_tian.png" />
    <title>金剛般若波羅蜜經 - 目錄</title>
    <link rel="stylesheet" href="./assets/styles/styles.css">
</head>
<body>
    <!-- 頁首 -->
    <header id="header">
        <img src="./assets/picts/king_tian.png" width="300" height="200" alt="四晝五經">
        <h1>金剛般若波羅蜜經</h1>
    </header><!-- /#header -->
    <table>
""")

    # 每行顯示三個章節
    for i, chapter in enumerate(chapters):
        if i % 3 == 0:
            index_file.write("<tr>\n")
        index_file.write(f'<td><li><a href="金剛般若波羅蜜經{str(i+1).zfill(3)}.html">{chapter}</a></li></td>\n')
        if i % 3 == 2:
            index_file.write("</tr>\n")
    
    # 如果最後一行不足三個，關閉行
    if len(chapters) % 3 != 0:
        index_file.write("</tr>\n")

    index_file.write("""
    </table>
</body>
</html>
""")

print("index.html generated.")
