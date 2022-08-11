n_nodes=int(input("Enter the no. of nodes:"))
n_input_nodes=0
nodes_status={}                   #Dict to indicate if nodes have been visited
graph_dict={}                     #Dict to hold the graph's adjacency data

#Recursive function to input the graph
def get_graph(node):
 global n_input_nodes
 global n_nodes
 n_input_nodes+=1
 nodes_status[node]=False
 graph_dict[node]=input(f"Enter nodes adjacent to {node}:\n").split()
 for child in graph_dict[node]:
  if(child not in graph_dict.keys()):
   if(n_input_nodes<n_nodes):
    get_graph(child)
   else:
    print("Invalid adjacent nodes")
    n_input_nodes-=1
    get_graph(node)
    return
  else:
   continue

#Breadth First Search
def bfs(start,end):
    queue=[start]
    nodes_status[start]=True
    while queue:
        curr_node=queue.pop(0)
        if(curr_node==end):
            print(curr_node,end="")
            return "\n Node found."
        else:
            print(curr_node,end="-")
            for child in graph_dict[curr_node]:
                if(nodes_status[child]==False):
                    queue.append(child)
                    nodes_status[child]=True
    return "\n Node not found."

#Depth First Search
def dfs(start,end):
    stack=[start]
    nodes_status[start]=True
    while stack:
        curr_node=stack.pop()
        if(curr_node==end):
            print(curr_node,end="")
            return "\nNode found."
        else:
            print(curr_node,end="-")
            adj_nodes=reversed(graph_dict[curr_node])
            for node in adj_nodes:
                if(nodes_status[node]==False):
                    stack.append(node)
                    nodes_status[node]=True
    return "\nNode not found."

#Resets the status of all nodes
def reset_dict():
    for key in nodes_status.keys():
        nodes_status[key]=False

#n_input_nodes=0                 #Count to indicate the no. of inputted nodes
first_node=input("Enter the first node :")
get_graph(first_node)
start=input("Enter the start node:")
end=input("Enter the end node:")
ch=0
while(ch!=3):
    ch=int(input("\n1.Breadth-First-Search\n2.Depth-First-Search\n3.Exit\nEnter your choice:"))
    if(ch==1):
        print("BFS:",end="")    
        print(bfs(start,end))
        reset_dict()
    elif(ch==2):
        print("DFS:",end="")
        print(dfs(start,end))
    else:
        print("Invalid choice")
