import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import './AlbumPage.css';

function AlbumPage() {
    const { albumId } = useParams();
    const [songs, setSongs] = useState([]);
    const [album, setAlbum] = useState(null);

    useEffect(() => {
        fetch(`/api/albums/${albumId}/songs`)
            .then((response) => response.json())
            .then((data) => {
                setSongs(data.Songs || []);
                setAlbum(data.Album || {});
            });
    }, [albumId]);

    return (
        <div className="album-page">
            <div className="album-header">
                {album && album.images && album.images.length > 0 ? (
                    <img 
                        src={album.images[0].url} 
                        alt={album.title} 
                        className="album-cover"
                    />
                ) : (
                    <div className="album-cover-placeholder">No Image Available</div>
                )}
                <h1 className="album-title">{album ? album.title : 'Untitled Album'}</h1>
                <div className="album-info">
                    <h3>Artist: {album ? album.artist : 'Unknown Artist'}</h3>
                    <h3>Released: {album ? album.released_year : 'Unknown'}</h3>
                    <h3>Songs: {songs.length}</h3>
                </div>
            </div>

            <div className="album-songs-list">
                <h2 className="songs-title">Songs</h2>
                {songs.map((song, index) => (
                    <div key={song.id} className="song-item">
                        <span className="song-number">{index + 1}</span>
                        <span className="song-title">{song.title}</span>
                        <span className="song-duration">{song.duration}</span>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default AlbumPage;