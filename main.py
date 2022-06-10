import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# ボットトークンとソケットモードハンドラーを使ってアプリを初期化します
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

# 'hello' を含むメッセージをリッスンします
# 指定可能なリスナーのメソッド引数の一覧は以下のモジュールドキュメントを参考にしてください：
# https://slack.dev/bolt-python/api-docs/slack_bolt/kwargs_injection/args.html
@app.message("hello")
def message_hello(message, say):
    say(f"Hey there <@{message['user']}>!")

@app.message("add")
def message_hello(message, say):
    print("Welcome")
    # イベントがトリガーされたチャンネルへ say() でメッセージを送信します
    say(f"Hey there <@{message['user']}>!")

@app.command("/act")
def repeat_text(ack, respond, command):
    # command リクエストを確認
    ack()
    respond(f"{command['text']}")

# アプリを起動します
if __name__ == "__main__":
    print("Welcome")
    app.start(port=int(os.environ.get("PORT", 3000)))