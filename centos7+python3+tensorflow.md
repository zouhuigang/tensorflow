### 发现放docker中，运行太慢了
>https://www.tensorflow.org/install/

	mkdir -p /home/tf && cd /home/tf

### 安装python3

	[root@localhost tf]# python --version
	Python 2.7.5
	
依赖：

	yum -y install gcc
	yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
	wget http://mirrors.sohu.com/python/3.5.2/Python-3.5.2.tgz
	tar xf Python-3.5.2.tgz
	cd Python-3.5.2
	./configure --prefix=/usr/local --enable-shared
	make
	make install
	ln –s /usr/local/bin/python3 /usr/bin/python3



### 安装tensorflow

	 $ pip3 install tensorflow     # Python 3.n; CPU support (no GPU support)
 	 $ pip3 install tensorflow-gpu # Python 3.n; GPU support 


卸载:

	pip3 uninstall tensorflow

下载的是：
 tensorflow-1.4.0-cp36-cp36m-manylinux1_x86_64.whl


换源：

	国内源：

	新版ubuntu要求使用https源，要注意。
	
	清华：https://pypi.tuna.tsinghua.edu.cn/simple
	
	阿里云：http://mirrors.aliyun.com/pypi/simple/
	
	中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
	
	华中理工大学：http://pypi.hustunique.com/
	
	山东理工大学：http://pypi.sdutlinux.org/ 
	
	豆瓣：http://pypi.douban.com/simple/


可以在使用pip的时候加参数-i https://pypi.tuna.tsinghua.edu.cn/simple

例如：pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyspider，这样就会从清华这边的镜像去安装pyspider库。


永久修改，一劳永逸：

Linux下，修改 ~/.pip/pip.conf (没有就创建一个文件夹及文件。文件夹要加“.”，表示是隐藏文件夹)

内容如下：

[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple

[install]
trusted-host=mirrors.aliyun.com

windows下，直接在user目录中创建一个pip目录，如：C:\Users\xx\pip，新建文件pip.ini。内容同上。





### 测试

	import tensorflow as tf
	a = tf.constant('hello world')
	sess=tf.Session()
	print(sess.run(a))


运行：

	[root@localhost tf]# python3 1.py
	2017-12-08 18:10:07.909476: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX AVX2 FMA
	b'hello world'




问题汇总:


Q1:

	python3: error while loading shared libraries: libpython3.6m.so.1.0: cannot open shared object file: No such file or directory


A1:

	find / -name 'libpython3.6m.so.1.0'

查找到的位置:

	/usr/local/lib/libpython3.6m.so.1.0
	/home/tf/Python-3.6.0a3/libpython3.6m.so.1.0

新建文件 vi  /etc/ld.so.conf.d/python3.conf,内容如下：

	/usr/local/lib/

之后运行

	ldconfig



Q2:

	RuntimeWarning: compiletime version 3.5 of module 'tensorflow.python.framework.fast_tensor_util' does not match runtime version 3.6

A2:
	将版本降回到3.5.2
	https://github.com/tensorflow/tensorflow/issues/14273

	https://github.com/lakshayg/tensorflow-build


Q3:

	Your CPU supports instructions that this TensorFlow binary was not compiled to use

A3:

	意思是可以用CPU来计算。这不是错误而是警告。再运行一下就通过了


