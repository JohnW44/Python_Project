import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import Melody_Logo from '../../../../../images/Melody_Logo.png'
import './SongsPage.css';
import { useSelector, useDispatch } from "react-redux";
import { fetchSongs } from "../../redux/songs";
import Songplayer from "../Songplayer/Songplayer";


function SongsPage() {
    const { songId } = useParams();
    const [song, setSongs] = useState(null);
    const [songLink, setSongLink] = useState(null);
    const sessionUser = useSelector(state => state.session.user);
    const navigate = useNavigate();
    const dispatch = useDispatch();


    useEffect(() => {
        fetch(`/api/songs/${songId}`)
        .then((response) => response.json())
        .then((data) => {
            console.log("Full song data:", JSON.stringify(data, null, 2));
            setSongs(data);

            if (data.audio_file) {
                setSongLink(data.audio_file)
            }
        })
    }, [songId]);


    const handleEdit = () => {
        navigate(`/songs/new?songId=${songId}`);
    }


    const handleDelete = () => {
        if (window.confirm("Are you sure you want to delete this song?")) {
            fetch(`/api/songs/${songId}`, {
                method: 'DELETE'
            })
            .then((response) => response.json())
            .then(() => {
                dispatch(fetchSongs())
                navigate('/');
            })
        }
    };
    
    

    return (
        <>
        <div className="songs-page">
            <div className="song-header">
                {song && song.images && song.images.length > 0 ? (
                    <img
                        src={song?.images?.[0]?.url || Melody_Logo}
                        alt={song.title}
                        className="song-cover"
                    />
                ) : (
                    <img
                    src={Melody_Logo}
                    alt="Default cover"
                    className="placeholder-image"
                />
                )}
                <h1 className="song-title">{song ? song.title : 'Untitled Song'}</h1>
                <div className="song-details">
                    <h3>Artist: {song ? song.artist : 'Unknown Artist'}</h3>
                    <h3>Album: {song ? song.album : 'Single'}</h3>
                    <h3>Duration: {song ? `${song.duration} seconds` : 'Unknown'}</h3>
                </div>
                {sessionUser && song && sessionUser.id === song.user_id && (
                     <div className="song-actions">
                           <button
                            type="button"
                            onClick={handleEdit}
                            className="edit-button"
                        >
                            Edit Song
                        </button>
                        <button
                            type="button"
                            onClick={handleDelete}
                            className="delete-button"
                        >
                            Delete Song
                        </button>
                     </div>
                )}
            </div>


            <div className="song-details-list">
                <h2 className="details-title">Song Info</h2>
                {song && (
                    <div className="song-details-item">
                        <p>Release Date: {song.released_date ? new Date(song.released_date).toLocaleDateString() : 'Unknown'}</p>
                        <p>Lyrics: {song.lyrics || 'No lyrics'}</p>
                    </div>
                )}
            {songLink && <Songplayer songLink= {songLink} />}
            </div>

        </div>
        </>
    );
}


export default SongsPage;
