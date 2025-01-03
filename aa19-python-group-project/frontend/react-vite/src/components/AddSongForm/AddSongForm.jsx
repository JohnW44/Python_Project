import { useEffect, useState } from 'react';
import { useDispatch } from 'react-redux';
import { addSongThunk, fetchSongs } from '../../redux/songs';
import { useNavigate } from 'react-router-dom';
import './AddSongForm.css'

function AddSongForm() {
    const [title, setTitle] = useState("");
    const [artist, setArtist] = useState("");
    const [releasedDate, setReleasedDate] = useState("");
    const [duration, setDuration] = useState("");
    const [lyrics, setLyrics] = useState("");
    const [imageFile, setImageFile] = useState(null);  // Changed back to imageFile
    const [audioFile, setAudioFile] = useState(null);
    const [errors, setErrors] = useState({});
   
    const handleAudioChange = (e) => {
        const file = e.target.files[0];
        if (file) {
            setAudioFile(file);
        }
    };

    const handleImageChange = (e) => {  // Restored handleImageChange
        const file = e.target.files[0];
        if (file) {
            setImageFile(file);
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

    const dispatch = useDispatch();
    const navigate = useNavigate();

    const onSubmit = async (e) => {
        e.preventDefault();
        const formData = new FormData();
        formData.append('title', title);
        formData.append('artist', artist);
        formData.append('released_date', releasedDate);
        formData.append('duration', duration);
        formData.append('lyrics', lyrics);
        
        if (imageFile) {
            formData.append('image', imageFile);  // Changed back to image file
        }
        if (audioFile) {
            formData.append('audio_file', audioFile);
        }

        const response = await dispatch(addSongThunk(formData));

        if (!response.error) {
            const newSongId = response.Songs.id; 
            if (newSongId) {
                navigate(`/songs/${newSongId}`);
                dispatch(fetchSongs());
            }
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
                Image
                <input
                    type="file"
                    accept="image/*"
                    onChange={handleImageChange}
                />
            </label>
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