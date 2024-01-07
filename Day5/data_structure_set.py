#자료 구조 (data_structure)
coffee = ['아메','라떼','바닐라']
burger = {'치즈','새우','불고기','치즈'} # {}set

article = """The war on Europe's eastern borders is going badly for Ukraine. That means, by extension, it is going badly for Nato and the EU, which have bankrolled Ukraine's war effort and its economy to the tune of tens of billions of dollars.

This time last year, hopes were high in Nato that, supplied with modern military equipment and intensive training in Western countries, Ukraine's army could press home the advantage it had gained that autumn and push the Russians out of much of the territory they had seized. That hasn't happened.

The problem has been one of timing. Nato countries took a long time making their mind up about whether they dared send modern Main Battle Tanks like Britain's Challenger 2 and Germany's Leopard 2 to Ukraine, in case it provoked President Vladimir Putin into some sort of rash retaliation.

In the end, the West delivered the tanks, President Putin did nothing. But by the time they were ready to be deployed on the battlefield in June, Russian commanders had looked at the map and rightly guessed where Ukraine's main effort was going to be."""

words = article.split()
words.sort()
filteredwords = list(set(words))  # set([단어들])
print(filteredwords)












