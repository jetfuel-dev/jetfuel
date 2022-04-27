import { useEffect, useState } from 'react';
import { makeStyles, createStyles } from "@mui/styles";
import ProfileChart from "./ProfileChart";
import { getDataAPI, Data } from "../logic/api";

const useStyles = makeStyles(() =>
  createStyles({})
);

interface Props {}

function Dashboard(props: Props) {
  const classes = useStyles();

  const [data, setData] = useState<{[name: string]: Data}>();
  
  const getData = () => {
    // TODO: Retrieve all data for now, until we implement selector
    // e.g. Something like: Date.now() / 1000 - (60 * 60)
    getDataAPI(0).then((data) => {
      setData(data.data);
    });
  }

  useEffect(() => {
    getData();

    const retriever = setInterval(getData, 5000);

    return () => {
      clearInterval(retriever);
    }
  }, []);

  return (
    <div>
      {data && Object.keys(data).map((name) => {
        const taskData = data?.[name] as Data;
        return <ProfileChart key={name} name={name} data={taskData}/>
      })}
    </div>
  );
}

export default Dashboard;
