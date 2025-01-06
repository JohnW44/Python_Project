import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { useSelector } from "react-redux";
import './AlbumPage.css';
import Melody_Logo from '../../../../../images/Melody_Logo.png'

function AlbumPage() {
    const { albumId } = useParams();
    const [songs, setSongs] = useState([]);
    const [album, setAlbum] = useState(null);
    const [albumSongs, setAlbumSongs] = useState([])
    const sessionUser = useSelector(state => state.session.user);
    const navigate = useNavigate()

    useEffect(() => {
        fetch(`/api/albums/${albumId}/songs`)
            .then((response) => response.json())
            .then((data) => {
                setSongs(data.Songs || []);
                setAlbum(data.Album || {});
            });
    }, [albumId]);

    const handleEdit = () => {
            navigate(`/albums/new?albumId=${albumId}`);
        }
        useEffect(() => {
            if (sessionUser && album && sessionUser.id === album.user_id) {
                fetch('/api/songs/')
                    .then((response) => response.json())
                    .then((data) => {
                        const albumSongs = data.Songs.filter(song => 
                            song.user_id === sessionUser.id && !song.album_id
                        );
                        setAlbumSongs(albumSongs);
                    });
            }
        }, [songs, album, sessionUser]);
    
    const handleAddSongToAlbum = async (songId) => {
            const response = await fetch(`/api/albums/${albumId}/${sessionUser.id}/songs`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ songid: songId })
            });

            if (response.ok) {
                fetch(`/api/albums/${albumId}/songs`)
                    .then((response) => response.json())
                    .then((data) => {
                        setSongs(data.Songs || []);
                    });
                } else {
                    const data = await response.json();
                    console.error("Failed to add song:", data.message);
                }
        };
    
    const handleRemoveSongFromAlbum = async (songId) => {
        const response = await fetch(`/api/albums/${albumId}/${sessionUser.id}/songs`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ songid: songId })
        });

        if (response.ok) {
            fetch(`/api/albums/${albumId}/songs`)
                .then((response) => response.json())
                .then((data) => {
                    setSongs(data.Songs || []);
                });
        } else {
            const data = await response.json();
            console.error("Failed to remove song:", data.message)
        }
    }
    
    const handleDelete = () => {
        if (window.confirm("Are you sure you want to delete this album?")) {
            fetch(`/api/albums/${albumId}`, {
                method: 'DELETE'
            })
            .then((response) => response.json())
            .then(() => {
                navigate('/');
            })
        }
    };

    const songclick = (songId) => {
        navigate(`/songs/${songId}`)

    }
    return (
        <div className="album-page2">
            <div className="album-header2">
                    <img 
                        src={album?.images?.[0]?.url || Melody_Logo} 
                        className='album-card-image2' 
                    />
                <h1 className="album-title2">{album ? album.title : 'Untitled Album'}</h1>
                <div className="album-info2">
                    <h3>Artist: {album ? album.artist : 'Unknown Artist'}</h3>
                    <h3>Released: {album ? album.released_year : 'Unknown'}</h3>
                    <h3>Songs: {songs.length}</h3>
                </div>
                {sessionUser && album && sessionUser.id === album.user_id && (
                    <div className="album-actions2">
                        <button
                            type="button"
                            onClick={handleEdit}
                            className="edit-album-button"
                        >
                            Edit Album
                        </button>
                        <button
                            type="button"
                            onClick={handleDelete}
                            className="delete-album-button"
                        >
                            Delete Album
                        </button>
                    </div>
                )}
            </div>

            <div className="album-songs-list2">
                <h2 className="songs-title2">Songs</h2>
                {songs.map((song, index) => (
                    <div key={song.id} className="song-item">
                        <div onClick={() => songclick(song.id)}>
                            <span className="song-number">{index + 1}</span>
                            <span className="song-title">{song.title}</span>
                            <span className="song-duration">{Math.floor(song.duration / 60)}:{String(song.duration % 60).padStart(2, '0')}</span>
                        </div>
                        {sessionUser && album && sessionUser.id === album.user_id && (
                            <button 
                                onClick={(e) => {
                                    e.stopPropagation();
                                    handleRemoveSongFromAlbum(song.id);
                                }}
                                className="remove-from-album-button"
                            >
                                Remove
                            </button>
                        )}
                    </div>
                ))}

                {sessionUser && album && sessionUser.id === album.user_id && (
                    <div className="add-songs-section">
                        <h3>Add Songs to Album</h3>
                        {albumSongs.length > 0 ? (
                            albumSongs.map(song => (
                                <div key={song.id} className="album-song-item">
                                    <span>{song.title}</span>
                                    <button 
                                        onClick={() => handleAddSongToAlbum(song.id)}
                                        className="add-to-album-button"
                                    >
                                        Add to Album
                                    </button>
                                </div>
                            ))
                        ) : (
                            <p>No available songs to add</p>
                        )}
                    </div>
                )}
            </div>
        </div>
    );
}

export default AlbumPage;