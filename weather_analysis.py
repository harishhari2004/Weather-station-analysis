days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")

weather = {
    "Kochi": {
        "temp": [31, 32, 30, 29, 31, 33, 32],
        "rain": [0, 5, 12, 20, 0, 0, 3]
    },
    "Munnar": {
        "temp": [18, 19, 17, 16, 18, 20, 19],
        "rain": [2, 8, 15, 25, 5, 0, 4]
    },
    "Palakkad": {
        "temp": [36, 37, 38, -999, 37, 39, 38],
        "rain": [0, 0, 0, 0, 0, 0, 0]
    },
    "Kozhikode": {
        "temp": [30, 31, 30, 29, 30, 32, 31],
        "rain": [0, 10, 8, 18, 2, 0, 1]
    }
}

print("SENSOR CHECK")
print("-" * 60)


def clean(values):
    new_temp = []

    for value in values:
        if value >= -20:
            new_temp.append(value)

    return new_temp


for city in sorted(weather):
    values = weather[city]["temp"]
    cleaned_values = clean(values)
    invalid_count = len(values) - len(cleaned_values)

    print(f"{city:<10} {invalid_count} invalid reading(s)")

print()

print("Weekly Summary")
print("-" * 60)
print(f"{'City':<10} {'Avg':>7} {'Max':>6} {'Min':>6} {'Rain':>7} {'Rainy':>7}")


def average(values):
    return sum(values) / len(values)


for place in sorted(weather):
    temp1 = weather[place]["temp"]
    cleaned_temp1 = clean(temp1)
    rain1 = weather[place]["rain"]

    avg_temp = average(cleaned_temp1)
    max_temp = max(cleaned_temp1)
    min_temp = min(cleaned_temp1)
    total_rain = sum(rain1)

    rainy_days = 0

    for rain in rain1:
        if rain > 0:
            rainy_days += 1

    print(
        f"{place:<10} {avg_temp:>7.1f} {max_temp:>6} "
        f"{min_temp:>6} {total_rain:>7} {rainy_days:>7}"
    )


print()
print("DAY TYPES")
print("-" * 40)
print(f"{'City':<10} {'Hot':>7} {'Warm':>8} {'Cool':>8}")


def day_type(temp, hot=35, warm=28):
    if temp >= hot:
        return "Hot"
    elif temp >= warm:
        return "Warm"
    else:
        return "Cool"


for place in sorted(weather):
    temp1 = weather[place]["temp"]
    cleaned_temp1 = clean(temp1)
    counts = {}

    for tempr in cleaned_temp1:
        temp2 = day_type(tempr)
        counts[temp2] = counts.get(temp2, 0) + 1

    print(
        f"{place:<10}{counts.get('Hot', 0):>7}"
        f"{counts.get('Warm', 0):>8}"
        f"{counts.get('Cool', 0):>8}"
    )


def city_averages(weather):
    averages = {}

    for pls in weather:
        temp3 = weather[pls]["temp"]
        cleaned_temp3 = clean(temp3)
        averages[pls] = average(cleaned_temp3)

    return averages


def extremes(averages):
    hot_city = ""
    cool_city = ""

    for citys in averages:
        if hot_city == "":
            hot_city = citys
            cool_city = citys
        else:
            if averages[citys] > averages[hot_city]:
                hot_city = citys

            if averages[citys] < averages[cool_city]:
                cool_city = citys

    print(f"Hottest city: {hot_city} ({averages[hot_city]:.1f})")
    print(f"Coolest city: {cool_city} ({averages[cool_city]:.1f})")


averages = city_averages(weather)
extremes(averages)


daily_rain = {}

for num, day in enumerate(days):
    total = 0

    for city in weather:
        total += weather[city]["rain"][num]

    daily_rain[day] = total


print()
print("RAINFALL BY DAY")

for day in days:
    print(f"{day:5} {daily_rain[day]:8} mm")


wet_day = ""
max_daily_rain = -1

for day in daily_rain:
    if daily_rain[day] > max_daily_rain:
        max_daily_rain = daily_rain[day]
        wet_day = day


print()
print(f"Wettest day: {wet_day} ({max_daily_rain} mm)")


def heavy_rain(day_index, limit=20):
    alerts = []

    for city in weather:
        mm = weather[city]["rain"][day_index]

        if mm >= limit:
            alerts.append((city, mm))

    alerts.sort()
    return alerts


print()
print("RAIN ALERTS (20 mm or more)")

for position, day in enumerate(days):
    alerts = heavy_rain(position)

    if len(alerts) > 0:
        print(f"{day}: ", end="")

        for i in range(len(alerts)):
            city, mm = alerts[i]

            if i > 0:
                print(", ", end="")

            print(f"{city} {mm} mm", end="")

        print()


print()
print("RAIN ALERTS (10 mm or more)")

for pos, day in enumerate(days):
    alerts = heavy_rain(pos, limit=10)

    if len(alerts) > 0:
        print(f"{day}: ", end="")

        for i in range(len(alerts)):
            city, mm = alerts[i]

            if i > 0:
                print(", ", end="")

            print(f"{city} {mm} mm", end="")

        print()
        
