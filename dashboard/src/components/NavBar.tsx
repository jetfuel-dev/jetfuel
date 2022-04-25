import { makeStyles, createStyles } from "@mui/styles";
import NavButton from './NavButton';

const useStyles = makeStyles(() =>
  createStyles({
    "navbar": {
      width: "100%",
      marginTop: "40px",
      borderBottom: "solid 1px white",
      display: "flex",
      flexDirection: "row",
      justifyContent: "center",
    },
  })
);

interface Props {
  options: string[];
  selected: string;
  setSelected: (option: string) => void;
}

function NavBar(props: Props) {
  const classes = useStyles();

  return (
    <div className={classes.navbar}>
      {props.options.map((option: string) => {
        return (
          <div onClick={() => {props.setSelected(option)}}>
            <NavButton selected={props.selected === option}>{option}</NavButton>
          </div>
        );
      })}
    </div>
  );
}

export default NavBar;
