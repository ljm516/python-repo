# effective-python

## chapter1: 编写 pythonic 代码

### Pythonic 定义

> 充分体现 python 自身特色的代码风格 

例子:

```python
>>> a = [1, 2, 3, 4]
>>> c = "abcdefg"
>>> print(a[::-1])
[4, 3, 2, 1]
>>> print(c[::-1])
gfedcba
>>> print(list(reversed(a)))
[4, 3, 2, 1]
>>>
```
翻转一个列表中的元素或者一个字符串，尽量使用 reversed() 方法。

* str.format(): python 最为推荐的字符串格式化方法。
```python
>>> print('{greet} from {language}!'.format(greet = 'hello world', language = 'python'))
hello world from python!
>>>
```

* python 的包和模块结构日益规范化，现在的库或者框架跟随一下潮流：

- 包和模块的命名采用小写、单数形式，而且短小。
- 包通常仅作为命令空间，如只包含空的 `__init__.py` 文件。

### 2. 编写 pythonic 代码

#### 经验之谈 

* 要避免劣化代码
	- 避免只用大小写来区分不同的对象。
	- 避免使用容易一起混淆的名称
		> 例如： 重复使用已经存在于上下文中的变量名来表示不同的类型；误用內建名称来表示其它含义的名称而使之在当前命名空间被屏蔽；etc... 推荐变量名与所要解决的问题域一致。看示例，示例2优于示例1：

		```python
		# 示例1
		def funA(list, num):
			for element in list:
				if num == element:
					return True
				else:
					return false

		# 示例2
		def find_num(searchList, num):
			for listValue in searchList:
				if num == listValue:
					return Ttue
				else:
					pass
		```

	- 不要害怕过长的变量名

* 深入理解 python 有助于编写 pythonic 代码
	
	- 官方手册 Language Regerence 和 Library Reference
	- 学习每个 python 新版本的新特性
	- 学习业界公认的比较 pythonic 的代码，如：flask、gevent、requests 等。

		> 代码格式化检查工具: pep8;
		> pip install -U pep8

		```
		D:\my-git-repo\python\python-learn\file-process>pep8 --first format_ad.py
		c:\program files\python36\lib\site-packages\pep8.py:2124: UserWarning:

		pep8 has been renamed to pycodestyle (GitHub issue #466)
		Use of the pep8 tool will be removed in a future release.
		Please install and use `pycodestyle` instead.

		$ pip install pycodestyle
		$ pycodestyle ...

		  '\n\n'
		format_ad.py:21:80: E501 line too long (89 > 79 characters)

		D:\my-git-repo\python\python-learn\file-process>pycodestyle format_ad.py
		format_ad.py:21:80: E501 line too long (89 > 79 characters)
		format_ad.py:43:80: E501 line too long (95 > 79 characters)

		D:\my-git-repo\python\python-learn\file-process>pycodestyle --show-source format_ad.py
		format_ad.py:21:80: E501 line too long (89 > 79 characters)
		    with codecs.open(file_path + file_name + '.txt', 'r', encoding='utf-8') as inputFile:
		                                                                               ^
		format_ad.py:43:80: E501 line too long (95 > 79 characters)
		    with codecs.open(file_path + file_name + '.json', 'w', encoding='UTF-8') as outputJsonFile:
                                                                               ^
		```                                                                           

### 3. 理解 python 与 c 的不同

- '缩进' 和 '{}'
- ' 和 "
- 三元操作符 `?:`

	```python
	x = 0
	y = 1
	print(x if x < y else y)
	```

- switch...case

	```python
	if condition:
		do something
	elif condition:
		do someting
	elif condition:
		do something
	else:
		do somethig
	```

### 4. 在代码中添加适当的注释
### 5. 通过适当添加空行是代码布局更为优雅合理
### 6. 编写函数的4个原则

* 函数设计尽量短小，嵌套层次不宜过深。
* 函数声明应该做到合理、简单、易于使用。
* 函数设计应该考虑向下兼容。
* 一个函数只做一件事，尽量保证函数语句粒度的一致性。

