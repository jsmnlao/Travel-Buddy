# ✈️ Travel Buddy

Travel Buddy aims to ease the stress of planning a trip. Everyone loves to travel but rarely does anyone like to plan. With Travel Buddy, users can simply input a desired destination and receive suggestions from Travel Buddy. Users can customize and finalize plans within the system by manually setting flight dates and times, hotel information, and fun excursions into our system. Are users completely lost with where to start? Our ChatGPT API integration can list out an entire suggested trip to their destination, within their budget. Travel Buddy displays all this information out in a dashboard to give users a clear overview of their ideal trip.

## 🙌 Team Members

| Name            | GitHub Handle | Contribution |
| --------------- | ------------- | ------------ |
| **Jasmine Lao** | @jsmnlao      |              |
| **Megan Ju**    | @Megan-J      |              |

## 🏗️ Project Overview

## 📚 Technical Stack

- Python
- Flask Server

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

5. Install all necessary dependencies with `pip install -r requitements.txt`
6. Start the project with `flask run`
7. Following the instructions on your CLI, open the website through the port given

### Dependencies

1. Amadeus API

- Instructions for obtaining the API Key and Secret can be found [here](https://developers.amadeus.com/self-service/apis-docs/guides/developer-guides/quick-start/)
