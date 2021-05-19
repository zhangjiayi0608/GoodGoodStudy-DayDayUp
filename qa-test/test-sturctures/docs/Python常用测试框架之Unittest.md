# Python常用测试框架之Unittest

## 概述

### Python单元测试框架

#### 示例代码：https://blog.csdn.net/kongsuhongbaby/article/details/84111435

### 基础概念

#### Test Fixture

##### 为展开测试所进行的准备工作、清理工作

###### setUp（）、tearDown（）

###### SetUPcLASS()

#### Test Case

##### 独立的测试单元，真实的测试函数

##### 基类：unittest.TestCase

##### 以test开头的类内函数

#### Test Suite

##### 测试套件：一系列case或suite，可以合并执行

#### Test Runner

##### 执行测试、输出测试结果的组件

## 命令行运行

### python -m unittest test1 test2

#### 运行一个Python文件（早期版本可能不支持）

### python -m unittest test.TestClass

#### 运行一个测试类（早期版本可能不支持）

### python -m unittest test.TestClass.test_method

#### 运行一个测试函数（测试用例）

### python -m unittest -h

#### 获取命令行帮助文档

### 其他常用参数

#### -v 

##### 展示更详细的信息

#### -b

##### 标准输出流与标准错误流放入缓冲区，如果成功则被丢弃

#### -c

##### 双击Ctrl c才停止，单击不影响

#### -f

##### 当出现第一个错误或失败时，即停止测试

#### -k

##### 只运行匹配模式或子串的方法和类，大小写敏感

## 组织测试代码

### 继承于TestCase

### 基础单元是testcase，以test开头的方法

#### 用assert断言验证测试输出

#### 除assert*（）外，其他类型的异常会当做错误处理

#### testcase的执行顺序是方法名的字符串排序

#### testcase的辅助函数是setUp于tearDown

##### setUp（）

###### 在每个testcase执行之前执行该函数，testcase的前置操作

###### 如果setUp异常，则发生了错误，不会运行testcase

##### tearDown（）

###### 在每个testcase执行之后执行该函数，testcase的后置操作

###### 如果setUp成功运行，无论testcase是否成功，都运行tearDown

#### __init__（）

##### 如果存在__init__()函数，在每个testcase运行时也会调用一次__init__()

### 如果需要集合testcase，采用testSuite

#### 基类为unittest.TestSuite()

#### suite.addTest(TestClass('test_case'))将指定的testcase添加进来

#### 调用执行器执行suite：unittest.TextTestRunner().run(suite())

## 常用装饰器

### 跳过测试

#### 跳过testcase/Class

##### @unittest.skip('无论何时都跳过')

##### @unittest.skipIf(满足指定条件时跳过)

##### @unittest.skipUnless（不满足指定条件时跳过）

##### self.skipTest('调用即可跳过')

#### 以上也适用于SetUp等

### 预计失败

#### @unittest.expectedFailure

##### 这个测试函数应该是失败的才是符合预期的

## 一些API

### 常用断言

#### https://docs.python.org/zh-cn/3/library/unittest.html#test-cases

#### assertEqual(a, b)     a == b
assertNotEqual(a, b)     a != b
assertTrue(x)     bool(x) is True
assertFalse(x)     bool(x) is False
assertIs(a, b)     a is b
assertIsNot(a, b)     a is not b
assertIsNone(x)     x is None
assertIsNotNone(x)     x is not None
assertIn(a, b)     a in b
assertNotIn(a, b)     a not in b
assertIsInstance(a, b)     isinstance(a, b)
assertNotIsInstance(a, b)     not isinstance(a, b)

### 组合测试

#### class unittest.TestSuite

##### addTest(test)

##### addTests(tests)

### 加载和运行测试

#### class unittest.TestLoader

##### TestLoader类用于从类和模块创建测试套件

## 数据驱动的测试

### unittest本身不支持

### 参考ddt模块

## HTML报告的生成

### HTMLTestRunner
