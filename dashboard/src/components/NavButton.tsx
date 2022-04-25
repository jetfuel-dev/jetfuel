import { useState } from 'react';
import { makeStyles, createStyles } from "@mui/styles";
import { Typography } from '@mui/material';
import clsx from 'clsx';

const useStyles = makeStyles(() =>
  createStyles({
    "container": {
      width: "200px",
      height: "30px",
      color: "white",
      cursor: "pointer",
      marginBottom: "2px",
    },
    "selected": {
      color: "#a1c5ff",
      marginBottom: "0px",
      borderBottom: "2px solid #a1c5ff",
    }
  })
);

interface Props {
  children: React.ReactNode;
  selected: boolean;
}

function NavButton(props: Props) {
  const classes = useStyles();

  const [hover, setHover] = useState(false);

  return (
    <div
      className={clsx(classes.container, (props.selected || hover) && classes.selected)}
      onMouseOver={() => {setHover(true)}}
      onMouseOut={() => {setHover(false)}}
    >
      <Typography variant="body1" align="center">
        {props.children}
      </Typography>
    </div>
  );
}

export default NavButton;
