from django.db import models

# Create your models here.


class UserInfo(models.Model):
    """
    员工表
    """
    name = models.CharField(verbose_name="姓名", max_length=48)
    pwd = models.CharField(verbose_name="密码", max_length=128)

    def __str__(self):
        return self.name


class MeetingList(models.Model):
    """
    会议室信息表
    """
    name = models.CharField(verbose_name="名称",max_length=128)
    address = models.CharField(verbose_name="地址", max_length=128)

    def __str__(self):
        return self.name


class Reserve(models.Model):
    """
    预定表
    """
    person = models.ForeignKey(verbose_name="预订人", to="UserInfo")
    room = models.ForeignKey(verbose_name="预定的会议室", to="MeetingList")
    reserve_date = models.DateField(verbose_name="预定的日期")
    reserve_time = models.TimeField(verbose_name="预定的时间段")
    create_time = models.DateTimeField(verbose_name="预定的时间")

    class Meta:
        unique_together = (("reserve_date", "reserve_time"),)

    def __str__(self):
        return self.person
