import React from 'react';
import { useState } from 'react'
import { Navigate } from 'react-router-dom'
  
const SignIn = () => {
  const [name, setName] = useState("");
  const [password, setPassword] = useState("");

  const [ redirect, setRedirect ] = useState(false);

  const handleSubmit = e => {
    e.preventDefault();
    let userinfo = {
      user_name : name,
      password : password
      }

      const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(userinfo)
      };

      fetch("/sign_in", requestOptions)
      .then(response => {
        if (response.status === 200)
          setRedirect(true)
      })
      .catch(err =>{
        console.log("error : ", err)
      })
    }
    
    if (redirect){
      return (
        <Navigate to='/'/>
      )
    }
    return(
    <div 
    className='signUpForm'
    style={{
      display: 'flex',
      justifyContent: 'Center',
      alignItems: 'Center',
      height: '100vh',
      lineHeight: 2.4,
    }}>
      
    <form>
      <h1>Sign In Page</h1>
      <br></br>
      <label>Enter Username: &emsp;
        <input
          type="text" 
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
      </label>
      
      <br></br>
      <label>Enter Password: &emsp;
        <input
          type="text" 
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
      </label>
      <br></br>
      <button onClick={handleSubmit}>Click Me!</button>
    </form>
  </div>
  );
};

export default SignIn;