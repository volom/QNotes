"""
Add categories with the script
"""

while True:
    cat = input("input categories with TAB delimiter ")
    with open('categories.txt', 'a') as c:
        c.write(f'{cat}\t')
        
    print(f"Categories {cat} was added successfully")
    
    if cat == '':
        break