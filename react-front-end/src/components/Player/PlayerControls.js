import { React } from "react";
import IconButton from '@mui/material/IconButton';
import CardContent  from "@mui/material/CardContent";
import PauseCircleIcon from '@mui/icons-material/PauseCircle';
import PlayCircleIcon from '@mui/icons-material/PlayCircle';
import SkipPreviousIcon from '@mui/icons-material/SkipPrevious';
import SkipNextIcon from '@mui/icons-material/SkipNext';
import AudiotrackIcon from '@mui/icons-material/Audiotrack';

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
    <CardContent>
      <IconButton onClick={() => props.SkipSong(false)}>
        <SkipPreviousIcon color="primary"/>
      </IconButton>
      <IconButton onClick={() => props.setIsPlaying(!props.isPlaying)}>
        {props.isPlaying ? <PauseCircleIcon color="primary" sx={{ height: 38, width: 38 }}/> : <PlayCircleIcon color="primary" sx={{ height: 38, width: 38 }}/>}
      </IconButton>
      <IconButton onClick={() => props.SkipSong()}>
        <SkipNextIcon color="primary"/>
      </IconButton>
      <IconButton onClick={handleSubmit}>
        <AudiotrackIcon color="primary"/>
      </IconButton>
    </CardContent>
  );
}

export default PlayerControls;