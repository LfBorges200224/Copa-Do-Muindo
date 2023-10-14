from exceptions import ImpossibleTitlesError, InvalidYearCupError, NegativeTitlesError


def data_processing(data):
    from datetime import datetime
    current_year = datetime.now().year
    first_cup = ""
    titles = 0

    for item in data:
        first_cup = datetime.strptime(data["first_cup"], "%Y-%m-%d").year
        titles = data["titles"]
        if data["titles"] < 0:
            raise NegativeTitlesError("titles cannot be negative")

        firts_cup_year = 1930
    cup_years = []
    while firts_cup_year < current_year:
        firts_cup_year = firts_cup_year + 4
        cup_years.append(firts_cup_year)
        if cup_years[-1] == current_year:
            break

    if (first_cup in cup_years or first_cup == 1930):
        print('certo')
    else:
        raise InvalidYearCupError("there was no world cup this year")

    w = []
    while first_cup < current_year:
        first_cup = first_cup + 4
        w.append(first_cup)
    if titles > len(w):
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")