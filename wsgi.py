#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WSGI入口文件
用于生产环境部署
"""

import os
import sys

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.dirname(__file__))

from app import app, db

# 初始化数据库
with app.app_context():
    db.create_all()

# WSGI应用对象
application = app

if __name__ == "__main__":
    application.run()