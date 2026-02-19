def paycheck(row, bet):
    match (row, bet):
        case (r, _) if r[0] == r[1] == r[2]:
            match(row, bet):
                case(r, _) if r[0] == "🍒":
                    return bet*3
                case (r, _) if r[0] == "🍉":
                    return bet*5
                case (r, _) if r[0] == "🔔":
                    return bet*10
                case (r, _) if r[0] == "🌟":
                    return bet*35
        case _:
            return 0
