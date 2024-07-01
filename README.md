# Phone Number Tracker

## Description

This project includes two Python scripts for tracking the location and carrier information of a phone number. The first script uses the `phonenumbers` library to get the geographic location and carrier, and then visualizes the location on a map using `folium`. The second script is a GUI-based application that allows users to enter a phone number and get the country associated with it using the `pycountry` library and `tkinter`.

## Scripts

### `tracker1.py`

This script does the following:
- Takes a phone number with country code as input.
- Parses the phone number to extract location and carrier details.
- Uses the `OpenCageGeocode` API to get the latitude and longitude of the location.
- Generates a map with a marker showing the location and saves it as an HTML file.

### `gsmgpstracker.py`

This is a GUI-based application that:
- Accepts a phone number input from the user.
- Determines the country of the phone number using the `pycountry` library.
- Displays the country in a GUI window.

## Installation

To run these scripts, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/phone-number-tracker.git
   cd phone-number-tracker
   ```

# 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

# 3. Install Dependencies

```bash
pip install -r requirements.txt
```

# Usage
## Running tracker1.py
   1. Open a terminal.
   2. Run the script:
```bash
    python tracker1.py
```
    3. Enter the phone number with the country code when prompted (e.g., +14155552671).
    4. The script will output the location and carrier information, and generate an HTML file (Location.html) with a map showing the location.

## Running gsmgpstracker.py
    1. Open a terminal.
    2. Run the script:
```bash
    python gsmgpstracker.py
```
    3. A GUI window will appear.
    4. Enter a phone number in the input field and click the "Track Country" button.
    5. The application will display the country associated with the phone number.

# Dependencies

## The following Python libraries are required for these scripts:
```bash
    phonenumbers
    folium
    opencage
    pycountry
    tkinter
    phone_iso3166
```
You can install all dependencies using the provided requirements.txt file.

# Example Outputs

    tracker1.py

### Console Output:
```bash
Enter the PhoneNumber with the country code : +14155552671
location : California
service provider : AT&T
```

### Generated HTML File:
    A map centered at the location with a marker showing the place name.

        gsmgpstracker.py

### GUI Window:
        Displays a text box to enter the phone number.
        Shows the country name after clicking the "Track Country" button.
