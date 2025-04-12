# Halfmarathon Estimator App

*Date of creation: 2024-10-20*

**Project description:**<br>
The aim of the project was to create an application that would use a regression algorithm to train models and would be able to predict (based on previously trained data) the time in which a user would run a half marathon - by providing specific data.<br>

**Project description:**<br>
- allowing the user to enter data freely (without any appropriate conversion of the record) -> the LLM model used extracts data from the user into a JSON structure and prepares it for use by the regression model,<br>
- simple functionality allows for the final estimation of the time to run a half marathon - using the trained best regression model,<br>
- the LLM model is connected to Langfuse to track the model's life cycle.

**To train the AI ​​model** I used PyCaret tools and I have included the implementation in a notebook ready for download:<br>
<a href="create_pipeline.ipynb" class="md-button md-button--primary">Download Notebook: Model training</a>

**Skills:**<br>
- Python,<br>
- PyCaret,<br>
- Machine Learning,<br>
- Langfuse,<br>
- OpenAI,<br>
- Streamlit,<br>
- Pandas,<br>
- Instructor,<br>
- Pydantic,<br>
- Langfuse,<br>
- Dotenv.

**Sample photos:**<br>
![alt text](data/title.png)
![alt text](data/result.png)

The application has been deployed on the Streamlit Community App and **is available for public use.**<br>
**To use the application you need your OpenAI API Key.**

[Link to repository](https://github.com/kasjansmigielski/halfmarathon_estimator_app)<br><br>
[Go to application](https://halfmarathon-estimator.streamlit.app/){ .md-button }