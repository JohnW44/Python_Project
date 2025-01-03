import { useEffect, useState } from 'react';
import { useDispatch } from 'react-redux';
import { addSongThunk } from '../../redux/songs';
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
    const [audioFile, setAudioFile] = useState(null);
    const [errors, setErrors] = useState({});
   
  

    const handleImageChange = (e) => {
        const file = e.target.files[0];
        if (file) {
            setImage(file);
            const previewUrl = URL.createObjectURL(file);
            setImagePreview(previewUrl);
        }
    };

    const handleAudioChange = (e) => {
        const file = e.target.files[0];
        if (file) {
            setAudioFile(file);
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
        if (!audioFile) {
            errObj.audioFile = "Audio file is required";
        }
        setErrors(errObj);
    }, [title, artist, releasedDate, duration, lyrics, audioFile]);


    const { closeModal } = useModal();

    const dispatch = useDispatch();

    const onSubmit = async (e) => {
        e.preventDefault();
        const formData = new FormData();
        formData.append('title', title);
        formData.append('artist', artist);
        formData.append('released_date', releasedDate);
        formData.append('duration', duration);
        formData.append('lyrics', lyrics);


        // if(albumId) {
        //     formData.append('Songs[0][album_id]', albumId);
        // }
        if (image) {
            formData.append('image_url', image);
        }
        if (audioFile) {
            formData.append('audio_url', audioFile);
        }

        const response = await dispatch(addSongThunk(formData));

        if (!response.error) {
            closeModal();
        } else {
            setErrors(response.errors || {});
        }
    


    };
    return (
        <form className='song-form' onSubmit={onSubmit} encType="multipart/form-data">
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
            <label>
                Audio File
                <input
                    type='file'
                    accept='.mp3,.wav,.ogg,'
                    onChange={handleAudioChange}
                    required
                />
            </label>
            <p className='errors'>{errors.audioFile}</p>
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