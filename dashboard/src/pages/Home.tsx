import { makeStyles, createStyles } from "@mui/styles";
import { Typography } from '@mui/material';
import logo from '../assets/mocha.svg';
import { fontWeight } from "@mui/system";

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
      // backgroundColor: "red",
      width: "1000px",
      height: "100%",
      margin: "0px auto",
    },
    "header": {
      fontWeight: "bold",
      color: "white",
    },
    "navbar": {
      width: "100%",
      height: "50px",
      marginTop: "20px",
      borderBottom: "solid 1px white",
    }
  })
);

function Home() {
  const classes = useStyles();

  return (
    <div className={classes.full}>
      <img src={logo} className={classes.logo} alt="logo" />
      <div className={classes.main}>
        <Typography variant="h6" align="center" className={classes.header}>
          Python Performance Profiling for Production
        </Typography>
        <div className={classes.navbar}>

        </div>
      </div>
    </div>
  );
}

export default Home;
