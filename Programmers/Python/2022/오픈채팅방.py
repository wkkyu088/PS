def solution(record):
    cmd = []
    result = []
    for r in record:
        cmd.append(r.split())
        
    users = {}
    for c in cmd:
        if c[0] == 'Enter':
            users[c[1]] = c[2]
        elif c[0] == 'Change':
            users[c[1]] = c[2]
    
    for c in cmd:
        if c[0] == 'Enter':
            result.append(users[c[1]] + "님이 들어왔습니다.")
        elif c[0] == 'Leave':
            result.append(users[c[1]] + "님이 나갔습니다.")
    return result

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))