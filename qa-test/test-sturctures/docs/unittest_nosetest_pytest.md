
--|unittest | nosetest |pytest
---|---|---|---
免安装 | 是|否|否
命令行 | python -m unittest testFile|nosetests -s -v testFile|pytest testFile
入口函数|runner.run(testSuite()) |不需要|pytest.main(['-s','testFile'])
框架|setup/teardown+suite|通过nose.tools继承自unittest|除setup/teardown以外支持灵活自定义
断言|丰富的assert函数|通过nose.tools集成unittest|简单的assert+条件即可
跳过测试|@unittest.skip\* |from nose.plugins.attrib import atrr辅助支持|@pytest.mark.skip\*辅助支持
预计失败|@unittest.expectedFailure|assert辅助|assert即可
超时机制|第三方库import timeout_decorator|同unittest|pip install pytest-timeout
数据驱动|ddt|ddt|@pytest.mark
测试报告|HTMLTestRunner|pip install nose-htmloutput ； --with-xunit|pip install -U pytest-htmlpy；pytest --junitxml=path；其他插件
多进程|手动|手动|pip install -U pytest-xdist
失败重试|--|nosetests -v --failed|pip install -U pytest-rerunfailures
