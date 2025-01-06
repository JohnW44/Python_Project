import { useEffect, useState, useContext } from 'react'
import './ProfilePage.css'
// import { thunkAuthenticate } from '../../redux/session';
import {useSelector} from 'react-redux';
import Songplayer from '../Songplayer/Songplayer';
import { useNavigate } from 'react-router-dom';
import { FaStar } from 'react-icons/fa';
import { LikedSongsContext } from '../../context/LikeSongs';

function ProfilePage(){
const navigate = useNavigate();
const { likedSongs, setLikedSongs } = useContext(LikedSongsContext);
// const [likedAlbums, setLikedAlbums] = useState([])
const user = useSelector(state => state.session.user);
const [songLink, setSongLink] = useState(null);
// const dispatch = useDispatch();

const handleUnlike = (song) => {
    if (!user) return;
    
    fetch(`/api/users/${user.id}/likedsongs`, {
        method: 'DELETE',
        headers: { 'Content-type': 'application/json' },
        body: JSON.stringify({ song_id: song.id })
    })
    .then(response => {
        if (response.ok) {
            setLikedSongs(current => current.filter(s => s.id !== song.id));
        }
    });
};


useEffect(() => {
    if (!user || !user.id) {
        navigate('/')
        return;
    }

    // console.log('useEffect here')
    fetch(`/api/users/${user.id}/likedsongs`)
    .then((response) => {
        // console.log('Songs response received:', response.status); 
    return response.json()
    })
        .then((data) => {
            // console.log('Songs data received:', data);
            if (data.Songs) {
                setLikedSongs(data.Songs || []); 
            }
        });
        
    }, [user, navigate, setLikedSongs]);

if (!user) {
    return null;
}

const handleSong = (song) => {
    console.log("song", song.audio_file)
    setSongLink(song.audio_file); 
  };

    return (
            <div className='profilebox'>
                <h1>Profile Page</h1>
                <div className='profileinfo'>
                    {user.profile_image ? (
                        <img 
                            src={user.profile_image} 
                            className='profile-pic'
                            alt="Profile"
                            onError={(e) => {
                                e.target.src = 'default-profile-image.png'; 
                                e.target.onerror = null; 
                            }}
                        />
                    ) : (
                        <img 
                            src='default-profile-image.png' 
                            className='profile-pic'
                            alt="Default Profile"
                        />
                    )}
                    <div className='details'>
                        <p>Username: {user.username}</p>
                        <p>Email: {user.email}</p>
                        <p>First Name: {user.first_name}</p>
                        <p>Last Name: {user.last_name}</p>
                    </div>
                </div>

                <div className="liked-section">
                    <h2>Loved Songs</h2>
                    {likedSongs.length > 0 ? (
                        <div className="songs-table">
                            {likedSongs.map((song) => (
                                <div key={song.id} className="song-row">
                                    <div className="song-info" onClick={() => handleSong(song)}>
                                        <img 
                                            src={song.album?.images?.[0]?.url || 'default-album-image.png'} 
                                            alt={song.title} 
                                            className="song-thumbnail" 
                                        />
                                        <div className="song-details">
                                            <p className="song-title">{song.title}</p>
                                            <p className="song-artist">{song.artist}</p>
                                            <p className="song-duration">
                                                {Math.floor(song.duration / 60)}:{String(song.duration % 60).padStart(2, '0')}
                                            </p>
                                        </div>
                                    </div>
                                    <button 
                                        onClick={(e) => {
                                            e.stopPropagation();
                                            handleUnlike(song);
                                        }} 
                                        className="unlike-button"
                                    >
                                        <FaStar className="star-icon filled" />
                                    </button>
                                </div>
                            ))}
                        </div>
                    ) : (
                        <p>No liked songs.</p>
                    )}
                    {songLink && <Songplayer songLink={songLink} />}
                </div>

        </div>
    );
}


export default ProfilePage