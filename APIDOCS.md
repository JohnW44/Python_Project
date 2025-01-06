# `Melody`

## Database Schema Design

[db-schema](./images/DBSchema.png)

## API Documentation

## USER AUTHENTICATION/AUTHORIZATION

### All endpoints that require authentication

All endpoints that require a current user to be logged in.

* Request: endpoints that require authentication
* Error Response: Require authentication
  * Status Code: 401
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Authentication required"
    }
    ```

### All endpoints that require proper authorization

All endpoints that require authentication and the current user does not have the
correct role(s) or permission(s).

* Request: endpoints that require proper authorization
* Error Response: Require proper authorization
  * Status Code: 403
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Forbidden"
    }
    ```

### Get the Current User

Returns the information about the current user that is logged in.

* Require Authentication: false
* Request
  * Method: GET
  * Route path: /api/auth
  * Body: none

* Successful Response when there is a logged in user
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
  {
    "email": "demo@aa.io",
    "first_name": "Demo",
    "id": 1,
    "last_name": "User",
    "likes": [],
    "profile_image": "https://m.media-amazon.com/images/M/MV5BNzBmYjBjODktMzE1ZC00NDY1LWJiYzktMWFkM2VjZDVjZTA2XkEyXkFqcGc@._V1_.jpg",
    "username": "Demo"
  }
    ```

* Successful Response when there is no logged in user
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "user": "null"
    }
    ```

### Log In a User

Logs in a current user with valid credentials and returns the current user's
information.

* Require Authentication: false
* Request
  * Method: POST
  * Route path: /api/auth/login
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "email": "demo@aa.io",
      "password": "password"
    }
    ```

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
    "email": "demo@aa.io",
    "first_name": "Demo",
    "id": 1,
    "last_name": "User",
    "likes": [],
    "profile_image": "https://m.media-amazon.com/images/M/MV5BNzBmYjBjODktMzE1ZC00NDY1LWJiYzktMWFkM2VjZDVjZTA2XkEyXkFqcGc@._V1_.jpg",
    "username": "Demo"
    }
    ```

* Error Response: Invalid credentials
  * Status Code: 401
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    
      {
    "email": [
        "Email provided not found."
    ],
    "password": [
        "No such user exists."
    ]
    }
    ```

* Error response: Body validation errors
  * Status Code: 401
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Unauthorized",
      "errors": {
        "email": "Email or username is required",
        "password": "Password is required"
      }
    }
    ```

### Log out a User
Logs out current User
* Require Authentication: True
* Request
  * Method: POST
  * Route path: /api/auth/logout
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "User logged out",
    }
    ```

### Sign Up a User

Creates a new user, logs them in as the current user, and returns the current
user's information.

* Require Authentication: false
* Request
  * Method: POST
  * Route path: /api/auth/signup
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "first_name": "John",
      "last_name": "Smith",
      "email": "john.smith@gmail.com",
      "username": "JohnSmith",
      "password": "secret password"
    }
    ```

* Successful Response
  * Status Code: 201
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
    "email": "john.smith@gmail.com",
    "first_name": "John",
    "id": 7,
    "last_name": "Smith",
    "likes": [],
    "profile_image": null,
    "username": "JohnSmith"
    }
    
    ```

* Error response: User already exists with the specified email or username
  * Status Code: 500
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
    "errors": {
        "email": [
            "Email address is already in use."
        ],
        "username": [
            "Username is already in use."
        ]
    }
    }
    ```

