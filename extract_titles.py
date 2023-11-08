import json

# JSONファイルを開き、データを読み込む
with open('input.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# タイトルだけを含むリストを作成する
titles = [page['title'] for page in data['pages'] if 'title' in page]

# 新しいJSONファイルにタイトルリストを書き込む
with open('titles.json', 'w', encoding='utf-8') as outfile:
    json.dump(titles, outfile, ensure_ascii=False, indent=4)

print('タイトルが titles.json ファイルに書き込まれました。')
