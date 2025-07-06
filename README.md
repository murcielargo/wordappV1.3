# WordApp V1.3

一个基于Flask的单词学习应用，支持用户注册、单词学习、复习计划和艾宾浩斯遗忘曲线管理。

## 功能特性

- 用户注册和登录系统
- 单词学习模块（中译英、英译中）
- 艾宾浩斯遗忘曲线复习系统
- 错误单词重复练习
- 学习进度跟踪
- 打卡积分系统
- 烟花庆祝动画

## 技术栈

- **后端**: Flask, SQLAlchemy, SQLite
- **前端**: HTML, CSS, JavaScript
- **部署**: Gunicorn, Nginx

## 项目结构

```
wordappV1.3/
├── app.py              # 主应用文件
├── config.py           # 配置文件
├── wsgi.py            # WSGI入口
├── gunicorn.conf.py   # Gunicorn配置
├── init_db.py         # 数据库初始化
├── requirements.txt   # Python依赖
├── templates/         # HTML模板
├── static/           # 静态资源
└── instance/         # 数据库文件
```

## 快速开始

### 本地开发

1. 克隆项目
```bash
git clone https://github.com/murcielargo/wordappV1.3.git
cd wordappV1.3
```

2. 创建虚拟环境
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate     # Windows
```

3. 安装依赖
```bash
pip install -r requirements.txt
```

4. 初始化数据库
```bash
python init_db.py
```

5. 启动开发服务器
```bash
python app.py
```

访问 http://localhost:5000 开始使用。

### 生产部署

详细的Ubuntu系统部署指南请参考项目文档。

## 数据库模型

- **User**: 用户信息
- **Word**: 单词数据
- **UserWordProgress**: 用户学习进度
- **StudySession**: 学习会话
- **StudyHistory**: 学习历史
- **WrongWordRecord**: 错误单词记录

## API接口

- `/api/start_learning` - 开始学习
- `/api/get_next_word` - 获取下一个单词
- `/api/submit_answer` - 提交答案
- `/api/finish_learning` - 完成学习
- `/api/get_wrong_words` - 获取错误单词
- `/api/practice_wrong_word` - 练习错误单词
- `/api/complete_wrong_words_practice` - 完成错误单词练习
- `/api/get_review_words` - 获取复习单词

## 贡献

欢迎提交Issue和Pull Request来改进这个项目。

## 许可证

MIT License