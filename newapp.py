
import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# ボットトークンと署名シークレットを使ってアプリを初期化します
app = App(
    token="xoxb-337343413792-3624549796291-C7z6RMc0CCL7IvBpF2EoCwtY",
    signing_secret="fd28327e4df2909cfb40dc7638d4c0be"
)

@app.message("hello")
def message_hello(message, say):
    # イベントがトリガーされたチャンネルへ say() でメッセージを送信します
    say(f"Hey there <@{message['user']}>!")

# アプリを起動します
if name == "main":
    app.start(port=int(os.environ.get("PORT", 3000)))