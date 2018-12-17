# Config的基本信息配置
from datetime import timedelta

from redis import StrictRedis


class Config:
    # 开启调试模式
    DEBUG = True
    # 数据库连接地址
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/info20"
    # 设置追踪数据库变化
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # redis的ip
    REDIS_HOST = "127.0.0.1"
    # redis的端口
    REDIS_PORT = 6379
    # Session的存储类型是redis，性能好，方便设置过期时间
    SESSION_TYPE = "redis"
    # redis连接对象
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # 设置sessionid加密  如果加密, 必须设置应用秘钥
    SESSION_USE_SIGNER = True
    # 设置应用秘钥
    SECRET_KEY = "QLDEP2v5YstktI0qP8SEk3MowGCG4KCegZKhYgZq33HB9dUV0Vb7FVzg30QLf16V"
    # 设置Session过期时间，默认设置了过期时间的
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)

# 针对不同的编程环境，设置不同的子类
class developmentConfig(Config):  # 开发环境
    DEBUG = True

class productConfig(Config):  # 生产环境
    DEBUG = False

config_dict = {
    "dev": developmentConfig,
    "pro": productConfig
}