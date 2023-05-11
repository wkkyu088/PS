def solution(s):
    words = s.split(" ")
    
    for i, w in enumerate(words):
        if len(w) > 1:
            words[i] = w[0].upper()+w[1:].lower()
        else:
            words[i] = w.upper()
    
    return " ".join(words)