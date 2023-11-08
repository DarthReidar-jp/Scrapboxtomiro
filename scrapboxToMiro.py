import json
import requests

# Miro APIへの付箋追加リクエストのサンプルコード
def create_sticky_note_on_miro(board_id, access_token, text):
    # Miro APIエンドポイント
    # widgetsエンドポイントにPOSTリクエストを送る必要がある
    url = f"https://api.miro.com/v1/boards/{board_id}/widgets/"
    
    # リクエストヘッダーに認証情報を追加
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    # 付箋のデータ
    # 付箋を作成するためのJSON構造をAPIの仕様に合わせる
    data = {
        "type": "sticker",  # 付箋のタイプを指定
        "text": text,       # 付箋のテキスト
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
        print(f"Sticky note created with content: '{text}'")
    else:
        print(f"Failed to create sticky note. Status code: {response.status_code}, Response: {response.text}")

# JSONファイルからタイトルのリストを読み込む
def read_titles_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        titles = json.load(file)  # ファイルからJSONデータを読み込む
        return titles  # 読み込んだデータ（ここでは文字列のリスト）をそのまま返す

# トークンとボードIDを設定
access_token =  "アクセストークンをここに"
board_id = "ボードのURLのID部分をここに"            # 実際のボードIDに置き換えてください

# JSONファイルのパスを設定
json_file_path = ''  # JSONファイルのパスを適切に設定してください。

# JSONファイルからタイトルを読み込む
titles = read_titles_from_json(json_file_path)

# 抽出したタイトルをMiroに付箋として追加（ここでは全てのタイトルを追加）
for title in titles:
    create_sticky_note_on_miro(board_id, access_token, title)

