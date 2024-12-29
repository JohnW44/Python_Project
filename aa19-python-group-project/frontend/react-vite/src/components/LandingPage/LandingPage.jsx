import { useNavigate } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import './LandingPage.css';
function LandingPage() {
   const navigate = useNavigate();
   const dispatch = useDispatch();
    // Placeholder data
   const albums = [
       { id: 1, title: 'Album 1', imageUrl: 'url1' },
       { id: 2, title: 'Album 2', imageUrl: 'url2' },
       // ... more albums
   ];
    return (
       <div className="landing-page-container">
           <div className="playlist-sidebar">
               {/* Playlist section */}
               <h2>Playlists</h2>
               <ul className="playlist-list">
                   {/* Add your playlists here */}
               </ul>
           </div>
            <div className="main-content">
               <div className="albums-grid">
                   {albums.map(album => (
                       <div key={album.id} className="album-circle">
                           <img src={album.imageUrl} alt={album.title} />
                           <p>{album.title}</p>
                       </div>
                   ))}
               </div>
           </div>
       </div>
   );
}


export default LandingPage;