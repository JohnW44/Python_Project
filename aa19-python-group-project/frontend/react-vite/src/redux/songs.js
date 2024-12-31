const LOAD_SONGS = 'songs/LOAD_SONGS';
const ADD_SONG = 'songs/ADD_SONG';

const loadSongs = (songsData) => ({
    type: LOAD_SONGS,
    payload: songsData
})

const addSong = (song) => ({
    type: ADD_SONG,
    payload: song
})

const initialState={
    allSongs: {}
}

//LOAD ALL SONGS
export const fetchSongs = () => async (dispatchEvent) => {
    const response = await fetch('/api/songs', {
        credentials: "same-origin"
    });
    
    if (response.ok) {
        const songsData = await response.json();
        console.log('Songs data received:', songsData);
        dispatchEvent(loadSongs(songsData));
    }
}

//ADD A SONG
export const addSongThunk = (formData) => async (dispatch) => {
    console.log("Sending request to /api/songs");
    
    const songData = {
        Songs: [{
            title: formData.get('Songs[0][title]'),
            artist: formData.get('Songs[0][artist]'),
            released_date: formData.get('Songs[0][released_date]'),
            duration: formData.get('Songs[0][duration]'),
            lyrics: formData.get('Songs[0][lyrics]')
        }]
    };

    const imageFile = formData.get('Images[0][url]');
    if (imageFile) {
        songData.Images = [{
            url: imageFile.name
        }];
    }

    console.log("Sending song data:", songData);

    const res = await fetch('/api/songs/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(songData),
        credentials: 'include'
    });

    console.log("Response status:", res.status);

    if (res.ok) {
        const song = await res.json();
        console.log("Response data:", song);
        dispatch(addSong(song.Songs[0]));
        return song;
    } else {
        console.log("Error response:", await res.text());
        return { error: true, errors: { _error: "Failed to add song" } };
    }
};


const songsReducer = (state = initialState, action) => {
    switch (action.type) {
        case LOAD_SONGS: {
            let newState = { ...state };
            newState.allSongs = {};
            if (action.payload.Songs) { 
                action.payload.Songs.forEach(song => {
                    newState.allSongs[song.id] = song;
                });
            }
            return newState;
        }
        case ADD_SONG: {
            let newState = { ...state };
            // newState.allSongs = { ...state.allSongs };
            newState.allSongs.push(action.payload)
            return newState;
        }
        default: return state;
    }
}

export default songsReducer;

