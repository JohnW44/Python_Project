# Melody

## General Info
Melody is a music platform for users to add music files and create their own albums, as well as view other users uploaded albums and play their songs in the browser.

## Features
* User authentication (signup, login, demo user)
* Create and manage Songs, saved by AWS
* Create profile with favorite songs and images saved by AWS
* Create Album and update, or remove albums

## Technologies
Project is created with:
* Frontend:
  * React 18
  * Redux
  * AWS
  * Vite
  * Wavesurfer.js
* Backend:
  * Python 3.9
  * Flask
  * SQLAlchemy
  * PostgreSQL
* Deployment:
  * Docker
  * Gunicorn

## Setup

### Prerequisites
* Python 3.9+
* Node.js
* PostgreSQL
* AWS API key

### Local Development
1. Clone the repository:
    ```bash
    git clone  https://github.com/JohnW44/Python_Project.git
    ```

2. Install dependencies

      ```bash
      pipenv install -r requirements.txt
      ```

3. Create a .env file
   ```
   SECRET_KEY=<your-secret-key>
   DATABASE_URL=sqlite:///dev.db
   SCHEMA=SCHEMA
   S3_Bucket=<your-S3-Bucket> 
   S3_KEY=<your-AWS-api-key>
   S3_SECRET=<your-AWS-secret-key>
   ```

4. For the backend get into your pipenv, migrate your database, seed your database, and run your Flask app

   ```bash
   pipenv shell
   ```

   ```bash
   flask db upgrade
   ```

   ```bash
   flask seed all
   ```

   ```bash
   flask run
   ```

5. To run the React frontend, cd into react-vite, run `npm i` to install dependencies.

    Next run `npm run dev`

    Both servers should be running on ports 5000 for backend and 5173 for front end to view the application locally.

## Usage

### User Features

1. **Account Management**
   * Create a new account or use demo login
   * Update profile information

2. **Add a Song**
   * Create a Song, fill out the form and add an image and music file
   * Update the Song
   * Delete the Song
   * Play songs with wavesurfer in song details page
   * View other users songs

3. **Create Album**
   * Add custom album, fill out the form
   * Update the album and add more songs
   * Remove the album or remove songs from album
   * View albums from other users

4. **Likes**
   * Like songs by clicking the star in the side nav bar
   * Liked songs will populate profile page in profile dropdown menu
   * Can remove liked songs 
   * Can play liked songs in wavesurfer player in user page



## Project Status
Project is: in progress

Current development focuses on:
* Enhancing user experience
* Adding playlist feature
* Adding more robust navigation througout the app


## Acknowledgements
* John and Dan for making a four person project workable with two people
