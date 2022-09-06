def demo_star_in_for_statement():
    a = range(10)
    b = range(50, 60)
    for i in *a, *b:
        print(i)
