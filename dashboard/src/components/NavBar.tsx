import { makeStyles, createStyles } from "@mui/styles";
import NavButton from './NavButton';

const useStyles = makeStyles(() =>
  createStyles({
    "navbar": {
      width: "min(1300px, calc(100% - 100px))",
      margin: "40px auto 0px auto",
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
          <div key={option} onClick={() => {props.setSelected(option)}}>
            <NavButton selected={props.selected === option}>{option}</NavButton>
          </div>
        );
      })}
    </div>
  );
}

export default NavBar;
