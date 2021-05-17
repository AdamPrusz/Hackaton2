# Poniżej mamy listą zawierającą krotki

data = [
    ('January', range(31)),
    ('February', range(28)),
    ('March', range(31)),
    ('April', range(30)),
    ('May', range(31)),
    ('June', range(30)),
    ('July', range(31)),
    ('August', range(31)),
    ('September', range(30)),
    ('October', range(31)),
    ('November', range(30)),
    ('December', range(31)),
      ]

def day_of_month(list):
    count = 1
    for day in list:
        if day == list[0]:
            print(day,end="\t")
            count += 1
        elif day == list[-1]:
            print(day, end="\n")
        elif count % 7 == 0:
            print(day, end="\n")
            count += 1
        else:
            print(day,end="\t")
            count += 1

for step in data:
    print(step[0])
    print()
    days = list(step[1])
    day_of_month(days)
    print()
    print()























