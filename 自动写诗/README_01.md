### 环境

	python3
	tensorflow 1.4.0


查看版本用：

	import tensorflow as tf
	print(tf.__version__)



### 读取文件

	#coding:utf-8
	import collections
	import numpy as np
	import tensorflow as tf
	import codecs
	#-------------------------------数据预处理---------------------------#
	
	poetry_file ='poetry.txt'
	
	# 诗集
	poetrys = []
	with open(poetry_file, "r", encoding='utf-8') as f:
	    #for line in f:
	    for (k,line) in enumerate(f):
	      try:
	            title, content = line.strip().split(':')
	            content = content.replace(' ','')
	            if '_' in content or '(' in content or '（' in content or '《' in content or '[' in content:
	                continue
	            if len(content) < 5 or len(content) > 79:
	                print('不符合: ', k+1,title,len(content))
	                continue
	            content = '[' + content + ']'
	            poetrys.append(content)
	      except Exception as e:
	            pass
	
	# 按诗的字数排序
	poetrys = sorted(poetrys,key=lambda line: len(line))
	print('唐诗总数: ', len(poetrys))
	print('过滤之后，得到的唐诗前10首内容为：\n', poetrys[0:10])
	
	
	import tensorflow as tf
	print(tf.__version__)



过滤掉古诗内容少于5个汉字的诗或者大于79个汉字的诗。


输出：

	不符合:  6 秋日即目 96
	不符合:  8 帝京篇十首 528
	不符合:  9 饮马长城窟行 120
	不符合:  10 执契静三边 240
	不符合:  11 正日临朝 96
	不符合:  12 幸武功庆善宫 120
	不符合:  13 重幸武功 120
	不符合:  14 经破薛举战地 120
	不符合:  15 过旧宅二首 132
	不符合:  17 入潼关 84
	.....
	不符合:  43020 酹江月 119
	不符合:  43021 水龙吟 129
	不符合:  43025 雨中花 114
	不符合:  43026 促拍满路花 104
	不符合:  43028 汉宫春 118
	唐诗总数:  34646

	过滤之后，得到的唐诗前10首内容为：
 	['[长宜子孙。]', '[李下无蹊。]', '[罗钳吉网。]', '[常杂鲍帖。]', '[扬一益二。]', '[枫落吴江冷。]', '[人生分外愁。]', '[木末上明星。]', '[犬熟护邻房。]', '[兔子上金床。]']

	1.4.0




问题汇总：

Q1:

	AttributeError: module 'tensorflow.python.ops.nn' has no attribute 'seq2seq'


A1:

	tf.nn.seq2seq.sequence_loss_by_example

	改为

	tf.contrib.legacy_seq2seq.sequence_loss_by_example