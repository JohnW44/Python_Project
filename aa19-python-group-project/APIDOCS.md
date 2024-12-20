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
      "user": {
        "id": 1,
        "firstName": "John",
        "lastName": "Smith",
        "email": "john.smith@gmail.com",
        "username": "JohnSmith"
      }
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
  * Method: GET
  * Route path: /api/auth/login
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "credential": "john.smith@gmail.com",
      "password": "secret password"
    }
    ```

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "user": {
        "id": 1,
        "first_name": "John",
        "last_name": "Smith",
        "email": "john.smith@gmail.com",
        "username": "JohnSmith"
      }
    }
    ```

* Error Response: Invalid credentials
  * Status Code: 401
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Invalid credentials"
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
        "credential": "Email or username is required",
        "password": "Password is required"
      }
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
        "id": 1,
        "first_name": "John",
        "last_name": "Smith",
        "email": "john.smith@gmail.com",
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
      "message": "User already exists",
      "errors": {
        "email": "User with that email already exists",
        "username": "User with that username already exists"
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
        "email": "Invalid email",
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
  * Route path: /songs
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
          "created_at": "2021-11-19 20:39:36",
          "duration": 500,
          "id": 1,
          "images": [
            {
              "album_id": 1,
              "id": 1,
              "song_id":1,
              "url": "url"
            }
          ],
          "lyrics": "Happy birthday too youu",
          "released_date": "year, month, date",
          "title": "Happy birthday",
          "user_id": 1,
        }
      ]
    }
    ```


### Get details of a Song from an id

Returns the details of a song specified by its id.

* Require Authentication: false
* Request
  * Method: GET
  * Route path: /songs/:songId
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
          "released_date": "1545",
          "created_at": "2021-11-19 20:39:36",
          "album_id": 1,
          "user_id": 1,
          "duration": 500,
          "lyrics": "Happy birthday too youu",
          "like": "True",
          "likeCount": 20,
        }
      ],
      "Images": [
        {
          "album_id": 1,
          "id": 1,
          "song_id": 1,
          "url": "image url",
        },
      ]
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

### Add a Song

Adds and returns a new song when a user is signed in.

* Require Authentication: true
* Request
  * Method: POST
  * Route path: /songs
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "Songs": [
        {
          "title": "Happy birthday",
          "artist": "Big Bird",
          "released_date": "1545",
          "album_id": 1,
          "user_id": 1,
          "lyrics": "Happy birthday too youu",
          //"genre": "kids songs"
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
  * Status Code: 201
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
          "released_date": "1545",
          "created_at": "2021-11-19 20:39:36",
          "album_id": 1,
          "user_id": 1,
          "duration": 500,
          "lyrics": "Happy birthday too youu",
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
  * Route path: /songs/:songId
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
      "Songs": [
        {
          "id": 1,
          "title": "Happy birthday",
          "artist": "Big Bird",
          "release_year": "1545",
          "created_at": "2021-11-19 20:39:36",
          "album_id": 1,
          "user_id": 1,
          "duration": 500,
          "lyrics": "Happy birthday too youu",
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
          "release_year": "Release year is required",
          "album_id": "Album id is require",
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
  * Route path: /songs/:songId
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

<!-- ### Create a comment for a Song based on the Song's id

Create and return a new comment for a song specified by id.

* Require Authentication: true
* Request
  * Method: POST
  * Route path: /songs/:songId/comments
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "comment": "This is an awesome song!",
    }
    ```

* Successful Response
  * Status Code: 201
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "id": 1,
      "userId": 1,
      "songId": 1,
      "comment": "This is an awesome song!",
      "createdAt": "2021-11-19 20:39:36"
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
        "comment": "Comment is required"
      }
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

### Delete a Comment for a Song based on the Song's id

Deletes an existing comment.

* Require Authentication: true
* Require proper authorization: Comment must belong to the current user
* Request
  * Method: DELETE
  * Route path: /songs/:songId/
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

* Error response: Couldn't find a Song with the specified id
  * Status Code: 404
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Song couldn't be found"
    }
    ``` -->

## ALBUMS

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
  * Route path: /albums/:albumId/songs
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
<!-- 
### Add an Image to a album based on the album's id

Create and return a new image for an album specified by id.

* Require Authentication: true
* Require proper authorization: Review must belong to the current user
* Request
  * Method: POST
  * Route path: /album/:albumId/addImage
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "url": "image url"
    }
    ```

* Successful Response
  * Status Code: 201
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "id": 1,
      "url": "image url"
    }
    ```

* Error response: Couldn't find album with the specified id
  * Status Code: 404
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Album couldn't be found"
    }
    ```

