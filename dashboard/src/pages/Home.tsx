import { makeStyles, createStyles } from "@mui/styles";
import logo from '../assets/mocha.svg';

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
      margin: "50px auto auto auto",
    }
  })
);

function Home() {
  const classes = useStyles();

  return (
    <div className={classes.full}>
      <img src={logo} className={classes.logo} alt="logo" />
    </div>
  );
}

export default Home;
