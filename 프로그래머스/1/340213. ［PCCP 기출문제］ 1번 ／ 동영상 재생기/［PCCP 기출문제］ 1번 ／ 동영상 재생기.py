def solution(video_len, pos, op_start, op_end, commands):
    def to_sec(t):
        mm, ss = t.split(':')
        return int(mm)*60 + int(ss)
    
    def to_mmss(s):
        return "{:02d}:{:02d}".format(s // 60, s % 60)
    
    video_len_s, pos_s, op_start_s, op_end_s = map(to_sec, [video_len, pos, op_start, op_end])
    
    if op_start_s <= pos_s <= op_end_s:
        pos_s = op_end_s
    
    for cmd in commands:
        if cmd == "prev":
            new_pos = pos_s - 10
            if new_pos < 0:
                new_pos = 0
        else:
            if video_len_s - pos_s <= 10:
                new_pos = video_len_s
            else:
                new_pos = pos_s + 10
        
        if op_start_s <= new_pos <= op_end_s:
            new_pos = op_end_s
        
        pos_s = new_pos
    
    return to_mmss(pos_s)