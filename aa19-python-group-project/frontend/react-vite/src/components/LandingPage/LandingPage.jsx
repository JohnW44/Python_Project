import './LandingPage.css';
import { useEffect, useState } from 'react';


function LandingPage() {

const [albums, setAlbums] = useState([]);

   useEffect(() => {
    const fetchalbum = async () => {
        const response = await fetch('http://localhost:5000/albums'); 

            if (response.ok) {
                const data = await response.json(); 
                console.log('Fetched albums:', data);
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
                       <div key={album.id} className="album-circle">
                       {album.images && album.images.length > 0 && album.images[0].url ? (
                           <img src={album.images[0].url} />
                        ) : (
                            <div>No image available</div> 
                        )}
                           <p>{album.title}</p>
                           <p>{album.artist}</p>
                       </div>
                   ))}
               </div>
           </div>
       </div>
    </>
   );
}


export default LandingPage;