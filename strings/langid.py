# _*_codeing: utf-8_*_
# Author: 13516
# Date: 2020/3/3 16:56
# Remark: Determine if it is Chinese, Japanese, Korean, Latin or Numbers


def is_chinese(uchar):
    """
    判断是否是中文字
    :param uchar:
    :return:bool
    """
    if not isinstance(uchar, str):
        uchar = str(uchar)

    if '\u4e00' <= uchar <= '\u9fff':
        return True
    else:
        return False


def is_japanese(uchar):
    """
    判断是否是日文
    :param uchar:
    :return:bool
    """
    if not isinstance(uchar, str):
        uchar = str(uchar)

    if '\u30a0' <= uchar <= '\u30ff' or '\u3040' <= uchar <= '\u309f':
        return True
    else:
        return False


def is_keran(uchar):
    """
    判断是否是韩文
    :param uchar:
    :return:bool
    """
    if not isinstance(uchar, str):
        uchar = str(uchar)

    if '\uac00'<= uchar <= '\ud7ff':
        return True
    else:
        return False


def is_number(uchar):
    """
    判断是否是数字
    :param uchar:
    :return:bool
    """
    if not isinstance(uchar, str):
        uchar = str(uchar)

    if '\u0030' <= uchar <= '\u0039':
        return True
    else:
        return False


def is_alphabet(uchar):
    """
    判断是否是英文字母, 英文I'm中的上飘号还未处理
    :param uchar:
    :return:bool
    """
    if not isinstance(uchar, str):
        uchar = str(uchar)

    if '\u0041' <= uchar <= '\u005a' or '\u0061' <= uchar <= '\u007a':
        return True
    else:
        return False


def is_punctuation(uchar):
    """
    判断是否是CJK的标点符号
    :param uchar:
    :return:bool
    """
    if not isinstance(uchar, str):
        uchar = str(uchar)

    if '\u3000' <= uchar <= '\u303F':
        return True
    else:
        return False


def is_CJK(uchar):
    """
    判断是否是中日韩文字
    :param uchar:
    :return: bool
    """
    if is_chinese(uchar) or is_japanese(uchar) or is_keran(uchar):
        return True
    else:
        return False


def is_sapce(uchar):
    """
    判断是否是空格
    :param ucahr:
    :return: bool
    """
    if not isinstance(uchar, str):
        uchar = str(uchar)

    if uchar == '\u0020' or uchar == "\t":
        return True
    else:
        return False

if __name__ == '__main__':
    aa = "你"
    bb = "당신"
    cc = "あなた"
    dd = 8
    print(is_chinese(aa), "\t", is_chinese(bb), "\t", is_chinese(cc))
    print(is_number(aa), "\t", is_number(bb), "\t", is_number(cc), "\t", is_number(dd))
    print(is_CJK(aa), "\t", is_CJK(bb), "\t", is_CJK(cc), "\t", is_CJK(dd))