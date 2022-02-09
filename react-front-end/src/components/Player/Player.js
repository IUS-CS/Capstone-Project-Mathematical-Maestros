import React, { useState, useRef, useEffect } from "react";
import PlayerControls from "./PlayerControls";
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';

const Player = (props) => {

  const audioElement = useRef(null);
  const [isPlaying, setIsPlaying] = useState(false);
  var songId = props.songs[props.currentSongIndex] && props.songs[props.currentSongIndex].id

  useEffect(() => {
    if (isPlaying) {
      audioElement.current.play();
    } else {
      audioElement.current.pause();
    }
  });

  const SkipSong = (forwards = true) => {
    if (forwards) {
      props.setCurrentSongIndex(() => {
        let temp = props.currentSongIndex;
        temp++;

        if (temp > props.songs.length - 1) {
          temp = 0;
        }

        return temp;
      });
    } else {
      props.setCurrentSongIndex(() => {
        let temp = props.currentSongIndex;
        temp--;

        if (temp < 0) {
          temp = props.songs.length - 1;
        }

        return temp;
      });
    }
  };

  const styles = {
    card: {
      margin: 'auto',
      marginTop: '25rem',
      width: '35%',
      padding: '20px',
      textAlign: 'center', 
      height: '10rem', 
      backgroundColor: '#354B46',
    },
  }
  
  return (
    <Card style={styles.card}>
      <Box>
        <CardContent>
          <Typography component="div" variant="h5" color='whitesmoke'>
            The Maestro's Music Box
          </Typography>
        </CardContent>
        <CardMedia>
          <audio
            src={songId && "http://localhost:5000/play/" + songId}
            ref={audioElement}
          ></audio>
          <PlayerControls
            isPlaying={isPlaying}
            setIsPlaying={setIsPlaying}
            SkipSong={SkipSong}
          />
        </CardMedia>
      </Box>
    </Card>
  );
}

export default Player;