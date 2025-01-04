import { useEffect, useState } from 'react';
import { useDispatch } from 'react-redux';
import { addSongThunk, fetchSongs } from '../../redux/songs';
import { useNavigate, useParams, useLocation } from 'react-router-dom';
import './AddSongForm.css'


function AddSongForm() {
    const [title, setTitle] = useState("");
    const [artist, setArtist] = useState("");
    const [releasedDate, setReleasedDate] = useState("");
    const [duration, setDuration] = useState("");
    const [lyrics, setLyrics] = useState("");
    const [imageFile, setImageFile] = useState(null);
    const [audioFile, setAudioFile] = useState(null);
    const [errors, setErrors] = useState({});
    const [albumId, setAlbumId] = useState(null);
    const [isEditing, setIsEditing] = useState(false);

    const { albumId: paramAlbumId } = useParams();
    const location = useLocation();
    const queryParams = new URLSearchParams(location.search);
    const editSongId = queryParams.get('songId');

    useEffect(() => {
        if (editSongId) {
            setIsEditing(true);
            fetch(`/api/songs/${editSongId}`)
                .then((response) => response.json())
                .then((data) => {
                    setTitle(data.title);
                    setArtist(data.artist);
                    const date = new Date(data.released_date);
                    const formattedDate = date.toISOString().split('T')[0];
                    setReleasedDate(formattedDate);
                    setDuration(data.duration);
                    setLyrics(data.lyrics || '');
                    setAlbumId(data.album_id);
                });
        }
    }, [editSongId]);

    const handleAudioChange = (e) => {
        const file = e.target.files[0];
        if (file) {
            setAudioFile(file);
        }
    };


    const handleImageChange = (e) => {  
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
        if (!isEditing && !audioFile) {
            errObj.audioFile = "Audio file is required";
        }
        setErrors(errObj);
    }, [title, artist, releasedDate, duration, lyrics, audioFile, isEditing]);


    useEffect(() => {
        if (paramAlbumId) {
            setAlbumId(paramAlbumId);
        }
    }, [paramAlbumId]);


    const dispatch = useDispatch();
    const navigate = useNavigate();


    const onSubmit = async (e) => {
        e.preventDefault();
        
        const formattedDate = new Date(releasedDate).toISOString().split('T')[0];
        
        const formData = new FormData();
        formData.append('title', title);
        formData.append('artist', artist);
        formData.append('released_date', formattedDate);
        formData.append('duration', duration);
        formData.append('lyrics', lyrics);
       
        if (albumId){
            formData.append('album_id', albumId)
        }
        if (imageFile) {
            formData.append('image', imageFile);
        }
        if (!isEditing && audioFile) {
            formData.append('audio_file', audioFile);
        }

        const response = isEditing 
            ? await fetch(`/api/songs/${editSongId}`, {
                method: 'PUT',
                body: formData,
            }).then(res => res.json())
            : await dispatch(addSongThunk(formData));
        
        if (!response.error) {
            const songId = isEditing ? editSongId : response.Songs.id;
            if (songId) {
                navigate(`/songs/${songId}`);
                dispatch(fetchSongs());
            }
        } else {
            setErrors(response.errors || {});
        }
    };


    return (
        <form className='song-form' onSubmit={onSubmit} encType="multipart/form-data">
            <h2>{isEditing ? 'Edit Song' : 'Add a New Song'}</h2>


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
            {!isEditing && (
                <>
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
                </>
            )}
            <button
                type='submit'
                disabled={Object.values(errors).length}
            >
                {isEditing ? 'Save Changes' : 'Add Song'}
            </button>
        </form>
    );
}


export default AddSongForm;
