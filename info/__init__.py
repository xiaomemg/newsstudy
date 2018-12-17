from flask import Flask
from flask_migrate import Migrate
from flask_script import Manager
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis

from config import Config, config_dict


# 定义一个函数封装应用的创建和配置　工产函数（调用者提供生产物料，函数内部封装创建过程）
def create_app(config_type):
    app = Flask(__name__)
    # 根据配置类型取出配置类
    config_class = config_dict.get(config_type)
    #　从对象中加载数据信息
    app.config.from_object(config_class)
    # 创建数据库连接对象
    db = SQLAlchemy(app)
    # 创建redis数据库连接对象
    sr = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
    # 初始化Session存储对象
    Session(app)
    # 设置数据迁移
    mgr = Manager(app)
    Migrate(app,db)
    return app