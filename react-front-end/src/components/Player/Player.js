import React, { useState, useRef, useEffect } from "react";
import { styled } from "@mui/material/styles";
import PlayerControls from "./PlayerControls";
import Box from "@mui/material/Box";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import CardHeader from "@mui/material/CardHeader";
import CardMedia from "@mui/material/CardMedia";
import Collapse from "@mui/material/Collapse";
import IconButton from "@mui/material/IconButton";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import PlayerForm from "./PlayerForm";
import PlayerRating from "./PlayerRating";

const ExpandMore = styled((props) => {
  const { expand, ...other } = props;
  return <IconButton {...other} />;
})(({ theme, expand }) => ({
  transform: !expand ? "rotate(0deg)" : "rotate(180deg)",
  marginLeft: "auto",
  transition: theme.transitions.create("transform", {
    duration: theme.transitions.duration.shortest,
  }),
}));

const Player = (props) => {
  const audioElement = useRef(null);
  const [isPlaying, setIsPlaying] = useState(false);
  const [expanded, setExpanded] = useState(false);
  const songId =
    props.songs[props.currentSongIndex] &&
    props.songs[props.currentSongIndex].id;
  const genre =
    props.songs[props.currentSongIndex] &&
    props.songs[props.currentSongIndex].genre;

  const handleExpandClick = () => {
    setExpanded(!expanded);
  };

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
      position: "absolute",
      left: "50%",
      top: "50%",
      webkitTransform: "translate(-50%, -50%)",
      transform: "translate(-50%, -50%)",
      backgroundColor: "#354B46",
      minWidth: "360px",
      textAlign: "center",
    },
  };

  return (
    <Card style={styles.card}>
      <Box>
        <CardHeader
          title={`Playing Song ${songId}`}
          subheader={`Genre: ${genre}`}
        />
        <CardMedia>
          <audio
            src={songId && `/api/play/${songId}`}
            ref={audioElement}
          ></audio>
          <PlayerControls
            isPlaying={isPlaying}
            setIsPlaying={setIsPlaying}
            SkipSong={SkipSong}
          />
          <PlayerRating songId={songId} />
        </CardMedia>
        <ExpandMore
          expand={expanded}
          onClick={handleExpandClick}
          aria-expanded={expanded}
          aria-label="show more"
        >
          <ExpandMoreIcon />
        </ExpandMore>
        <Collapse in={expanded} timeout="auto" unmountOnExit>
          <CardContent>
            <PlayerForm />
          </CardContent>
        </Collapse>
      </Box>
    </Card>
  );
};

export default Player;
