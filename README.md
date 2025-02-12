# Animal Shelter Dashboard

## Overview
The **Animal Shelter Dashboard** is a **Python-based web application** built using **Dash, MongoDB, and Plotly**. Originally developed during **CS-340**, this dashboard allows users to **filter, visualize, and analyze animal rescue data** stored in a **MongoDB database**. The application provides **interactive filtering, data visualization, and geo-location mapping**, making it a powerful tool for managing and understanding animal shelter records.

## Features
✅ **Database Integration** – Uses **MongoDB** with an optimized **CRUD module** for efficient data retrieval.  
✅ **Data Visualization** – Implements **Dash and Plotly** to generate **interactive pie charts and tables**.  
✅ **Geo-Location Mapping** – Uses **Dash Leaflet** to display **real-time locations of shelter animals**.  
✅ **Performance Optimization** – Enhances **MongoDB query efficiency** using **aggregation pipelines**.  
✅ **User Interaction** – Allows **filtering by rescue type**, sorting, and selecting specific records.  

## Enhancements Made
- **Expanded the database**: Added **new animals** (cats, parrots, hamsters) for a more diverse dataset.  
- **Optimized filtering and sorting**: Improved query performance for **real-time** data updates.  
- **Added visual insights**: Implemented **pie charts** to display animal breed distribution.  
- **Integrated geo-mapping**: Displayed animal locations using **Dash Leaflet** for spatial analysis.  

## Justification for Inclusion in ePortfolio
This artifact was chosen for my **ePortfolio** because it demonstrates **full-stack development, database management, and data visualization skills**. Key highlights of this project include:

- **Scalable Data Processing**: Optimized large dataset retrieval using **MongoDB aggregation**.  
- **Interactive UI**: Designed a **user-friendly dashboard** with **real-time updates**.  
- **Database Optimization**: Ensured **fast and secure access** to animal shelter data.  

The **enhanced version** of this dashboard reflects **best practices in software engineering**, ensuring **performance, maintainability, and usability**.

## Course Outcomes Achieved
✔ **Design and Evaluate Computing Solutions** – Created an optimized **database-driven** dashboard with enhanced interactivity.  
✔ **Use of Innovative Techniques and Tools** – Leveraged **Dash, Plotly, MongoDB aggregation, and Leaflet mapping**.  
✔ **Develop a Security Mindset** – Optimized **data handling** and prevented vulnerabilities.  

## Reflection on the Enhancement Process
### **Key Learnings**
- **Database Optimization Matters** – Improved **MongoDB indexing and query efficiency**.  
- **Interactive UI Enhancements Improve Usability** – Adding **charts and maps** made the dashboard more intuitive.  
- **Performance Trade-offs** – Balanced **query speed, real-time updates, and data accuracy** for a smooth user experience.  

### **Challenges Faced**
⚠ **Data Expansion & Integrity** – Ensuring **consistency** while adding new animal records.  
⚠ **Query Optimization** – Fine-tuning **MongoDB aggregation pipelines** for **faster** data retrieval.  
⚠ **Geo-Location Integration** – Mapping animal locations required **careful formatting of lat/lon data**.  

## Setup & Installation
### **Prerequisites**
- **Python 3.x**
- **MongoDB Atlas or Local MongoDB**
- **Required Python Libraries**
  ```sh
  pip install dash jupyter_dash pandas pymongo dash-leaflet plotly
