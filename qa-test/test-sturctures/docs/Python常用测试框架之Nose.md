# Python常用测试框架之Nose

## 安装

### pip install -U nose

## 组织测试代码

### 方法以test开头

### 跳过测试用例

#### from nose.plugins.attrib import attr

##### @attr(speed='slow')

##### nosetests -a speed=slow

### 脚手架

#### 包级别

##### setUp teardown放在init文件中

#### 模块级别

##### 有自己的setup与teardown函数

#### 测试级别

##### with_setup装饰器设置

## 运行

### nosetests python.py

### 测试报告

#### pip install nose-htmloutput

##### --with-html --html-file=

#### --with-xunit

### 重试运行失败的case

#### nosetests -v --failed

### 可以自动收集并运行case，无需unittest.main()

### nose.tools

#### unittest全部assert

#### 测试执行时间

#### 异常输出

## 参数化

### 结合ddt
