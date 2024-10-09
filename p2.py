def convert_seconds(seconds):
    if seconds < 0 or seconds >= 8640000:
        return "Число повинно бути більше або дорівнювати 0 і менше ніж 8640000."

    days, remainder = divmod(seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    if days == 1:
        day_word = "день"
    elif 2 <= days <= 4:
        day_word = "дні"
    else:
        day_word = "днів"
    time_str = f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"

    return f"{days} {day_word}, {time_str}"

print(convert_seconds(0))
print(convert_seconds(224930))
print(convert_seconds(466289))
print(convert_seconds(950400))
print(convert_seconds(1209600))
print(convert_seconds(1900800))
print(convert_seconds(8639999))
print(convert_seconds(22493))
print(convert_seconds(7948799))
