import React from 'react';
import { useState } from 'react'
import { Navigate } from 'react-router-dom'
import Card from '@mui/material/Card';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Alert from '@mui/material/Alert'

const styles = {
  card: {
    margin: 'auto',
    marginTop: '25rem',
    width: '35%',
    padding: '20px',
    textAlign: 'center',  
  },
  h3: {
    fontSize: '42px',
    fontWeight: 'bold',
    letterSpacing: '1.5px',
    textAlign: 'center',
  },
  form: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',   
  },
  textField: {
    margin: '10px',
  },
  button: {
    margin: '10px',
  },
  alert: {
    margin: '10px',
  }
}

const SignUp = () => {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const [ redirect, setRedirect ] = useState(false);
  const [ alert, setAlert ] = useState(false);

  const handleSubmit = e => {
    e.preventDefault();
    let userinfo = {
      user_name : name,
      email : email,
      password : password
      };

      const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(userinfo),
        credentials: "include"
      };

      fetch("/users", requestOptions)
      .then(response => {
        if (response.status === 200)
          setRedirect(true)
        if (response.status === 401)
           setAlert(true)
      })
      .catch(err =>{
        console.log("error : ", err)
      })
    }
    
    if (redirect){
      return (
        <Navigate to='/signIn'/>
      )
    }
  
    return (
      <Card style={styles.card}>
        <h3 style={styles.h3}>Sign Up</h3>
        { alert && <Alert severity="error">Username already exists or email is invalid</Alert> }
        <form style={styles.form}>
          <TextField id="outlined-basic"
            style={styles.textField}
            label="Username"
            placeholder='Enter Username'
            variant="outlined"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
          <TextField id="outlined-basic"
            style={styles.textField}
            label="Email"
            placeholder='Enter Email'
            variant="outlined"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
          <TextField id="outlined-basic"
            style={styles.textField}
            placeholder='Enter Password'
            label="Password"
            variant="outlined"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <Button style={styles.button} variant="contained" color="primary" type="submit" onClick={handleSubmit}>
            Register
          </Button>
        </form>
      </Card>
  );  
};  

export default SignUp;