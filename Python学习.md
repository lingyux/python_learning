# Python学习

## 注释

### 单行注释

**#**

### 多行注释

**``` **

**```**

### 特殊注释

`#!/usr/bin/env python3`

`#--coding=utf-8--`

- - - - - -

## 变量

- **python**是一门强类型语言
- 赋值变量时不需要指定变量类型
- 给这个变量赋值什么数据类型，这个变量就是什么类型

### 定义

`变量名 = 数据`

```python
a = 10
a = '王子康'
print(a)
```

### 基本数据类型

#### 数字(num): 

- int(有符号整数)
- float(浮点型)
- complex(复数)
- bool(布尔值)
  - true
  - false

```python
type(变量名)	//查看变量类型
```

#### 高级数据类型

- 字符串(str)

  ```python
  b=''
  print(type(b))
  ```

- 字典(dict)

  ```python
  b={}
  print(type(b))
  ```

- 元组(Tuple)

  ```python
  a=()
  print(type(a))
  ```

- 列表(list)

  ```python
  a=[]
  print(type(a))
  ```

### 变量的命名规则

- 变量必须以字母(a - z,A - Z)或者下划线(_)开头
- 变量区分大小写
- Python关键字不能用于变量命名
- 支持中文变量名

### 基本操作运算符

#### 算数运算符

| 算数运算符 | 作用描述                                       | 示例      |
| ---------- | ---------------------------------------------- | --------- |
| +          | 算术加法                                       | a+b=10    |
| -          | 算数减法                                       | a-b=4     |
| *          | 算数乘法                                       | a*b=21    |
| **指数     | 左边的是底数，右边的是指数                     | a**b=343  |
| %          | 取余                                           | a%b=1     |
| /          | x/y结果包含小数点后面的数                      | a/b=2.333 |
| //         | x//y结果是忽略小数点后面的小数位，只保留整数位 | a//b=2    |

```python
a=7
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)
```

#### 比较运算符

| 比较运算符 | 名称     | 示例 | 结果描述                     |
| ---------- | -------- | ---- | ---------------------------- |
| ==         | 等于     | x==y | 如果x=y,结果为真             |
| !=         | 不等于   | x!=y | 如果x!=y，结果为真           |
| >          | 大于     | x>y  | 如果x大于y，结果为真         |
| <          | 小于     | x<y  | 如果x小于y，结果为真         |
| >=         | 大于等于 | x>=y | 如果x大于或者等于y，结果为真 |
| <=         | 小于等于 | x<=y | 如果x小于等于y，结果为真     |

```python
a,b=10,5
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)
print(a<b)
print(a>b)

```

#### 逻辑运算符

| 逻辑运算符 | 示例    | 结果描述                                        |
| ---------- | ------- | ----------------------------------------------- |
| and        | x and y | x,y同为真，则结果为真，如有一个为假，则结果为假 |
| or         | x or y  | x,y有一个为真，则结果为真，全部为假，则结果为假 |
| not        | not x   | 取反                                            |

```python
a,b,c,d=23,18,10,3
#and
print(a+b>c and c<d)
print(c>d and a>b)
#or
print(a+b>c or c<d)
print(a<b or c<d)
#not
print(not a>b)
```

#### 运算优先级

==() -> not -> and -> or==

#### 赋值运算符

| 赋值运算符 | 作用描述       | 结果描述                       |
| ---------- | -------------- | ------------------------------ |
| =          | 赋值运算符     | 将等号右边的值赋给等号左边的值 |
| +=         | 加法赋值运算符 | c+=a 等效于 c = c + a          |
| -=         | 减法赋值运算符 | c-=a 等效于 c = c - a          |
| *=         | 乘法赋值运算符 | c*=a 等效于 c = c * a          |
| /=         | 除法赋值运算符 | c/=a 等效于 c = c / a          |
| %=         | 取模赋值运算符 | c%=a 等效于 c = c % a          |
| **=        | 幂赋值运算符   | c ** =a 等效于 c = c ** a      |
| //=        | 取整赋值运算符 | c // = a 等效于 c = c // a     |

```python
a,b,c,d=23,18,10,3
a+=c
print(a)	#目前python中不能直接打印复杂表达式
```

### Python的输入与输出

#### 输出

==**%**==占位符**%**后面跟的是变量的类型

==**%s**字符占位符，**%d**数字占位符**\n**换行==

| 格式符号 |            转换             |
| :------: | :-------------------------: |
|    %c    |         字符(char)          |
|    %s    | 通过str()字符串转换来格式化 |
|    %i    |      有符号十进制整数       |
|    %d    |      有符号十进制整数       |
|    %u    |      无符号十进制整数       |
|    %o    |         八进制整数          |
|    %x    |        十六进制整数         |
|    %e    |       索引符号(小写e)       |
|    %E    |       索引符号(大写E)       |
|    %f    |          浮点实数           |
|    %g    |        %f和%e的简写         |
|    %G    |        %f和%E的简写         |



```python
#name='谢尔顿'
#classPro='普林斯顿'
#print('我的名字是：%s，来自[%s]'%(name,classPro))

name = '老夫子'
QQ = 66666666
PhoneNumber = 1214451351
address = '广州市'
print('===============================')
print('姓名:%s\nQQ:%d\n手机号：%d\n公司地址%s'%(name,QQ,PhoneNumber,address))
print('===============================')
```

格式化输出采用**.format()**，不需要指定数据类型

```python
name = '老夫子'
QQ = 66666666
PhoneNumber = 1214451351
address = '广州市'
print('姓名：{}，年龄为:{}'.format(name,23))
print('QQ：{}'.format(QQ))
print('手机号：{}'.format(PhoneNumber))
print('公司地址：{}'.format(address))
```

#### 输入

Python提供了**input**方法获取键盘输入

`a = input('请输入你的名字')`

==input接受的键盘输入结果都是**str**类型的，如果接受数字类型需要将**str**转成**int**==

`age=int(input('请输入你的年龄：'))`

```python
name = input('请输入你的名字：')
QQ = input('请输入你的qq：')
PhoneNumber = input('请输入你的手机：')
address = input('请输入你的地址：')
print('姓名：{}，年龄为:{}'.format(name,23))
print('QQ：{}'.format(QQ))
print('手机号：{}'.format(PhoneNumber))
print('公司地址：{}'.format(address))
```

- - - - - -

## 程序控制语句

### 条件表达式

**比较运算符/逻辑运算符/复合运算符**

### 条件判断语句

#### 单分支语句

##### 语法格式

```python
if 条件表达式:
	code
    code
    code
    ...
```

```python
score1=61
if score1>60:#满足条件执行，否则跳过
	print('及格')
	pass #空语句填补程序所用
print('语句运行结束')
```



#### 双分支语句

##### 语法格式

```python
if 条件表达式:
    code
    code
    code
    ...
else:
    code
    code
    code
    ...
	
```

```python
score=59
if score>=60:
	print('成绩不错')
	pass
else:
	print('成绩不是很理想')
	pass
print('语句运行结束')
```



#### 多分支语句

##### 语法格式

```python
if 条件表达式:
    code
    code
    code
    ...
elif 条件表达式:
    code
    code
    code
    ...
......
else:
    code
    code
    code
    ...
```

```python
#多条件判断
score=70
if score<60:
	print('不及格')
	pass
elif score>=60 and score<70:
	print('及格')
	pass
elif score>=70 and score<80:
	print('中')
	pass
elif score>=80 and score<90:
	print('良')
	pass
else:
	print('优')
	pass
print('语句执行结束')
```

```python
# 0:石头 1：剪刀 2：布
import random
person=int(input('请出拳:0:石头 1：剪刀 2：布\n'))
computer=random.randint(0,2)
print('电脑出的是：%d\n'%computer)
if person>2:
    print('无效数据')
    pass
elif person==0 and computer==0:
    print('平手')
    pass
elif person==0 and computer==1:
    print('你赢了')
    pass
elif person==0 and computer==2:
    print('你输了')
    pass
elif person==1 and computer==0:
    print('你输了')
    pass
elif person==1 and computer==1:
    print('平手')
    pass
elif person==1 and computer==2:
    print('你赢了')
    pass
elif person==2 and computer==0:
    print('你赢了')
    pass
elif person==2 and computer==1:
    print('你输了')
    pass
elif person==2 and compter==2:
    print('平手')
    pass
```

#### 嵌套if

```python
score = int(input('请输入您的学分'))
if score > 10:
    grade = int(input('请输入您的成绩'))
    if grade > 80:
        print('恭喜您，你可以升级了')
        pass
    else:
        print('你还需要努力')
        pass
else:
    print('您的成绩也太差了')

```



### 循环控制语句

#### while

##### 语法格式

1. 必须有一个初始值

2. 条件表达式

3. 变量【循环体内的技术变量】的自增或者自减，否则会造成死

   循环

```python
while 条件表达式:
    code
    code
    code
    ...
```

##### 使用场景

循环的次数不确定，是依靠循环条件来结束

##### 实例

```python
# 0:石头SublimeCodeIntel 1：剪刀 2：布
import random
count = 1
while count < 10:
    person = int(input('请出拳:0:石头 1：剪刀 2：布\n'))
    computer = random.randint(0, 2)
    computer1 = '拳头'
    if computer == 0:
        computer1 = '拳头'
        pass
    elif computer == 1:
        computer1 = '剪刀'
        pass
    elif computer == 2:
        computer1 = '布'
        pass
    print('电脑出的是：%s\n' % computer1)
    if person > 2:
        print('无效数据')
        pass
    elif person == 0 and computer == 0:
        print('平手')
        pass
    elif person == 0 and computer == 1:
        print('你赢了')
        pass
    elif person == 0 and computer == 2:
        print('你输了')
        pass
    elif person == 1 and computer == 0:
        print('你输了')
        pass
    elif person == 1 and computer == 1:
        print('平手')
        pass
    elif person == 1 and computer == 2:
        print('你赢了')
        pass
    elif person == 2 and computer == 0:
        print('你赢了')
        pass
    elif person == 2 and computer == 1:
        print('你输了')
        pass
    elif person == 2 and computer == 2:
        print('平手')
        pass
    count += 1

```

