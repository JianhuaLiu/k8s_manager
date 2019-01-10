# -*- coding: utf-8 -*-

STATUS_VALUE = (
    (1,'上架'),
    (2,'下架'),
    (3,'在线'),
    (4,'离线'),
)

TYPE_VALUE = (
    (1,'内部服务器'),
    (2,'内部虚拟机'),
    (3,'阿里云'),
    (4,'腾讯云'),
    (5,'交换机'),
    (6,'防火墙'),
)

type_list = map(lambda x: x[1], TYPE_VALUE)
status_list = map(lambda x: x[1], STATUS_VALUE)


VERSION_STATUS_VALUE = (    
    (1,'需求收集'),
    (2,'需求评审'),
    (3,'立项'),
    (4,'排期'),
    (5,'开发'),
    (6,'测试'),
    (7,'安全测试'),
    (8,'发布'),
    (9,'验收'),
)

version_status_list = map(lambda x: x[1], VERSION_STATUS_VALUE)