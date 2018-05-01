def toestandsbepaling(dataframe, eigenschap, kwalificatie):
    
    # groepeer per eigenschap
    per_eigenschap = pd.DataFrame(dataframe.groupby([eigenschap, kwalificatie]).size())
    per_eigenschap = per_eigenschap.rename(columns={0: 'aantal'})
    
    # unstack de dataframe en verander ontbrekende waarden in nullen
    per_eigenschap_unstack = per_eigenschap['aantal'].unstack(level=1).fillna(0)
    
    # verander de volgorde van de kolommen
    per_eigenschap_unstack = per_eigenschap_unstack[['nieuw', 'goed', 'voldoende', 'matig']]
    
    # bereken het totaal per eigenschap uit en zet dat in nieuwe kolom 'totaal'
    per_eigenschap_unstack['totaal'] = per_eigenschap_unstack.sum(axis=1)
    
    # sorteer op basis van het totaal aantal per eigenschap
    per_eigenschap_unstack = per_eigenschap_unstack.sort_values(['totaal'])

    # maak een dataframe met percentage bij bepaalde kwalificatie hoort
    per_eigenschap_unstack_relatief = per_eigenschap_unstack.div(0.01 * per_eigenschap_unstack.totaal, axis='index').iloc[:,:-1]

    # plot het resultaat
    fontsize = 14
    per_eigenschap_unstack_relatief.plot(kind = 'barh', figsize=(20, 10), stacked=True,
                                    fontsize=fontsize, color = ['blue','green','orange','red'])
    
    plt.xlabel('Aantal afsluiters (%)', fontsize=fontsize+2)
    plt.ylabel(eigenschap, fontsize=fontsize+2)
    plt.title('Toestandsbepaling afsluiters per eigenschap 2018', fontsize=fontsize+2)

    for i in range(len(per_eigenschap_unstack_relatief)):
        plt.text(100.5, i-0.1, str(per_eigenschap_unstack.iloc[i]['totaal']), fontsize=fontsize)

    plt.legend(loc=8, bbox_to_anchor=(0.5,-0.15), fontsize=fontsize, ncol=4)
    
    return plt.show()