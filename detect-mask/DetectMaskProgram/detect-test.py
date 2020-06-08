#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/17 10:59
# @Author  : legend
import jpype


class GetJarClass(object):
    def start_JVM(self):
        # 路径为相对路径，或者写绝对路径
        jars = ["./datamasking.jar"]
        # 获得系统的jvm路径
        jvm_path = jpype.getDefaultJVMPath()
        # jvm参数
        jvm_cp = "-Djava.class.path={}".format(":".join(jars))
        # 启动虚拟机
        jpype.startJVM(jvm_path, jvm_cp)

    def shutdown_JVM(self):
        # 关闭jvm
        jpype.shutdownJVM()

    def Detect(self):
        # 使用JAVA字节码中定义的类(detect)为FinderEngine的对应package地址
        finder_engine_class = jpype.JClass("detect.FinderEngine")
        # 实例化对象
        finder_engine = finder_engine_class()
        return finder_engine

    def Mask(self):
        # public MaskFactory(){
        #     this(new FinderEngine());
        # }
        mask_factory_class = jpype.JClass("mask.MaskFactory")
        # 实例化maskfactory
        mask_factory = mask_factory_class()
        return mask_factory


if __name__ == "__main__":
    details = "Here is my id : finder@test.com and my machine info:124.234.223.12 , ok ?"
    # 实例化class
    get_class = GetJarClass()
    start_jvm = get_class.start_JVM()
    if jpype.isJVMStarted():
        print("jvm is start")
    detect = get_class.Detect()
    result = detect.find(details).getMatches()
    print(result)
    mask = get_class.Mask()
    masker = mask.getMasker()
    result2 = masker.mask(details)
    print(result2)
    shutdown_jvm = get_class.shutdown_JVM()
