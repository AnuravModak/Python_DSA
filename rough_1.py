class graph:











if __name__ == '__main__':
    routes=[
        ("mumbai","paris"),
        ("mumbai","dubai"),
        ("paris","new york"),
        ("dubai","new york"),
        ("new york","toronto")
    ]
    # so first step is to make adjacency list
    adj_list={}
    for i in routes:
        if i[0] in adj_list:
            adj_list[i[0]].append(i[1])
        else:
            adj_list[i[0]]=[i[1]]
    print(adj_list)