def solution(id_list, report, k):
    cnt = {i: 0 for i in id_list}
    ans = {i: 0 for i in id_list}
    
    for r in set(report):
        cnt[r.split()[1]] += 1

    for r in set(report):
        if cnt[r.split()[1]] >= k:
            ans[r.split()[0]] += 1
    return list(ans.values())