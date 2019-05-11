# 此文件用来存放序列化器

from rest_framework import serializers  # 序列化器都存放在这里
from MySer.models import *

class StudentSerializer(serializers.Serializer):
	'''
	里面写的是每一个序列化/反序列化的字段
	跟定义模型基本一致
	'''
	# name = serializers.CharField(label='姓名', max_length=20)
	# age = serializers.IntegerField()
	# score = serializers.IntegerField()

	class Meta:
		# 告诉序列化器，对应哪个模型
		model = Student
		# fields = ['name', 'age', 'score']
		fields = '__all__'