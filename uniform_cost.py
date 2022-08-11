import sys

n_nodes=int(input("Enter the no. of nodes:"))
n_input_nodes=0
graph_dict={}                     #Dict to hold the graph's adjacency data

#Recursive function to input the graph
def get_graph(node):
 global n_input_nodes
 global n_nodes
 n_input_nodes+=1
 nodes_n_weights=input(f"Enter nodes adjacent to {node} with their distance:\n").split()
 i=0
 adj_nodes=[]
 while (i<len(nodes_n_weights)):
  neighbour=(nodes_n_weights[i],int(nodes_n_weights[i+1]))
  adj_nodes.append(neighbour)
  i+=2
 graph_dict[node]=adj_nodes
 for child in graph_dict[node]:
  if(child[0] not in graph_dict.keys()):
   if(n_input_nodes<n_nodes):
    get_graph(child[0])
   else:
    print("Invalid adjacent nodes")
    n_input_nodes-=1
    get_graph(node)
    return
  else:
   continue


#Perform uniform cost search on graph
def uniform_cost_search(start,end):
    
    priority_queue=[[[start],0]]
    while priority_queue:
        priority_queue=sorted(priority_queue,key=lambda x : x[1])
        front=priority_queue.pop(0)
        front_path=front[0]
        curr_node=front_path[-1]
        if(curr_node==end):
            return "Node found.",front
        else:
            for adj_node in graph_dict[curr_node]:
                    updated_cost=front[1]+adj_node[1]
                    priority_queue.append([front_path+[adj_node[0]],updated_cost])
    return "Node not found.",[[],0]

#Function to print the returned path
def print_path(path):
    print("Path:",end="")
    for i in range(0,len(path[0])-1):
        print(path[0][i],end="-")
    print(path[0][-1])
    print(f"Path cost:{path[1]}",end="")


while True:
    ch=int(input("\n1.Enter graph\n2.Find Path\n3.Exit\nEnter your choice"))
    if(ch==1):
        get_graph(input("Enter the first node:"))
    elif(ch==2):    
        start=input("Enter the start node:")
        end=input("Enter the end node:")
        status,path=uniform_cost_search(start,end)
        if(status=="Node found."):
            print(status)
            print_path(path)
        else:
            print(status)
    elif(ch==3):
        sys.exit()
    else:
        print("Invalid Choice")
