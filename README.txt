Összefoglalás: Adatfeldolgozás, Modellválasztás és Alkalmazásfejlesztés

1. Dataset
Adathalmaz: Egy diákok felvételi eredményeit tartalmazó adathalmazt használtam. A dataset jellemzői:

Jellemzők:
	Age (Életkor)
	Gender (Nem: Male vagy Female)
	Admission Test Score (Felvételi teszt pontszáma)
	High School Percentage (Középiskolai teljesítmény százalékban)
	City (Diák származási városa)

Célváltozó:
	Admission Status (Elfogadták-e a jelentkezést: Accepted vagy Rejected)

2. Cél
	A cél az volt, hogy a fenti jellemzők alapján egy prediktív modellt hozzunk létre, amely megjósolja, hogy egy jelentkezőt felvesznek-e az 	egyetemre (Accepted) vagy elutasítják (Rejected).

3. Adatfeldolgozás
	Az adathalmaz előkészítése a következő lépéseket tartalmazta:

	Adattisztítás:
		Hiányzó értékeket numerikus oszlopokban az átlaggal töltöttünk ki.
		Kategóriák (pl. Gender és City) numerikus kódokra lettek alakítva.
		A hiányzó Admission Status sorokat eltávolítottuk.
		Korrelációs mátrix: Vizualizáltuk az attribútumok közötti korrelációkat, hogy azonosítsuk a célváltozóhoz kapcsolódó jellemzőket.
		Train-test split: Az adathalmazt 80%-os tréning és 20%-os teszthalmazra bontottuk.

4. Modellválasztás
	Kipróbált modellek:
		Logistic Regression: Egyszerű, lineáris megközelítés.
		Decision Tree: Nemlineáris döntéshozatalra alkalmas.
		Random Forest: Több döntési fa kombinációja az erősebb predikciók érdekében.
	
	Hiperparaméter optimalizálás:
		GridSearchCV segítségével megkerestük a modellek legjobb hiperparamétereit (pl. max_depth, C értékek).
	Legjobb modell: A Decision Tree érte el a legjobb teljesítményt a keresztvalidáció során (~54% pontosság).
	Végső modell: A Decision Tree modellt választottuk, és elmentettük egy decision_tree_model.pkl fájlba.

5. Backend (FastAPI)
	A backend a FastAPI keretrendszeren alapult, amely a mentett Decision Tree modellt használva predikciót végez az új adatokra.
	Az endpoint bemeneti jellemzőket fogad (Age, Gender, stb.) és visszaadja a predikciót (Accepted vagy Rejected).
	A FastAPI alkalmazást a main.py fájlban definiáltuk, és Uvicorn segítségével futtattuk.

6. Frontend (Streamlit)
	A felhasználó megadja a bemeneti adatokat (életkor, nem, teszt pontszám stb.).
	A Streamlit küld egy kérést a FastAPI backendhez, amely visszaadja a predikciót.
	Az eredményt (Accepted vagy Rejected) vizuálisan jeleníti meg.
	A Streamlit alkalmazást az app.py fájlban definiáltuk.

7. Végeredmény: A felhasználó a Streamlit felületen adja meg a jellemzőket.
	Az alkalmazás a FastAPI szerverhez küld kérést.
	A szerver visszaadja a modell predikcióját.
	
	Használat:
		A Google Colab-on keresztül futtatható.
		LocalTunnel segítségével publikus URL-t generáltunk a Streamlit alkalmazás eléréséhez.(Ez valamiért nem sikerült.)
