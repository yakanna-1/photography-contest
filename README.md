# Photography Contest Management System

## Introduction
The **Photography Contest Management System** is a web-based platform that allows users to submit photos for contests, rate other participants' photos, and view contest results. It provides a seamless experience for both contestants and judges.

## Features
- **Photo Submission**: Users can upload their photos for a contest.
- **Photo Rating**: Judges or users can rate submitted photos.
- **Contest Results**: Displays top-rated photos based on ratings.
- **Dynamic Web Pages**: Uses Flask for backend logic and HTML/CSS for the frontend.

## Technologies Used
- **Backend**: Python (Flask)
- **Frontend**: HTML, CSS
- **Static Files**: CSS for styling

## File Structure
```
Photography Contest Management System/
│── app.py                     # Main backend application (Flask)
│── static/
│   └── styles.css             # CSS for frontend styling
│── templates/
│   ├── home.html              # Homepage
│   ├── submit_photo.html      # Photo submission page
│   ├── rate_photos.html       # Photo rating page
│   ├── results.html           # Contest results page
```

## Installation & Setup
1. **Clone the Repository**
   ```sh
   git clone <repository_link>
   cd Photography-Contest-Management-System
   ```
2. **Install Dependencies**
   ```sh
   pip install flask
   ```
3. **Run the Application**
   ```sh
   python app.py
   ```
4. **Access the System**
   Open a web browser and go to `http://127.0.0.1:5000`

## Usage
- **Participants**: Submit photos for the contest.
- **Judges/Users**: Rate the submitted photos.
- **View Results**: Check the leaderboard of top-rated photos.

## Future Enhancements
- Implement authentication for users and judges.
- Add a database (e.g., SQLite, MySQL) to store photo submissions and ratings.
- Enhance UI with JavaScript and more styling.

## License
This project is open-source and free to use under the MIT License.

