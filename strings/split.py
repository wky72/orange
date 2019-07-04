# coding=utf-8
import re


def my_split(string):
    """
    中文拆句
    将引号内看作整体保存与队列，后面再换回
    省略号暂时不加
    # todo 可以考虑说话部分的分句，
    # 例如‘xxx：“xxx。”xx，xxxx。’
    # 还可分。
    """
    SPLIT_SIGN = '%%%%'  # 需要保证字符串内本身没有这个分隔符

    # 替换的符号用: $PACK$
    SIGN = '$PACK$'
    search_pattern = re.compile('\$PACK\$')
    pack_pattern = re.compile('(“.+?”|（.+?）|《.+?》|〈.+?〉|[.+?]|【.+?】|‘.+?’|「.+?」|『.+?』|".+?"|\'.+?\')')
    # pack_queue = []
    pack_queue = re.findall(pack_pattern, string)
    string = re.sub(pack_pattern, SIGN, string)

    pattern = re.compile('(?<=[。？！])(?![。？！])')
    result = []
    while string != '':
        s = re.search(pattern, string)
        if s is None:
            result.append(string)
            break
        loc = s.span()[0]
        result.append(string[:loc])
        string = string[loc:]

    result_string = SPLIT_SIGN.join(result)
    while pack_queue:
        pack = pack_queue.pop(0)
        loc = re.search(search_pattern, result_string).span()
        result_string = result_string[:loc[0]] + pack + result_string[loc[1]:]

    return result_string.split(SPLIT_SIGN)