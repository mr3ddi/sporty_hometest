# Home Test - Sporty Group

This repository contains the automated test solutions for the Home Test assignment. It is divided into two parts:
1. **Web App Testing:** A scalable Selenium framework using the Page Object Model (POM) to test the Twitch mobile web view.
2. **API Testing:** An automated test suite using `pytest` and `requests` to validate the JSONPlaceholder API.


## Project Structure

The project follows a standard Page Object Model (POM) structure to ensure scalability and separation of concerns.

```
├── pages/
│   ├── base_page.py           # Shared methods (clicks, scrolls, waits)
│   └── home_page.py           # Twitch-specific locators and logic
├── tests/
│   ├── conftest.py            # Pytest fixtures (Driver setup, Mobile Emulation)
│   ├── test_twitch_mobile.py  # Part A: Twitch Test Script
│   └── test_api.py            # Part B: API Test Script
├── requirements.txt           # Project dependencies
└── README.md                  # Documentation

```

## Setup & Installation
Prerequisites
* Python 3.x installed
* Google Chrome installed

Installation
* Clone this repository.

Install the required Python packages:
```pip install -r requirements.txt```

## Part A: Web App (Selenium)
This framework automates a user flow on Twitch.tv using Chrome Mobile Emulation 
(configured for Pixel 7).

Scenarios Covered
* Mobile Emulation: launches Chrome in "Pixel 7" mode.
* Popup Handling: Automatically handles Cookie Consent, "Open in App" banners, and Mature Content warnings.
* Search Workflow: Navigates to "Browse", searches for "StarCraft II", and selects the correct game category.
* Dynamic Content: Scrolls down to load live streamers and selects a random streamer from the results.
* Validation: Waits for the video player to load and captures a confirmation screenshot.

How to Run: 
 ```pytest tests/test_sporty_mobile.py```

Execution Demo 
![](starcraft_twitch.gif)

## Part B: API Tests
This tests the JSONPlaceholder API (https://jsonplaceholder.typicode.com/.)

How to Run:
```pytest tests/test_api.py -v```

Test Cases
- `1.` test_get_single_post --> GET	Verifies that fetching a valid resource ID returns 200 OK and the correct data fields.
- `2.` test_get_non_existent_resource --> GET Negative Test: Verifies that fetching a non-existent ID returns 404 Not Found.
- `3.` test_create_post	POST --> POST Verifies that creating a new resource returns 201 Created and echoes the sent payload.
- `4.` test_get_users_parametrized --> GET Parametrized: Validates data consistency for multiple distinct user IDs to ensure coverage.