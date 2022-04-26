import React, { useEffect } from 'react';
import Box from '@mui/material/Box';
import Rating from '@mui/material/Rating';
import httpClient from '../../httpClient';
  
const PlayerRating = (props) => {
  
  const [averageRating, setAverageRating] = React.useState(null);
  const [currentUser, setCurrentUser] = React.useState(null);
  const [ratingValue, setRatingValue] = React.useState(0);

  useEffect(() => {
    (async () => {
      try {
        const resp = await httpClient.get("/api/users/session");
        setCurrentUser(resp.data);
      } catch(error) {
        console.log("Not authenticated");
      }
    })();
  }, []);

  useEffect(() => {
    if(props.songId){
      (async () => {
        try {
          const resp = await httpClient.get(`/api/song/rating/${props.songId}`);
          setAverageRating(resp.data);
        } catch(error) {
          console.log("Not authenticated");
        }
      })();
    }
  }, [props.songId, ratingValue]);

  const handleClick = (newValue) => {

    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ song_id: props.songId, user_id: currentUser.id, stars: newValue })
    };

    if(newValue !== 0 && newValue !== null) {
      try {
        fetch("/api/song/rating", requestOptions)
        .then(response => response.json())
        .then(res => console.log(res))
        // Set Rating Value after Fetch, see above useEffect dependency.
        setRatingValue(newValue);
      } 
      catch(err) {
        console.log(err)   
      }
    }
  }

  return (
    <div style={{ display: 'block' }}>
      <Box component="fieldset" mb={3} borderColor="transparent">
        <Rating
          name="Rating Label"
          value={averageRating && averageRating}
          onChange={(event, newValue) => {
            handleClick(newValue);
          }}
          precision={0.5}
          readOnly={currentUser ? false : true}
          size="large"
        />
      </Box>
    </div>
  );
}

export default PlayerRating;