# Find Friends App

*Data of creation: 2024-10-09*

**Project description:**<br>
The aim of the project was to create an application that would enable the use of a clustering model to match a user to the appropriate group from a loaded data set (data comes from an anonymized survey) - based on data provided by the user.<br>

**Main functionalities:**<br>
- the user filters basic data, such as: age, education, gender, favorite animals or favorite places - corresponding to their preferences,<br>
- then the previously trained clustering model creates the appropriate number of clusters for the survey data and matches the user's preferences to the matching group,<br>
- finally, using LLM, adequate cluster descriptions are generated.

**To train the AI ​​model** I used Scikit-learn tools and I have included the implementation in a notebook ready for download:<br>
<a href="clustering_model_training.ipynb" class="md-button md-button--primary">Download Notebook: Model training</a>

**To generate Clusters names** I used the LLM model and I have included the implementation in a notebook ready for dowlonad:<br>
<a href="clusters_naming.ipynb" class="md-button md-button--primary">Download Notebook: Clusters naming</a>

**Skills:**<br>
- Python,<br>
- Langfuse,<br>
- OpenAI,<br>
- Streamlit,<br>
- Scikit-learn,<br>
- Plotly,<br>
- PyCaret (Clustering),<br>
- NumPy,<br>
- Matplotlib.

**Sample photos:**<br>
![alt text](image-2.png)
![alt text](image-1.png)

The application has been deployed on the Streamlit Community App and **is available for public use.**

**Link to repository:** https://github.com/kasjansmigielski/find_friends_app<br>
**Link to app:** https://find-friends-app.streamlit.app/


[Go to application](https://find-friends-app.streamlit.app/){ .md-button }