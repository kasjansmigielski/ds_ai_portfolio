# Student Profiler

*Project: March 2025 — June 2025*

**Role:** Backend / Data Engineer

**Company:** GOTOIT sp. z o.o.

**Status:** Production

---

## Project description

<div style="text-align: justify;">
Mentors and course instructors lacked a tool for systematic monitoring of student activity on Discord.

Analysis of engagement, work regularity, and interaction history:

- was scattered across many channels,
- required manual message review,
- provided no basis for automatic conclusions or scaling the mentoring process.

There was no single, central system for collecting and analyzing data.

I designed and developed <strong>Student Profiler</strong> — a tool for automatic monitoring of student activity in the Discord environment.
</div>

---

## Solution

<div style="text-align: justify;">
The core of the system is a <strong>Discord Bot</strong> that:

- fetches historical data from channels,
- listens for new messages and events in real-time,
- saves data in a relational database,
- feeds the analytical layer and user interface.

The architecture is prepared for further development of AI-based features (humanized mentor bot, sentiment analysis, OCR, predictive models).
</div>

---

## Architecture

![System architecture](data/architecture_logic.png)

---

## Main functionalities

- Discord Bot integration for monitoring activity and automated messaging
- Scheduled hourly data collection from Discord channels
- Data storage system using PostgreSQL for messages and Digital Ocean Spaces for attachments
- Streamlit-based UI for easy access and analysis of Discord data
- Scalable architecture with future implementation plans for AI features

---

## What I did

1. Designed system architecture following **Single Responsibility Principle**
2. Implemented **Discord Bot** for:
   - fetching message history
   - listening for new events
   - handling automated responses
3. Created **hourly data collection scheduler**
4. Designed and deployed **PostgreSQL** database
5. Integrated **DigitalOcean Spaces** for attachment storage
6. Built **analytical UI in Streamlit** with Plotly visualizations
7. Prepared **Docker** environment for local and cloud deployment
8. Implemented application configuration using **pydantic-settings**

---

## Skills

- Python
- Discord API
- PostgreSQL
- Streamlit
- Docker
- DigitalOcean
- Pandas
- SQL
- Plotly
- Psycopg
- Requests
- Schedule
- Pydantic-settings
- SRP design

---

## Results

- Central data source for student activity on Discord
- Automatic and regular data collection without manual mentor intervention
- Clear dashboard for engagement and trend analysis
- Stable foundation for further AI feature development:
  - communication sentiment analysis
  - student activity drop prediction
  - humanized mentor bot

---

## Sample photos

![Dashboard overview](data/title.png)
![Activity pie chart](data/pie.png)
![Activity box plot](data/box.png)
