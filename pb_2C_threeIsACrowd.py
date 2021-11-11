# Three is a Crowd
def crowd_test(names):
    if(len(names) > 3):
        print("The room is crowded!")

names = ["Michael", "Taimur", "Sebnem", "Alice", "Xander", "Hunter", "Eiko", "Chase", "Vanessa"]
print(names)
crowd_test(names)

while(len(names) > 3):
    names.pop()
crowd_test(names)

