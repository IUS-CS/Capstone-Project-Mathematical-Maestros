import React from 'react';
  
const SignIn = () => {
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
        <h1>Sign In Page</h1><br></br>
        <h1>Username:</h1>
        
        <input type="textbox" name="usernameBox"></input><br></br>
        <h2>Password:</h2>
        <input type="textbox" name="passwordBox"></input><br></br>
        <br></br>
        <button type="button" onClick="enter()">Enter</button>
        
        <button onClick="forgot">Forgot Password</button>
      </body>
    </div>
  );
};
  
export default SignIn;