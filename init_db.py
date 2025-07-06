from app import app, db, Word, User, UserWordProgress, StudySession, StudyHistory
from werkzeug.security import generate_password_hash
import json
import os

def init_database():
    """
    初始化数据库，创建表并导入初始数据
    """
    with app.app_context():
        # 创建所有表
        db.create_all()
        print("数据库表创建完成")
        
        # 创建测试用户
        create_test_user()
        
        # 检查是否已有单词数据
        existing_words = Word.query.count()
        if existing_words > 0:
            print(f"数据库中已有 {existing_words} 个单词，跳过导入")
            return
        
        print("数据库初始化完成，请手动导入单词数据")

def create_test_user():
    """
    创建测试用户
    """
    # 检查是否已有测试用户
    existing_user = User.query.filter_by(username='test').first()
    if existing_user:
        print("测试用户已存在")
        return
    
    # 创建测试用户
    password_hash = generate_password_hash('test123')
    test_user = User(
        username='test',
        password_hash=password_hash
    )
    
    db.session.add(test_user)
    db.session.commit()
    print("测试用户创建完成 - 用户名: test, 密码: test123")

def show_database_stats():
    """
    显示数据库统计信息
    """
    with app.app_context():
        total_words = Word.query.count()
        print(f"\n数据库统计信息:")
        print(f"总单词数: {total_words}")
        
        # 按单元统计
        unit_stats = db.session.query(
            Word.unit,
            db.func.count(Word.id)
        ).group_by(Word.unit).all()
        
        print(f"\n单元分布:")
        for unit, count in unit_stats:
            print(f"第{unit}单元: {count}个单词")

if __name__ == '__main__':
    print("开始初始化数据库...")
    init_database()
    show_database_stats()
    print("\n数据库初始化完成！")