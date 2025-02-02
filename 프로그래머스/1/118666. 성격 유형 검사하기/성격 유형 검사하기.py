def solution(survey, choices):
    kakao = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    for s, c in zip(survey, choices):
        if c < 4:  
            kakao[s[0]] += 4 - c
        elif c > 4: 
            kakao[s[1]] += c - 4
    r1 = 'R' if kakao['R'] >= kakao['T'] else 'T'
    r2 = 'C' if kakao['C'] >= kakao['F'] else 'F'
    r3 = 'J' if kakao['J'] >= kakao['M'] else 'M'
    r4 = 'A' if kakao['A'] >= kakao['N'] else 'N'
    return r1+r2+r3+r4
    
    
    
        
        
            
            