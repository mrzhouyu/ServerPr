# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 9:51
# @Author  : YuChou
# @Site    : 
# @File    : conf.py
# @Software: PyCharm
"""
命令配置 供调用
"""
MODE1_SEND = b"\x5A\xFF\xFF\x08\xA4\x7E\x3C\xB0\xA3\x63\x63\x6D\x64\x5A\xFF\xFF\x08\x29\x69\x73\x63\x65\x6E\x65\x43\x6F\x5A\xFF\xFF\x08\x4A\x6E\x66\x63\x6D\x69\x64\x64\x75\x5A\xFF\xFF\x08\x54\x75\x69\x64\x69\x73\x63\x65\x6E\x5A\xFF\xFF\x08\x3F\x65\x4D\x6F\x64\x65\x00\xD7\x7E"
MODE_ACK = b"\x5A\x01\xFF\x08\xA5\x7E\x3C\xB0\xA4\x63\x63\x6D\x64\x5A\x01\xFF\x08\x2D\x65\x72\x43\x6F\x6E\x66\x63\x6D\x5A\x01\xFF\x08\x4C\x69\x64\x64\x75\x75\x69\x64\x64\x5A\x01\xFF\x08\xE9\x72\x65\x73\x70\x00\x62\x69\x64\x5A\x01\xFF\x03\x07\x00\x89\x7E"

MODE2_SEND =b"\x5A\xFF\xFF\x08\xA4\x7E\x3C\xB0\xA3\x63\x63\x6D\x64\x5A\xFF\xFF\x08\x29\x69\x73\x63\x65\x6E\x65\x43\x6F\x5A\xFF\xFF\x08\x4A\x6E\x66\x63\x6D\x69\x64\x64\x75\x5A\xFF\xFF\x08\x54\x75\x69\x64\x69\x73\x63\x65\x6E\x5A\xFF\xFF\x08\x41\x65\x4D\x6F\x64\x65\x01\xD8\x7E"

MODE3_SEND =b"\x5A\xFF\xFF\x08\xA4\x7E\x3C\xB0\xA3\x63\x63\x6D\x64\x5A\xFF\xFF\x08\x29\x69\x73\x63\x65\x6E\x65\x43\x6F\x5A\xFF\xFF\x08\x4A\x6E\x66\x63\x6D\x69\x64\x64\x75\x5A\xFF\xFF\x08\x54\x75\x69\x64\x69\x73\x63\x65\x6E\x5A\xFF\xFF\x08\x43\x65\x4D\x6F\x64\x65\x02\xD9\x7E"

MODE4_SEND =b"\x5A\xFF\xFF\x08\xA4\x7E\x3C\xB0\xA3\x63\x63\x6D\x64\x5A\xFF\xFF\x08\x29\x69\x73\x63\x65\x6E\x65\x43\x6F\x5A\xFF\xFF\x08\x4A\x6E\x66\x63\x6D\x69\x64\x64\x75\x5A\xFF\xFF\x08\x54\x75\x69\x64\x69\x73\x63\x65\x6E\x5A\xFF\xFF\x08\x45\x65\x4D\x6F\x64\x65\x03\xDA\x7E"

MODE5_SEND = b"\x5A\xFF\xFF\x08\xA4\x7E\x3C\xB0\xA3\x63\x63\x6D\x64\x5A\xFF\xFF\x08\x29\x69\x73\x63\x65\x6E\x65\x43\x6F\x5A\xFF\xFF\x08\x4A\x6E\x66\x63\x6D\x69\x64\x64\x75\x5A\xFF\xFF\x08\x54\x75\x69\x64\x69\x73\x63\x65\x6E\x5A\xFF\xFF\x08\x47\x65\x4D\x6F\x64\x65\x04\xDB\x7E"

MODE6_SEND = b"\x5A\xFF\xFF\x08\xA4\x7E\x3C\xB0\xA3\x63\x63\x6D\x64\x5A\xFF\xFF\x08\x29\x69\x73\x63\x65\x6E\x65\x43\x6F\x5A\xFF\xFF\x08\x4A\x6E\x66\x63\x6D\x69\x64\x64\x75\x5A\xFF\xFF\x08\x54\x75\x69\x64\x69\x73\x63\x65\x6E\x5A\xFF\xFF\x08\x49\x65\x4D\x6F\x64\x65\x05\xDC\x7E"

MODE7_SEND = b"\x5A\xFF\xFF\x08\xA4\x7E\x3C\xB0\xA3\x63\x63\x6D\x64\x5A\xFF\xFF\x08\x29\x69\x73\x63\x65\x6E\x65\x43\x6F\x5A\xFF\xFF\x08\x4A\x6E\x66\x63\x6D\x69\x64\x64\x75\x5A\xFF\xFF\x08\x54\x75\x69\x64\x69\x73\x63\x65\x6E\x5A\xFF\xFF\x08\x4B\x65\x4D\x6F\x64\x65\x06\xDD\x7E"

MODE8_SEND = b"\x5A\xFF\xFF\x08\xA4\x7E\x3C\xB0\xA3\x63\x63\x6D\x64\x5A\xFF\xFF\x08\x29\x69\x73\x63\x65\x6E\x65\x43\x6F\x5A\xFF\xFF\x08\x4A\x6E\x66\x63\x6D\x69\x64\x64\x75\x5A\xFF\xFF\x08\x54\x75\x69\x64\x69\x73\x63\x65\x6E\x5A\xFF\xFF\x08\x4D\x65\x4D\x6F\x64\x65\x07\xDE\x7E"

MODE9_SEND = b"\x5A\xFF\xFF\x08\xA4\x7E\x3C\xB0\xA3\x63\x63\x6D\x64\x5A\xFF\xFF\x08\x29\x69\x73\x63\x65\x6E\x65\x43\x6F\x5A\xFF\xFF\x08\x4A\x6E\x66\x63\x6D\x69\x64\x64\x75\x5A\xFF\xFF\x08\x54\x75\x69\x64\x69\x73\x63\x65\x6E\x5A\xFF\xFF\x08\x4F\x65\x4D\x6F\x64\x65\x08\xDF\x7E"

MODE10_SEND = b"\x5A\xFF\xFF\x08\xA4\x7E\x3C\xB0\xA3\x63\x63\x6D\x64\x5A\xFF\xFF\x08\x29\x69\x73\x63\x65\x6E\x65\x43\x6F\x5A\xFF\xFF\x08\x4A\x6E\x66\x63\x6D\x69\x64\x64\x75\x5A\xFF\xFF\x08\x54\x75\x69\x64\x69\x73\x63\x65\x6E\x5A\xFF\xFF\x08\x51\x65\x4D\x6F\x64\x65\x09\xE0\x7E"

MODE11_SEND = b"\x5A\xFF\xFF\x08\xA4\x7E\x3C\xB0\xA3\x63\x63\x6D\x64\x5A\xFF\xFF\x08\x29\x69\x73\x63\x65\x6E\x65\x43\x6F\x5A\xFF\xFF\x08\x4A\x6E\x66\x63\x6D\x69\x64\x64\x75\x5A\xFF\xFF\x08\x54\x75\x69\x64\x69\x73\x63\x65\x6E\x5A\xFF\xFF\x08\x53\x65\x4D\x6F\x64\x65\x0A\xE1\x7E"
