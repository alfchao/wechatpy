from typing import List, Tuple

from flask import Flask, request
from wechatpy.enterprise import WeChatClient
from wechatpy.session.redisstorage import RedisStorage
from redis import Redis

app = Flask(__name__)


from api.config import Settings

settings = Settings()


def send_msg(user_ids: List[str], msg: str) -> Tuple[int, str]:
    print(settings.redis_url)
    redis_client = Redis.from_url(settings.redis_url)
    session_interface = RedisStorage(
        redis_client,
        prefix=settings.redis_prefix,
    )
    wechat_client = WeChatClient(
        settings.corp_id,
        settings.corp_secret,
        session=session_interface
    )
    wechat_client.API_BASE_URL = settings.WECHAT_API_URL
    wechat_client.message.send_text(settings.agent_id, user_ids=user_ids, content=msg)
    return 0, 'ok'


@app.route('/', methods=['GET'])
def home():
    args = request.args
    print(args)
    if args.get('sendKey') != settings.sendKey:
        return 'error'
    else:
        send_msg(args.get('user_ids').split(','), args.get('msg'))
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)
