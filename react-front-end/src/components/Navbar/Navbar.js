import * as React from "react";
import { useState } from "react";
import { NavLink } from "react-router-dom";
import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import Toolbar from "@mui/material/Toolbar";
import IconButton from "@mui/material/IconButton";
import MenuIcon from "@mui/icons-material/Menu";
import Drawer from "@mui/material/Drawer";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import logo from "./logo.png";
import logoAlt from "./logo-alt.png";

const Navbar = () => {
  const [isDrawerOpen, setIsDrawerOpen] = useState(false);

  const styles = {
    root: {
      display: "flex",
    },
    appBar: {
      backgroundColor: "#44BBA4",
    },
    menuButton: {
      marginLeft: "auto",
      marginRight: 36,
      color: "#000000",
      opacity: "1",
    },
    logo: {
      marginLeft: 36,
      marginRight: "auto",
      opacity: "1",
    },
    list: {
      width: "15rem",
    },
    listItem: {
      color: "#000000",
      fontSize: "1.5rem",
      display: "flex",
      alignText: "center",
    },
    link: {
      textDecoration: "none",
    },
  };

  return (
    <Box style={styles.root}>
      <AppBar position="static" style={styles.appBar}>
        <Toolbar>
          <IconButton style={styles.logo}>
            <NavLink to="/">
              <picture>
                <source media="(min-width:650px)" srcset={logo} />
                <source media="(min-width:350px)" srcset={logoAlt} />
                <img src={logo} alt="logo" />
              </picture>
            </NavLink>
          </IconButton>
          <IconButton
            style={styles.menuButton}
            onClick={() => setIsDrawerOpen(true)}
          >
            <MenuIcon />
          </IconButton>
          <Drawer
            open={isDrawerOpen}
            onClose={() => setIsDrawerOpen(false)}
            anchor="right"
            PaperProps={{
              sx: {
                backgroundColor: "#97B0AA",
              },
            }}
          >
            <List style={styles.list}>
              <NavLink to="/signUp" style={styles.link}>
                <ListItem button style={styles.listItem}>
                  Sign Up
                </ListItem>
              </NavLink>
              <NavLink to="/signIn" style={styles.link}>
                <ListItem button style={styles.listItem}>
                  Sign In
                </ListItem>
              </NavLink>
            </List>
          </Drawer>
        </Toolbar>
      </AppBar>
    </Box>
  );
};

export default Navbar;
