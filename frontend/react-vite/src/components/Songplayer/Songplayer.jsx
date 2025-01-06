import { useEffect, useRef } from 'react';
import WaveSurfer from 'wavesurfer.js';
import './Songplayer.css';


const Songplayer = ({ songLink }) => {
  const waveformRef = useRef(null);
  const wavesurferRef = useRef(null);


  useEffect(() => {
    if (songLink) {
        console.log('song from URL:', songLink);
      if (wavesurferRef.current) {
        wavesurferRef.current.destroy();
      }
      wavesurferRef.current = WaveSurfer.create({
        container: waveformRef.current,
        height: 100,
        barWidth: 3,
        responsive: true,
        cursorColor: 'gray',
      });
      wavesurferRef.current.load(songLink);


      wavesurferRef.current.on('ready', () => {
        wavesurferRef.current.stop();
      });
    }


    return () => {
      if (wavesurferRef.current) {
        wavesurferRef.current.destroy();
      }
    };
  }, [songLink]);


  return (
    <div className="player">
      <div ref={waveformRef}></div>
      <div className="controls">
        <button onClick={() => wavesurferRef.current.playPause()}>
          {wavesurferRef.current?.isPlaying() ? 'Pause' : 'Play'}
        </button>
        <button onClick={() => wavesurferRef.current.stop()}>
          Stop
        </button>
      </div>
    </div>
  );
};


export default Songplayer;



