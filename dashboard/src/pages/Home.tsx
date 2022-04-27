import { useState } from 'react';
import { makeStyles, createStyles } from "@mui/styles";
import { Typography } from '@mui/material';
import NavBar from "../components/NavBar";
import Dashboard from "../components/Dashboard";
import logo from '../assets/jetfuel.png';


const useStyles = makeStyles(() =>
  createStyles({
    "full": {
      width: "100vw",
      height: "100vh",
      position: "absolute",
      top: "0",
      left: "0",
      display: "flex",
      flexDirection: "column",
    },
    "logo": {
      width: "200px",
      margin: "70px auto 0px auto",
    },
    "main": {
      height: "100%",
      width: "100%",
      margin: "0px auto",
    },
    "header": {
      fontWeight: "bold",
      color: "white",
    },
    "body": {
      height: "calc(100vh - 250px)",
      overflowY: "scroll",
      padding: "0px calc(50vw - 700px)",
    }
  })
);

function Home() {
  const classes = useStyles();

  const options = ["Dashboard"];
  const [selected, setSelected] = useState(options[0]);

  return (
    <div className={classes.full}>
      <img src={logo} className={classes.logo} alt="logo" />
      <div className={classes.main}>
        <Typography variant="h6" align="center" className={classes.header}>
          Python Performance Profiling for Production
        </Typography>
        <NavBar
          options={options}
          selected={selected}
          setSelected={(option: string) => {
            setSelected(option);
          }}
        />
        <div className={classes.body}>
          <Dashboard/>
        </div>
      </div>
    </div>
  );
}

export default Home;
