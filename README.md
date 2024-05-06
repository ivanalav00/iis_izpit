# Vzpostavitev projekta
1. Ustvarjanje novega poetry projekta: poetry new iis_izpit
2. Premik v mapo: cd iis_izpit
3. Dodajanje knjižnic: poetry add pandas, poetry add scikit-learn, poetry add evidently
4. Kreiranje ostalih map: mkdir -p data/{processed,raw} models reports src/{data,models}
5. Priprava __init__.py: touch src/__init__.py
6. Inicializacija git-a: git init 
7. Ustvarjanje repota na githubu. 
8. Povezava lokalnega repota z githubom: git remote add origin git@github.com:ivanalav00/iis_izpit.git
9. Inital commit: git add ., git commit -m "Initial commit", git push --set-upstream origin master, 

# Vzpostavitev verzioniranja podatkov
1. Inicializacija dvc: dvc init.
2. Priprava repo-ta na Dagshubu (povezava z github projektom). 
3. Dodajanje dvc remote: dvc remote add origin s3://dvc, dvc remote modify origin endpointurl https://dagshub.com/ivanalav00/iis_izpit.s3
4. Konfiguracija: dvc remote modify origin --local access_key_id ###, dvc remote modify origin --local secret_access_key #####
5. Verzioniranje mape data: dvc add data
6. Dodajanje na git: git add .gitignore data.dvc, git commit -m "First data.dvc", git push
7. Push na dagshub: dvc remote default origin, dvc push

# Združevanje podatkov
1. Dodajanje dodatne knjižnice: poetry add openpyxl
2. Implementacija kode.
2. Dodajanje na dvc: dvc add data/raw
3. Dodajanje na git: git add ., git commit -m "Korak 3", git push
4. Push na dvc: dvc push -r origin

# Validiranje in Testiranje podatkov
1. Implementacija validacije v validate_data.py
2. Interpretacija: Podatki niso uspešno validarani, saj ima current_data.csv stolpec AVG_subject, reference data pa tega nima.
2. Implementacija testiranje v test_data.py
3. Interpretacija: Vsi podatki imajo drift score 1 - data drift ni detected. To pomeni da je distribucija podatkov enaka tako pri reference data kot current data. 
4. Dodajanje na dvc: dvc add data/processed
5. Dodajanje na git: git add ., git commit -m "Korak 4 in 5", git push
6. Push na dvc: dvc push -r origin

# Učenje napovednega modela
1. Implementacija modela v train_eval.py
2. Dodajanje na git: git add ., git commit -m "Korak 6", git push
