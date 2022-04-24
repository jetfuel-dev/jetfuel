import Home from './pages/Home';
import { makeStyles, createStyles } from "@mui/styles";

import '@fontsource/roboto/300.css';
import '@fontsource/roboto/400.css';
import '@fontsource/roboto/500.css';
import '@fontsource/roboto/700.css';

const useStyles = makeStyles(() =>
  createStyles({
    "root": {
      width: "100vw",
      height: "100vh",
      backgroundColor: "#1f1f1f",
      position: "absolute",
      top: "0",
      left: "0",
    }
  })
);

function App() {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <Home/>
    </div>
  );
}

export default App;
