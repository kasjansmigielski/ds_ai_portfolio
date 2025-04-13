# Find Friends App

*Data of creation: 2024-10-09*

## Project description
<div style="text-align: justify;">
The aim of the project was to create an application that would enable the use of a clustering model to match a user to the appropriate group from a loaded data set (data comes from an anonymized survey) - based on data provided by the user.
</div style>

## Main functionalities
<div style="text-align: justify;">
  <ul>
    <li>The user filters basic data, such as: age, education, gender, favorite animals, or favorite places - corresponding to their preferences</li>
    <li>Then the previously trained clustering model creates the appropriate number of clusters for the survey data and matches the user's preferences to the matching group</li>
    <li>Finally, using LLM, adequate cluster descriptions are generated</li>
  </ul>
</div>

## ML model training
<div style="text-align: justify;">
I used Scikit-learn tools and I have included the implementation in a notebook ready for download:<br><br>
<a href="clustering_model_training.ipynb" class="md-button md-button--primary">Download Notebook: Model training</a>
</div style>

## Clusters naming
<div style="text-align: justify;">
I used the LLM model and I have included the implementation in a notebook ready for dowlonad:<br><br>
<a href="clusters_naming.ipynb" class="md-button md-button--primary">Download Notebook: Clusters naming</a>
</div style>


## Skills
<ul>
  <li>Python</li>
  <li>Langfuse</li>
  <li>OpenAI</li>
  <li>Streamlit</li>
  <li>Scikit-learn</li>
  <li>Plotly</li>
  <li>PyCaret (Clustering)</li>
  <li>NumPy</li>
  <li>Matplotlib</li>
</ul>

## Sample photos
![alt text](data/first.png)
![alt text](data/second.png)

## Application testing
<div style="text-align: justify;">
The application has been deployed on the Streamlit Community App and <strong>is available for public use.</strong>
</div style>

[Link to repository](https://github.com/kasjansmigielski/find_friends_app)<br><br>
[Go to application](https://find-friends-app.streamlit.app/){ .md-button }