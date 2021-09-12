def get_max_occorence(string):
    all_freq = {}
    for i in string:
        if i not in all_freq:
            all_freq[i] = 0 
        all_freq[i] += 1
        
    most_occuerd = max(all_freq, key = all_freq.get) 
    return most_occuerd
    
print(get_max_occorence('xxxaaabbb'))
