### Part Three -- your code goes here. 
def main():
    list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    list = sort_list(list)
    list = remove_reoccurances(list)
    list = add_elements(list, [7,8])
    print (list)

#sorts list
def sort_list(list):
    list.sort()
    return list

#removes any reoccuring elements
def remove_reoccurances(list):
    seen = []
    fixed_list = []
    for _ in list:
        if _ not in seen:
            fixed_list.append(_)
            seen.append(_)
    return fixed_list

#adds requested elements
def add_elements(list, add):
    list.extend(add)
    return list
    
main()