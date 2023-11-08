import json
import requests

# 設定を読み込む関数
def load_config():
    with open('secret_directory/config.json', 'r', encoding='utf-8') as config_file:
        return json.load(config_file)

# Miro APIへの付箋追加リクエストのサンプルコード
def create_sticky_note_on_miro(board_id, access_token, text, position):
    # Miro APIエンドポイント
    url = f"https://api.miro.com/v1/boards/{board_id}/widgets/"
    
    # リクエストヘッダーに認証情報を追加
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    # 付箋のデータ
    data = {
        "type": "sticker",  # 付箋のタイプを指定
        "text": text,       # 付箋のテキスト
        "x": position[0],   # 付箋のx座標
        "y": position[1],   # 付箋のy座標
        "style": {
            "backgroundColor": "#fff9b1",
            "textAlign": "center",
            "fontSize": 14
        }
    }
    
    # POSTリクエストを送信
    response = requests.post(url, json=data, headers=headers)
    
    # レスポンスを確認
    if response.status_code == 201:
        print(f"Sticky note created with content: '{text}' at position ({position[0]}, {position[1]})")
    else:
        print(f"Failed to create sticky note. Status code: {response.status_code}, Response: {response.text}")

# JSONファイルからタイトルのリストを読み込む
def read_titles_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        titles = json.load(file)
        return titles

# トークンとボードIDを設定
config = load_config()
access_token = config['access_token']
board_id = config['board_id']

# JSONファイルのパスを設定
json_file_path = config['json_file_path'] # JSONファイルのパスを適切に設定してください。

# JSONファイルからタイトルを読み込む
titles = read_titles_from_json(json_file_path)

# 付箋の初期位置とステップサイズを設定
initial_x = -1000  # 開始x座標
initial_y = -500   # 開始y座標
step_x = 150       # x軸のステップサイズ
step_y = 150       # y軸のステップサイズ
row_limit = 10     # 1行あたりの付箋数

# 抽出したタイトルをMiroに付箋として追加
for index, title in enumerate(titles):
    # 位置を計算
    x = initial_x + (index % row_limit) * step_x
    y = initial_y + (index // row_limit) * step_y
    # 付箋を作成
    create_sticky_note_on_miro(board_id, access_token, title, (x, y))
