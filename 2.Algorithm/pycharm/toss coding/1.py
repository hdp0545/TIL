from collections import deque

def solution(servers, sticky, requests):
    request_logs = {}
    server_idx_que = deque([i for i in range(servers)])
    list_servers = [[] for _ in range(servers)]
    for idx, request in enumerate(requests):
        if sticky:
            if request in request_logs.keys():
                server_id = request_logs[request]
                server_idx_que.remove(server_id)
            else:
                server_id = server_idx_que.popleft()
                request_logs[request] = server_id
        else:
            server_id = server_idx_que.popleft()
        list_servers[server_id].append(request)
        server_idx_que.append(server_id)
    return list_servers

print(solution(3, True, [12]))
