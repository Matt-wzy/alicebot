from alicebot.utils import is_config_class


class TestIsConfigClass:
    def test_none(self):
        assert is_config_class(None) is False

    def test_class(self):
        class A:
            pass

        assert is_config_class(A) is False
