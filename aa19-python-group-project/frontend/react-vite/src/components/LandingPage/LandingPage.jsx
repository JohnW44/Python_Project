import { useNavigate } from 'react-router-dom';
import './LandingPage.css';
import { useEffect, useState } from 'react';


function LandingPage() {

const [albums, setAlbums] = useState([]);
const navigate = useNavigate();

   useEffect(() => {
    const fetchalbum = async () => {
        const response = await fetch('/api/albums'); 

            if (response.ok) {
                const data = await response.json(); 
                // console.log('Fetched albums:', data);
                if (data.Albums) {
                    setAlbums(data.Albums);
                }
            }
        };

        fetchalbum();
    }, []);

    return (
        <>
        <div className="landing-page-container">
            <div className="main-content">
               <div className="albums-grid">
                   {albums.map(album => (
                    <div 
                     key={album.id} 
                     className="album-card"
                     onClick={() => navigate(`/albums/${album.id}`)}
                        >
                     {album.images && album.images.length > 0 && album.images[0].url ? (
                         <img src={album.images[0].url} alt={album.title} className='album-card-image' />
                     ) : (
                         <div>No image available</div> 
                     )}
                        <div className='album-card-details'> 
                            <p className= "album-title"> {album.title}</p>
                            <p className='album-artist'>{album.artist}</p>
                        </div>
                    </div>
                   ))}
               </div>
           </div>
       </div>
    </>
   );
}


export default LandingPage;