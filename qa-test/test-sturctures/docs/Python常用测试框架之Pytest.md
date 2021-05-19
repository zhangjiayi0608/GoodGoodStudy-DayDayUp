# Python常用测试框架之Pytest

## 概述

### 基于unittest衍生

### 可兼容unittest

### 支持selenium

#### pytest-selenium

## 安装

### pip install -u pytest

## 组织测试代码

### 测试文件以test_开头或_test结尾

### 测试类以Test开头，不带有init方法

### 测试函数以test_开头

### 断言使用基本的assert即可

### 前置与后置

#### setup_module、teardown_module

#### setup_function、teardown_function

#### setup_class、teardown_class

#### setup_method、teardown_method

#### setup/teardown

##### setup_method---setup---teardown---teardown_method

#### 自定义

##### fixture(scope=”function”, params=None, autouse=False, ids=None, name=Noe)

##### 方式灵活、实现共享、支持跨文件使用一个来完成测试

### 跳过测试用例

#### @pytest.mark.skipif(condition)

#### @pytest.mark.xfail

### 超时机制

#### pip install pytest-timeout

##### @pytest.mark.timeout(60)

##### pytest --timeout=300

## 退出码 

### 退出代码0    成功地收集并传递了所有测试
退出代码1    测试被收集和运行, 但一些测试失败
退出代码2    测试执行被用户中断
退出代码3    执行测试时发生内部错误
退出代码4    pytest 命令行使用错误
退出代码5    未收集任何测试

## 运行

### 函数

#### pytest.main(["-s","test_abc.py"])

### 命令行

#### 运行一个测试文件

##### pytest ./test_abc.py

#### 运行一个类

##### pytest test_se.py::TestClassOne

#### 运行一个测试用例

##### pytest test_mod.py::test_func

#### 运行类里面的测试用例

##### pytest test_abc.py::Test_Class::test_c

#### 失败即结束

##### pytest -x

#### 第2个失败就结束

##### pytest --maxfail=2

#### 可用的内置函数展示

##### pytest --fixtures

### 测试报告

#### pip install -U pytest-htmlpy

##### pytest --html=report.html

#### pytest --junitxml=path

#### 支持pytest-TML、allure插件

### 多进程运行

#### pip install -U pytest-xdist

#### pytest test_se.py -n NUM

##### NUM为并发的进程数

### 重试运行失败的case

#### pip install -U pytest-rerunfailures

#### pytest test_se.py --reruns NUM

##### NUM为重试的次数

## 参数化

### 装饰器

#### @pytest.mark.parametrize

##### 标记测试用例

##### 执行时加 -m即可
