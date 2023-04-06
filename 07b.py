from collections import defaultdict

graph = [[[], []] for _ in range(10**4)]  # children, content sizes
parent = [-1 for _ in range(10**4)]
dir_name_to_node_numbers = defaultdict(lambda: [])

dir_name_to_node_numbers["/"] = [0]
node_number = 1
current_node = 0

answer = 10**10


def dfs(u: int, min_to_delete: int) -> int:
    global answer
    current = sum(graph[u][1])
    for v in graph[u][0]:
        current += dfs(v, min_to_delete)
    if answer >= current >= min_to_delete:
        answer = current
    return current


with open("input.txt", "r") as input_file:
    lines = input_file.readlines()
    for line in lines:
        if line[0] == "$":
            args = line.strip().split()
            if args[1] == "ls":
                continue
            else:
                if args[2] == "/":
                    current_node = 0
                elif args[2] == "..":
                    current_node = parent[current_node]
                else:
                    for u in dir_name_to_node_numbers[args[2]]:
                        if u in graph[current_node][0]:
                            current_node = u
                            break
        else:
            tokens = line.strip().split()
            if tokens[0] == "dir":
                dir_name = tokens[1]
                graph[current_node][0].append(node_number)
                parent[node_number] = current_node
                dir_name_to_node_numbers[dir_name].append(node_number)
                node_number += 1
            else:
                graph[current_node][1].append(int(tokens[0]))
    total = dfs(0, 10**10)
    unused = 7 * 10**7 - total
    min_to_delete = 3 * 10**7 - unused
    _ = dfs(0, min_to_delete)
    print(answer)