```python
#99乘法表
row = 1
while row < 9:
    col = 1
    while col <= row:
        print("%d * %d = %d" % (row, col, row*col), end=" ")
        col += 1
        pass
    row += 1
    print()
    pass

```

```python
#打印直角三角形
row = 1
while row <= 7:
    j = 1
    while j <= row:
        print('*', end=' ')
        j += 1
        pass
    print()
    row += 1
    pass
```



#### for

##### 语法格式

```python
for ... in 可迭代集合对象:
    code
    code
    code
    ......
```

##### 语法特点

遍历操作，一次的取集合容器中的每个值

##### 实例

```python
tags = '我是一个中国人'  # 字符串类型本身就是一个字符类型的集合
for item in tags:
    print(item, end='')
    pass

```

==**range**可以生成一个数据集合列表==

`range(起始,结束,步长)`步长不能为0

`range(1,100,2)`

```python
for data in range(1, 100, 2):#左开右闭区间
    print(data, end=' ')
    pass
sum = 0
for data in range(1, 100, 2):
    print(data, end=' ')
    pass
print()
for data in range(1, 101):
    sum += data
    pass
print('sum = {}'.format(sum))

```

#### break && continue

##### break

代表中断结束，满足条件直接跳出本层循环

##### continue

终止本次循环，继续接下的循环

==这两个关键字只能用在循环语句中==

```python
sum = 0
for data in range(1, 50):
    if sum > 100:
        break
        pass
    else:
        sum += data
        pass
print(sum, data)

for item in range(1, 101):
    if item % 2 == 1:
        continue
        pass
    else:
        print(item, end=' ')
        pass

for data in range(1, 100):
    if data == 50:
        break
        pass
    elif data % 2 == 0:
        continue
        pass
    else:
        print(data, end=' ')
```

#### for -- else && while -- else

```python
account = 'admin'
pwd = 'admin'

for i in range(3):
    zh = input('请输入您的账号：')
    pd = input('请输入您的密码：')
    if account == zh and pwd == pd:
        print('恭喜你登陆成功！')
        break
        pass
    else:
        print('您输入的账号或密码错误，请重新输入：')
    pass
else:
    print('您的账号已经被锁定！')
```

-------

## 高级数据类型

### 序列

#### 序列类型

在python中，序列就是一组按照顺序排列的值[数据集合]

- 字符串
- 列表
- 元组

#### 优点

可以支持索引和切片的操作

#### 特征

第一个正索引为0，指向的是左端，第一个索引为负数的时候，指向的是右端

### 字符串



#### 字符串的常用函数

|           函数名            |                             作用                             |
| :-------------------------: | :----------------------------------------------------------: |
|        capitalize()         |                         首字母变大写                         |
|    endswith/startswith()    |                       是否 x结束/开始                        |
|           find()            | 检查x是否在字符串中<br />`查找第一个目标对象在序列对象中的位置,如果没有找到返回-1` |
|          isalnum()          |                     判断是否是字母和数字                     |
|          isalpha()          |                        判断是否是字母                        |
|          isdigit()          |                        判断是否是数字                        |
|          islower()          |                        判断是否为小写                        |
|           join()            |                   循环取出所有值用xx去连接                   |
|        lower/upper()        |                          大小写转换                          |
|          swapcase           |                    大写变小写，小写变大写                    |
|     lstrip/rstrip/strip     |                      移除左/右/两侧空白                      |
|           split()           |                          切割字符串                          |
|           title()           |                  把每个单词的首字母变成大写                  |
| replace(old,new,count=None) | old为被替换的字符串<br />new为替换的字符串<br />count替换多少个<br />无count表示全部替换 |
|           count()           |                        统计出现的次数                        |
|           index()           |       返回的为目标对象的下标值，检测不到报错，产生异常       |

**id()的作用是查看对象的内存地址**

#### 切片操作

##### 定义

切片指的是根据下标截取字符串中的部分内容。

##### 语法

`[起始下标:结束下标:步长]`

切片截取的内容不包含结束下标对应的数据，步长指的是隔几个下标取数据，默认为1

#### 与其他类型综合操作

#### 代码

```python
Test = 'python'
# print(type(Test))
# for item in Test:
#     print(item, end='')
print('首字母变大写 %s' % Test.capitalize())
a = '     hello     '
b = a.strip()
print(a, '\n', b)
print(a.lstrip())
print(a.rstrip())
print('a的地址为%d' % id(a))  # id()的作用是查看对象的内存地址
print(a.find('l'))  # 查找第一个目标对象在序列对象中的位置,如果没有找到返回-1
print(a.index('lo'))  # 返回的为目标对象的下标值，检测不到报错，产生异常
print(a.startswith(' '))
print(a.endswith(' '))
print(a.upper())

# 排序
print(Test[::-1])

```



### 列表(list)

#### 定义

列表是一种有序的数据集合

#### 特点

1. 支持随意的增删改查
2. 列表内的数据是可以变化的[数据项可一变化，内存地址不会改变]
3. 用[]来表示列表类型，数据项之间用**,**分割。列表中的数据项可以是任意类型的数据
4. 支持索引和切片来进行操作

| 方法名  |                 作用                 |
| :-----: | :----------------------------------: |
|  index  |         获取指定的元素索引号         |
| insert  |         在指定的位置插入数据         |
|   pop   |           删除最后一个元素           |
| remove  |       移除左边找到的第一个元素       |
| reverse |               反转列表               |
|  sort   | 列表排序<br />==reverse=True==为倒叙 |

==len==：返回字符串、列表的长度

```python
li = [1, 2, 3, '你好']
print(len(li))

print(type(li))
listA = ['abcd', 785, 12.23, '取值', True]

print(listA)  # 输出整个列表
print(listA[0])  # 输出第一个元素
print(listA[1:3])  # 输出第二项到第三项元素
print(listA[2:])  # 输出从第三项至最后一项元素
print(listA[::-1])  # 负数表示倒叙输出
print(listA*2)  # 输出多次次列表
print('----------常用的函数----------')
print('追加之前的数据', listA)
listA.append(['fff', 'ddd'])  # 追加的列表
listA.append(8888)
print('追加之后的数据', listA)
listA.insert(1, '这是我插入的字符串')  # 指定位置插入数据
print(listA)
rsData = list(range(10))  # 强制转换成list对象
print(type(rsData))
listA.extend(rsData)  # 批量变价，扩展
listA.extend([11, 22, 33, 44])
print(listA)
print('----------修改list----------')
print('修改之前之前的数据', listA)
listA[0] = 'lingyux'

print('修改之后', listA)
listB = list(range(10, 50))
print('----------删除操作----------')
print(listB)
# del listB[0]  # 删除列表中的元素

del listB[1:3]  # 通过切片批量删除多个数据

listB.remove(20)  # 移除指定的元素具体的数据值
listB.pop(0)  # 可以移除指定项 参数为索引值
print(listB)

print(listB.index(19))  # 返回的是索引下标

```



### 元组

#### 定义

是一种不可变的序列，在创建之后不能做任何的修改

#### 特点

1. 不可变
2. 用**()**创建元组类型，数据项用==**,**==分割，可以是任意类型
3. 当元组中只有一个元素时，要加上==**,**==，不然解释器会当做整形处理
4. 支持切片操作

==元组中的列表可以被修改==

```python
tupleA = ()  # 空元组
print(id(tupleA))
tupleA = ('abcd', 12, 9.12, 'lingyux', [11, 22, 33])
print(id(tupleA))
print(tupleA)
print(type(tupleA))
# 元组的查询
for item in tupleA:
    print(item, end=' ')
    pass
    print()
print(tupleA[2:4])

print(tupleA[::-1])
print(tupleA[::-2])  # 表示反转字符串每隔两个取一次
print(tupleA[-2:-1:])
tupleA[4][1] = 1231232
print(tupleA)
tupleC = (1, 2, 3, 1, 12, 32)
print(tupleC.count(1))  # 可以统计元素出现的次数

```



### 字典

#### 定义

字典是Python之中重要的数据类型，可以存储任意对象。字典是以键值对的形式创建的`{'key':value}`利用大括号包裹着的

字典中查找某个元素的时候，是根据键、值字典的每个元素由2部分组成，键：值

访问值的安全方式**get**方法，在我们不确定字典是否存在某个键而又想获取其值时，可以使用**get**方法，害了一设置默认值

#### 注意点

1. 字典的键(key)不能重复，值(value)可以重复。
2. 字典的键(key)只能是不可变的类型，如数字，字符串，元组等

#### 字典常用的方法

| 方法名     | 关键字 | 用途                                                         |
| ---------- | :----- | :----------------------------------------------------------- |
| 修改元素   | 、、   | 字典中的值是可以修改的，通过键找到对应的值践行修改           |
| 新增元素   | 、、   | 如果使用`变量名['键']=数据`时，如果这个键在字典中不存在，那么就会新增一个元素 |
| 删除元素   | del    | 删除指定元素**clear**清空字典                                |
| 统计个数   | len()  | 查看字典中有几个键值对                                       |
| 获取键     | keys   | 返回包含字典中所有key值的dict keys对象，用for循环可以去除每隔key值 |
| 获取值     | values | 返回一个包含所有值(value)的dict values对象                   |
| 获取键值对 | 、、   | 返回一个包含所有(key、value)元组的列表dict items对象         |
| 删除指定键 | pop()  | 删除指定的键                                                 |

#### 特点

