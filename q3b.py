def add_binary(a, b):
    a = a[2:]
    b = b[2:]
    
    i = len(a) - 1
    j = len(b) - 1
    carry = 0
    result = ""
    
    
    while i >= 0 or j >= 0 or carry:
        bit_a = 0
        bit_b = 0
        
        if i >= 0:
            bit_a = ord(a[i]) - ord('0')
            i -= 1
        
        if j >= 0:
            bit_b = ord(b[j]) - ord('0')
            j -= 1
        
        total = bit_a + bit_b + carry
        
       
        result = chr((total % 2) + ord('0')) + result
        
        
        carry = total // 2
    
    return "0b" + result