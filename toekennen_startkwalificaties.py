def toekennen_startkwalificaties(dataframe, jaren_nieuw, jaren_goed, jaren_voldoende, jaren_matig):

    # toekennen van de startkwalificatie bij elke afsluiter
    voorwaarden = [(dataframe['Jaar van eerste aanleg'].isin(jaren_nieuw)),
                   (dataframe['Jaar van eerste aanleg'].isin(jaren_goed)),
                   (dataframe['Jaar van eerste aanleg'].isin(jaren_voldoende)),
                   (dataframe['Jaar van eerste aanleg'].isin(jaren_matig))]

    startkwalificaties = ['nieuw', 'goed', 'voldoende', 'matig']

    dataframe['startkwalificatie'] = np.select(voorwaarden, startkwalificaties)
    
    return dataframe