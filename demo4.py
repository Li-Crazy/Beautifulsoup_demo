'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/4/20 21:41
@Software: PyCharm
@File    : demo4.py
'''
from bs4.element import Tag
from bs4.element import NavigableString
from bs4 import BeautifulSoup
html = """
<table class="tablelist" cellpadding="0" cellspacing="0">
	<tbody>
	    <tr class="h">
		    		<td class="l" width="374">职位名称</td>
		    		<td>职位类别</td>
		    		<td>人数</td>
		    		<td>地点</td>
		    		<td>发布时间</td>
		    	</tr>
		    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=49481&amp;keywords=python&amp;tid=0&amp;lid=0">22989-云计算后台开发工程师</a></td>
					<td>技术类</td>
					<td>2</td>
					<td>深圳</td>
					<td>2019-04-17</td>
		    	</tr>
		    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=49468&amp;keywords=python&amp;tid=0&amp;lid=0">25928-Gcloud游戏云平台后台开发</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-04-17</td>
		    	</tr>
		    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=49471&amp;keywords=python&amp;tid=0&amp;lid=0">25923-大数据运维工程师（深圳）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-04-17</td>
		    	</tr>
		    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=49457&amp;keywords=python&amp;tid=0&amp;lid=0">30359-存储运营开发高级工程师</a></td>
					<td>技术类</td>
					<td>4</td>
					<td>深圳</td>
					<td>2019-04-17</td>
		    	</tr>
		    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=49449&amp;keywords=python&amp;tid=0&amp;lid=0">PCG04-应用分发测试开发工程师（深圳）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-04-17</td>
		    	</tr>
		    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=49442&amp;keywords=python&amp;tid=0&amp;lid=0">31504-云售前架构师</a></td>
					<td>技术类</td>
					<td>2</td>
					<td>深圳</td>
					<td>2019-04-17</td>
		    	</tr>
		    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=49447&amp;keywords=python&amp;tid=0&amp;lid=0">TME-腾讯音乐移动产品质量测试工程师（深圳）</a></td>
					<td>技术类</td>
					<td>3</td>
					<td>深圳</td>
					<td>2019-04-17</td>
		    	</tr>
		    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=49439&amp;keywords=python&amp;tid=0&amp;lid=0">TEG12-web前端开发工程师（深圳）</a></td>
					<td>技术类</td>
					<td>2</td>
					<td>深圳</td>
					<td>2019-04-17</td>
		    	</tr>
		    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=49441&amp;keywords=python&amp;tid=0&amp;lid=0">30628-腾讯广告机器学习平台研究员（研发中心-深圳）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-04-17</td>
		    	</tr>
		    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=49414&amp;keywords=python&amp;tid=0&amp;lid=0">22989-腾讯云DNSPod域名服务PHP/<span>Python</span>开发工程师</a></td>
					<td>技术类</td>
					<td>2</td>
					<td>深圳</td>
					<td>2019-04-17</td>
		    	</tr>
	    </tbody>
</table>
<div>
    文本
</div>
<p>
<!--注释-->
</p>
"""
soup = BeautifulSoup(html,'lxml')
# print(type(soup))
# table = soup.find('table')
# print(type(table))
div = soup.find('div')
print(type(div.string))
p = soup.find('p')
print(p.string)#只返回直接子元素，存在多个子元素无法返回
print(p.contents)#打印所有子元素
print(type(p.contents))
print(type(p.children))
print(type(p.string))