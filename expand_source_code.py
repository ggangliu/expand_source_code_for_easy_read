# -*- coding: utf-8 -*-
import os, re

'''
替换源代码中的OS_PROCESS(func_name)，将其替换为函数头的形式void func_name(void)
'''

path = "E:\\00_Source Code\\rrul62b40"
os_process = 'OS_PROCESS('
match_pattern_os = r'OS_PROCESS\((.*?)\)'

test_str = r'OS_PROCESS(XEPP)/*lint -esym(714, XEPP)*/'


def test_modified_line(line_str):
    func_name = re.match(match_pattern_os, line_str)
    if func_name:
        print "old_str: " + line_str
        line_str = line_str.replace("OS_PROCESS({0})".format(func_name.group(1)), "void {0}(void)".format(func_name.group(1)))
        print "new_str: " + line_str


def check_and_modified_file(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()

    with open(file_name, "w") as f_w:
        for line in lines:
            func_name = re.match(match_pattern_os, line)
            if func_name:
                print file_name, line
                line = line.replace("OS_PROCESS({0})".format(func_name.group(1)), "void {0}(void)".format(func_name.group(1)))
                print file_name, line
            f_w.write(line)


def each_file(file_path):
    for parent, dir_names, file_names in os.walk(file_path):
        for file_name in file_names:
            if os.path.splitext(file_name)[1] == '.c' or os.path.splitext(file_name)[1] == '.cc':
                check_and_modified_file(parent + '\\' + file_name)


if __name__ == '__main__':
    each_file(path)
    #test_modified_linetest_str)
