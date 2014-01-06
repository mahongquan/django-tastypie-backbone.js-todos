# -*- coding: utf-8 -*-
from django.db import models
import datetime
import logging
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _

MAYBECHOICE = (
(0,"样品审核"),
(1,"样品分配"),
(2,"样品待检测"),
(3,"样品检测中"),
(4,"结果审核"),
(5,"检测完成"),
(6,"样品审核未通过"))
class Contact(models.Model):
    #=======销售===========
    user =  models.ForeignKey(User, related_name="wtr",verbose_name=_('wtr'))#委托人
    shenqing_date = models.DateTimeField(verbose_name=_('shenqing time'))#申请时间
    danwei = models.CharField(max_length=30,verbose_name=_('Company'))#用户单位
    sampletype=models.CharField(max_length=30,verbose_name=_('sample type'))#样品类型
    samplect=models.IntegerField(verbose_name=_('sample count'))#样品数量
    yiqi=models.CharField(max_length=30,verbose_name=_('instrument'))#仪器或技术
    fenxizhouqi=models.FloatField(verbose_name=_('analysis time'))#分析周期
    wtbz = models.CharField(max_length=100,null=True,blank=True,verbose_name=_('apply memo'))#委托备注
    #======应用中心=====
    jieshou_date = models.DateTimeField(null=True,blank=True,verbose_name=_('acceive date'))#接收时间
    contactbh = models.CharField(max_length=30,null=True,blank=True,verbose_name=_('ContactId'))#委托单编号
    state=models.IntegerField(default=0,choices=MAYBECHOICE,verbose_name=_('state'))#进度 状态
    fxy = models.ForeignKey(User,related_name="fxy",null=True,blank=True,verbose_name=_('operator'))#分析员
    gj_date= models.DateTimeField(null=True,blank=True,verbose_name=_('Estimate time'))#预计完成时间
    sj_date= models.DateTimeField(null=True,blank=True,verbose_name=_('Finish time'))#实际完成时间
    manyidu=models.CharField(max_length=30,null=True,blank=True,verbose_name=_('custom feel'))#满意度
    fxbz= models.CharField(max_length=100,null=True,blank=True,verbose_name=_('Analysis memo'))#分析备注
    fxbg= models.FileField(upload_to="upload/",null=True,blank=True,verbose_name=_('Analysis Report'))#报告
    #=======not use==============
    # dianhua = models.CharField(max_length=30,null=True,blank=True)#联系电话
    # lianxiren= models.CharField(max_length=10,null=True,blank=True) #联系人
    # zhiyangzhouqi=models.FloatField(null=True,blank=True)#制样周期
    # shifouzhiyang=models.BooleanField(default=False,blank=True)#
    contact_date = models.DateTimeField(auto_now=True,verbose_name=_('generate date'))#委托单生成日期
    def todict(self):
        m=self._meta
        fs=m.fields#get_all_field_names()
        dic={}
        for f in fs:
            if f.attname!="fxbg":
                dic[f.attname]=self.__getattribute__(f.attname)
        return dic
    def show(self):
        logging.info(self.user)# =  models.ForeignKey(User)#委托人
        logging.info(self.shenqing_date)# = models.DateTimeField()#申请时间
        logging.info(self.danwei)# = models.CharField(max_length=30)#用户单位
        logging.info(self.sampletype)#=models.CharField(max_length=30)#样品类型
        logging.info(self.samplect)#=models.IntegerField()#样品数量
        logging.info(self.yiqi)#=models.CharField(max_length=30)#仪器或技术
        logging.info(self.fenxizhouqi)#=models.FloatField()#分析周期
        logging.info(self.wtbz)# = models.CharField(max_length=100)#委托备注
        #======应用中心=====
        logging.info(self.jieshou_date)# = models.DateTimeField()#接收时间
        logging.info(self.contactbh)# = models.CharField(max_length=30,null=True)#委托单编号
        logging.info(self.state)#=models.IntegerField(default=0)#进度 状态
        logging.info(self.fxy)# =  models.IntegerField(null=True)#分析员
        logging.info(self.gj_date)#= models.DateTimeField(null=True)#预计完成时间
        logging.info(self.sj_date)#= models.DateTimeField(null=True)#实际完成时间
        logging.info(self.manyidu)#=models.CharField(max_length=30)#满意度
        logging.info(self.fxbz)#= models.CharField(max_length=100)#分析备注
    class Meta:
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')
class Ajax(models.Model):
    engine = models.CharField(max_length=30)
    browser=models.CharField(max_length=30,null=True)
    platform=models.CharField(max_length=30,null=True)
    version=models.FloatField()
    grade=models.CharField(max_length=30,null=True)
class Todo(models.Model):
    title = models.CharField(max_length=30)
    def __str__(self):
        return self.title
