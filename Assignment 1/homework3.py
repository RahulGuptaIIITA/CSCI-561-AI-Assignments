#Breadth-first-search
def bfs(graph, start_state, end_state, places, inv_places, path_order, outputFile):
	queue = list()
	explored = list()
	paths = list()
	buff = list()
	queue.append(start_state)
	paths.append([start_state])

	while(1):
		if len(queue)==0:
			break
		current_node = queue[0]
		current_path = paths[0]
		del queue[0]
		del paths[0]
		explored.append(current_node)
		if current_node == end_state:
			file = open(outputFile, 'w')
			cost = 0
			flag=0
			for ele in current_path:
				if flag==0:
					file.write(str(ele) + " " + str(cost))
					flag=1
				else:
					file.write("\n" + str(ele) + " " + str(cost))
				cost += 1
			file.close()
			break
		else:
			for i in range(len(places)):
				if graph[places[current_node]][i]!=0:
					if (inv_places[i] not in queue) and (inv_places[i] not in explored):
						mini_path = current_node + " " + inv_places[i]
						current_path.append(inv_places[i])
						buff.append(tuple((path_order[mini_path], inv_places[i], list(current_path))))
						del current_path[-1]
			if len(buff)!=0:
				buff = sorted(buff)
				while len(buff)!=0:
					queue.append(buff[0][1])
					paths.append(list(buff[0][2]))
					del buff[0]

#Depth-first search
def dfs(graph, start_state, end_state, places, path_order, outputFile):
	stack = list()
	explored = list()
	paths = list()
	buff = list()
	stack.append(start_state)
	paths.append([start_state])

	while(1):
		if len(stack)==0:
			break
		current_node = stack[-1]
		current_path = paths[-1]
		del stack[-1]
		del paths[-1]
		explored.append(current_node)
		if current_node == end_state:
			file = open(outputFile, 'w')
			cost = 0
			flag=0
			for ele in current_path:
				if flag==0:
					file.write(str(ele) + " " + str(cost))
					flag=1
				else:
					file.write("\n" + str(ele) + " " + str(cost))
				cost += 1
			file.close()
			break
		else:
			for i in range(len(places)):
				if graph[places[current_node]][i]!=0:
					if (inv_places[i] not in stack) and (inv_places[i] not in explored):
						mini_path = current_node + " " + inv_places[i]
						current_path.append(inv_places[i])
						buff.append(tuple((path_order[mini_path], inv_places[i], list(current_path))))
						del current_path[-1]
			if len(buff)!=0:	
				buff = sorted(buff)
				while len(buff)!=0:
					stack.append(buff[-1][1])
					paths.append(list(buff[-1][2]))
					del buff[-1]

#Uniform cost search
def ucs(graph, start_state, end_state, places, path_order, outputFile):
	priority_q = list()
	explored = list()
	buff = list()
	time_of_entry = 1

	#Cost, Time of entry, Path 
	priority_q.append(tuple((0, 0, str(start_state)+ " " + str(0)+" ",)))

	while(1):
		if len(priority_q)==0:
			break

		current_node = priority_q[0][2].strip().split()[-2]
		current_path = priority_q[0][2]
		current_cost = priority_q[0][0]
		del priority_q[0]
		q_nodes = [x[2].strip().split()[-2] for x in priority_q]
		explored_nodes = [x[0] for x in explored]

		if current_node == end_state:
			file = open(outputFile, 'w')
			flag=0
			unravelled_path = current_path.strip().split()
			for i in range(0, len(unravelled_path), 2):
				if flag==0:
					file.write(str(unravelled_path[i]) + " " + str(unravelled_path[i+1]))
					flag = 1
				else:
					file.write("\n" + str(unravelled_path[i]) + " " + str(unravelled_path[i+1]))
			file.close()
			break
		else:
			for i in range(len(places)):
				if graph[places[current_node]][i]!=0:
					temp_cost = current_cost + int(graph[places[current_node]][i])
					mini_path = current_node + " " + inv_places[i]
					if (inv_places[i] not in q_nodes) and (inv_places[i] not in explored_nodes):
						buff.append(tuple((temp_cost, path_order[mini_path], current_path+str(inv_places[i])+" "+str(temp_cost)+" ",)))
					elif inv_places[i] in q_nodes:
						if temp_cost < (priority_q[q_nodes.index(inv_places[i])][0]):
							buff.append(tuple((temp_cost, path_order[mini_path], current_path+str(inv_places[i])+" "+str(temp_cost)+" ",)))
							del priority_q[q_nodes.index(inv_places[i])]
							del q_nodes[q_nodes.index(inv_places[i])]
					elif inv_places[i] in explored_nodes:
						if temp_cost < (explored[explored_nodes.index(inv_places[i])][1]):
							buff.append(tuple((temp_cost, path_order[mini_path], current_path+str(inv_places[i])+" "+str(temp_cost)+" ",)))
							del explored[explored_nodes.index(inv_places[i])]
							del explored_nodes[explored_nodes.index(inv_places[i])]
			
			if len(buff)!=0:
				buff = sorted(buff)
				priority_q.append(tuple((buff[0][0], time_of_entry, buff[0][2])))
				time_of_entry += 1
				del buff[0]
				while len(buff)!=0:
					priority_q.append(tuple((buff[0][0], time_of_entry, buff[0][2])))
					time_of_entry += 1
					del buff[0]

		explored.append(tuple((current_node, current_cost)));
		priority_q = sorted(priority_q)


