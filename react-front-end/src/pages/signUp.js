import React from 'react';
  
const SignUp = () => {
  return (
    <div
      style={{
        display: 'flex',
        justifyContent: 'Center',
        alignItems: 'Center',
        height: '100vh',
      }}
    >
      <body>
        <h1>Sign Up</h1><br></br>
        <h2>Email:</h2>
        <input type="textbox" name="Email"></input><br></br>
        <h2>Username:</h2>
        <input type="textbox" name="username"></input><br></br>
        <h2>Password:</h2>
        <input type="textbox" name="passwordBox"></input><br></br> 
        <br></br>
        <button type="button" onClick="enter()">Enter</button><br></br>

      </body>
    </div>
  );
};
  
export default SignUp;