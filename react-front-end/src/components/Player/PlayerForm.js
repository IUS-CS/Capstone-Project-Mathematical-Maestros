import * as React from 'react';
import Radio from '@mui/material/Radio';
import RadioGroup from '@mui/material/RadioGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import FormControl from '@mui/material/FormControl';
import FormLabel from '@mui/material/FormLabel';
import LoadingButton from '@mui/lab/LoadingButton';

const PlayerForm = () => {
  const [genre, setGenre] = React.useState('');
  const [error, setError] = React.useState(false);
  const [loading, setLoading] = React.useState(false);

  const handleRadioChange = (event) => {
    setGenre(event.target.value);
    setError(false);
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    if (!genre) {
        setError(true);
        return;
    }

    const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ genre: genre, rating: 0.0 })
    };
    
    setLoading(true);
    try {
        fetch("http://localhost:5000/song", requestOptions)
        .then(response => response.json())
        .then(() => setLoading(false))
        .then(res => console.log(res));
    } catch(err) {
        setLoading(false);
        console.log(err)
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <FormControl sx={{ m: 3 }} error={error} variant="standard">
        <FormLabel id="player-genre-radios">Select a Genre</FormLabel>
        <RadioGroup
          aria-labelledby="player-genre-radios"
          name="form-genre"
          value={genre}
          onChange={handleRadioChange}
        >
          <FormControlLabel value="Rock" control={<Radio />} label="Rock" />
          <FormControlLabel value="Blues" control={<Radio />} label="Blues" />
        </RadioGroup>
        <LoadingButton sx={{ mt: 1, mr: 1 }} type="submit" variant="outlined" loading={loading}>
          Generate!
        </LoadingButton>
      </FormControl>
    </form>
  );
};

export default PlayerForm;