* Error response: Cannot add any more images because there is a maximum of 10
  images per resource
  * Status Code: 403
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Maximum number of images for this resource was reached"
    }
    ``` -->

 ### Users should be able to view all albums created by users

Returns all the albums created by the current user.

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
          "image": "image url"
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

Add Songs based on albumId.

* Require Authentication: True
* Request
  * Method: POST
  * Route path: /users/:userId/albums/:albumId/songs
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
          "songs": [
            {
            "songid": 1
          }
          ]
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

    * Successful Response
  * Status Code: 201
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
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
  * Route path: /albums/:albumId/songs/:songId
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



### Users should be able DELETE albums based on AlbumId

Deletes an existing album, based on AlbumId.

* Require Authentication: true
* Require proper authorization: Album must belong to the current user
* Request
  * Method: DELETE
  * Route path: /albums/:albumId/
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

### Get all Songs liked by the Current User

Returns all the songs liked by the current user.

* Require Authentication: true
* Request
  * Method: GET
  * Route path: /users/:userId/likedsongs
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
### Get all liked Albums of the Current User

Returns all the albums liked by the current user.

* Require Authentication: true
* Request
  * Method: GET
  * Route path: /users/:userId/likedalbums
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

### Users should be able to like a Song

Like song based on songId


* Require Authentication: true
* Request
  * Method: POST
  * Route path: /users/:userId/likedsongs
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


### Users should be able to like an Album

Like album based on albumId


* Require Authentication: true
* Request
  * Method: POST
  * Route path: /users/:userId/likedalbums
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
* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Successfully Liked Album"
    }
    ```

* Error response: Couldn't find Album with the specified id
  * Status Code: 404
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Album couldn't be found"
    }
   ```
   
### Users should be able to unlike a Song

Unlike song based on songId


* Require Authentication: true
* Request
  * Method: PUT
  * Route path: /users/:userId/likedsongs
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


### Users should be able to unlike an album

Unlike album based on albumId


* Require Authentication: true
* Request
  * Method: PUT
  * Route path: /users/:userId/likedalbums
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
* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Successfully Unliked Album"
    }
    ```

* Error response: Couldn't find Song with the specified id
  * Status Code: 404
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Album couldn't be found"
    }
   ```

## PLAYLISTS


### User should GET all playlists created by user based on userId

Returns all the playslists that belong to a userId specified by id.

* Require Authentication: false
* Request
  * Method: GET
  * Route path: /users/:userId/playlists
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "playlist": [
        {
          "id": 1,
          "playlistId": 4,
          "created_at": "2022-11-19 20:39:36",
          "name": "Happy Songs Playlist",
          "updated_at":  "2022-11-19 20:39:36",
        }
      ]
    }
    ```

* Error response: Couldn't find a Playlist with the specified id
  * Status Code: 404
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Playlist couldn't be found"
    }
    ```

### Create a new playlist based on user Id

Create new playlist

* Require Authentication: True
* Request
  * Method: POST
  * Route path: /users/:userId/playlists/:playlistId
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "playlist": [
        {
          "id": 1,
          "playlistId": 4,
          "created_at": "2022-11-19 20:39:36",
          "name": "Happy Songs Playlist",
          "updated_at":  "2022-11-19 20:39:36",
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
      "message": "Playlist successfully created"
    }
    ```

* Error response: Couldn't add a Playlist with the specified id
  * Status Code: 404
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Playlist Not Created"
    }
    ```



### Add Songs to an User created Playlist based on Playlist's id

Add Songs based on playListId.

* Require Authentication: True
* Request
  * Method: POST
  * Route path: /users/:userId/playlists/:playlistId/song/:songId
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "playlist": [
        {
          "id": 1,
          "playlistId": 4,
          "created_at": "2022-11-19 20:39:36",
          "name": "Happy Songs Playlist",
          "updated_at":  "2022-11-19 20:39:36",
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
      "message": "Song successfully added to Playlist"
    }
    ```

* Error response: Couldn't find a Playlist with the specified id
  * Status Code: 404
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Playlist Not Found"
    }
    ```

### Delete a song on users playlist    
Add Songs based on playListId.

* Require Authentication: True
* Request
  * Method: DELETE
  * Route path: /users/:userId/playlists/:playlistId/song/:songId
  * Body: none
   
   
    * Successful Response
  * Status Code: 201
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Song successfully deleted from Playlist"
    }
    ```


### Users should be able DELETE playlists based on PlaylistId

Deletes an existing playlist, based on PlaylistId.

* Require Authentication: true
* Require proper authorization: Playlist must belong to the current user
* Request
  * Method: DELETE
  * Route path: /users/userId/playlists/:playlistId
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

* Error response: Couldn't find a Playlist with the specified id
  * Status Code: 404
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Playlist couldn't be found"
    }
   ```

