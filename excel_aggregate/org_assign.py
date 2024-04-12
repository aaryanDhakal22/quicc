# Oriole = 5 - 12
# windsor = 20-27
# Lombardi's = 32 -39
# dragon = 44-49
# vitos = 57-59
# pizza city = 66-70


def org_name(row):
    if 5 <= row <= 12:
        return "ORIOLE"
    elif 20 <= row <= 27:
        return "WINDSOR"
    elif 32 <= row <= 39:
        return "LOMBARDIS"
    elif 44 <= row <= 49:
        return "DRAGON"
    elif 57 <= row <= 59:
        return "VITOS"
    elif 66 <= row <= 70:
        return "PIZZA CITY"
