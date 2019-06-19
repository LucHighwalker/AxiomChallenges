def optimize_farm(total_acres, total_hours, corn_profit, oats_profit, corn_hours, oats_hours):
    pass


if __name__ == "__main__":
    tests = [
        {
            'x': 240,
            'y': 320,
            'p1': 40,
            'p2': 30,
            'h1': 2,
            'h2': 1
        },
        {
            'x': 300,
            'y': 380,
            'p1': 70,
            'p2': 45,
            'h1': 3,
            'h2': 1
        },
        {
            'x': 180,
            'y': 420,
            'p1': 65,
            'p2': 55,
            'h1': 3,
            'h2': 2
        }
    ]

    for test in tests:
      print(optimize_farm(test['x'], test['y'], test['p1'], test['p2'], test['h1'], test['h2']))
