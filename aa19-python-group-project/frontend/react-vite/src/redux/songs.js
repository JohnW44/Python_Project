
const LOAD_SONGS = 'songs/LOAD_SONGS';
// const ADD_SONGS = 'songs/ADD_SONG';

const loadSongs = (songsData) => ({
    type: LOAD_SONGS,
    payload: songsData
})

const initialState={
    allSongs: {}
}

// const addSong = (song) => ({
//     type: ADD_SONGS,
//     payload: song
// })

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


const songsReducer = (state = initialState, action) => {
    switch (action.type) {
        case LOAD_SONGS: {
            const newState = { ...state };
            newState.allSongs = {};
            action.payload.forEach(song => {
                newState.allSongs[song.id] = song;
            });
            return newState;
        }
        default: return state;
    }
}

export default songsReducer;

