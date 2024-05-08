from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Config for the application.
    """
    redis_url: str = ''
    redis_prefix: str = ''
    corp_id: str = ''
    corp_secret: str = ''
    agent_id: str = ''
    WECHAT_API_URL: str = 'https://qyapi.weixin.qq.com/cgi-bin/'
    sendKey: str = ''
