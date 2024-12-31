// import React from "react";
import ReactPlayer from "react-player";

const Songplayer= ({songLink}) => {
    return (
        <>
            <div>
                <ReactPlayer
                    url= {songLink}
                    controls = {true}
                    width="500px"
                    height="200px"
                />
            </div>
        </>
    )
}



































export default Songplayer;
