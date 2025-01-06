import { useEffect, useState } from 'react'
import './ProfilePage.css'
// import { thunkAuthenticate } from '../../redux/session';
import {useSelector} from 'react-redux';
import Songplayer from '../Songplayer/Songplayer';
import { useNavigate } from 'react-router-dom';

function ProfilePage(){
const navigate = useNavigate();
const [likedSongs, setLikedSongs] = useState([]);
// const [likedAlbums, setLikedAlbums] = useState([])
const user = useSelector(state => state.session.user);
const [songLink, setSongLink] = useState(null);
// const dispatch = useDispatch();

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
        
}, [user, navigate]);

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
                    <div className="albums-grid">
                        {likedSongs.map((song) => (
                        <div
                            key={song.id}
                            className="album-card"
                            onClick={() => handleSong(song)} >
                            {song.album && song.album.images && song.album.images.length > 0 && song.album.images[0].url ? (
                            <img src={song.album.images[0].url} alt={song.title} className="album-card-image" />
                            ) : (
                            <div>No image available</div>
                            )}
                            <div className="album-card-details">
                            <p className="album-title">{song.title}</p>
                            <p className="album-artist">{song.artist}</p>
                            </div>
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