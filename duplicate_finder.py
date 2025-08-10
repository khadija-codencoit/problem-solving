def find_duplicates(items):
    s = set()
    duplicates = set()

    for item in items:
        if item in s:
            duplicates.add(item)
        else:
            s.add(item)
    if duplicates:
        return list(duplicates)
    else:
        return "No dublicats found"

list1 = [11,8,8,99,99]  

duplicate = find_duplicates(list1)

print("Duplicate Values : ",duplicate)



