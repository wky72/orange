# coding=utf-8
# Author: 13516
# Date: 2020/3/26 12:56
# Remark:

# -*- coding: cp936 -*-


def B2Q(uchar):
    """单个字符 半角转全角"""
    inside_code = ord(uchar)
    if inside_code < 0x0020 or inside_code > 0x7e: # 不是半角字符就返回原来的字符
        return uchar
    if inside_code == 0x0020: # 除了空格其他的全角半角的公式为: 半角 = 全角 - 0xfee0
        inside_code = 0x3000
    else:
        inside_code += 0xfee0
    return chr(inside_code)


def Q2B(uchar):
    """单个字符 全角转半角"""
    inside_code = ord(uchar)
    if inside_code == 0x3000:
        inside_code = 0x0020
    else:
        inside_code -= 0xfee0
    if inside_code < 0x0020 or inside_code > 0x7e: #转完之后不是半角字符返回原来的字符
        return uchar
    return chr(inside_code)


def string_full2half(ustring):
    """
    句子级全半角转换
    :param ustring:
    :return:
    """
    return ''.join([Q2B(uchar) for uchar in ustring])


def string_half2full(ustring):
    """
    句子级半全角转换
    :param ustring:
    :return:
    """
    return ''.join([B2Q(uchar) for uchar in ustring])


def string_full2half_lower(ustring):
    return ''.join([Q2B(uchar).lower() for uchar in ustring])


def string_half2full_lower(ustring):
    return ''.join([B2Q(uchar).lower() for uchar in ustring])


if __name__ == '__main__':
    full_ss = "ｍｎ123aBc博客园"
    half_ss = string_full2half_lower(full_ss)
    print(half_ss)
    full_ss_converted = string_half2full_lower(half_ss)
    print(full_ss_converted)

