import pandas as pd

cyber = pd.read_csv("ATTACK_MAIN.csv", encoding="utf8")
# print (cyber)
popis = cyber["DESCRIPTION"]
# print (popis)
number = 0
password = 0
keyword_result = []
phising = 0
phising_col = []

pravidla = [
            ['ATM','card'],
            ['password','poor','weak','credential'],
            ['password','repetitive','same'],
            ['password','username'],
            ['password','authoriz'],
            ['Aktualizace softwarů'],
            ['social','media','network','Facebook','Twitter','Instagram'],
            ['scam'],
            ['email','phishing'],
            ['email','campaign','business'],
            ['suspici'],
            ['wifi','public'],
            ['network','security'],
            ['antivir'],
            ['open','document','attach'],
            ['web','hacked'],
            ['credentials'],
            ['Nepůjčute neznámým osobám telefon'],
            ['Nenechávejte elektroniku na neznýmách místech bez dozoru'],
            ['reinstall'],
            ['Odstraňte váš účet a vytvořte nový'],
            ['router'],
            ['Nepřipojujte k počítači či mobilu neznámá zařízení'],
            ['USB'],
            ['Před prodejem elektroniky ji vymažte'],
            ['Udržujte přístupové informace v soukromí'],
            ['warning'],
            ['bitcoin'],
            ['blackmail','pressure'],
            ['Nejdřív myslete a pak vyplňujte'],
            ['Dbejte na zabezpečení vaší rodiny'],
            ]

for row in popis:
  row_result = []
  if isinstance (row,str):
    for pravidlo_number, pravidlo in enumerate(pravidla):
      password = 0
      key_cnt = 0
      for key in pravidlo:
        key_cnt+=1
        if key in row.lower():
          password+= 1
      if password == key_cnt:
        row_result.append(pravidlo_number)
          # print (f'{number}:{row}')


    
  else:
    row_result.append (None)
  keyword_result.append(list(set(row_result)))

cyber['keyword_result'] = keyword_result
print (cyber.describe())

cyber[['keyword_result','ID','DATE','DESCRIPTION']].to_csv("ATTACK_MAIN_out.csv", encoding="utf8")