* Error response: Body validation errors
  * Status Code: 400
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Bad Request", 
      "errors": {
        "email": "Please provide valid email",
        "username": "Username is required",
        "firstName": "First Name is required",
        "lastName": "Last Name is required"
      }
    }
    ```

## SONGS


### Get all Songs


Returns all the songs.


* Require Authentication: false
* Request
  * Method: GET
  * Route path: api/songs
  * Body: none


* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:


    ```json
    {
    "Songs": [
        {
            "album_id": 1,
            "artist": "Daft Punk",
            "audio_file": "https://melody-songs.s3.us-east-1.amazonaws.com/07a9740ea7754e2292a349e8d6932620.mp3",
            "created_at": "Sun, 05 Jan 2025 22:46:15 GMT",
            "duration": 313,
            "id": 1,
            "images": [
                {
                    "album_id": null,
                    "id": 1,
                    "song_id": 1,
                    "url": "https://melody-images.s3.amazonaws.com/894af893cf264901abeed04663974000.jpeg"
                }
            ],
            "likes": [],
            "lyrics": "Iam a whole bunch of lyrics",
            "released_date": "Tue, 01 Jan 2013 00:00:00 GMT",
            "title": "One more time",
            "user_id": 1
        },
        {
            "album_id": 1,
            "artist": "Daft Punkers",
            "audio_file": "https://melody-songs.s3.us-east-1.amazonaws.com/07a9740ea7754e2292a349e8d6932620.mp3",
            "created_at": "Sun, 05 Jan 2025 22:46:15 GMT",
            "duration": 313,
            "id": 2,
            "images": [
                {
                    "album_id": null,
                    "id": 1,
                    "song_id": 2,
                    "url": "https://melody-images.s3.amazonaws.com/894af893cf264901abeed04663974000.jpeg"
                }
            ],
            "likes": [],
            "lyrics": "Iam a whole bunch of lyrics",
            "released_date": "Tue, 01 Jan 2015 00:00:00 GMT",
            "title": "Two more times",
            "user_id": 1
        } ]
    }
    ```




### Get details of a Song from an id


Returns the details of a song specified by its id.


* Require Authentication: false
* Request
  * Method: GET
  * Route path: api/songs/:songId
  * Body: none


* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:


    ```json
    {
    "album_id": 1,
    "artist": "Daft Punk",
    "audio_file": "https://melody-songs.s3.us-east-1.amazonaws.com/07a9740ea7754e2292a349e8d6932620.mp3",
    "created_at": "Sun, 05 Jan 2025 22:46:15 GMT",
    "duration": 313,
    "id": 1,
    "images": [
        {
            "album_id": null,
            "id": 1,
            "song_id": 1,
            "url": "https://melody-images.s3.amazonaws.com/894af893cf264901abeed04663974000.jpeg"
        }
    ],
    "likes": [],
    "lyrics": "Iam a whole bunch of lyrics",
    "released_date": "Tue, 01 Jan 2013 00:00:00 GMT",
    "title": "One more time",
    "user_id": 1
    }
    ```


* Error response: Couldn't find a Song with the specified id
  * Status Code: 404
  * Headers:
    * Content-Type: application/json
  * Body:


    ```json
    {
      "error": "Song couldn't be found"
    }
    ```


### Add a Song


Adds and returns a new song when a user is signed in.


* Require Authentication: true
* Request
  * Method: POST
  * Route path: api/songs
  * Headers:
    * Content-Type: application/json
  * Body:


    ```json
  {
    "Songs": [
        {
            "title": "Happy birthday",
            "artist": "Daft Punk",
            "released_date": "2024-12-19", 
            "album_id": 1,
            "duration": 180, 
            "lyrics": "Happy birthday to you"
        }
    ],
    "Images": [
        {
            "url": "image url"
        }
    ]
  }
    ```


* Successful Response
  * Status Code: 201
  * Headers:
    * Content-Type: application/json
  * Body:


  ```json
  {
    "Songs": {
        "album_id": 1,
        "artist": "Daft Punk",
        "created_at": "Fri, 20 Dec 2024 17:40:06 GMT",
        "duration": 180,
        "id": 3,
        "images": [
            {
                "album_id": 1,
                "id": 3,
                "song_id": 3,
                "url": "image url"
            }
        ],
        "likes": [],
        "lyrics": "Happy birthday to you",
        "released_date": "Thu, 19 Dec 2024 00:00:00 GMT",
        "title": "Happy birthday",
        "user_id": 1,
    }
  }
    ```


* Error Response: Body validation errors
  * Status Code: 400
  * Headers:
    * Content-Type: application/json
  * Body:


    ```json
 
     {
       "message": "Bad Request",
       "errors": {
          "title": "Title is required",
          "artist": "Artist is required",
          "released_date": "Release year is required",
          "album_id": "Album id is required",
          "user_id": 1,
          "lyrics": "Happy birthday too youu",
        }
      ,
      "Images": [
        {
          "id": 1,
          "url": "Image url is required",
        },
      ]
    }
  ```


### Update a Song


Updates and returns an existing song.


* Require Authentication: true
* Require proper authorization: Song must belong to the current user
* Request
  * Method: PUT
  * Route path: api/songs/:songId
  * Headers:
    * Content-Type: application/json
  * Body:


    ```json
     {
      "Songs": [
        {
          "title": "Happy birthday",
          "artist": "Big Bird",
          "release_year": "1545",
          "album_id": 1,
          "user_id": 1,
          "lyrics": "Happy birthday too youu",
          "duration": 900
        }
      ],
      "Images": [
        {
          "id": 1,
          "url": "image url",
        },
      ]
    }
    ```


* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:


    ```json
  {
    "Songs": {
        "album_id": 2,
        "artist": "Updated Artist",
        "created_at": "Fri, 20 Dec 2024 17:48:58 GMT",
        "duration": 900,
        "id": 4,
        "images": [
            {
                "album_id": 1,
                "id": 4,
                "song_id": 4,
                "url": "image url"
            }
        ],
        "likes": [],
        "lyrics": "Updated lyrics here...",
        "released_date": "Sun, 01 Dec 2024 00:00:00 GMT",
        "title": "newTitle",
        "user_id": 1
    }
  }
    ```


* Error Response: Body validation errors
  * Status Code: 400
  * Headers:
    * Content-Type: application/json
  * Body:


    ```json
   {
    "error": "{object} cannot be empty"
   }
    ```
* Error response: User not authorized to delete song
  * Status Code: 403
  * Headers:
    * Content-Type: application/json
  * Body:


    ```json
    {
      "message": "Unauthorized"
    }
    ```


* Error response: Couldn't find a Song with the specified id
  * Status Code: 404
  * Headers:
    * Content-Type: application/json
  * Body:


    ```json
    {
      "message": "Song couldn't be found"
    }
    ```


### Delete a Song


Deletes an existing song.


* Require Authentication: true
* Require proper authorization: Song must belong to the current user
* Request
  * Method: DELETE
  * Route path: api/songs/:songId
  * Body: none


* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:


    ```json
    {
      "message": "Song Successfully deleted"
    }
    ```


* Error response: Couldn't find a Song with the specified id
  * Status Code: 404
  * Headers:
    * Content-Type: application/json
  * Body:


    ```json
    {
      "message": "Song couldn't be found"
    }
    ```


* Error response: User not authorized to delete song
  * Status Code: 403
  * Headers:
    * Content-Type: application/json
  * Body:


    ```json
    {
      "message": "Unauthorized"
    }
    ```

## ALBUMS


### Users should be able to Create albums


Creates an album.


* Require Authentication: true
* Require proper authorization: false
* Request
  * Method: POST
  * Route path: /albums/:albumId/
  * Body:
  ```json
  {
    "title":"Create album",
    "artist": "artist name",
    "released_year": 20237,
    "duration": 4534,
    "images" : [
      "https://m.media-amazon.com/images/M/MV5BNDRkM2NjMzctNGNmNy00ZjUzLWJlN2UtM2ZlZGI5M2NkMTAyXkEyXkFqcGc@._V1_.jpgdd"
      ]
  }
  ```


* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:


    ```json
    {
    "Album": {
        "artist": "artist name",
        "created_at": "Thu, 19 Dec 2024 17:52:12 GMT",
        "duration": 4534,
        "id": 5,
        "images": [
            {
                "album_id": 5,
                "id": 4,
                "song_id": null,
                "url": "https://m.media-amazon.com/images/M/MV5BNDRkM2NjMzctNGNmNy00ZjUzLWJlN2UtM2ZlZGI5M2NkMTAyXkEyXkFqcGc@._V1_.jpgdd"
            }
        ],
        "released_year": 20237,
        "songs": [],
        "title": "Create album",
        "user_id": 1
    },
    "message": "Album successfully created"
    }
    ```


* Error response: Please enter all required fields
  * Status Code: 404
  * Headers:
    * Content-Type: application/json
  * Body:


    ```json
    {
    "message": "Please enter required fields"
    }
   ```


### Get all Albums


Returns all the albums.


* Require Authentication: false
* Request
  * Method: GET
  * Route path: /albums
  * Body: none


* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:
  ```json
    {
      "Album": [
        {
          "id": 1,
          "playlistId": 4,
          "artist": "Big Bird",
          "released_year": 2022,
          "created_at": "2022-11-19 20:39:36",
          "title": "Happy Songs",
          "Images": [
            {
              "id": 1,
              "url": "image url"
            }
          ],
        }
      ]
    }
    ```


### Get all Songs by an Album's id


Returns all the songs that belong to an album specified by id.


* Require Authentication: false
* Request
  * Method: GET
  * Route path: api/albums/:albumId/songs
  * Body: none


* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:


    ```json
   
    {
    "Songs": [
        {
            "album_id": 1,
            "artist": "Big Bird",
            "created_at": "Wed, 18 Dec 2022 12:13:46 GMT",
            "duration": 400,
            "id": 1,
            "lyrics": "gadsfgeag",
            "released_date": "Tue, 01 Jan 2013 00:00:00 GMT",
            "title": "first",
            "user_id": 1
        },
        {
            "album_id": 1,
            "artist": "Big Bird",
            "created_at": "Wed, 18 Dec 2022 12:13:46 GMT",
            "duration": 450,
            "id": 2,
            "lyrics": "gweagwea",
            "released_date": "Fri, 01 Feb 2013 00:00:00 GMT",
            "title": "second ",
            "user_id": 1
        }
      ]
    }
    ```


* Error response: Couldn't find a Album with the specified id
  * Status Code: 404
  * Headers:
    * Content-Type: application/json
  * Body:


    ```json
    {
      "message": "No Album found"
    }
    ```


 ### Users should be able to view all albums created by users


Returns all the albums created by the user.


* Require Authentication: true
* Request
  * Method: GET
  * Route path: albums/users/:userId
  * Body: none


* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:


    ```json
    {
      "Albums": [
        {
          "id": 1,
          "title": "Happy Songs",
          "artist": "Big Bird",
          "album_id": 1,
          "duration": 500,
          "created_at": "Thu, 19 Dec 2024 11:53:11 GMT",
          "released_year": 2013,
          "images": [
                {
                    "album_id": 1,
                    "id": 1,
                    "song_id": 1,
                    "url": "https://cdn-p.smehost.net/sites/35faef12c1b64b21b3fda052d205af13/wp-content/uploads/2023/02/230222-daftpunk-ram10.jpg"
                }
            ],
        }
      ]
    }
    ```


  * Error response: Couldn't find album with the specified id
  * Status Code: 404
  * Headers:
    * Content-Type: application/json
  * Body:


    ```json
    {
      "message": "No Albums found"
    }
    ```


### Add Songs to an User created Album based on Album's id


Add Songs based on albumId if user is album owner.


* Require Authentication: True
* Request
  * Method: POST
  * Route path: api/albums/:albumId/:userId/songs
  * Body: none


* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:


    ```json
    {
        "songid": 8
    }


    ```


    * Successful Response
  * Status Code: 201
  * Headers:
    * Content-Type: application/json
  * Body:


    ```json
    {
    "Album": [
        {
            "artist": "Daft Punk",
            "created_at": "Thu, 19 Dec 2024 14:03:12 GMT",
            "duration": 4464,
            "title": "Random Access Memories",
            "user_id": 1,
            "id": 1,
            "images": [
                {
                    "album_id": 1,
                    "id": 1,
                    "song_id": 1,
                    "url": "https://cdn-p.smehost.net/sites/35faef12c1b64b21b3fda052d205af13/wp-content/uploads/2023/02/230222-daftpunk-ram10.jpg"
                }
            ],
            "released_year": 2013,
            "songs": [
                {
                    "album_id": 1,
                    "artist": "Daft Punk",
                    "created_at": "Thu, 19 Dec 2024 14:03:12 GMT",
                    "duration": 200,
                    "id": 8,
                    "lyrics": "buy it, use it, break it, fix it, trash it, change it, mail, upgrade it",
                    "released_date": "Tue, 17 May 2005 00:00:00 GMT",
                    "title": "Technologic",
                    "user_id": 1
                }
            ],
          }
      ],
      "message": "Song successfully added to Album"
    }
    ```


* Error response: Couldn't find a Album with the specified id
  * Status Code: 404
  * Headers:
    * Content-Type: application/json
  * Body:


    ```json
    {
      "message": "Album Not Found"
    }
    ```
    
### Users should be able to remove songs from albums based on AlbumId


Deletes an existing song, based on AlbumId.


* Require Authentication: true
* Require proper authorization: Song must belong to the current user
* Request
  * Method: DELETE
  * Route path: api/albums/:albumId/:userId/songs
  * Body: none


* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:


    ```json
    {
      "message": "Successfully deleted"
    }
    ```


* Error response: Couldn't find a Album with the specified id
  * Status Code: 404
  * Headers:
    * Content-Type: application/json
  * Body:


    ```json
    {
      "message": "Album couldn't be found"
    }
    ```


### Users should be able to DELETE albums based on AlbumId


Deletes an existing album, based on AlbumId.


* Require Authentication: true
* Require proper authorization: Album must belong to the current user
* Request
  * Method: DELETE
  * Route path: api/albums/:albumId
  * Body: none


* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:


    ```json
    {
      "message": " Successfully deleted"
    }
    ```


* Error response: Couldn't find a Album with the specified id
  * Status Code: 404
  * Headers:
    * Content-Type: application/json
  * Body:


    ```json
    {
      "message": "Album couldn't be found"
    }
   ```
   



## LIKES

### Users should be able to like a Song

Like song based on songId


* Require Authentication: true
* Request
  * Method: POST
  * Route path: api/users/:userId/likedsongs
  * Body: 
  ```json
  {
    "song_id": 1
  }
  ```
* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "Songs": [
        {
          "id": 1,
          "song_id": 1,
          "artist": "Big Bird",
          "album_id": 1,
        }
      ]
    }
    ```
* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Successfully Liked Song"
    }
    ```

* Error response: Couldn't find Song with the specified id
  * Status Code: 404
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Song couldn't be found"
    }
   ```

### Users should be able to unlike a Song

Unlike song based on songId


* Require Authentication: true
* Request
  * Method: PUT
  * Route path: api/users/:userId/likedsongs
  * Body: none
* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "Songs": [
        {
          "id": 1,
          "title": "Happy birthday",
          "artist": "Big Bird",
          "album_id": 1,
          "duration": 500,
        }
      ]
    }
    ```
* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Successfully Unliked Song"
    }
    ```

* Error response: Couldn't find Song with the specified id
  * Status Code: 404
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Song couldn't be found"
    }
   ```

   ### Get all Songs liked by the Current User

  Returns all the songs liked by the current user.

  * Require Authentication: true
  * Request
  * Method: GET
  * Route path: api/users/:userId/likedsongs
  * Body: none
  * Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "Songs": [
        {
          "id": 1,
          "title": "Happy birthday",
          "artist": "Big Bird",
          "album_id": 1,
          "duration": 500,
        }
      ]
    }
    ```
    

