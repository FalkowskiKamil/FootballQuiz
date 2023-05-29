def calculate_score(answer, rank_table, equalizer = 0, top=100):
    #Checking if answer are in database
    if answer not in rank_table:
        return 0
    else:
        #Checking if answer are in best
        if rank_table.index.get_loc(answer) > top:
            score=0
        else:
            score=len(rank_table) - rank_table.index.get_loc(answer) - equalizer
        return score