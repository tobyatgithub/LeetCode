from Reverse_Integer import Solution


def test_import():
    assert Solution()


def test1():
    assert Solution().reverse(123) == 321


def test2():
    assert Solution().reverse(-123) == -321


def test3():
    assert Solution().reverse(120) == 21

def test4():
    assert Solution().reverse(0) == 0


