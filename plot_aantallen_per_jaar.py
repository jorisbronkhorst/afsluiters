def plot_aantallen_per_jaar(dataframe, jaren_nieuw, jaren_goed, jaren_voldoende, jaren_matig):    
    
    fontsize = 14
    
    jaar_df = pd.DataFrame(dataframe.groupby(['Jaar van eerste aanleg']).size())
    jaar_df.index = jaar_df.index.astype(int)
    jaar_df = jaar_df.rename(columns={0: 'aantal'})
    
    startkwalificatie_aantallen = g_afsluiter.groupby('startkwalificatie').size()
    
    ax = jaar_df.plot(kind='bar', figsize=(20, 10), fontsize=fontsize, color = 'blue', legend=False)

    for i in range(len(jaar_df)):
        if i < len(jaren_matig):
            ax.patches[i].set_facecolor('red')
        if len(jaren_matig) <= i < len(jaren_matig) + len(jaren_voldoende):
            ax.patches[i].set_facecolor('orange')
        if len(jaren_matig) + len(jaren_voldoende) <= i < len(jaren_matig) + len(jaren_voldoende) + len(jaren_goed):
            ax.patches[i].set_facecolor('green')
                      
    plt.title('Totaal aantal afsluiters in gebruik per jaar van aanleg in 2018', fontsize=fontsize+2)
    plt.grid(axis='y')
    plt.xlabel('Jaar' ,fontsize=fontsize)
    plt.ylabel('aantal', fontsize=fontsize)

    plt.axvline(x=len(jaren_matig) - 0.75, color='black', linestyle='--')
    plt.axvline(x=len(jaren_matig)+len(jaren_voldoende) - 0.75, color='black', linestyle='--')
    plt.axvline(x=len(jaren_matig)+len(jaren_voldoende)+len(jaren_goed) - 0.75, color='black', linestyle='--')

    plt.text(len(jaren_matig)/2 - 3, max(jaar_df.aantal)*0.95, ' matig\n '+ str(startkwalificatie_aantallen['matig']),
             fontsize=fontsize+2, color='red')
    plt.text(len(jaren_matig) + 5, max(jaar_df.aantal)*0.95, 'voldoende\n '+ str(startkwalificatie_aantallen['voldoende']),
             fontsize=fontsize+2, color='orange')
    plt.text(len(jaren_matig)+len(jaren_voldoende) + 5, max(jaar_df.aantal)*0.95, 'goed\n '+ str(startkwalificatie_aantallen['goed']),
             fontsize=fontsize+2, color='green')
    plt.text(len(jaren_matig)+len(jaren_voldoende)+len(jaren_goed), max(jaar_df.aantal)*0.95, 'nieuw\n '+ str(startkwalificatie_aantallen['nieuw']),
             fontsize=fontsize+2, color='blue')

    return plt.show()