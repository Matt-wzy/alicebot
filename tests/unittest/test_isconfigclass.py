from alicebot.utils import is_config_class
from alicebot.config import ConfigModel
from pydantic import BaseModel
import coverage

cov = coverage.Coverage()
cov.start()


class TestIsConfigClass:


    # 边界条件: config_class 是 None
    def test_is_config_class_with_none(self):
        assert is_config_class(None) is False

    # 边界条件: config_class 是一个非类对象
    def test_is_config_class_with_non_class_object(self):
        assert not is_config_class("Not a class")

    # 等价类: config_class 是一个配置类
    def test_is_config_class_with_valid_config_class(self):
        class Config(ConfigModel):
            """测试用配置类。

            """

            __config_name__ = "testconfig"
        assert is_config_class(Config)

    # 等价类: config_class 是一个非配置类
    def test_is_config_class_with_non_config_class(self):
        class NonConfigClass:
            pass

        assert is_config_class(NonConfigClass) is False

    # 等价类: config_class 是一个抽象类
    def test_is_config_class_with_abstract_class1(self):
        from abc import ABC as AbstractBaseClass
        class AbstractClass(ConfigModel, AbstractBaseClass):
            __config_name__ = "AbstractConfig"
        assert is_config_class(AbstractClass) is False

    # 边界条件: config_class 没有复写 __config_name__ 属性，即此属性为 ''.
    def test_is_config_class_with_missing_config_name(self):
        class MissingConfigName(ConfigModel):
            pass
        assert is_config_class(MissingConfigName)

    # 边界条件: config_class 没有 __config_name__ 属性
    def test_is_config_class_with_missing_config_name_2(self):
        class MissingConfigName(BaseModel):
            pass
        assert is_config_class(MissingConfigName) is False

    # 边界条件: config_class 的 __config_name__ 不是字符串
    def test_is_config_class_with_invalid_config_name(self):
        class InvalidConfigName(ConfigModel):
            __config_name__ = 123
        assert is_config_class(InvalidConfigName) is False

    # 边界条件: config_class 的基类包含 ABC
    def test_is_config_class_with_abc_in_bases(self):
        from abc import ABC
        class ABCClass(ConfigModel, ABC):
            __config_name__ = "ABCConfig"
        assert is_config_class(ABCClass) is False


    # # 边界条件: config_class 是一个抽象类
    # def test_is_config_class_with_abstract_class(self):
    #     class AbstractClass(ConfigModel):
    #         __config_name__ = "AbstractConfig"
    #         @classmethod
    #         def __subclasshook__(cls, subclass):
    #             return True
    #     assert not is_config_class(AbstractClass)

cov.stop()
cov.report()
