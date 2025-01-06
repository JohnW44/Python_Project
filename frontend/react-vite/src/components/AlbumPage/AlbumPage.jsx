import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import './AlbumPage.css';
import Melody_Logo from '../../../../../images/Melody_Logo.png'

function AlbumPage() {
    const { albumId } = useParams();
    const [songs, setSongs] = useState([]);
    const [album, setAlbum] = useState(null);
    const navigate = useNavigate()

    useEffect(() => {
        fetch(`/api/albums/${albumId}/songs`)
            .then((response) => response.json())
            .then((data) => {
                setSongs(data.Songs || []);
                setAlbum(data.Album || {});
            });
    }, [albumId]);

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
            </div>

            <div className="album-songs-list2" >
                <h2 className="songs-title2">Songs</h2>
                {songs.map((song, index) => (
                    <div key={song.id} className="song-item" onClick={() => songclick(song.id)}>
                        <span className="song-number">{index + 1}</span>
                        <span className="song-title">{song.title} </span>
                        <span className="song-duration">{song.duration} </span>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default AlbumPage;