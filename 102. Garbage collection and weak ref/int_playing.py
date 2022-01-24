import gc
import sys


class ObjClass:
    name = "str"


if __name__ == '__main__':
    x = 300
    y = 300
    # print(id(x))  # 2789489229104
    # print(id(y))  # 2789489229104
    # print(x == y)  # True
    # so in result 300's ref count is 2
    #
    # NOTE THAT IN REPL it will result in false and each var would be different
    print(len(gc.get_referrers(y)))

    obj_class_i = ObjClass()
    print(len(gc.get_referrers(obj_class_i)))
    # playing with sys ref count
    print("playing with sys ref count")
    print(sys.getrefcount(obj_class_i))  # will increase per one and decrease after going out of scope
    print(sys.getrefcount(obj_class_i))
    print(sys.getrefcount(obj_class_i))
