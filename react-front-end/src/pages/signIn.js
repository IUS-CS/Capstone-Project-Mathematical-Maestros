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

const SignIn = () => {
  const [name, setName] = useState("");
  const [password, setPassword] = useState("");

  const [redirect, setRedirect] = useState(false);
  const [failureAlert, setFailureAlert] = useState(false);
  const [successAlert, setSuccessAlert] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    let userinfo = {
      user_name: name,
      password: password,
    };

    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(userinfo),
      credentials: "include",
    };

    fetch("/api/users/session", requestOptions)
      .then((response) => {
        if (response.status === 200) {
          setSuccessAlert(true);
          setTimeout(() => {
            setRedirect(true);
          }, 1000);
        }
        if (response.status === 401) setFailureAlert(true);
      })
      .catch((err) => {
        console.log("error : ", err);
      });
  };

  if (redirect) {
    return <Navigate to="/" />;
  }

  return (
    <Card style={styles.card}>
      <Typography variant="h2" gutterBotton>
        Sign In
      </Typography>
      <Divider variant="middle" light />
      {failureAlert && (
        <Alert severity="error" style={styles.alert}>
          Incorrect username or password
        </Alert>
      )}
      {successAlert && (
        <Alert severity="success" style={styles.alert}>
          Log in Successful!
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
          Login
        </Button>
      </form>
    </Card>
  );
};

export default SignIn;
