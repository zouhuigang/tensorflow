### 统计筛选出的唐诗，每个字出现的次数


把每条评论转换为向量, 转换原理：

	 假设lex为['woman', 'great', 'feel', 'actually', 'looking', 'latest', 'seen', 'is'] 当然实际上要大的多
 	评论'i think this movie is great' 转换为 [0,1,0,0,0,0,0,1], 把评论中出现的字在lex中标记，出现过的标记为1，其余标记为0


代码:

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
	                continue
	            content = '[' + content + ']'
	            poetrys.append(content)
	      except Exception as e:
	            pass
	
	# 按诗的字数排序
	poetrys = sorted(poetrys,key=lambda line: len(line))
	print('唐诗总数: ', len(poetrys))
	
	
	# 统计每个字出现次数
	all_words = []
	for poetry in poetrys[0:10]:
	    all_words += [word for word in poetry]
	counter = collections.Counter(all_words)
	count_pairs = sorted(counter.items(), key=lambda x: -x[1])
	words, _ = zip(*count_pairs)
	
	
	# 取前多少个常用字
	words = words[:len(words)] + (' ',)
	# 每个字映射为一个数字ID
	word_num_map = dict(zip(words, range(len(words))))
	# 把诗转换为向量形式
	to_num = lambda word: word_num_map.get(word, len(words))
	poetrys_vector = [ list(map(to_num, poetry)) for poetry in poetrys]
	print(len(poetrys_vector),poetrys_vector[0])



输出：

	唐诗总数:  34646
	34646 [1, 32, 7, 3, 29, 0, 2]



