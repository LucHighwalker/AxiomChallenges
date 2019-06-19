def optimize_farm(total_acres, total_hours, corn_profit, oats_profit, corn_hours, oats_hours, accuracy=0.01):
    optimized = False
    divider = accuracy
    most_profit = (0, 0, 0)

    while not optimized and divider <= 1:
        corn_acres = divider * total_acres
        oats_acres = total_acres - corn_acres

        corn_time = corn_acres * corn_hours
        oats_time = oats_acres * oats_hours

        total_time = corn_time + oats_time

        if total_time >= total_hours:
            optimized = True
        else:
            total_corn_profit = corn_acres * corn_profit
            total_oats_profit = oats_acres * oats_profit
            total_profit = round(total_corn_profit + total_oats_profit, 2)

            if total_profit > most_profit[0]:
                most_profit = (total_profit, round(
                    corn_acres, 2), round(oats_acres, 2))

        divider += accuracy

    return most_profit


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

    for i, test in enumerate(tests):
        results = optimize_farm(
            test['x'], test['y'], test['p1'], test['p2'], test['h1'], test['h2'])
        print("Results for test {}:\n   with {} acres of land and {} available hours\n   most profitable at ${}: {} acres of corn and {} acres of oats.\n\n".format(
            i + 1, test['x'], test['y'], results[0], results[1], results[2]))
