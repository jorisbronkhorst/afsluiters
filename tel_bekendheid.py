def tel_bekendheid(Afsluiters, jaar = None):
    
    if jaar != None:
        Afsluiters = Afsluiters[Afsluiters['Jaar van eerste aanleg'] == jaar]
        
    eigenschappen = ['Identificatienummer', 'Type', 'Soort afsluiter', 'Fabrikaat', 'Functie']
    
    eigenschap_bekendheid = pd.DataFrame(index=['bekend', 'onbekend'], columns=eigenschappen)
    
    eigenschap_bekendheid.loc['bekend'] = (Afsluiters[eigenschappen] != 'Onbekend').sum()
    eigenschap_bekendheid.loc['onbekend'] = (Afsluiters[eigenschappen] == 'Onbekend').sum()

    eigenschap_bekendheid.columns.name = 'jaar: %s, aantal afsluiters: %i' % (jaar, len(Afsluiters))
    
    telling = (Afsluiters[eigenschappen] == 'Onbekend').sum(axis=1)
    aantal_onbekenden = telling.to_frame().groupby(0).size().to_frame('Aantal afsluiters')
    
    aantal_onbekenden.index.name = 'Aantal onbekenden eigenschappen'
    aantal_onbekenden.columns.name = 'jaar: %s, aantal afsluiters: %i' % (jaar, len(Afsluiters))
    
    return eigenschap_bekendheid, aantal_onbekenden