def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"


print(get_phone(country="+98", area=123, first=456, last=7890))
