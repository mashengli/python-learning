#!/usr/bin/env python
# -*- coding: utf-8 -*-
#encoding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
print '-------学习变量与运算符'
numa = 100.0
print 'numa=', numa
numb = 3
print 'numb=', numb

print 'numa/numb=',numa/numb
print '\n---------学习赋值' 
chara = 'abc'
print 'chara=',chara
charb = chara
print 'chara=charb=',charb
chara = 'xyz'
print 'chara=',chara
print 'charb=',charb

print '\n-----------学习编码'
codea = '中文'
print 'codea=',codea,',len(codea"utf-8")=',len(codea)
codea.decode('utf-8').encode('gbk')
print 'len(codea"gbk")=',len(codea)

print '\n--------学习占位'
posa = '马胜利'
posb = 100000000
print '%s你好！您的账户余额仅剩 %d元，请及时充值'%(posa,posb)

print '\n---------学习list and tuple'
arraya = [100, 200, 300]
print 'arraya=',arraya
print 'arraya[0]=',arraya[0]
print 'arraya[-1]=',arraya[-1]
arraya.append('400')
print 'arraya.append("400")=',arraya
print 'arraya[0] + arraya[1]=', arraya[0]+arraya[1]
print 'arraya[0] + arraya[-1]=%s' % arraya[0]+arraya[-1]
arraya.pop()
print 'arraya.pop()=',arraya
arrayb = ['arrayb',500]
arraya[-1] = arrayb
print 'arrayb=',arrayb
print 'arraya[-1]=arrayb,arraya=', arraya
print 'arraya[2,1]=',arraya[2][1]
print 'len(arraya)=',len(arraya)
print 'len(arrayb)=',len(arrayb)

tuplea = (100,200,[300,400])
print 'tuplea=', tuplea
tuplea[2][0] = 200
tuplea[2][1] = 100
print 'tuplea=',tuplea

if len(tuplea) >= 3:
	print 'len(tuplea)>3'
else:
	print 'len(tuplea)<3'
	
print '----------学习循环'
print '遍历tuplea'
for ele in tuplea:
	print ele
tupleb = tuplea[-1];
for ele in tupleb:
	print ele
print '快速生成数组range()函数'
arraya = range(5)
print 'arraya=range(10)=',arraya

print 'while 循环'
n = len(arraya)
i = 0
while i < n:
	print 'arraya[%d]=' % i,arraya[i]
	i = i + 1
	
print '---------学习dict和set'
dic1 = {"a":1,"b":2}
print 'dic1=', dic1
print 'dic1["a"]=',dic1["a"]
dic2 = {1:1,2:2}
print 'dic2=', dic2
print 'dic2[1]=',dic2[1]
if dic2.get(1):
	print 'dic2[1] exists'
else:
	print 'dic2[1] not exists'
if not dic2.get(3):
	print 'dic2[3] not exists'
else:
	print 'dic[3] exists'

print '---------学习函数'
def sum(range):
	if not isinstance(range, (int)):
		raise TypeError('类型错误异常')
	if range < 0:
		raise RuntimeWarning('范围错误')
		return 0
	sum = 0
	i = 0
	while i <= range:
		sum = sum + i
		i = i + 1
	return sum
print '定义函数sum(range)累加求和，sum(10)=', sum(10)
#print '定义函数sum(range)累加求和，sum(-1)=', sum(-1)
#print '定义函数sum(range)累加求和，sum("a")=', sum('a')
