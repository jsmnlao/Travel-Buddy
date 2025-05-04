# ✈️ Travel Buddy

Travel Buddy aims to ease the stress of planning a trip. Everyone loves to travel but rarely does anyone like to plan. With Travel Buddy, users can simply input a desired destination and receive suggestions from Travel Buddy. Users can customize and finalize plans within the system by manually setting flight dates and times, hotel information, and fun excursions into our system. Are users completely lost with where to start? Our Amadeus API integration can list out an entire suggested trip to their destination, within their budget. Travel Buddy displays all this information out in a dashboard to give users a clear overview of their ideal trip.

## 🙌 Team Members

| Name            | GitHub Handle | Contribution |
| --------------- | ------------- | ------------ |
| **Jasmine Lao** | @jsmnlao      |              |
| **Megan Ju**    | @Megan-J      |              |

## 🏗️ Project Overview
Traveling is an exciting and memorable experience, but for people who want to be well-prepared for trips, planning the details can be a hassle. From booking flights to researching activities and food options while staying on budget, the planning process can be discouraging. That’s why Travel Buddy was developed to simplify and organize travel planning, making the process more enjoyable, personalized, and most importantly, stress-free. 

Travel Buddy offers a variety of features designed to allow users to customize and finalize their plans to organize all essential trip details. Features of Travel Buddy include:

1. **Comprehensive Dashboard**: This hub presents all the necessary trip information in a user-friendly way. This dashboard gives an organized view of the itinerary, flight information, booking confirmations, and any activities on the schedule. With this feature, every aspect of the trip is contained in one central place for easy access.
2. **Customizable Trip Planning**: Users can manually input key details such as flight dates and flight number, hotel reservation, and activities. This feature allows user to have full control over their itinerary and fine-tune their trip plans to their personal preferences. 
3. **AI-Generated Itinerary**: By integrating with the Amadeus API, users can automatically generate a complete trip itinerary if they don’t know where to start. Based on the user’s destination and budget, this AI-driven feature will recommend a full itinerary and suggest activities for users who are not sure where to begin. 

Our app aims for a wide range of users who are seeking a simpler way to plan their trips. Our primary audience includes:
- _Casual Travelers_: Individuals who are looking for a well-planned trip but find trip planning stressful and time-consuming
- _Students_: Users who want AI-assisted travel recommendations and an organized place for itinerary management 
- _First-time Travelers_: Individuals who may feel overwhelmed in their first travel experience and are looking for recommendations or suggestions 

Travel Buddy is designed to tailor to each traveler’s needs by offering users full control over every aspect of their trip through manual setup, while also curating travel plans for those who need a little more assistance to get started. With a combination of customization and AI-assistance, our app provides the tools for traveling users to plan their trips effortlessly and efficiently. 


## 📚 Technical Stack

- Frontend: **Bootstrap** framework for built-in components, consistency, and responsiveness
- Backend: **Flask** (Python) to handle backend logic, routing, processing user input, and integration with external services
- Database: **SQLite**, a simple and lightweight database ideal for small applications and its easy integration with Flask 
- External: **Amadeus API**

## 👩🏽‍💻 Setup & Execution

### To execute this project on your machine:

1. Clone the reposity with `git clone` and the web URL found in the `<> Code` drop down above.
2. Download and install Python on your device. You can follow the instructions [here](https://www.python.org/downloads/).
3. Navigate to the project through your CLI
4. Open the project in an IDE or create a `.env` file inside the project directory.

In this file, you will need to get the API Client ID and Secret Keys for each of the dependencies listed below. Your `.env file` should look something like this:

```
AMADEUS_CLIENT_ID=<here you put your client id>
AMADEUS_CLIENT_SECRET=<here you put your secret>
```

5. Install all necessary dependencies with `pip install -r requirements.txt`
6. Start the project with `flask run`
7. Following the instructions on your CLI, open the website through the port given

### Dependencies

1. Amadeus API

- Instructions for obtaining the API Key and Secret can be found [here](https://developers.amadeus.com/self-service/apis-docs/guides/developer-guides/quick-start/)