1. 不是一个序列类型，没有下标的概念，是一个无序的 键值集合，是python内置的高级数据类型
2. 用{}来表示字典对象，每个键值用逗号分割
3. 键必须是不可变的类型[元组、字符串]，值可以是任意类型
4. 每个键必定是唯一的，如果存在重复的键，后者会覆盖前者

```python
dictA = {"pro": '电子信息', "school": '南京工业大学'}  # 空字典
# 添加字典数据
dictA['name'] = 'lingyux'  # name 代表key
dictA['age'] = '30'
dictA['pos'] = '小说家'
print(dictA)  # 输出完整的字典
print(len(dictA))  # 字典长度
print(type(dictA))

print(dictA['name'])  # 通过键获取对应的值
dictA['name'] = 'lingyuxia'  # 修改键对应的值

dictA.update({'pro': '计算机'})
dictA.update({'height': '180'})  # 可以添加或修改
print(dictA['name'])
# 获取所有的键
print(dictA.keys())
# 获取所有的值
print(dictA.values())
# 获取所有的键值对
print(dictA.items())

for key, value in dictA.items():
    print('%s==%s' % (key, value))

# 删除操作
del dictA['name']  # 通过指点键进行删除
dictA.pop('age')
print(dictA)
# 排序 按照key排序
print(sorted(dictA.items(), key=lambda d: d[0]))
# 按照 value 排序
print(sorted(dictA.items(), key=lambda d: d[1]))

```

### 通用操作

| 操作名称         | 关键字 | 用途                           | 适用对象                 |
| ---------------- | :----: | ------------------------------ | ------------------------ |
| 合并操作         |   +    | 两个对象相加操作会合并两个对象 | 字符串、列表、元组       |
| 复制             |   *    | 对象自身按指定次数进行 + 操作  | 字符串、列表、数组       |
| 判断元素是否存在 |   in   | 判断指定元素是否存在于对象中   | 字符串、列表、元组、字典 |

------

## Python函数基础

### 函数基础

#### 概念

函数就是一系列Python语句的组合，可以在程序中一次或多次的运行的，具有一定功能的代码块。

为了代码复用的最大化以及最小化冗余代码，整体代码结构清晰，问题局部化

#### 函数定义

`def + 关键字 + 小括号 + 冒号 + 换行缩进 + 代码块`

```python
def 函数名():
    代码块
```

#### 函数的调用

`函数名 + ()`即可使用该函数 

在调用函数之前必须先行定义

### 函数参数

```python
def printInfo(name, height, weight, hobby, pro):
    print('%s的身高是%.2fcm' % (name, height))
    print('%s的体重是%.2fkg' % (name, weight))
    print('%s的爱好是%s' % (name, hobby))
    print('%s的专业是%s' % (name, pro))
    pass


printInfo('lingyux', 190, 200, 'game', 'computer')

```

#### 参数的分类

##### 必选参数

```python
def sum(a, b):  # 形式参数：形参只是意义上的一种参数，在定义的时候是不占用内存空间的
    sum = a+b
    print(sum)
    pass


# 函数的调用 在调用的时候是必须要赋值的
sum(20, 15)  # 20和15就是实际参数，简称实参 占用内存地址
sum(20.5, 30)

```



##### 默认参数(缺省参数)

```python
def sum1(a=20, b=30):  # 始终存在于参数列表的尾部
    print('默认参数的使用=%.1f' % (a+b))
    pass


# 默认参数的调用
sum1()
sum1(10)
sum1(20.5, 20.6)
```



##### 可变参数

当参数的个数不确定的时候使用，比较灵活

```python
def get_computer(*args):
    '''
    可变长的参数类型
    计算累加和
    '''
    # print(args)
    result = 0
    for item in args:
        result += item
    pass
    print('result=%d' % result)


get_computer(1, 2)
get_computer(1, 2, 3, 4, 5, 6)
```



##### 关键字参数

用**来定义 

在函数体内 参数关键字是一个字典类型 key是一个字符串

==可选参数必须放在关键字可选参数之前==

```python
def keyFunc(**kwargs):
    print(kwargs)
    pass


# 调用
dictA = {'name': 'Leo', 'age': 22}
keyFunc(**dictA)
keyFunc(name='peter', age=22)


def complex_func(*args, **kwargs):
    print(args)
    print(kwargs)
    pass


complex_func(1, 2, 3, 4, name='lingyux')
```

### 函数的返回值

#### 定义

函数执行完成以后会返回一个对象，如果在函数内部有**return**就可以返回实际的值，否则就会返回空。

可以返回任意的类型

#### 用途

给调用方返回数据

在一个函数体内，可以出现多个**return**关键字，但是只能返回一个**return**

如果在一个函数体内执行一个**return**，就意味着函数执行完成退出，**return**后面的代码不会被执行

#### 实例

```python
def sum(a, b):
    sum = a+b
    return sum  # 将计算结果返回
    pass


result = sum(10.6, 30)  # 将返回值赋给其他的变量
print(result)
print(sum(10, 30))  # 函数的返回值返回到调用的地方


def caluate_computer(num):
    li = []
    result = 0
    i = 1
    while i <= num:
        result += i
        i += 1
        pass
    li.append(result)
    return li
    pass


value = caluate_computer(10)
print(value)
print(type(value))


def returnTuple():
    # return 1, 2, 3
    return {'name': 'lingyux', 'age': 10}
    pass


a = returnTuple()
print(type(a))

```

### 函数嵌套调用

```python
def fun1():
    print('---------------fun1 start---------------')
    print('---------------执行代码省略---------------')
    print('---------------fun1 end---------------')
    pass


def fun2():
    print('---------------fun2 start---------------')
    fun1()
    print('---------------fun2 end---------------')
    pass


fun2()  # 调用函数2

```

### 函数的基本类型

- 无参数无返回值的
- 无参数有返回值的
- 有参数无返回值的
- 有参数有返回值的

### 局部变量和全局变量

```python
pro = '计算机信息管理'


def printInfo():
    name = 'lingyux'
    print('{} {}'.format(name, pro))
    pass


def TestMethod():
    name = 'lingyuxia'
    print(name)
    print(pro)
    pass


printInfo()
TestMethod()


def changeGlobal():
    '''
    修改全局变量
    '''
    global pro  # 修改全局变量，如果函数内部没有global关键字，则修改的内容被视为局部变量
    pro = '市场营销'
    print(pro)
    pass


changeGlobal()
print(pro)

```



#### 局部变量

##### 定义和作用域

在函数内部定义的变量，作用域仅仅局限于函数内部

不同的函数可以定义相同的局部变量，但是是各自用各自的不会相互影响

##### 作用

为了临时的保存数据，需要在函数中定义来进行存储

#### 全局变量

##### 定义

在全局使用的变量，作用域在全部的代码中

##### 特点

当全局变量和局部变量冲突时，函数会优先读取局部变量的值

### 引用

1. 在**python**当中，万物皆是对象，在函数调用的时候，实参传递的就是对象的引用
2. 了解了原理之后就可以更好的取把控在函数内部的处理是否会影响到函数外部的数据变化
3. 参数传递是通过对象引用完成的

```python
a = 1  # 不可变的类型

# 传递的是对对象的引用


def func(x):
    print('x的地址为{}'.format(id(x)))
    x = 2
    print('x修改后的地址为{}'.format(id(x)))
    pass


print('a的地址为{}'.format(id(a)))
func(a)


# 可变类型
li = []


def testindex(parms):
    print(id(parms))
    li.append([1, 2, 3, 4, 5, 6])
    print(id(parms))
    print('内部的变量对象{}'.format(parms))
    pass


print(id(li))
testindex(li)
print('外部的变量对象{}'.format(li))

```

### 匿名函数

#### 定义

**python**中使用**lambda**关键字创建匿名函数，所谓的匿名即这个函数没有名字不用**def**关键字创建标准的函数

#### 语法规则

`lambda 参数1,参数2,参数3:执行表达式`

#### 特点

匿名函数冒号后面的表达式有且只有一个，注意：是表达式，而不是语句

匿名函数自带**return**，返回的内容就是计算后的结果

#### 实例

```python
test = lambda x,y:x+y
test(1,3)
test(4,5)
```

#### 缺点

**lambda**只能是单个表达式，不是一个代码块，**lambda**的设计产区吃为了满足简单的函数使用

仅能实现简单的逻辑，复杂逻辑使用不了

### 递归函数

#### 定义

如果一个函数在内部不调用其他的函数，而是调用自己本身，这个函数就是递归函数。

#### 条件

递归函数必须有一个结束条件，否则递归无法结束会已知递归执行下去，直到到达最大递归深度时报错

#### 优点

逻辑简单、定义简单

#### 缺点

容易导致栈溢出M内存资源紧张，甚至内存泄露

很难调试

#### 实例

```python
# 求皆乘

def jicheng(n):
    result = 1
    for item in range(1, n+1):
        result *= item
        pass
    return result
    pass


print('5的阶乘为{}'.format(jicheng(5)))


# 递归方式实现
def diguiJc(n):
    '''
    递归方式实现阶乘函数
    '''
    if n == 1:
        return 1
    else:
        return n*diguiJc(n-1)
    pass

# 递归调用


print('递归调用阶乘{}'.format(diguiJc(5)))

```

#### 案例

```python
# 递归案例：模拟实现树形结构的遍历
import os  # 引用文件操作模块


def find_file(file_path):
    listRs = os.listdir(file_path)  # 得到该路径下所有的文件夹
    for fileItem in listRs:
        full_path = os.path.join(file_path, fileItem)  # 获取完整的文件路径
        if os.path.isdir(full_path):  # 判断是否是文件夹
            find_file(full_path)  # 如果是文件夹 再次递归
        else:
            print(fileItem)
            pass
        pass
    else:
        return
    pass


# 调用搜索文件夹对象
find_file('D:\\00学习课件')

```

------

## Python内置函数

### 数学运算

