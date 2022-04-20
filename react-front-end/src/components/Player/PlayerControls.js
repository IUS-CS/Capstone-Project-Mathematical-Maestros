import { React } from "react";
import IconButton from '@mui/material/IconButton';
import CardContent  from "@mui/material/CardContent";
import PauseCircleIcon from '@mui/icons-material/PauseCircle';
import PlayCircleIcon from '@mui/icons-material/PlayCircle';
import SkipPreviousIcon from '@mui/icons-material/SkipPrevious';
import SkipNextIcon from '@mui/icons-material/SkipNext';

const PlayerControls = (props) => {

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
    </CardContent>
  );
}

export default PlayerControls;