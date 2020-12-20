# -*-coding:utf-8-*-
import functools
import os
import random
import time


def time_stamp():
    time_now = time.strftime('%Y%m%d%H%M%S', time.localtime())
    return str(time_now)


def random_phone():
    pre_list = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
                "147", "150", "151", "152", "153", "155", "156", "157", "158", "159",
                "186", "187", "188", "189"]
    phone_num = random.choice(pre_list) + "".join(random.choice("0123456789") for i in range(8))
    return str(phone_num)