def astar(graph, start_state, end_state, places, path_order, sunday_times, outputFile):
	priority_q = list()
	explored = list()
	buff = list()
	time_of_entry = 1

	#Cost, Time of entry, Path 
	priority_q.append(tuple((int(sunday_times[start_state]), 0, str(start_state)+" "+str(0)+" ",)))

	while(1):
		if len(priority_q)==0:
			break

		current_node = priority_q[0][2].strip().split()[-2]
		current_path = priority_q[0][2]
		current_cost = int(priority_q[0][2].strip().split()[-1])
		current_hcost = priority_q[0][0]
		del priority_q[0]
		q_nodes = [x[2].strip().split()[-2] for x in priority_q]
		explored_nodes = [x[0] for x in explored]

		if current_node == end_state:
			file = open(outputFile, 'w')
			flag=0
			unravelled_path = current_path.strip().split()
			for i in range(0, len(unravelled_path), 2):
				if flag==0:
					file.write(str(unravelled_path[i]) + " " + str(unravelled_path[i+1]))
					flag = 1
				else:
					file.write("\n" + str(unravelled_path[i]) + " " + str(unravelled_path[i+1]))
			file.close()
			break
		else:
			for i in range(len(places)):
				if graph[places[current_node]][i]!=0:
					temp_cost = current_cost + int(graph[places[current_node]][i])
					mini_path = current_node + " " + inv_places[i]
					if (inv_places[i] not in q_nodes) and (inv_places[i] not in explored_nodes):
						buff.append(tuple((temp_cost + int(sunday_times[inv_places[i]]), path_order[mini_path], current_path+str(inv_places[i])+" "+str(temp_cost)+" ",)))
					elif inv_places[i] in q_nodes:
						if (temp_cost + int(sunday_times[inv_places[i]])) < (priority_q[q_nodes.index(inv_places[i])][0]):
							buff.append(tuple((temp_cost + int(sunday_times[inv_places[i]]), path_order[mini_path], current_path+str(inv_places[i])+" "+str(temp_cost)+" ",)))
							del priority_q[q_nodes.index(inv_places[i])]
							del q_nodes[q_nodes.index(inv_places[i])]
					elif inv_places[i] in explored_nodes:
						if (temp_cost + int(sunday_times[inv_places[i]])) < (explored[explored_nodes.index(inv_places[i])][1]):
							buff.append(tuple((temp_cost + int(sunday_times[inv_places[i]]), path_order[mini_path], current_path+str(inv_places[i])+" "+str(temp_cost)+" ",)))
							del explored[explored_nodes.index(inv_places[i])]
							del explored_nodes[explored_nodes.index(inv_places[i])]
			
			if len(buff)!=0:
				buff = sorted(buff)
				priority_q.append(tuple((buff[0][0], time_of_entry, buff[0][2])))
				time_of_entry += 1
				del buff[0]
				while len(buff)!=0:
					priority_q.append(tuple((buff[0][0], time_of_entry, buff[0][2])))
					time_of_entry += 1
					del buff[0]

		explored.append(tuple((current_node, current_hcost)));
		priority_q = sorted(priority_q)

#Main program
inputFile = 'input.txt'
outputFile = 'output.txt'

info = list()

#Maps places to order
places = dict()

#Maps order to places
inv_places = dict()

#Maps paths to order
path_order = dict()

sunday_times = dict()
place_num = 0
path_num = 0

with open(inputFile) as f:
	for line in f.readlines():
		info.append(line.strip())

algorithm = info[0]
start_state = info[1]
end_state = info[2]

#Building the graph
for i in range(4, int(info[3])+4):
	line = info[i].strip().split()
	if places.get(line[0], -1)==-1:
		places[line[0]] = place_num
		inv_places[place_num] = line[0]
		place_num += 1
	if places.get(line[1], -1)==-1:
		places[line[1]] = place_num
		inv_places[place_num] = line[1]
		place_num += 1

	mini_path_entry = " ".join(info[i].strip().split()[0:2])
	if path_order.get(mini_path_entry, -1)==-1:
		path_order[mini_path_entry] = path_num;
		path_num += 1

#Create adjacency graph
graph = [[0 for i in range(len(places))] for j in range(len(places))]
for i in range(4, int(info[3])+4):
	line = info[i].strip().split()
	graph[places[line[0]]][places[line[1]]] = line[2]

#Sunday times
for i in range(int(info[3])+5, len(info)):
	line = info[i].strip().split()
	sunday_times[line[0]] = line[1]

if info[0]=='BFS':
	bfs(graph, start_state, end_state, places, inv_places, path_order, outputFile)
elif info[0]=='DFS':
	dfs(graph, start_state, end_state, places, path_order, outputFile)
elif info[0]=='UCS':
	ucs(graph, start_state, end_state, places, path_order, outputFile)
elif info[0]=='A*':
	astar(graph, start_state, end_state, places, path_order, sunday_times, outputFile)
