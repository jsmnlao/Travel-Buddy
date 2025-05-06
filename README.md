# ✈️ Travel Buddy

Travel Buddy aims to ease the stress of planning a trip. Everyone loves to travel but rarely does anyone like to plan. With Travel Buddy, users can simply input a desired destination and receive suggestions from Travel Buddy. Users can customize and finalize plans within the system by manually setting flight dates and times, hotel information, and fun excursions into our system. Are users completely lost with where to start? Our LLaMA integration can list out an entire suggested trip to their destination, within their budget. Travel Buddy displays all this information out in a dashboard to give users a clear overview of their ideal trip.

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
3. **AI-Generated Itinerary**: By integrating with the LLaMA, users can automatically generate a complete trip itinerary if they don’t know where to start. Based on the user’s destination and budget, this AI-driven feature will recommend a full itinerary and suggest activities for users who are not sure where to begin.

Our app aims for a wide range of users who are seeking a simpler way to plan their trips. Our primary audience includes:

- _Casual Travelers_: Individuals who are looking for a well-planned trip but find trip planning stressful and time-consuming
- _Students_: Users who want AI-assisted travel recommendations and an organized place for itinerary management
- _First-time Travelers_: Individuals who may feel overwhelmed in their first travel experience and are looking for recommendations or suggestions

Travel Buddy is designed to tailor to each traveler’s needs by offering users full control over every aspect of their trip through manual setup, while also curating travel plans for those who need a little more assistance to get started. With a combination of customization and AI-assistance, our app provides the tools for traveling users to plan their trips effortlessly and efficiently.

## 📚 Technical Stack

- Frontend: **Bootstrap** - framework for built-in components, consistency, and responsiveness.
- Backend: **Flask** - (Python) to handle backend logic, routing, processing user input, and integration with external services.
- Database: **SQLite** - a simple and lightweight database ideal for small applications and its easy integration with Flask.
- External: **LLaMA** - powers local language understanding and generation using a lightweight transformer model.

## 👩🏽‍💻 Setup & Execution

### To execute this project on your machine:

1. Clone the repository with `git clone` and the web URL found in the `<> Code` drop down above.
2. Download and install Python on your device. You can follow the instructions [here](https://www.python.org/downloads/).
3. Open the project in an IDE or create a .env file inside the project directory.
   In this file, you will need to get the API Key to add LLaMA. Your .env file should look something like this:

```
OPENROUTER_API_KEY=your_api_key
```

4. Get your API Key from [here](https://openrouter.ai/)
5. Navigate to the project through your CLI
6. Start the virtual environment by typing `source env/bin/activate` for Mac or `env\Scripts\activate.bat` for Windows (CMD) or `env\Scripts\Activate.ps1` for Windows (PowerShell)
7. Install all necessary dependencies with `pip install -r requirements.txt`
8. Start the project with `flask run --port 5050`
9. Following the instructions on your CLI, open the website through the port given

To deactivate the environment use `deactivate`.
