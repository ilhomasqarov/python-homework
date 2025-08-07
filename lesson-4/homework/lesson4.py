
sales = {"Alice": 350, "Bob": 200, "Charlie": 400, "Diana": 250}
asc_sorted = dict(sorted(sales.items(), key=lambda x: x[1]))
desc_sorted = dict(sorted(sales.items(), key=lambda x: x[1], reverse=True))
print("Ascending:", asc_sorted)
print("   Descending:", desc_sorted)


inventory = {0: 10, 1: 20}
inventory[2] = 30
print(Updated dictionary:", inventory)

dept_a = {1: 10, 2: 20}
dept_b = {3: 30, 4: 40}
dept_c = {5: 50, 6: 60}
merged = {**dept_a, **dept_b, **dept_c}
print("Merged dictionary:", merged)


n = 5
squares = {x: x*x for x in range(1, n + 1)}
print("Squares up to 5:", squares)


squares_15 = {x: x**2 for x in range(1, 16)}
print(" Squares from 1 to 15:", squares_15)



project_tags = {"python", "api", "logistics", "automation"}
print("6. Created set:", project_tags)


print("7. Iterating over set:")
for tag in project_tags:
    print("-", tag)


project_tags.add("backend")
project_tags.update(["database", "async"])
print( After adding members:", project_tags)


project_tags.discard("api")  
project_tags.discard("frontend") 
print(" After discards:", project_tags)

to_remove = "database"
if to_remove in project_tags:
    project_tags.remove(to_remove)
print(" After conditional removal:", project_tags)
