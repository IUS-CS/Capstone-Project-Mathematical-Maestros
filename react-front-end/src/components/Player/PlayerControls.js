import { React } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faPlay,
  faPause,
  faForward,
  faBackward,
  faMusic,
} from "@fortawesome/free-solid-svg-icons";

const PlayerControls = (props) => {

  const handleSubmit = e => {
    e.preventDefault();

    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ steps: 128 })
    };
   
    try {
      fetch("http://localhost:5000/song", requestOptions)
      .then(response => response.json())
      .then(res => console.log(res));  
    }
    catch(err) {
      console.log(err)
    }
  };
  
  return (
    <div className="music-player--controls">
      <button className="skip-btn" onClick={() => props.SkipSong(false)}>
        <FontAwesomeIcon icon={faBackward} />
      </button>
      <button
        className="play-btn"
        onClick={() => props.setIsPlaying(!props.isPlaying)}
      >
        <FontAwesomeIcon icon={props.isPlaying ? faPause : faPlay} />
      </button>
      <button className="skip-btn" onClick={() => props.SkipSong()}>
        <FontAwesomeIcon icon={faForward} />
      </button>
      <button className="new-song-btn" onClick={handleSubmit}>
        <FontAwesomeIcon icon={faMusic} />
      </button>
    </div>
  );
}

export default PlayerControls;