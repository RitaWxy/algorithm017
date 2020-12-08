学习笔记
Trie树: <br>
1. 节点本身不存完整单词
2. 从根节点到某一节点，路径上经过的字符串相连为该节点对应的字符串
3. 每个节点的所有子节点路径代表的字符都不相同

并查集：(组团、配对问题)<br>

def init(p): 
	# for i = 0 .. n: p[i] = i; 
	p = [i for i in range(n)] 
 
def union(self, p, i, j): 
	p1 = self.parent(p, i) 
	p2 = self.parent(p, j) 
	p[p1] = p2 
 
def parent(self, p, i): 
	root = i 
	while p[root] != root: 
		root = p[root] 
	while p[i] != i: # 路径压缩 
		x = i
		i = p[i]
		p[x] = root 
	return root