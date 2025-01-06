import { createContext, useState, useEffect } from 'react';
import { useSelector } from 'react-redux';

export const LikedSongsContext = createContext();

export function LikedSongsProvider({ children }) {
    const [likedSongs, setLikedSongs] = useState([]);
    const user = useSelector(state => state.session.user);

    useEffect(() => {
        if (!user || !user.id) return;

        fetch(`/api/users/${user.id}/likedsongs`)
            .then(response => response.json())
            .then(data => {
                if (data.Songs) {
                    setLikedSongs(data.Songs || []);
                }
            })
            .catch(error => console.error("Error fetching liked songs:", error));
    }, [user]);

    return (
        <LikedSongsContext.Provider value={{ likedSongs, setLikedSongs }}>
            {children}
        </LikedSongsContext.Provider>
    );
}