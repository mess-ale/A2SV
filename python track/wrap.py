import textwrap

def wrap(string, max_width):
    
    words = []
    for i in range(0, len(string), max_width):
        words.append(string[i: i+max_width])
        
    return "\n".join(words)
        
if __name__ == '__main__':
