def legendcalculation(AAPLdailyopen_n, AMZNdailyopen_n, GOOGLdailyopen_n, FBdailyopen_n, MSFTdailyopen_n, NFLXdailyopen_n):
    #Determine where to put legend board in relative stock performance graph
    stockgoodperformance = 0
    #Default location for legends of small graphs is top right, will change to bottom right depending on graph
    AAPLlegendloc = 1
    AMZNlegendloc = 1
    GOOGLlegendloc = 1
    FBlegendloc = 1
    MSFTlegendloc = 1
    NFLXlegendloc = 1

    #Find number of stocks closing higher than when they opened
    if AAPLdailyopen_n[-1] > AAPLdailyopen_n[0]:
        stockgoodperformance += 1
        AAPLlegendloc = 4
    if AMZNdailyopen_n[-1] > AMZNdailyopen_n[0]:
        stockgoodperformance += 1
        AMZNlegendloc = 4
    if GOOGLdailyopen_n[-1] > GOOGLdailyopen_n[0]:
        stockgoodperformance += 1
        GOOGLlegendloc = 4
    if FBdailyopen_n[-1] > FBdailyopen_n[0]:
        stockgoodperformance += 1
        FBlegendloc = 4
    if MSFTdailyopen_n[-1] > MSFTdailyopen_n[0]:
        stockgoodperformance += 1
        MSFTlegendloc = 4
    if NFLXdailyopen_n[-1] > NFLXdailyopen_n[0]:
        stockgoodperformance += 1
        NFLXlegendloc = 4

    if stockgoodperformance >= 5:
        legendloc = 4 #stocks mostly rised, place legend bottom right
    elif stockgoodperformance <= 2:
        legendloc = 3 #stocks mostly tumbled, place legend bottom left
    else: #Mixed, place legend center-left
        # legendloc = 9
        legendloc = 6

    # Auto detect best location
    # legendloc = 0

    return {"legendloc": legendloc,
            "stockloc": [AAPLlegendloc, AMZNlegendloc, GOOGLlegendloc, FBlegendloc, MSFTlegendloc, NFLXlegendloc]}