with open("input.txt", 'r') as input_file:
    lines = input_file.readlines()
    for line in lines:
        tokens = line.strip().split()
        u = tokens[1]
        flow_rate = tokens[4][5:-1]
        vs = tokens[9:]
        n = len(vs)
        for i in range(n):
            if vs[i][-1] == ',':
                vs[i] = vs[i][:-1]
        print(u, flow_rate)
        print(n, ' '.join(vs))