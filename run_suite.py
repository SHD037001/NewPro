# 创建测试套件
import unittest

suite = unittest.defaultTestLoader.discover("./scripts")

# 运行测试套件
# with open("./report/login{}.html".format(time.strftime("%H_%M_%S")),"wb") as f:
#     HTMLTestRunner(f).run(suite)
unittest.TextTestRunner().run(suite)