```python
# # print(abs(-90))
# # a = max([12, 323423, 123123123, 533452, 123123, 2132])
# # print(a)
# a, b, c = 1, 2, 3
# print('动态执行的函数={}'.format(eval('a*b+c-30')))


# def test_fun():
#     print('我执行了吗')
#     pass


# eval('test_fun()')


dic = dict(name='lingyu', age=18)  # 创建一个字典
print(type(dic))
# dict['name'] = '小明'
# dict['age'] = 18
print(dic)


print(bytes('我喜欢Python', encoding='utf-8'))

```



### 序列操作

```python
# 序列操作：str,元组，列表
print(all([]))
print(all([1, 2, 3, False]))


print(any((0, False, 1)))


# sort && sorted
li = [2, 3, 12, 1, 32, 10]
# li.sort()  # list自带的排序方法直接修改的是也是对象
print('排序之前{}'.format(li))
# sort只能用于列表排序
li0 = sorted(li, reverse=True)  # 默认为False 升序排列
print(li0)

tupArray = (1, 32, 23, 55, 22, 10)
tupArray01 = sorted(tupArray)
print(tupArray01)


# reverse反转排序

# range 创建一个整数列表

```

#### zip()

##### 作用

将对象中对应的元素打包成一个个元组，返回由这些元组组成的列表

如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用*****作为操作符，可以将元组解压为列表

##### 语法

`zip(iterable,....)`

iterable -- 一个或多个迭代器

```python
# zip() 就是用来打包的 会把序列中索引对应的元素存储为一个元祖对象
s1 = ['a', 'b', 'c']
s2 = ['你', '我', '他']
print(zip(s1))
print(list(zip(s1)))  # 压缩一个数据

ziplist = zip(s1, s2)
print(list(ziplist))

```

##### 实例

```python
# zip() 就是用来打包的 会把序列中索引对应的元素存储为一个元祖对象
s1 = ['a', 'b', 'c']
s2 = ['你', '我', '他']
print(zip(s1))
print(list(zip(s1)))  # 压缩一个数据

ziplist = zip(s1, s2)
print(list(ziplist))


def printBookInfo():
    books = []  # 存储所有的图书信息
    bookid = input('请输入图书的编号：每个以空格分隔')
    bookName = input('请输入图书的书名：每个以空格分隔')
    bookPos = input('请输入图书的位置：每个以空格分隔')
    idlist = bookid.split(' ')
    namelist = bookName.split(' ')
    poslist = bookPos.split(' ')

    bookInfo = zip(idlist, namelist, poslist)
    for bookItem in bookInfo:
        '''
        遍历图书信息进行存储
        '''
        dictInfo = {'编号': bookItem[0], '书名': bookItem[1], '位置': bookItem[2]}
        books.append(dictInfo)
        pass
    for item in books:
        print(item)
        pass
    pass


printBookInfo()

```

#### enumerate()

##### 语法：

`enumerate(sequence,[start=0])`

**sequence**：一个序列、迭代器或是其他支持迭代的对象

**start**：下标起始位置

**返回值**：返回**enumerate()**(枚举)对象

##### 实例

```python
listObj = ['1', 'b', 'c']
for index, item in enumerate(listObj, 5):
    print(index, item)
    pass

dicObj = {}
dicObj['name'] = 'lingyux'
dicObj['hobby'] = 'sing'
dicObj['pro'] = 'art'

for index, item in enumerate(dicObj):
    print(index, item, end=' ')
    print(dicObj[item])
listObj = ['1', 'b', 'c']
for index, item in enumerate(listObj, 5):
    print(index, item)
    pass
```

### 集合操作

#### 集合的定义

**set**是**python**中的一种数据类型，是一个无序不重复的元素集合

#### 集合的创建

- 方法1

`set1 = {"1","2"}`

- 方法2

`list1 = ['1','2','3','4']`

`set2 = set(list1)`

#### 集合的操作函数

**add() clear() difference() intersection() union() pop() discard() update()**

#### 实例

```python
# set 不支持索引和切片，是一个无序的且不重复的容器
# 类似于字典，但是没有value 只有key
dic1 = {1: 3}
set1 = {1, 2, 3}
# print(type(set1))
# print(type(dic1))
# 集合添加
set1.add('python')
print(set1)
# 集合清空
set1.clear()
print(set1)

a = {12, 32, 23}
b = {12, 32, 44, 23}
# 差
print(b.difference(a))
print(b-a)
# 交集
print(a.intersection(b))
print(a & b)
# 并集
print(a.union(b))
print(a | b)
# 随机移除数据 pop没有参数
deldata = b.pop()
print(b)
print(deldata)
# 直接指定移除数据
print(a.discard(12))

print(a.update(b))

```

### 作业

#### 求三组连续的自然数的和：1-10 20-30 35-45

```python
def sumRange(m, n):
    '''
    求从m到n的连续自然数的总和
    '''
    return sum(range(m, n+1))
    pass


print(sumRange(1, 10))
print(sumRange(20, 30))
print(sumRange(35, 45))
```



#### 100个和尚吃100个馒头，大和尚一个人吃3个馒头，小和尚三个人吃1个馒头，问大和尚小和尚各有多少人

```python
def person_sount():
    '''
    计算有多少个和尚
    假设大和尚有a个，小和尚有100-n个
    '''
    for a in range(1, 100):
        if(a*3+(100-a)/3) == 100:
            # 100个和尚吃100个馒头
            return (a, 100-a)
        pass
    pass


rsObj = person_sount()
print('大和尚有{}个人，小和尚有{}个人'.format(rsObj[0], rsObj[1]))

```



#### 指定一个列表，列表中含有唯一一个只出现过一次的数字。写程序找出这个数字

```python
li = [1, 3, 4, 3, 3, 5, 2, 4, 2, 1, 7, 5]
set1 = set(li)
print(set1)
for i in set1:
    li.remove(i)
    pass
set2 = set(li)  # set2中存储的数据就是li中有重复的数据集合
print(set1-set2)
for i in set1:
    if i not in set2:
        print(i)
        pass
    pass
```

------

## 面向对象基础

### 面向对象介绍

- 面向过程：根据业务逻辑从上到下编写代码
  - 从计算机角度，面向过程不适合做大项目
- 函数式：将某些功能代码封装到函数中，日后无需再次编写，进调用函数即可
- 将数据和函数绑定到一起，进行封装，这样能够更快的开发程序，减少了重复代码的重写过程

### 类和对象的概念

#### 类

##### 定义

类就是一个模板，模板里可以包含多个函数，函数可以实现一些功能

类是具有相同相似属性[特征]和行为[方法]的一系列对象的集合

##### 组成部分

- 类的名称：类名
- 类的属性：一组数据(特征)
- 类的方法：允许对进行操作的方法(行为)

#### 对象

##### 定义

对象就是根据模板创建的实例，通过实例对象可以执行类中的函数

##### 类和对象的关系

类是对象的抽象化，对象是类的一个实例

### 定义类和对象

#### 定义类

##### 格式

```python
class Foo(object):
    方法列表
```

#### 定义对象

##### 格式

```python
对象名 = 类名()
```

#### 实例

```python
class Person:
    # 属性
    name = 'lingyux'
    age = 22
    # 方法

    def eat(self):
        print('大口吃饭')
        pass

    def run(self):
        print('飞速的跑')
        pass


# 创建对象[类的实例化]
xm = Person()
xm.eat()  # 调用函数
xm.run()
print('{}的年龄是{}'.format(xm.name, xm.age))

```

### 实例方法和属性

#### 实例方法

##### 定义

在==类的内部==，使用**def**关键字可以定义一个实例方法，与一般的函数定义不同，第一个参数默认为==**self**==，名字标识可以是其他的名字，但是这个位置必须被占用

实例方法归于 类的实例所有

```python
class Animal(object):
    
    #实例方法
    def test(self):
        print('我是实例方法')
        pass
    
```

#### 属性

##### 定义

定义在类的内部，方法外面的属性称之为类属性，所有实例的共有属性

定义在方法里面使用**self**引用的属性称之为实例属性，归属于一个实例

```python
class Animal(object):
    color='white' #类属性
    
    def __init__(self):
        self.name='Puppy' #实例属性
        pass
    #实例方法
    def test(self):
        print('我是实例方法')
        pass
    def show(self):
        print('Animal show')
        pass
```



### _ init _方法

#### 特点

- Python自带的内置函数，具有特殊的作用，两边使用**__**包裹起来(**magic**)
- 是一个初始化的方法，用来定义实例属性，和初始化数据的，在创建对象的时候自动调用，不用手动调用
- 可以利用参数传递的机制让我们的定义功能更加的强大，方便

#### 实例

```python
class Animal(object):
    def __init__(self):
        self.name = 'Jerry'
        self.color = 'blue'
        pass

    def eat(self):
        print('吃饭')
        pass


dog = Animal()
dog.color = 'white'
dog.name = 'Puppy'
print(dog.name)

cat = Animal()
cat.color = 'black'
cat.name = 'Tom'
print(cat.name)

mouse = Animal()
mouse.color = 'yellow'
print(mouse.name, mouse.color)

```

```python
#改进__init--
class People(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        pass

    def talk(self, food):
        print('I am {},I am a {},I am {} years old,I like eating {}'.format(
            self.name, self.sex, self.age, food))
        pass


lingyux = People('lingyux', 20, 'man')
print(lingyux.name, lingyux.age, lingyux.sex)

lingyux.talk('fish')

```



### 理解self

#### 定义

**self**和对象指向同一个内存地址，可以认为**self**就是对象的引用

```python
#证明
class Person(object):
    """docstring for Person"""

    def eat(self):
        print(self)
        print('self={}'.format(id(self)))
        pass
    pass


# xw是一个新的实例化对象
xw = Person()

xw.eat()
print('xw={}'.format(id(xw)))

```

#### 参数传递

