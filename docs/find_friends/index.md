# Aplikacja: Find Friends

*2024-10-09*

#### **Opis projektu:**
Celem projektu było stworzenie aplikacji, która umożliwi wykorzystanie modelu klastrującego w celu dopasowania użytkownika do odpowiedniej grupy z wczytanego zbioru danych (dane pochodzą ze zanonimizowanej ankiety) - na podstawie danych, które użytkownik podał.<br><br>
**Główne funkcjonalnośći:**<br>
- użytkownik filtruje podstawone dane, takie jak: wiek, wykształcenie, płeć, ulubione zwierzęta czy ulubione miejsca - odpowiadające jego preferencjom,<br>
- następnie wytrenowany wcześniej model klastrujący tworzy dla danych z ankiety odpowiednią ilość klastrów i dopasowuje preferencje użytkownika do pasującej grupy,<br>
- finalnie za pomocą LLM są generowane adekwatne opisy klastrów.

**Do wytrenowania modelu klastrującego** wykorzystałem narzędzia Scikit-learn, natomiast sam algorytm umieściłem notebooku - gotowym do pobrania.
<a href="clustering_model_training.ipynb" class="md-button md-button--primary">Pobierz Notebook: "Trenowanie modelu"</a>

**Do wygenerowania nazw klastrów** wykorzystałem model LLM, natomiast sam algorytm umieściłem w notebooku - gotowym do pobrania.<br>
<a href="clusters_naming.ipynb" class="md-button md-button--primary">Pobierz Notebook: "Nazywanie klastrów"</a>


Aplikacja została wdrożona na Streamlit Community App i jest dostępna do publicznego użytku.

**Wykorzystane technologie:**<br>
- Python,<br>
- Langfuse,<br>
- OpenAI,<br>
- Streamlit,<br>
- Scikit-learn,<br>
- Plotly,<br>
- PyCaret (Clustering),<br>
- NumPy,<br>
- Matplotlib.


![alt text](image-2.png)
![alt text](image-1.png)


**Link do repozytorium:** https://github.com/kasjansmigielski/find_friends_app<br>
**Link do aplikacji:** https://find-friends-app.streamlit.app/


[Przejdź do aplikacji](https://find-friends-app.streamlit.app/){ .md-button }