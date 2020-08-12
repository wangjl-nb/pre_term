from django.db import models

# Create your models here.
from django.db.models import CASCADE
from django.utils import timezone


# 文档
class File(models.Model):
    title = models.CharField(max_length=64, blank=False)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)
    creator = models.CharField(max_length=64)

    class Meta:
        db_table = "file"


# 用户
class User(models.Model):
    u_username = models.CharField(max_length=32, unique=True)
    u_password = models.CharField(max_length=64)
    u_email = models.EmailField(blank=False, unique=True)
    u_icon = models.ImageField(upload_to='icons/%Y/%m/%d/')
    is_active = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)

    class Meta:
        db_table = "User"


# 删除记录时间
class delete_date(models.Model):
    file = models.ForeignKey(File, CASCADE)
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, CASCADE)

    class Meta:
        db_table = "delete_date"


# 个人文档创建记录
class Personal_record(models.Model):
    files = models.ForeignKey(File, on_delete=CASCADE)
    user = models.ForeignKey(User, on_delete=CASCADE)

    class Meta:
        db_table = "personal_record"


# 团队信息
class Team(models.Model):
    name = models.CharField(max_length=64, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)
    number_num = models.IntegerField(default=1)
    describe = models.TextField()
    icon = models.ImageField(upload_to='team_icons/%Y/%m/%d/')

    # 头像上传路径

    class Meta:
        db_table = "team"


# 团队文档创建记录
class Team_record(models.Model):
    files = models.ForeignKey(File, on_delete=CASCADE)
    team = models.ForeignKey(Team, on_delete=CASCADE)

    class Meta:
        db_table = "team_record"


# 团队文档收藏
class Team_collection(models.Model):
    team = models.ForeignKey(Team, on_delete=CASCADE)
    file = models.ForeignKey(File, on_delete=CASCADE)

    class Meta:
        db_table = "team_collection"


# 文档收藏
class Personal_collection(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    file = models.ForeignKey(File, on_delete=CASCADE)

    class Meta:
        db_table = "personal_collection"


# 团队关系列表
# 0 游客 1 普通成员 2 创建者
class Team_relation(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    team = models.ForeignKey(Team, on_delete=CASCADE)
    level = models.IntegerField(default=1)
    comment = models.BooleanField(default=False)
    change = models.BooleanField(default=False)

    class Meta:
        db_table = "team_relation"


# 模板信息
class Template(models.Model):
    title = models.CharField(max_length=64, blank=False)
    content = models.TextField()
    score = models.DecimalField(max_digits=3, decimal_places=1)
    accept_num = models.IntegerField(default=0)

    class Meta:
        db_table = "templete"


# 文档评论
class Comment(models.Model):
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    file = models.ForeignKey(File, on_delete=CASCADE)
    user = models.ForeignKey(User, on_delete=CASCADE)

    class Meta:
        db_table = 'comment'


# 文档修改日志
class File_log(models.Model):
    file = models.ForeignKey(File, on_delete=CASCADE)
    user = models.ForeignKey(User, on_delete=CASCADE)
    change_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'file_log'
