import React from "react";
import { useState } from "react";
import { Navigate } from "react-router-dom";
import Card from "@mui/material/Card";
import Divider from "@mui/material/Divider";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import Alert from "@mui/material/Alert";
import Typography from "@mui/material/Typography";

const styles = {
  card: {
    position: "absolute",
    left: "50%",
    top: "50%",
    webkitTransform: "translate(-50%, -50%)",
    transform: "translate(-50%, -50%)",
    textAlign: "center",
    minWidth: "360px",
  },
  form: {
    margin: "10px",
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
  },
  textField: {
    margin: "10px",
  },
  button: {
    margin: "10px",
  },
  alert: {
    margin: "10px",
  },
};

const SignUp = () => {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const [redirect, setRedirect] = useState(false);
  const [failureAlert, setFailureAlert] = useState(false);
  const [successAlert, setSuccessAlert] = useState(false);
  const [invalidAlert, setInvalidAlert] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    let userinfo = {
      user_name: name,
      email: email,
      password: password,
    };

    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(userinfo),
      credentials: "include",
    };

    if ((name === "") | (email === "") | (password === "")) {
      setInvalidAlert(true);
      return;
    }

    fetch("/api/users", requestOptions)
      .then((response) => {
        if (response.status === 200) setSuccessAlert(true);
        setTimeout(() => {
          setRedirect(true);
        }, 1000);
        if (response.status === 401) setFailureAlert(true);
      })
      .catch((err) => {
        console.log("error : ", err);
      });
  };

  if (redirect) {
    return <Navigate to="/signIn" />;
  }

  return (
    <Card style={styles.card}>
      <Typography variant="h2" gutterBotton>
        Sign Up
      </Typography>
      <Divider variant="middle" light />
      {failureAlert && (
        <Alert severity="error" style={styles.alert}>
          Username already exists or email is invalid.
        </Alert>
      )}
      {successAlert && (
        <Alert severity="success" style={styles.alert}>
          Registration Successful!
        </Alert>
      )}
      {invalidAlert && (
        <Alert severity="warning" style={styles.alert}>
          Invalid. You have not been registered.
        </Alert>
      )}
      <form style={styles.form}>
        <TextField
          id="outlined-basic"
          style={styles.textField}
          label="Username"
          placeholder="Enter Username"
          variant="outlined"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        <TextField
          id="outlined-basic"
          style={styles.textField}
          label="Email"
          placeholder="Enter Email"
          variant="outlined"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <TextField
          id="outlined-basic"
          style={styles.textField}
          placeholder="Enter Password"
          label="Password"
          variant="outlined"
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <Button
          style={styles.button}
          variant="contained"
          color="primary"
          type="submit"
          onClick={handleSubmit}
        >
          Register
        </Button>
      </form>
    </Card>
  );
};

export default SignUp;