### 7. 将常量集中在一个文件里

**chapter1 end** 

## chapter2: 编程惯用法

### 8. 利用 assert 语句发现问题

> 主要为调试程序服务，能够快速方便的检查程序的异常或者发现不恰当的输入等，可防止意想不到的情况发生。1.5版本开始引入。

### 9. 数据交换值不推荐使用中间变量

- 示例1：
	```python
	a = 1
	b = 2
	temp = a
	a = b
	b = temp
	```
- 示例2：
	```python
	a = 1
	b = 2
	a, b = b, a
	```
推荐使用第二种形式，效率更高。

### 10. 充分利用 Lazy evalution 特性

> Lazy evaluation: 懒计算、延迟计算。指的是仅仅在需要的时候才计算表达式的值。

#### Lazy evaluation 的好处

- 避免不必要的计算，带来性能的提升。
- 节省空间，是的无限循环的数据结构成为可能。（最典型的例子：列表生成式）

### 11. 理解枚举替代实现的缺陷

### 12. 不推荐使用 type 来进行类型检查

### 13. 尽量转换为浮点类型再做除法

### 14. 警惕 eval() 的安全漏洞

### 15. 使用 enumerate() 获取序列迭代的索引和值

迭代可使用的方法：

```python
# method 1 每次循环对索引值自增
li = ['a', 'b', 'c', 'd', 'e']
index = 0
for i in li:
	print('index:', index, 'element: ', i)
	index += 1

# method 2 使用 range() 和 len()
li = ['a', 'b', 'c', 'd', 'e']
for i in range(len(li)):
	print('index:', i, 'element: ', li[i])

# method 3 使用 while, 用 len() 获取循环次数
li = ['a', 'b', 'c', 'd', 'e']
index = 0
while index < len(li):
	print('index:', index, 'element: ', li[index])
	index += 1

# method 4 使用 zip() 方法
li = ['a', 'b', 'c', 'd', 'e']
for i, e in zip(range(len(li)), li):
	print('index:', i, 'element: ', e)

# method 5 使用 enumerate() 获取序列迭代的索引和值
li = ['a', 'b', 'c', 'd', 'e']
for i, e in enumerate(li):
	print('index:', index, 'element: ', i)
	index += 1
```

这里推荐使用 method 5。代码清晰简洁，可读性最好。2.3 版本开始引入。主要为了解决在循环中获取索引以及对应值的问题。具有一定的惰性，每次仅在需要的时候才会产生一个 (index, item) 对。

该方法对字典的迭代不适用。迭代字典可使用 iteritems()

```python
info = {"name": "ljm", "age": 25, "company": "vipkid"}
for k, v in [dict].iteritems():
	print("key: ", k , "value: ", v) 
```

### 16. 分清 == 与 is 的适用场景

操作符 | 意义
---|---
is | object identity
== | equal

`is` 表示的是对象标示符，而 `==` 标示是相等。

`is` 的作用是用来检查对象的标示符是否一致，也就是比较两个对象在内存中是否拥有同一块内存空间，并不适用于判断两个字符时候相等。

`==` 检验的是两个对象的值是否相等。它实际调用内部 `__eq()__`方法, 所以说 `==` 可以被重载，而 `is` 不能被重载。

### 17. 考虑兼容性，尽可能使用  unicode

python 內建的字符串有两种类型: `str` 和 `Unicode`, 它们有共同的父类 basestring。

### 18. 构建合理的包层次来管理  module


## chapter3: 基础语法

### 19. 有节制地使用 from...import 语句

python 提供了 3 种方式来引入外部模块: `import` 语句、`from...import...` 及 `__import__` 函数。其中较为常见的为前面两种，而 `__import__` 函数与 import 语句类似，不同点在于前者显示地将模块的名称作为字符串传递并赋值给命名空间的变量。

在使用 import 的时候注意一下几点:

- 一般情况下，尽量优先使用 import a 形式，如访问 B 时需要使用 a.B 的形式。
- 有节制地使用 from a import B 形式，可以直接访问 B。
- 尽量避免使用 from a import * ，因为这会污染命名空间，并且无法清晰地表示导入了那些对象。

