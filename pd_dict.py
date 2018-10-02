import pandas as pd

tweet_dict = {'#DrowningInPlastic': [], '#ScouseFilmTitles': [], '#UniversityChallenge': [], '#CPFC': [], '#Strangers': [], 'lewis f': [], 'Primera Air': [], 'Geoffrey Hayes': [], 'Halloween': [], 'Philip Hammond': [], 'Charles Aznavour': [], 'Carlos Ezquerra': [], 'Jeremy Hunt': [],'Matilda': [], 'David Brooks': [], 'Valencia': [], 'Boris Johnson': [], 'Gemma Collins': [], 'Indonesia': [], '1st of October': [], 'Vitality Stadium': [], 'Chris Grayling': [], 'Kevin De Bruyne': [], '#TheUndateables': [], '#poisonous': [], '#hellboy': [], '#CPC18': [],'#InternationalCoffeeDay': [], '#MondayMotivation': [], '#BlackHistoryMonth': [], '#October1st': [], '#BOUCRY': [], '#worldvegetarianday': [], '#OlderPeoplesDay': [], '#MICHELINSTAR19': [], '#lincolnshireday': [], '#mondaymorning': [], '#TheCry': [], '#WilderFury': [], '#conservatives2018': [], '#PinchPunch': [], '#RyderCup': [], '#Marr': [], '#breastcancerawarenessmonth': [], '#monkmanandseagull': [], '#Stoptober': [], '#WorldArchitectureDay': [], '#NigeriaAt58': [], '#ParentsinSportWeek2018': [], '#ConservativeConference2018': []}

tweet_df = pd.DataFrame.from_dict(tweet_dict)

print(tweet_df)