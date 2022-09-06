def demo_star_in_for_statement() -> None:
    a = range(10)
    b = range(50, 60)
    for i in *a, *b:
        print(i)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--for-statement", action="store_true")
    args = parser.parse_args()
    if args.for_statement:
        demo_star_in_for_statement()
