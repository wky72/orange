# _*_codeing: utf-8_*_
# Author: 13516
# Date: 2020/3/3 17:38
# Remark:
from strings import langid


def merge_non_block_char(sentence, space=False):
    """
    合并句子中非中日韩文字的字符
    :param sentence:
    :return: list, str; 返回合并后的字符集，返回以\x00分割的句子
    """
    non_cjk_str = ""
    word_list = []
    sentence_splited = ""
    __delimiter = " " if space is True else "\u0000"
    for char in sentence:
        if not langid.is_CJK(char) and not langid.is_sapce(char):
            non_cjk_str += char
        elif langid.is_sapce(char):
            word_list.extend([non_cjk_str, char]) if non_cjk_str != "" else word_list.append(char)
            if non_cjk_str != "":
                sentence_splited = sentence_splited + non_cjk_str + __delimiter + char + __delimiter
            else:
                sentence_splited = sentence_splited + char + __delimiter
            non_cjk_str = ""
        else:
            if "" == non_cjk_str:
                word_list.append(char)
                sentence_splited = sentence_splited + char + __delimiter
            else:
                word_list.extend([non_cjk_str, char])
                sentence_splited = sentence_splited + non_cjk_str + __delimiter + char + __delimiter
                non_cjk_str = ""

    if non_cjk_str != "":
        word_list.append(non_cjk_str)
        sentence_splited = sentence_splited + non_cjk_str

    return word_list, sentence_splited.strip()


if __name__ == '__main__':

    aa = "你好我想听marrson5的歌"
    bb = "hkj知道吗"
    cc = "知不知道小7去哪里了"
    dd = "长官我的编号是08787"
    ee = "你的快递单号是212080对吗"
    ff = "你的工作very good"
    gg = "2个苹果够吃吗"
    hh = "这把枪的型号是AK47"

    # print("aa", merge_non_block_char(aa))
    # print("bb", merge_non_block_char(bb))
    # print("cc", merge_non_block_char(cc))
    # print("dd", merge_non_block_char(dd))
    # print("ee", merge_non_block_char(ee))
    # print("ff", merge_non_block_char(ff))
    # print("gg", merge_non_block_char(gg))
    # print("hh", merge_non_block_char(hh))

    words, sen = merge_non_block_char(ff)
    elems = sen.split("\x00")
    print(words)
    print(sen)
    print(len(sen))
    print(elems)