### 20. 优先使用 absolute import 来导入模块

### 21. i+=1 不等于 ++i

`++` 在 python 语法中是合法的，但不意味着自增。`--` 也是类似。

### 22. 使用 with 自动关闭资源

with 语句可以在代码执行完毕后还原进入该代码块时的现场。包含有 with 语句的代码块的执行过程如下:

1. 计算表达式的值，返回一个上下文管理器对象。
2. 加载上下文管理器对象的 `__exit__()` 方法以备后用。
3. 调用上下文管理器对象的 `__enter__()` 方法。
4. 如果 with 语句中设置了目标对象，则将 `__enter__()` 方法的返回值赋值给目标对象。
5. 执行 with 中的代码块。
6. 如果步骤 5 中代码征程结束，调用上下文管理器对象的 `__exit__()` 方法，其返回值直接忽略。
7. 如果步骤 5 中代码执行过程中发生异常，调用上下文管理器对象的 `__exit__()` 方法，并将异常类型、值及 traceback 信息作为参数传递给 `__exit__()` 方法。如果 `__exit__()` 返回值为 false，则异常会重新抛出；如果其返回值为 true, 异常被挂起，程序继续执行。

### 23. 使用 else 字句简化循环(异常处理)

### 24. 遵循异常处理的几点基本原则

- 注意异常的粒度，不推荐在 try 中放入过多的代码。
- 谨慎使用单独的 except 语句处理所有的异常，最好能定位具体的异常。同样也不推荐使用 except Exception 或者 except StandardError 来捕获异常。
- 注意异常捕获的顺序，在合适的层次处理异常。
- 使用更为友好的异常信息。

### 25. 避免 finally 中可能发生的陷阱

### 26. 深入理解 None，正确判断对象是否为空

python 中以下数据会当控来处理:

- 常量 None
- 常量 False
- 任何形式的数据类型零，如0、0L、0.0、0j
- 空的序列，如''、()、[]
- 空的字典{}
- 当用户定义的类中定义了 nonzero() 方法和 len() 方法，并且该方法返回整数 0 或者布尔值 False 的时候

### 27. 连接字符串应优先使用  join 而不是 + 

### 28. 格式化字符串时尽量使用  `.format` 方式而不是 `%`

### 29. 区别对待可变对象和不可变对象

### 30. []、()、和 {}: 一致的容器初始化形式

### 31. 记住函数传参既不是传值也不是传引用

### 32. 警惕默认参数潜在的问题

### 33. 慎用变长参数

python 支持可变长度的参数列表，可以通过在函数定义的时候使用 `*args` 和 `**kwargs` 这个特殊语法来实现。

1. 使用 `*args` 来实现可变参数列表：`*args` 用于接受一个包装为元组形式参数列表来传递非关键字参数，参数个数可以任意。
2. 使用 `**kwargs` 接受字典形式的关键字参数列表。其中字典的键值对分别表示不可变参数的参数名和值。
	
### 34. 深入理解 str() 和 repr() 的区别

函数 str() 和 repr() 都可以将 python 中的对象转换成字符串，使用和输入都非常相似，但又有不同之处。

```python
>>> a = 1
>>> print('str:', str(a), 'repr: ', repr(a))
str: 1 repr:  1
>>> a = 0.1
>>> print('str:', str(a), 'repr: ', repr(a))
str: 0.1 repr:  0.1
>>> a = 'abc'
>>> print('str:', str(a), 'repr: ', repr(a))
str: abc repr:  'abc'
>>> a = (1, 2, 3)
>>> print('str:', str(a), 'repr: ', repr(a))
str: (1, 2, 3) repr:  (1, 2, 3)
>>> class A:
...     pass
...
>>> a = A()
>>> print('str:', str(a), 'repr: ', repr(a))
str: <__main__.A object at 0x000001E190514E48> repr:  <__main__.A object at 0x000001E190514E48>
>>>
```

### 35. 分清 staticmethod 和 classmethod 的适用场景


































