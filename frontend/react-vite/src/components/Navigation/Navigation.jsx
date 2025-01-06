import { NavLink } from "react-router-dom";
import { useEffect, useContext } from "react";
import ProfileButton from "./ProfileButton";
import { useDispatch, useSelector } from "react-redux";
// import { FaSearch } from 'react-icons/fa';
import logo from '../../../../../images/Melody_Logo1.png'
import { LikedSongsContext } from "../../context/LikeSongs";
import { fetchSongs } from "../../redux/songs";
import { FaStar, FaRegStar } from 'react-icons/fa';
// import LoginFormModal from "../LoginFormModal";
import "./Navigation.css";




function Navigation() {
  const sessionUser = useSelector(state => state.session.user);
  const dispatch = useDispatch();
  const allSongs = useSelector(state => state.songs.allSongs);
  const { likedSongs, setLikedSongs } = useContext(LikedSongsContext);

  useEffect(() => {
    if (sessionUser) {
      fetch(`/api/users/${sessionUser.id}/likedsongs`)
      .then(response => response.json())
      .then(data => {
        setLikedSongs(data.Songs || [])
      })
    }
  }, [sessionUser, setLikedSongs]);

  const handleLike = (song) => {
    if (!sessionUser) return;
    const isLiked = likedSongs.some(likedSong => likedSong.id === song.id);
    
    fetch(`/api/users/${sessionUser.id}/likedsongs`, {
      method: isLiked ? 'DELETE' : 'POST',
      headers: { 'Content-type': 'application/json' },
      body: JSON.stringify({ song_id: song.id })
    })
    .then(response => response.json())
    .then(() => {
      if (isLiked) {
        setLikedSongs(current => current.filter(s => s.id !== song.id));
      } else {
        setLikedSongs(current => [...current, song]);
      }
    });
  };

  useEffect(() => {
    dispatch(fetchSongs());
  }, [dispatch]);


  const userSongs = sessionUser ? Object.values(allSongs).filter(song => song.userId === sessionUser.id) : [];
  const otherSongs = sessionUser ? Object.values(allSongs).filter(song => song.userId !== sessionUser.id) : Object.values(allSongs);
 
  const isSongLiked = (songId) => {
    return likedSongs.some(likedSong => likedSong.id === songId)
  };

  return (
    <>
    <nav className="nav-container">
      <div className="nav-left">
      <NavLink to="/" className="site-name">
          <img src={logo} alt="Logo" className="Logo"/>
        </NavLink>
        <NavLink to="/" className='site-name'>
          Melody
        </NavLink>
      </div>
     
      <div className="nav-center">
        <div className="search-container">
          {/* <FaSearch className="search-icon" />
          <input
            type="search"
            className="search-bar"
            placeholder="Search for songs..."
            /> */}
      </div>
      </div>
      <div className="nav-right">
        {sessionUser && (
          <>
          <NavLink to="/songs/new" className="nav-link">
            Add Song
          </NavLink>
          <NavLink to="/albums/new" className="nav-link">
            Create Album
          </NavLink>
          </>
        )}
        <ProfileButton />
      </div>
    </nav>
    <div className="side-bar">
      {sessionUser && (
        <>
          {/* <NavLink to="/playlists" className="side-nav">
            Playlists
          // </NavLink> */}
          {/* // <div className="my-songs-header">My Songs</div> */}
          <div className="songs-list">
          {userSongs.map(song => (
                <div key={song.id} className="song-item user-song">
                  <NavLink to={`/songs/${song.id}`} className='song-link'>
                    {song.title}
                  </NavLink>
                  <button onClick={() => handleLike(song)} className="like-button">
                    {isSongLiked(song.id)
                    ? <FaStar className="star-icon filled" />
                    : <FaRegStar className="star-icon"/>}
                  </button>
                </div>
              ))}
          </div>
        </>
      )}
     
      <div className="all-songs-header">All Songs</div>
      <div className="songs-list">
      {otherSongs.map(song => (
            <div key={song.id} className="song-item">
              <NavLink to={`/songs/${song.id}`} className='song-link'>
                {song.title}
              </NavLink>
              {sessionUser && (
              <button onClick={() => handleLike(song)} className="like-button">
                    {isSongLiked(song.id)
                    ? <FaStar className="star-icon filled" />
                    : <FaRegStar className="star-icon"/>}
                  </button>
              )}
          </div>
        ))}
      </div>
    </div>
        </>
  );
}




export default Navigation;
