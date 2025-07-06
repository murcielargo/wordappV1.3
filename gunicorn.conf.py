# Gunicorn配置文件

# 绑定地址和端口
bind = "0.0.0.0:5000"

# 工作进程数量（建议为CPU核心数的2倍）
workers = 4

# 工作进程类型
worker_class = "sync"

# 每个工作进程的线程数
threads = 2

# 工作进程的最大请求数，超过后重启进程
max_requests = 1000
max_requests_jitter = 100

# 超时设置
timeout = 30
keepalive = 2

# 进程名称
proc_name = "wordapp"

# 用户和组（生产环境建议使用非root用户）
# user = "www-data"
# group = "www-data"

# 日志配置
accesslog = "logs/access.log"
errorlog = "logs/error.log"
loglevel = "info"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)s'

# 预加载应用
preload_app = True

# 进程文件
pidfile = "logs/gunicorn.pid"

# 守护进程模式（生产环境可启用）
# daemon = True

# 临时目录
tmp_upload_dir = None

# 安全设置
limit_request_line = 4094
limit_request_fields = 100
limit_request_field_size = 8190