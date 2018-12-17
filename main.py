from flask_migrate import MigrateCommand
from flask_script import Manager

# 创建应用
from info import create_app

app = create_app("pro")
# 创建管理器
mgr = Manager(app)

# 管理器生成迁移变量
mgr.add_command('mc',MigrateCommand)


@app.route('/')
def index():
    return 'hello world'

if __name__ == '__main__':
    mgr.run()