- 所谓的**self**，可以理解为对象自己，某个对象调用其方法时，python解释器会把这个对象作为第一个参数传递给**self**，所以开发者只需要传递后面的参数即可

```python
class Person(object):
    """docstring for Person"""

    def eat(self, name, food):
        # print(self)
        # print('self={}'.format(id(self)))
        print('{} 喜欢吃 {}'.format(name, food))
        pass
    pass


# xw是一个新的实例化对象
xw = Person()

xw.eat('lingyux', 'fish')
print('xw={}'.format(id(xw)))

```

#### 特点

1. **self**只有在类中定义实例方法的时候才有意义，在调用的时候不需要传入相应的参数，而是由解释器自动的指向
2. **self**的名称是可以更改的，可以定义成其他的名字，只是约定俗成的定义成**self**
3. **self**指的是 类实例对象本身，相当于**java**中的**this**



### magic方法

#### 概述

在python中有一些内置好的特定的方法，方法名通常为**_ _ xxx _ _**，在进行特定的操作时会被自动调用，这些方法称之为魔法方法。

#### 常用的魔法方法

- `__init__`：初始化一个类，在创建实力对象为其赋值的时候使用
- `__str__`：在将对象转换为字符串 **str**测试的时候，打印对象的信息
- `__new__`：创建并返回一个实例对象，调用了一次，就会得到一个对象
- `__class__`：获得已知对象的类(对象`__class__`)
- `__del__`：对象在程序运行结束后进行对象销毁的时候调用这个方法，来释放资源

#### 实例

```python
class Person(object):
    """docstring for Person"""

    def __init__(self,  name, food, pro):
        self.name = name
        self.food = food
        self.pro = pro
        print('---init---函数已执行')
        pass

    def __str__(self):
        return '我是{} 是{}专业,喜欢吃 {}'.format(self.name, self.pro, self.food)

    def __new__(cls, *args, **kwargs):
        '''
        每调用一次就会生成一个新的对象
        场景：可以控制创建对象的一些属性限定，通常用于单例模式的时候使用 
        '''
        print('---new---函数已执行')
        return object.__new__(cls)  # 在这里是真正创建对象实例的函数
        pass

    def eat(self):
        # print(self)
        # print('self={}'.format(id(self)))
        print('{} 喜欢吃 {}'.format(self.name, self.food))
        pass
    pass


# xw是一个新的实例化对象
lingyux = Person('lingyux', 'fish', 'act')

print(lingyux)

```

#### `__new__`和`__init__`的区别

`__new__`类的实例化方法，必须返回实例，否则对象创建不成功

`__init__`用来做数据属性的初始化工作，也可以认为是实例的构造方法，接受类的实例**self**并对其进行构造

`__new__`至少有一个参数是**cls**代表要实例化的对象，此参数在实例化时由**python**解释器自动完成

`__new__`函数执行要早于`__init__`函数

### 实例

#### 问题分析

- 决战紫禁之巅有两个人物，西门吹雪和叶孤城

  - 属性：
    - name：玩家姓名
    - blood：玩家血量

  - 方法：
    - tong()捅对方一刀，对方掉血10滴
    - kanren() 砍对方一刀，对方掉血15滴
    - chiyao() 吃掉一颗药，补血10滴
    - `__str__` 打印玩家状态

```python
import time  # 导入设置时间的包

# 需要先去定义一个角色类


class Role(object):
    def __init__(self, name, hp):
        '''
        初始化构造函数
        name:角色姓名
        hp：角色血量
        '''
        self.name = name
        self.hp = hp
        pass

    def tong(self, enemy):
        # 捅一刀
        # 敌人扣掉10滴血
        enemy.hp -= 10
        info = '{}捅了{}一刀'.format(self.name, enemy.name)
        print(info)

        pass

    def kanren(self, enemy):
        enemy.hp -= 15
        info = '{}砍了{}一刀'.format(self.name, enemy.name)
        print(info)
        pass

    def chiyao(self):
        self.hp += 10
        info = '{}吃了一颗补血药丸，增加了10滴血'.format(self.name)
        print(info)
        pass

    def __str__(self):
        return '{}还剩下{}滴血'.format(self.name, self.hp)


# 创建两个实例化对象
xmcx = Role('西门吹雪', 100)
ygc = Role('叶孤城', 100)
while True:
    if xmcx.hp <= 0 or ygc.hp <= 0:
        break
        pass
    xmcx.tong(ygc)  # 西门吹雪捅了叶孤城一刀
    print(xmcx)  # 打印状态
    print(ygc)
    print('*********************')
    ygc.tong(xmcx)
    print(xmcx)  # 打印状态
    print(ygc)
    print('*********************')
    xmcx.chiyao()
    print(xmcx)  # 打印状态
    print(ygc)
    print('*********************')
    time.sleep(1)  # 休眠一秒钟


print('游戏结束')

```

###  析构方法

#### 概述

当一个对象被删除或者销毁时，**python**解释器会默认调用一个方法，这个方法为`__del__()`方法，也称为析构方法

#### 定义

```python
class Animal:
    def __init__(self, name):
        self.name = name
        print('这是构造初始化方法')
        pass

    def __del__(self):
        print('当在某个作用域下面没有被引用的情况下，解释器会自动的调用此函数')
        print('这是析构方法')
        print('{}这个对象被彻底清理了'.format(self.name))
        pass


cat = Animal('ketty')
del cat  # 手动删除对象
#当对象被删除的时候也会调用__del__方法	
input('程序等待中')
print('*'*29)

dog = Animal('柯基') #程序完成时会自动的调用__del__方法

```

#### 作用

用来操作对象的释放，一旦释放完毕，就不能再次使用该对象

### 单继承

#### 继承

和现实当中的继承是一样的，也就是说：子可以集成父的内容【属性和行为】

对于面向对象的继承来说其实就是将多个类共有的方法提取到父类中，子类只需要继承父类，而不需要一一去实现，能够最大化的提高代码的编写效率，可以精简代码的层级结构，便于扩展

**子类可以继承父类中的公共方法**

```python
class Animal:
    def eat(self):
        print('eat somthing')
        pass

    def drink(self):
        print('drink somthing')
        pass
    pass


class Dog(Animal):#()里面就是父类
    def talk(self):
        print('小狗汪汪叫')
        pass

    pass


class Cat(Animal):
    def talk(self):
        print('小猫喵喵叫')
        pass
    pass


d1 = Dog()
d1.eat()

c1 = Cat()
c1.eat()
c1.talk()

```



### 多继承

#### 概念

子类可以继承一个父类，也可以同时继承多个父类，可以同时拥有多个父类的属性和方法

#### 实例

```python
class shenxian:
    def fly(self):
        print('神仙都会飞')
        pass
    pass


class Monkey:
    def eat(self):
        print('猴子喜欢吃桃')
        pass
    pass


class Sunwukong(shenxian, Monkey):  # 既是神仙也是猴子

    pass


swk = Sunwukong()
swk.eat()
swk.fly()

class D(object):
    def eat(self):
        print('eat')
        pass
    pass


class C(D):
    def eat(self):
        print('C.eat')
        pass
    pass


class B(D):

    pass


class A(B, C):
    pass


a = A()
a.eat()  # 在执行eat()方法的查找顺序是
# 首先去A中查找，如果A中没有，则继续取B中查找，如果B中则取C类中查找，如果C类中没有，则取D类中查找，否则报错
print(A.__mro__)  # 查看类的依次继承关系
```



### 继承的传递

```python
class Grandfather(object):
    def eat(self):
        print('eat')
        pass
    pass


class Father(Grandfather):
    pass


class Son(Father):
    pass


son = Son()
son.eat()
print(Son.__mro__)

```

### 重写父类方法

#### 概念

所谓重写就是子类中，有一个和父类相同名称的方法，在子类中的方法会覆盖掉父类的方法

```python
class Grandfather(object):
    def eat(self):
        print('G.eat')
        pass
    pass


class Father(Grandfather):
    def eat(self):  # 因为父类中已经存在相同的方法，这里相当于方法重写[方法覆盖]
        print('F.eat')
        pass
    pass


class Son(Father):
    pass


son = Son()
son.eat()
print(Son.__mro__)

```

#### 原因

父类的方法已经不能满足子类的需要，需要子类对方法进行重写或完善

### 调用父类方法

```python
class Dog(object):
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def talk(self):
        print('wangwang')
        pass
    pass


class kejiquan(Dog):
    def __init__(self, name, color):  # 调用父类的方法
        # Dog.__init__(self, name, color)  # 重写父类的方法，执行完毕就可以具备父类的属性
        # 扩展其他的属性
        # 还可以利用super关键字
        super().__init__(name, color)  # 自动查找父类，自动调用方法
        # 如果继承了多个父类，那么会按照顺序诸葛的查找
        self.height = 90
        self.weight = 20

    def talk(self):  # 重写父类的方法
        super().talk()
        print('叫的跟狗一样')

    def __str__(self):
        return '{} {} {} {}'.format(self.name, self.color, self.height, self.weight)  # noqa: E501
    pass


kj = kejiquan('qt', 'red')
kj.talk()
print(kj)

```

### 多态

#### 概念

定义时的类型和运行时的类型不一样，此时就称为多态，就是同一种行为对于不同的子类【对象】有不同的行为表现

#### 前提

> 1. 必须存在继承关系，即必须发生在父类和子类之间
> 2. 重写，子类需要重写父类的方法

#### 实例

```python
# 父类
class Animal(object):
    def say_who(self):
        print('我是一个动物')
        pass
    pass

# 子类


class Duck(Animal):

    def say_who(self):
        print('我是一只鸭子')
        pass
    pass


class Dog(Animal):
    def say_who(self):
        print('我是一只狗')
        pass
    pass


def commonInvoke(obj):
    '''
    统一调用的方法
    '''
    obj.say_who()


# duck1 = Duck()
# duck1.say_who()
# dog1 = Dog()
# dog1.say_who()
listObj = [Duck(), Dog()]
for item in listObj:
    commonInvoke(item)

```

