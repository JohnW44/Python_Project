import { useEffect, useState } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import './AddAlbumForm.css';

function AddAlbumForm() {
    const [title, setTitle] = useState("");
    const [artist, setArtist] = useState("");
    const [releasedYear, setReleasedYear] = useState("");
    // const [duration, setDuration] = useState("");
    const [imageFile, setImageFile] = useState(null);
    const [errors, setErrors] = useState({});
    const [isEditing, setIsEditing] = useState(false);

    const navigate = useNavigate();
    const location = useLocation();
    const queryParams = new URLSearchParams(location.search)
    const editAlbumId = queryParams.get('albumId')

    const handleImageChange = (e) => {  
        const file = e.target.files[0];
        if (file) {
            setImageFile(file);
        }
    };

    useEffect(() => {
        if (editAlbumId) {
            setIsEditing(true);
            fetch(`/api/albums/${editAlbumId}/songs`)
                .then((response) => response.json())
                .then((data) => {
                    if (data.Album) {
                        setTitle(data.Album.title);
                        setArtist(data.Album.artist);
                        setReleasedYear(data.Album.released_year);
                    }
                });
        }
    }, [editAlbumId]);

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
        if (!releasedYear){
            errObj.releasedYear = "Release year is required";
        }
        // if (duration <= 0) {
        //     errObj.duration = "Album duration must be at least one second";
        // }
        setErrors(errObj);
    }, [title, artist, releasedYear]); //took out Duration

    const onSubmit = async (e) => {
        e.preventDefault();
        
        const formData = new FormData();
        formData.append('title', title);
        formData.append('artist', artist);
        formData.append('released_year', releasedYear);
        formData.append('duration', '1');
        
        if (imageFile) {
            formData.append('images', imageFile);
        }
        const response = await fetch(
            isEditing ? `/api/albums/${editAlbumId}` : '/api/albums/', 
            {
                method: isEditing ? 'PUT' : 'POST',
                body: formData,
            }
        );

        if (response.ok) {
            const data = await response.json();
            navigate(`/albums/${isEditing ? editAlbumId : data.Album.id}`);
        } else {
            const data = await response.json();
            setErrors(data.errors || {});
        }
    };

    return (
        <form className='album-form' onSubmit={onSubmit} encType="multipart/form-data">
            <h2>{isEditing ? 'Edit Album' : 'Create New Album'}</h2>

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
                Release Year
                <input
                    type='number'
                    value={releasedYear}
                    onChange={(e) => setReleasedYear(e.target.value)}
                    min="1900"
                    max={new Date().getFullYear()}
                    required
                />
            </label>
            <p className='errors'>{errors.releasedYear}</p>
{/* 
            <label>
                Duration (seconds)
                <input
                    type='number'
                    value={duration}
                    onChange={(e) => setDuration(e.target.value)}
                    required
                />
            </label>
            <p className='errors'>{errors.duration}</p> */}

            <label>
                Album Cover
                <input
                    type="file"
                    accept="image/*"
                    onChange={handleImageChange}
                />
            </label>

            <button
                type='submit'
                disabled={Object.values(errors).length > 0}
            >
                {isEditing ? 'Save Changes' : 'Create Album'}
            </button>
        </form>
    );
}

export default AddAlbumForm;