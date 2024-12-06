# NUTrack

Link to Project Demo Video: https://youtu.be/kdu2AG0IZ9w

## Team Members
- **Christian Bacalhau** ([ChristianBacalhau](https://github.com/ChristianBacalhau))  
- **Robel Wondwosen** ([RobW321](https://github.com/RobW321))  
- **Matthew Faust** ([MatthewFaust](https://github.com/MatthewFaust))  
- **Samson Ajayi** ([sajayi12](https://github.com/sajayi12))  
- **Gurshan Sidhu** ([gurshan-sidhu](https://github.com/gurshan-sidhu))  
- **Rohan Batra** ([StubblySeeker](https://github.com/StubblySeeker))  

## Project Overview
In today’s competitive tech job market, students often find themselves applying to hundreds of co-ops and internships just to secure a single interview. This process can be overwhelming and disorganized, with many resorting to basic spreadsheets or notes apps that lack the tools needed to track progress effectively.  

Our application, **NUTracks**, addresses this problem by providing a dedicated, data-driven job application tracker tailored for co-op searches. With NUTracks, students can:
- Organize their applications
- Filter by status, priority, or other criteria
- Prioritize their next steps with ease  

NUTracks empowers students to take control of their co-op search process, reducing stress and improving outcomes.

## Code Structure

### Backend
The backend code is located in the `api/backend` directory. Each folder within this directory contains `GET`, `POST`, `PUT`, and `DELETE` routes specific to its respective blueprint. The `rest_entry.py` file is responsible for registering all blueprints within our application, ensuring clean and modular routing.

### Frontend
The frontend code is located in the `app/src` directory. It is built using modular design principles, with two primary components:  

1. **Modules Folder**  
   Contains reusable components, such as the navigation sidebar, which appears on every screen in the app.

2. **Pages Folder**  
   Contains all individual web pages. Each user persona has a dedicated homepage for a personalized experience. One page for each database interaction that can be refrenced by multiple personas. 

3. **Home file**
    Contains the home/landing page of our app with buttons to navagate through each user and their pages. 
    

