def replace_string(str_1: str, str_2: str) -> None:
    '''
    :param str_1: Input string
    :param str_2: Input string
    :return: None
    优先考虑字符串类型自身的 replace 方法，实现对字符串中旧字符的替换，并指定最大替换次数。
    解法二：re.sub 方法
    使用正则匹配的方法，也可以实现对字符串的替换，比如使用 re 模块提供的 sub 方法实现字符串中匹配的字符串替换成想要的字符串，并指定最大替换次数。
    import re
    def replace_string(str_1: str, str_2: str) -> None:
        print(re.sub('\*', 'career', str_1))
        print(re.sub('\*', 'career', str_2, 1))
    '''
    # -- write your code here --
    print(str_1.replace('*', 'career'))
    print(str_2.replace('*', 'career', 1))