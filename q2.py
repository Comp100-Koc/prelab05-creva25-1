def remove_adjacent_duplicates(s):
    result = ""
    
    for ch in s:
        if len(result) > 0 and result[-1] == ch:
            
            result = result[:-1]
        else:
            result += ch
    
    return result