#### 优点

> 1. 增加程序的灵活性
> 2. 增加程序的扩展性



### 类属性与实例属性

#### 类属性

类对象所拥有的属性，被所有类对象所共有，类对象和实例对象都可以访问

#### 实例属性

实例对象所拥有的属性，只能通过实例对象访问

#### 实例

```python
class Student(object):
    name = '李明'  # 属于类属性，就是student所拥有的属性

    def __init__(self, age):
        self.age = age
        pass
    pass


lm = Student(18)
Student.name = '刘德华'
print(lm.name)
print(Student.name)
# print(Student.age)不能访问

```



### 类方法与静态方法

#### 类方法的定义

类对象所拥有的方法，需要用装饰器**@classmethod**来标记为类方法，对于类方法，第一个参数必须是类对象，一般以**cls**作为第一个参数，类方法可以通过类对象，实例对象调用

#### 实例

```python
class People(object):
    country = 'China'

    @classmethod  # 类方法
    def get_country(cls):
        return cls.country  # 访问类属性
        pass

    @classmethod
    def change_country(cls, data):
        cls.country = data
        pass
    pass


print(People.get_country())
xm = People()
print('实例对象访问{}'.format(xm.get_country()))
People.change_country('English')
print(People.get_country())

```

#### 静态方法

类对象所拥有的方法，需要用**@staticmethod**来表示静态方法，静态方法不需要任何参数

```python
class People(object):
    country = 'China'

    @classmethod  # 类方法
    def get_country(cls):
        return cls.country  # 访问类属性
        pass

    @classmethod
    def change_country(cls, data):
        cls.country = data
        pass

    @staticmethod
    def print_country():
        print('静态方法{}'.format(People.country))
        pass
    pass


print(People.get_country())
xm = People()
print('实例对象访问{}'.format(xm.get_country()))
People.change_country('English')
print(People.get_country())
People.print_country()  # 一般情况下，不会通过实例对象访问静态方法



import time  # 引入时间模块

#显示当前时间
class TimeTest(object):
    @staticmethod
    def show_time():
        return time.strftime("%H:%M:%S", time.localtime())
        pass
    pass


print(TimeTest.show_time())
```

静态方法主要用来存放逻辑性的代码，本身和类及实例对象没有交互，不会涉及类中的方法和属性的操作

------

### 私有化属性

#### 语法

两个下划线开头，声明该属性为私有属性，不能在类的外部被使用或者直接访问

```python
class Person(object):
    __age = 18#定义一个私有化属性

```

#### 使用私有属性的场景

- 把特定的属性隐藏起来，不想让类的外部进行直接调用
- 保护这个属性，不想属性的值被随意改变
- 保护这个属性，不想让派生类【子类】继承这个属性

#### 结论

- 私有化的实例属性不能在外部直接的访问，可以在内部随意的访问
- 子类不能继承父类的私有化属性，只能继承父类公共的属性和行为
- 在属性名的前面直接加两给下划线就能进行私有化了

#### 实例

```python
class Person(object):
    __hobby = 'dance'  # 私有类属性

    def __init__(self):
        self.__name = 'lingyux'  # 加上__将此属性私有化 类的内部可以访问
        self.age = 22
        pass

    def __str__(self):
        return '{} is {} years old,he likes {}'.format(self.__name, self.age, self.__hobby)  # noqa: E501
        pass

    def changeValue(self):
        Person.__hobby = 'sing'


class student(Person):

    def printInfo(self):
        print(self.__name)
    pass


lingyux = Person()
# print(lingyux.__name)  # 通过类对象进行外部访问
# 私有化之后不能再外部直接访问
lingyux.changeValue()
print(lingyux)
print(lingyux.hobby)
print('*'*20)
stu = student()
print(stu)
print(stu.__name)  # 属性不能被子类继承，但是可以通过父类的方法进行访问

stu.printInfo()

```



### 私有化方法

#### 语法

在方法名前面加上两个下划线

```python
class A(object):
    def __myname(self):
        print('lingyux')
        pass
    def myname(self):
        print(xiaoming)
        pass
    pass
a=A() a.myname()#正常调用
a.__myname()#错误调用
```

#### 特性

- 私有化方法一般是类内部调用，子类不能继承，外部不能调用

#### 实例

```python
class Animal(object):
    def __eat(self):
        print('eat')
        pass

    def run(self):
        self.__eat()  # 在此调用私有化方法
        print('run')
        pass
    pass


class Bird(Animal):
    pass


b1 = Bird()
b1.run()
b1.eat()

```



### Property属性函数

#### 实现方式

- 类属性，在类中定义值为**property**对象的类属性

```python
class Person(object):
    def __init__(self):
        self.__age = 18
        pass

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age < 0:
            print('年龄不能小于0')
        else:
            self.__age = age
            pass
        pass
    age = property(get_age, set_age)

    pass


p1 = Person()
print(p1.age)
p1.age = -1
print(p1.age)

```



- 装饰器

```python
# 实现方式2：通过装饰器
class Person(object):
    def __init__(self):
        self.__age = 18
        pass

    @property
    def age(self):
        return self.__age
        pass

    @age.setter
    def age(self, age):
        if age < 0:
            print('年龄不能小于0')
        else:
            self.__age = age
            pass
        pass


p1 = Person()
print(p1.age)
p1.age = 30
print(p1.age)
```



### `__new__`方法

#### 作用

`__new__`方法的作用是，创建并返回一个实例对象，如果`__new__`值调用了一次就会得到一个对象。继承自**object**的新式类才有**new**这一个魔法方法

#### 注意事项

- `__new__`是一个在对象实例化时所调用的第一个方法
- `__new__`至少需要一个参数**cls**，代表要实例化的类，此参数在实例化的时候由**Python**解释器自动提供，其他的参数是用来直接传递给`__init__`方法
- `__new__`决定是否要使用该`__init__`方法，因为`__new__`可以调用其他类的构造方法或者直接返回别的实例对象来作为本类的实例，如果`__new__`没有返回实例对象，则`__init__`不会被调用
- 在`__new__`方法中，不能调用自己的`__new__`方法，即：`return cls.__new__(cls)`，否则会报错

- 在新式类中，new方法才是真正实例化的方法，为类提供外壳制造出实例框架，然后用该框架内的构造方法`__init__`进行丰富完善

#### 实例

```python
class Animal(object):
    def __init__(self):
        self.color = 'red'
        pass
        # 在python当中，如果不重写 ，new方法的默认结构如下

    def __new__(cls, *args, **kwargs):
        return super().__new(cls, *args, **kwargs)
        return object.__new(cls, *args, **kwargs)
    pass


tiger = Animal()  # 实例化的过程会自动调用new方法创建实例

```



### 单例模式

#### 概述

单例模式是常用设计模式的一种，用来确保某一个类只有一个实例存在，如果希望在某个系统中，某个类只能出现一个实例的时候，单例模式就能满足需求

#### 实现步骤

- 利用类属性保存初次创建的对象，第二次实例化的时候判断类属性是否有保存实例对象，如果有就返回类属性保存的实例，否则调用父类`__new__`方法创建新的实例对象

- 只执行一次**init**方法，通过类变量进行标记控制

#### 实例

```python
# 创建一个单例对象 基于__new__方法实现
class DataBaseClass(object):
    def __new__(cls, *args, **kwargs):
        # cls._instance=cls.__new__(cls)
        # 不能使用自身的new方法，会造成迭代死循环
        if not hasattr(cls, '_instance'):  # 如果不存在就创建
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class DBoptSignle(DataBaseClass):
    pass


db1 = DataBaseClass()
db2 = DataBaseClass()
db3 = DataBaseClass()
print(id(db1))
print(id(db2))
print(id(db3))
db1 = DBoptSignle()
db2 = DBoptSignle()
db3 = DBoptSignle()
print(id(db1))
print(id(db2))
print(id(db3))

```



### 错误与异常处理

#### 语法格式

- **try**：可能出现错误的代码块

  - 将可能出错的代码放到**try**里面，**except**可以指定类型捕获异常。**except**里面的代码是捕获到异常时执行，将错误捕获，这样程序就不会因为一段代码包异常而导致整个程序崩溃

  - **except**在捕获错误异常的时候是要根据具体的错误类型来捕获的

  - 同一个**try**可以捕获多个不同类型的异常

  - **Exception**可以捕获所有异常，当对出现的问题或错误不确定的时候，可以使用**Exception**

  - 捕获到异常之后尽量去处理所遇到的异常

  - ```python
    
    try:
        print(b)  # 捕获逻辑的代码
        # li = [1, 2, 34]
        # print(li[10])
        # a = 10/0
        pass
    # except NameError as msg:
    #     # 捕获到错误才会到这里执行
    #     print(msg)
    #     pass
    # except IndexError as msg:
    #     print(msg)
    #     pass
    # except ZeroDivisionError as msg:
    #     print(msg)
    #     pass
    except Exception as result:
        print(result)
    print('初次接触到异常')
    
    ```

  - 不需要在每个可能出错的地方去捕获，只需要在合适的层次区捕获错误就可以了

    ```python
    def A(s):
        return 10/int(s)
        pass
    
    
    def B(s):
        return A(s)*2
        pass
    
    
    def main():
        try:
            B('0')
            pass
        except Exception as msg:
            print(msg)
            pass
        pass
    
    
    main()
    
    ```

- **except**：出错之后执行的代码块

**异常抛出的机制**

如果在运行时发生异常，解释器会查找相应的异常捕获类型

如果没有找到的话，他会将异常传递给上一层的调用函数，看能否处理

如果在最外层没有找到的话，解释器就会退出，程序就会结束

- **else**：没有出错的代码块

  ```python
  try:
      print('aa')
      pass
  except Exception as msg:
      print(msg)
  else:
      print('当try没有错误的情况下，执行此代码')
  
  ```

  

