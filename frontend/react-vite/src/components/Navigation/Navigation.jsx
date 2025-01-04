import { NavLink } from "react-router-dom";
import { useEffect } from "react";
import ProfileButton from "./ProfileButton";
import { useDispatch, useSelector } from "react-redux";
import { FaSearch } from 'react-icons/fa';
import logo from '../../../../../images/Melody_Logo1.png'
import "./Navigation.css";
import { fetchSongs } from "../../redux/songs";
// import LoginFormModal from "../LoginFormModal";




function Navigation() {
  const sessionUser = useSelector(state => state.session.user);
  const dispatch = useDispatch();
  const allSongs = useSelector(state => state.songs.allSongs);


  useEffect(() => {
    dispatch(fetchSongs());
  }, [dispatch]);


  const userSongs = sessionUser ? Object.values(allSongs).filter(song => song.userId === sessionUser.id) : [];
  const otherSongs = sessionUser ? Object.values(allSongs).filter(song => song.userId !== sessionUser.id) : Object.values(allSongs);
 
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
          <FaSearch className="search-icon" />
          <input
            type="search"
            className="search-bar"
            placeholder="Search for songs..."
            />
      </div>
      </div>
      <div className="nav-right">
        {sessionUser && (
          <NavLink to="/songs/new" className="nav-link">
            Add Song
          </NavLink>
        )}
        <ProfileButton />
      </div>
    </nav>
    <div className="side-bar">
      {sessionUser && (
        <>
          {/* <NavLink to="/playlists" className="side-nav">
            Playlists
          </NavLink> */}
          <div className="my-songs-header">My Songs</div>
          <div className="songs-list">
          {userSongs.map(song => (
                <div key={song.id} className="song-item user-song">
                  <NavLink to={`/songs/${song.id}`} className='song-link'>
                    {song.title}
                  </NavLink>
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
          </div>
        ))}
      </div>
    </div>
        </>
  );
}




export default Navigation;
