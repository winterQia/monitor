#!/usr/bin/python
# -*- coding: utf-8 -*-
# auther: qianxd
# date: 2019/3/2022:49 
from elasticsearch import Elasticsearch
es = Elasticsearch([{'host':'192.168.200.178','port':9200}])
es.index(index='logs-2019.03.20',q='message')
print es.index