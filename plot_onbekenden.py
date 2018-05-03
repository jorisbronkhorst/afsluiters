Afsluiters = Afsluiters[Afsluiters['Jaar van eerste aanleg'] >= 1960]
jaar_aantallen = Afsluiters.groupby('Jaar van eerste aanleg').size()
jaar_aantallen = jaar_aantallen.drop('Onbekend')
jaardata = Afsluiters[eigenschappen] != 'Onbekend'
jaardata['Jaar van eerste aanleg'] = Afsluiters['Jaar van eerste aanleg']
jaardata = jaardata.groupby('Jaar van eerste aanleg').sum().divide(0.01 * jaar_aantallen, axis=0).drop(['Onbekend', 2018.0]).astype(int)
jaardata.index = jaardata.index.astype(int)

import matplotlib.pyplot as plt
ax = jaardata.plot(figsize=(20, 10), fontsize=14, xticks=jaardata.index,
                   rot=90,
                   style='.-',
                   linewidth=2,
                   color = ['blue', 'red', 'green', 'orange', 'gray'])
ax.legend(fontsize = 16)
plt.xlabel('Jaar' ,fontsize=16)
plt.ylabel('Percentage [%]', fontsize=16)
plt.grid(axis='y')
plt.axhline(y=eigenschap_bekendheid['Identificatienummer']['% bekend'], color='blue', linestyle='--')
plt.axhline(y=eigenschap_bekendheid['Type']['% bekend'], color='red', linestyle='--')
plt.axhline(y=eigenschap_bekendheid['Soort afsluiter']['% bekend'], color='green', linestyle='--')
plt.axhline(y=eigenschap_bekendheid['Fabrikaat']['% bekend'], color='orange', linestyle='--')
plt.axhline(y=eigenschap_bekendheid['Functie']['% bekend'], color='gray', linestyle='--')
plt.show()