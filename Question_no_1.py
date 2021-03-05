chemicals = ['Amazon', 'Microsoft', 'Google']
symbols = ['I', 'Am', 'cro', 'le', 'abc']

def match_symbol(chemicals, symbols):
    import re
    combined = []
    
    for s in symbols:
        for c in chemicals:
            r = re.search(s, c)
            if r:
                combined.append(re.sub(s, "[{}]".format(s), c))

    return combined		    
    

print match_symbol(chemicals, symbols)