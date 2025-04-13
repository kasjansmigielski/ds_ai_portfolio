# Halfmarathon Estimator App

*Date of creation: 2024-10-20*

## Project description
<div style="text-align: justify;">
The aim of the project was to create an application that would use a regression algorithm to train models and would be able to predict (based on previously trained data) the time in which a user would run a half marathon - by providing specific data.
</div style>

## Main functionalities
<ul>
  <li>allowing the user to enter data freely (without any appropriate conversion of the record) -> the LLM model used extracts data from the user into a JSON structure and prepares it for use by the regression model</li>
  <li>simple functionality allows for the final estimation of the time to run a half marathon - using the trained best regression model</li>
  <li>the LLM model is connected to Langfuse to track the model's life cycle</li>
</ul>

## ML model training
<div style="text-align: justify;">
I used PyCaret tools and I have included the implementation in a notebook ready for download:<br><br>
<a href="create_pipeline.ipynb" class="md-button md-button--primary">Download Notebook: Model training</a>
</div style>

## Skills
<ul>
  <li>Python</li>
  <li>PyCaret</li>
  <li>Machine Learning</li>
  <li>Langfuse</li>
  <li>OpenAI</li>
  <li>Streamlit</li>
  <li>Pandas</li>
  <li>Instructor</li>
  <li>Pydantic</li>
  <li>Dotenv</li>
</ul>

## Sample photos
![alt text](data/title.png)
![alt text](data/result.png)

## Application testing
<div style="text-align: justify;">
The application has been deployed on the Streamlit Community App and is available for public use.
<strong><br>To use the application you need your OpenAI API Key.</strong>
</div style>

[Link to repository](https://github.com/kasjansmigielski/halfmarathon_estimator_app)<br><br>
[Go to application](https://halfmarathon-estimator.streamlit.app/){ .md-button }