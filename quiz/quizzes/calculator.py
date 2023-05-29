def calculate_score(answer, rank_table, equalizer = 0, top=100):
    if answer not in rank_table:
        return 0
    else:
        if rank_table.index.get_loc(answer) > top:
            score=0
        else:
            score=len(rank_table) - rank_table.index.get_loc(answer) - equalizer
        return score