- **finally**：不管有没有出错都执行的代码块

```python
try:
    int('34')
    open('aaa.txt')
    pass
except Exception as msg:
    print(msg)
    pass
finally:
    print('不管有没有出错都会执行的代码')

```

#### 自定义异常

- 自定义异常，都要直接或间接的继承**Error**或者**Exception**类

- 由开发者主动抛出自定义异常，在**Python**中使用**raise**关键字

  

```python
class ToolongMyException(Exception):
    def __init__(self, length):
        self.len = length
        pass

    def __str__(self):
        return '您输入的姓名数据长度是'+str(self.len)+'超出规定长度'
        pass
    pass


def name_test():
    name = input('请输入您的姓名')
    try:
        if len(name) > 5:
            raise ToolongMyException(len(name))
            pass
        else:
            print(name)
            pass
        pass
    except ToolongMyException as msg:
        print(msg)
        pass
    finally:
        print('函数执行完毕')


name_test()

```



### Python动态添加属性和方法

#### 动态添加属性

```python
class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass

    def __str__(self):
        return '{}今天{}岁了'.format(self.name, self.age)
        pass


zyh = Student('lingyux', 20)
zyh.weight = 80  # 动态添加属性
print(zyh)
print(zyh.weight)
print('-'*30)
zm = Student('lingyuxia', 20)
print(zm)
# print(zm.weight)
print('-'*30)
Student.school = '南京大学'  # 动态添加类属性

print(zm.school)

```

#### 动态添加方法

```python
import types  # 导入添加方法的库


def dymicMethod(self):
    print('{}的体重是：{},学校是{}'.format(self.name, self.weight, Student.school))
    pass


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass

    def __str__(self):
        return '{}今天{}岁了'.format(self.name, self.age)
        pass


Student.school = '南京大学'  # 动态添加类属性
zyh = Student('lingyux', 20)
zyh.weight = 80  # 动态添加属性
# 绑定方法
zyh.printInfo = types.MethodType(dymicMethod, zyh)
print(zyh)
print(zyh.weight)
zyh.printInfo()  # 调用动态绑定的方法
print('-'*30)
zm = Student('lingyuxia', 20)
print(zm)
# print(zm.weight)
print('-'*30)


print(zm.school)
print('-'*30)
# 动态添加实例方法

```

#### 给类绑定类方法和静态方法

- 使用方式：类名.方法名 = xxx

- ```python
  import types  # 导入添加方法的库
  
  
  def dymicMethod(self):
      print('{}的体重是：{},学校是{}'.format(self.name, self.weight, Student.school))
      pass
  
  
  @classmethod
  def classTest(cls):
      print('这是一个类方法')
      pass
  
  
  @staticmethod
  def staticMethodTest():
      print('这是一个静态方法')
      pass
  
  
  class Student(object):
      def __init__(self, name, age):
          self.name = name
          self.age = age
          pass
  
      def __str__(self):
          return '{}今天{}岁了'.format(self.name, self.age)
          pass
  
  
  print('绑定类方法')
  Student.Testmethod = classTest
  Student.Testmethod()
  print('绑定类方法执行结束')
  print('绑定静态方法')
  Student.TeststaticMethod = staticMethodTest
  Student.TeststaticMethod()
  print('静态方法执行结束')
  Student.school = '南京大学'  # 动态添加类属性
  zyh = Student('lingyux', 20)
  print('实例调用类方法')
  zyh.Testmethod()
  zyh.weight = 80  # 动态添加属性
  # 绑定方法
  zyh.printInfo = types.MethodType(dymicMethod, zyh)
  print(zyh)
  print(zyh.weight)
  zyh.printInfo()  # 调用动态绑定的方法
  print('-'*30)
  zm = Student('lingyuxia', 20)
  print(zm)
  # print(zm.weight)
  print('-'*30)
  
  
  print(zm.school)
  print('-'*30)
  # 动态添加实例方法
  
  ```

  

### `__slots__`属性

#### 概述

> - **python**是动态语言，在运行的时候可以动态添加属性。如果限制在运行的时候给类添加属性，**Python**允许在定义**class**的时候，定义一个特殊的`__slots__`变量，来限制该**class**实例能够添加的属性。
> - 只有在`__slots__`变量中的属性才能被添加，没有在`__slots__`变量中的属性会添加失败。可以防止其他人在调用类的时候胡乱添加属性或方法。`__slots__`属性子类不会继承，只在当前类中有效

#### 实例

```python
# 作用：
# 限制要添加的实例属性
# 节约内存空间
class Student(object):
    __slots__ = ('name', 'age', 'score')

    def __str__(self):
        return '{} {} {}'.format(self.name, self.age, self.score)

    pass


xw = Student()
xw.name = 'xw'
xw.age = 10
xw.score = 96
# print(xw.__dict__)  # 所有的数据都存放在字典里，但是占用空间较大
# 在定义了__slots__变量之后，student类已经不能随意创建不在__slots__范围内的属性了
print(xw)

# 在继承关系中的使用
# 子类未声明 __slots__属性的时候，子类不会继承父类的__slots__
# 子类声明__slots__，子类会继承父类的__slots__属性
# 子类的__slots__范围是自身的范围加上父类的范围


class subStudent(Student):

    __slots__ = ('gender', 'pro')
    pass


lm = subStudent()
lm.gender = '男'
lm.pro = 'computer'
print(lm.gender, lm.pro)

```

## 飞机大战

### 需求描述

> - 四个对象：我方飞机，敌方飞机 ，我方子弹，敌方子弹
> - 功能：我方飞机可以根据按键控制移动，敌方飞机随机移动，双方飞机都可以发射子弹 背景音乐的添加

### 步骤

> - 创建一个窗口
> - 创建一个我方飞机，根据方向键左右移动
> - 给我方飞机添加发射子弹的方法【按下空格键】
> - 创建一个敌机，敌机随机移动，可以发射子弹

#### pygame介绍

Pygame是一个利用SDl库写的游戏库，全名**Simple DirectMedia Layer**，**SDL**是用C语言写的，不过它可以使用**C++**进行开发，**Pygame**就是**Python**使用它的一个库

```python
import pygame  # 引用第三方的模块
import random  # 随机生成一个数据
from pygame.locals import *
'''
1.实现飞机的显示，并且可以控制飞机的移动
'''
# 抽象出一个基类


class BasePlane(object):
    def __init__(self, screen, imagePath):
        self.screen = screen
        self.image = pygame.image.load(imagePath)
        self.bulletList = []
        pass

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        # 完善子弹的展示逻辑
        needDelItem = []
        for item in self.bulletList:
            if item.judge():
                needDelItem.append(item)
                pass
            pass
        # 重新遍历一下
        for i in needDelItem:
            self.bulletList.remove(i)
            pass
        for bullet in self.bulletList:
            bullet.display()  # 显示一下子弹的位置
            bullet.move()  # 子弹进行移动 下次在显示的话就会看到子弹在修改后的位置了

    pass


class Basebullet(object):
    def __init__(self, x, y, screen, bulletType):
        self.type = bulletType
        self.screen = screen
        if self.type == 'hero':
            self.x = x + 13
            self.y = y-20
            self.imagepath = './feiji/bullet.png'
            pass
        elif self.type == 'enemy':
            self.x = x
            self.y = y + 10
            self.imagepath = './feiji/enemybullet.png'
            pass
        self.image = pygame.image.load(self.imagepath)
        pass

    def move(self):
        if self.type == 'hero':
            self.y -= 2
            pass
        elif self.type == 'enemy':
            self.y += 2
            pass
        pass

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        pass

    def judge(self):
        if self.y > 500 or self.y < 0:
            return True
            pass
        else:
            return False
            pass
        pass
    pass


class HeroPlane(BasePlane):
    def __init__(self, screen):
        '''
        初始化对象
        screen:主窗体对象
        '''
        # 设定飞机的默认位置
        self.x = 150
        self.y = 450
        super().__init__(screen, './feiji/hero.png')  # 调用父类的方法
        pass

    def moveLeft(self):
        '''
        左移动
        '''
        if self.x > 0:
            self.x -= 10
        pass

    def moveRight(self):
        '''
        右移动
        '''
        if self.x < 350-40:
            self.x += 10
        pass

    # 发射子弹

    def shoot(self):
        newbullet = Basebullet(self.x, self.y, self.screen, 'hero')
        self.bulletList.append(newbullet)
        pass

    pass


def key_control(heroObj):
    '''
    定义普通的函数实现键盘的检测
    '''
    eventList = pygame.event.get()
    for event in eventList:
        if event.type == QUIT:
            print('退出')
            exit()
            pass
        elif event.type == KEYDOWN:
            if event.type == K_a or event.key == K_LEFT:
                print('left')
                heroObj.moveLeft()  # 调用函数实现左移动
                pass
            elif event.type == K_d or event.key == K_RIGHT:
                print('right')
                heroObj.moveRight()  # 调用函数实现右移动
                pass
            elif event.key == K_SPACE:
                print('space')
                heroObj.shoot()
                pass
            pass

# 创建子弹类


# 创建敌机
class Enemy(BasePlane):
    def __init__(self, screen):
        # 默认设置一个方向
        self.direction = 'right'
        self.x = 0
        self.y = 0
        super().__init__(screen, './feiji/enemy.png')
        pass

    def shoot(self):
        # 敌方随机发射子弹
        num = random.randint(1, 20)
        if num == 3:
            newBullet = Basebullet(self.x, self.y, self.screen, 'enemy')
            self.bulletList.append(newBullet)
        pass

    def move(self):
        # 随机移动
        if self.direction == 'right':
            self.x += 2
            pass
        elif self.direction == 'left':
            self.x -= 2
            pass
        if self.x > 350-20:
            self.direction = 'left'
            pass
        elif self.x < 0:
            self.direction = 'right'
            pass
        pass
    pass


def main():
    # 首先创建一个窗口 用来显示内容
    screen = pygame.display.set_mode((330, 500), depth=32)
    # 设定一个背景图片
    background = pygame.image.load('./feiji/background.png')
    # 设置一个标题
    pygame.display.set_caption('阶段总结 - 飞机小游戏')
    # 添加背景音乐
    pygame.mixer.init()
    pygame.mixer.music.load('./feiji/background.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)  # 循环次数 -1表示无限循环
    # 创建一个飞机对象
    hero = HeroPlane(screen)
    # 创建一个敌机对象
    enemyplane = Enemy(screen)
    while True:
        screen.blit(background, (0, 0))
        # 显示玩家图片，需要给一个坐标
        hero.display()
        enemyplane.display()  # 显示
        enemyplane.move()  # 敌机移动
        enemyplane.shoot()  # 敌机发射子弹
        # 获取键盘事件
        key_control(hero)
        # 更新显示的内容
        pygame.display.update()
        pygame.time.Clock().tick(20)
    pass


if __name__ == '__main__':
    main()

```

