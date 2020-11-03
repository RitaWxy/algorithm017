<<<<<<< HEAD
学习笔记 
1、BFS:
=======
学习笔记 <br>
1、BFS:<br>
>>>>>>> 3c684b4150a9e471e22a9a7207b1374f3e94a777
def BFS(graph, start, end):

    visited = set()
	queue = [] 
	queue.append([start]) 
	
	while queue: 
		node = queue.pop() 
		visited.add(node)
		
		process(node) 
		nodes = generate_related_nodes(node) 
		queue.push(nodes)
		
	# other processing work 
	...
	
2、DFS
# 非递归
def DFS(self, tree): 

	if tree.root is None: 
		return [] 455

	visited, stack = [], [tree.root]

	while stack: 
		node = stack.pop() 
		visited.add(node)

		process (node) 
		nodes = generate_related_nodes(node) 
		stack.push(nodes) 

	# other processing work 
	...
# 递归
visited = set() 

def dfs(node, visited):

    if node in visited: # terminator
    	# already visited
    	return 

	visited.add(node) 

	# process current node here. 
	...
	for next_node in node.children(): 
		if next_node not in visited: 
			dfs(next_node, visited)
			
3、二分查找<br>
前提：目标函数单调性（有序），存在上下界，能够通过索引访问
left,right = 0,len(array)-1<br>
while left <= right:
    mid = (left+right)/2
    if mid == target:
        # find target
        break or return
    elif array[mid] < target:
        left = mid+1
    else: right = mid -1


	
