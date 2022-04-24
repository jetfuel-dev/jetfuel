import { makeStyles, createStyles } from "@mui/styles";
import { Typography } from '@mui/material';

const useStyles = makeStyles(() =>
  createStyles({
    "container": {
      width: "200px",
      height: "30px",
      color: "white",
      cursor: "pointer",
      marginBottom: "2px",
      "&:hover": {
        color: "#baffc9",
        marginBottom: "0px",
        borderBottom: "2px solid #baffc9",
      }
    },
  })
);

interface Props {
  children: React.ReactNode;
}

function NavButton(props: Props) {
  const classes = useStyles();

  return (
    <div className={classes.container}>
      <Typography variant="body1" align="center">
        {props.children}
      </Typography>
    </div>
  );
}

export default NavButton;
