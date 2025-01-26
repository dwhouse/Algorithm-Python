def solution(mats, park):
    rs, cs = len(park), len(park[0])
    
    mats.sort(reverse=True) # 큰 돗자리부터
    
    for m in mats:
        if m > rs or m > cs:
            continue # 애초에 공원보다 돗자리가 큼
        
        # (r, c) 를 좌상단 시작점
        for r in range(rs - m + 1):
            for c in range(cs - m + 1):
                is_okay = True
                
                # m * m 검사
                for rr in range(r, r+m):
                    for cc in range(c, c+m):
                        if not park[rr][cc] == "-1":
                            is_okay = False
                            break
                    if not is_okay:
                        break
                
                if is_okay:
                    return m
    return -1
            