## Python文件操作

### 文件关闭与打开

#### 操作步骤

- 打开文件
  - **open**函数
  - 语法格式：`open('文件名称','打开模式')`
  - 示例：`open('test.txt','w')`
- 读/写文件
- 保存文件
- 关闭文件

```python

# 打开文件
# 默认的编码是gdk 中文编码，最好的习惯就是指定一个编码
fobj = open('./test.txt', 'w', encoding='utf-8')  # 模式和C语言基本一致
# 读取/写入数据 已经存在，会将其覆盖
fobj.write('在苍茫的大海上\n')
fobj.write('狂风卷积着乌云\n')
fobj.close()  # 保存关闭文件


# 以二进制的方式写入
fobj01 = open('test01.txt', 'wb')  # str -> bytes
fobj01.write('在乌云和大海之间\n'.encode('utf-8'))
fobj01.close()

fobj01 = open('test.txt', 'a', encoding='utf-8')  # a追加
fobj01.write('在乌云和大海之间\n')
fobj01.write('海燕像黑色的闪电\n')
fobj01.close()


# 二进制字节追加
# 以二进制的方式写入
fobj01 = open('test01.txt', 'ab')  # str -> bytes
fobj01.write('在乌云和大海之间'.encode('utf-8'))
fobj01.close()

```

```python
# 读取数据
fobj = open('test.txt', 'r', encoding='utf-8')  # 需要指定编码格式
# a = fobj.read() #读取所有数据
# print(a)
b = fobj.read(12)
print(b)
# 第二次读取会从第一次读取的末尾开始读取
print(fobj.readline())  # 读取一行
print(fobj.readlines())  # 读取的是一个列表
fobj.close()


# 读取数据
fobj = open('test01.txt', 'rb')  # 需要指定编码格式
# a = fobj.read() #读取所有数据
# print(a)
b = fobj.read(12)
print(b.decode('utf-8'))
# 第二次读取会从第一次读取的末尾开始读取
print(fobj.readline())  # 读取一行
print(fobj.readlines())  # 读取的是一个列表
fobj.close()

```

- **with**

  - **with**语句，不管处理文件过程中是否发生异常，都能保证**with**语句执行完毕之后关闭打开的文件

  - ```python
    with open('test.txt', 'a', encoding='utf-8') as f:
        # print(f.read())
        f.write('oh my god')
    
    ```

#### 小结

- **read**：**r r+ rb rb+**
- **r r+**：只读，适用于普通读取场景
- **rb rb+**：适用于文件，图片，视频，音频
- **write**：**w w+ wb+ wb a ab**
- **w wb+ wb**每次都会创建新的文件
- **a ab a+**：在原有的基础上在文件的末尾追加

### 应用：文件备份脚本

```python
#小文件的读写
# 文件的备份
def copyFile():
    # 接受用户输入的文件名
    old_file = input('请输入要备份的文件名')
    file_list = old_file.split('.')
    # 构造新的文件名 加上备份的后缀
    new_file = file_list[0]+'_backup.'+file_list[1]
    old_file = open(old_file, 'r', encoding='utf-8')
    new_file = open(new_file, 'w', encoding='utf-8')  # 以写的模式打开新文件
    content = old_file.read()  # 读取文件内容
    new_file.write(content)  # 将内容写入到备份文件
    new_file.close()
    old_file.close()
    pass


copyFile()

```



### 文件定位

#### tell()

- 文件定位指的是当前文件的指针读取到的光标位置，在读取文件的过程中，如果想知道当前位置，可以用**tell()**获取

```python
# 返回指针当前所在的位置
with open('test01.txt', 'r', encoding='utf-8') as f:
    print(f.read(3))
    print(f.tell())
    print(f.read(2))
    print(f.tell())

```

#### truncate()

- 可以对源文件进行截取操作

```python
with open('test01.txt', 'r', encoding='utf-8') as f:
    print(f.read())
    pass
print('截取之后的数据')
with open('test01.txt', 'r+', encoding='utf-8') as f:
    f.truncate(15)#保留前15个字符
    print(f.read())
```

#### seek()

- 如果在操作文件的过程中，需要定位到其他的位置进行操作，可以使用**seek()**
- **seek(offset,from)**有连个参数，**offset**表示偏移量，单位为字节，负数是往回偏移，正数是向前偏移，**from**表示其实位置，0表示文件开头，1表示当前位置，2表示文件末尾

```python
with open('test01.txt', 'rb') as f:
    data = f.read(2)
    print(data.decode('utf-8'))
    f.seek(-2, 1)  # 相当于光标向前移动2个字节
    print(f.read(4).decode('utf-8'))
    f.seek(-6, 2)#2代表在文件末尾处，-6表示向前移动6个字节
    print(f.read(6).decode('utf-8'))
```



### 模块介绍

#### import导入模块

##### 语法格式

`import time`

##### 调用语法格式

`模块名.函数名`

**import**在首次导入模块的时候，会发生如下3步操作

- 打开模块文件
- 执行模块对应的文件，将 执行过程中的产生的名字都丢到模块的名称空间
- 在程序当中会有一个模块的名称指向模块的名称空间

##### 语法格式

`from ... import`

如果 一个模块存在很多个函数，如果只想导入其中几个函数可以使用此种办法

`from time import ctime,time`

使用此种方法导入，如果函数名相同，后面导入的会覆盖前面导入的

**一次性导入所有函数**：

`from time import *`

首次导入的操作：

1. 以模块为准，创建一个模块的名称空间

2. 执行模块对应的文件，将执行过程中产生的名称丢到名称空间

3. 在当前执行文件的名称空间中拿到一个名字，该名字直接指向模块中的某一个名字，这意味着不用加前缀，直接使用方法

   优点：代码较为简介

   缺点：易产生名称冲突

```python
# import time
# print(time.ctime())
from time import ctime, time  # 部分导入
print(ctime())
print(time())
#可以对库重新命名
import time as Mytime
print(Mytime.ctime())
```





### os模块操作文件

```python
import os
import shutil
# # os.rename('test.txt', 'test-1.txt')
# os.remove('test01.txt')  # 前提是文件必须存在
# os.mkdir('test')#不允许级联创建文件夹
# os.rmdir('test')#只能删除空目录
# os.makedirs('d:/01Python/core')
# # 如果删除非空目录，需要引入shutil模块
# shutil.rmtree('d:/01Python/')  # 多级删除非空目录

# 获取当前目录
# print(os.getcwd())
# 路径的拼接
# print(os.path)
# os.path.join(os.getcwd())

# 获取目录列表
# listrs = os.listdir('d:/')
# for item in listrs:
#     print(item)
# scandir和with一起使用，上下文管理器会在迭代器遍历完成之后会自动的释放资源
# with os.scandir('d:/') as dir:
#     for item in dir:
#         print(item.name)
basepath = 'd:/'
for item in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, item)):
        print(item)

```



### 模块的制作、发布、安装

#### 模块的定义

在**Python**当中一个**.py**文件就是一个模块

#### 作用:

- 可以让我们有逻辑的区组织我们的**Python**代码 

- 以库的形式封装起来，非常方便的区让调用者使用 

- 可以定义函数，类，变量，也能包含可执行的代码

#### 注意

不同的模块可以定义相同的变量名，但是每一个模块的变量名作用域只是在本模块中

#### 分类

内置模块 自己定义的模块 第三方的模块

## Python的垃圾回收

### 引用计数机制

#### 优点

- 简单
- 实时性较好：一旦没有引用，内存直接就释放
- 处理回收内存的时间分配到了平时

#### 缺点

- 维护引用计数会资源资源
- 循环引用

### Python中的循环数据结构及引用计数

#### 标记清除机制

1. 标记垃圾对象(垃圾检测)
2. 清除垃圾(垃圾回收)

#### 分代回收





### Python中的GC模块

#### 主要任务

1. 为新生成的对象分配内存
2. 识别那些是垃圾对象
3. 从垃圾对象回收内存

#### 触发垃圾回收机制的情况

1.当gc模块的计数器达到阀值的时候，自动回收垃圾

2.调用gc.collect()，手动回收垃圾

3.程序退出的时候，python解释器来回收垃圾

### Python内存优化

#### 小整数与大整数对象池

Python为了优化速度，使用了小整数对象池，避免整数的使用频繁的申请和销毁空间

大整数池没有提前创建好对象，是一个空的池子，需要我们自己创建，创建好之后，他会把创建好的整数对象保存到池子里面，后面不需要再行创建。小整数池提前将对象创建好，不需要再次创建

### Python pep8规范

### Python命令行参数

```python
import sys

print('参数的个数为：', len(sys.argv), '个参数')
print('参数列表：', str(sys.argv[1:]))

```

#### argparse

可以轻松编写用户友好的命令行界面