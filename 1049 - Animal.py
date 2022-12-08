vertebrados = {'ave': {'carnivoro': 'aguia','onivoro': 'pomba'}, 'mamifero': {'onivoro': 'homem', 'herbivoro': 'vaca'}}
invertebrados = {'inseto': {'hematofago': 'pulga','herbivoro': 'lagarta'}, 'anelideo': {'hematofago': 'sanguessuga', 'onivoro': 'minhoca'}}

entrada = str(input()).strip().lower() 
entrada2 = str(input()).strip().lower() 
entrada3 = str(input()).strip().lower() 

if entrada == 'vertebrado':
    print(f"{vertebrados[entrada2][entrada3]}")
else:
    print(f"{invertebrados[entrada2][entrada3]}")