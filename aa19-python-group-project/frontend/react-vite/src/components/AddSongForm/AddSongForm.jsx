import { useEffect, useState } from 'react';
// import { useDispatch } from 'react-redux';
import { useModal } from '../../context/Modal'
// import { useNavigate } from 'react-router-dom';
import './AddSongForm.css'


function AddSongForm() {
    const [title, setTitle] = useState("");
    const [artist, setArtist] = useState("");
    const [releasedDate, setReleasedDate] = useState("");
    const [duration, setDuration] = useState("");
    const [lyrics, setLyrics] = useState("");
    const [image, setImage] = useState(null);
    const [imagePreview, setImagePreview] = useState(null);
    const [errors, setErrors] = useState({});
  
    
    const handleImageChange = (e) => {
        const file = e.target.files[0];
        if (file) {
            setImage(file);
            const previewUrl = URL.createObjectURL(file);
            setImagePreview(previewUrl);
        }
    };

    useEffect(() => {
        const errObj = {};
        if (title.length <= 0) {
            errObj.title = "Must include title";
        } else if (title.length > 255) {
            errObj.title = "Title must be less than 255 characters";
        }
        if (artist.length <= 0){
            errObj.artist = "Must include name of Artist";
        } else if (artist.length > 255){
            errObj.artist = "Artist name must be less than 255 characters";
        }
        if (!releasedDate){
            errObj.releasedDate = "Date Released is required";
        }
        if (duration <=0) {
            errObj.duration = "Song duration must be at least one second";
        }
        if (lyrics.length > 50000) {
            errObj.lyrics = "Lyrics cannot exceed 50,000 characters";
        }
        setErrors(errObj);
    }, [title, artist, releasedDate, duration, lyrics]);


    const { closeModal } = useModal();


    const onSubmit = async (e) => {
        e.preventDefault();
        const formData = new FormData();
        formData.append('Songs[0][title]', title);
        formData.append('Songs[0][artist]', artist);
        formData.append('Songs[0][released_date]', releasedDate);
        formData.append('Songs[0][duration]', duration);
        formData.append('Songs[0][lyrics]', lyrics);


        // if(albumId) {
        //     formData.append('Songs[0][album_id]', albumId);
        // }
        if (image) {
            formData.append('Images[0][url]', image);
        }

        const res = await fetch('/api/songs', {
            method: 'POST',
            body: formData,
            credentials: 'include'
        })
        if (res.ok) {
            closeModal();
        } else {
            const data = await res.json();
            setErrors(data.errors || {})
        }

    };
    return (
        <form className='song-form' onSubmit={onSubmit}>
            <h2>Add a New Song</h2>


            <label>
                Title
                <input
                    type="text"
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                    required
                />
            </label>
            <p className='errors'>{errors.title}</p>
            <label>
                Artist
                <input
                    type="text"
                    value={artist}
                    onChange={(e) => setArtist(e.target.value)}
                    required
                />
            </label>
            <p className='errors'>{errors.artist}</p>
            <label>
                Release Date
                <input
                    type='date'
                    value={releasedDate}
                    onChange={(e) => setReleasedDate(e.target.value)}
                    required
                />
            </label>
            <p className='errors'>{errors.releasedDate}</p>
            <label>
                Duration (seconds)
                <input
                    type='number'
                    value={duration}
                    onChange={(e) => setDuration(e.target.value)}
                    required
                />
            </label>
            <p className='errors'>{errors.duration}</p>
            <label>
            Lyrics
               <textarea
                   value={lyrics}
                   onChange={(e) => setLyrics(e.target.value)}
               />
            </label>
            <p className='errors'>{errors.lyrics}</p>
           <label>
            Song Image
            <input
                type='file'
                accept='image/*'
                onChange={handleImageChange}
                />
           </label>
           {imagePreview && (
            <div className='image-preview'>
                <img 
                    src={imagePreview}
                    alt='Preview'
                />
            </div>
           )}
            <button
               type='submit'
               disabled={Object.values(errors).length}
           >
            Add Song
            </button>
        </form>
    );
}


export default AddSongForm;