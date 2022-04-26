import { makeStyles, createStyles } from "@mui/styles";
import { Typography } from '@mui/material';
import ReactECharts from 'echarts-for-react';
import { Data } from "../logic/api";

const useStyles = makeStyles(() =>
  createStyles({
    "container": {
      width: "100%",
      marginTop: "30px",
    },
    "chartContainer": {
      width: "100%",
      height: "300px",
      overflow: "show",
      display: "flex",
      flexDirection: "row",
    },
    "title": {
      color: "white",
      textAlign: "center",
    }
  })
);

interface Props {
  name: string;
  data: Data;
}

function ProfileChart(props: Props) {
  const classes = useStyles();

  // Calculate histogram
  const nBins = 50;
  const max = Math.max(...props.data.max);
  const min = Math.min(...props.data.min);
  const binWidth = (max - min) / nBins;

  const histogramBins = [];
  let histogramValues = [];

  for (var i = 0; i < nBins; i++) {
    histogramBins.push(min + (i * binWidth));
    histogramValues.push(0);
  }

  console.log(histogramBins)

  let totalValue = 0;
  for (var i = 0; i < props.data.mean.length; i++) {
    histogramValues[Math.floor((props.data.mean[i] - min) / binWidth)] += props.data.count[i];
    totalValue += props.data.count[i];
  }
  histogramValues = histogramValues.map(value => 100 * value / totalValue);


  return (
    <div className={classes.container}>
      <Typography variant="h6" className={classes.title}>
        {props.name}
      </Typography>
      <div className={classes.chartContainer}>
        <ReactECharts
          style={{width: "calc(100% - 150px)", height: "100%"}}
          option={{
            grid: {
              top: 10,
              right: 0,
              bottom: 10,
              left: 50,
              show: true,
              borderColor: "#555",
              backgroundColor: "#1f1f1f",
            },
            tooltip: {
              trigger: 'axis'
            },
            xAxis: {
              type: 'category',
              data: props.data.x.map(timestamp => new Date(timestamp * 1000)),
              show: false,
              axisLine: {
                show: true
              }
            },
            yAxis: {
              max: Math.round(max),
              min: Math.round(min),
              splitNumber: 5,
              axisTick: {
                show: true,
              },
              axisLine: {
                show: true
              },
              splitLine: {
                lineStyle: {
                  color: "#555"
                }
              },
              axisLabel: {
                formatter: '{value} s'
              }
            },
            series: [
              {
                name: 'Max',
                type: 'line',
                data: props.data.max,
                lineStyle: {
                  opacity: 0
                },
                areaStyle: {
                  color: '#003810',
                  opacity: 1,
                },
                symbol: 'none'
              },
              {
                name: 'Average',
                type: 'line',
                data: props.data.mean,
                showSymbol: false,
                lineStyle: {
                  color: "#00d639",
                  width: 1,
                },
              },
              {
                name: 'Min',
                type: 'line',
                data: props.data.min,
                lineStyle: {
                  opacity: 0
                },
                areaStyle: {
                  color: '#1f1f1f',
                  opacity: 1,
                },
                symbol: 'none'
              },
            ]
          }}
          lazyUpdate={true}
          notMerge={true}
        />
        <ReactECharts
          style={{width: "150px", height: "100%"}}
          option={{
            grid: {
              top: 10,
              right: 50,
              bottom: 10,
              left: 0,
              show: true,
              borderColor: "#555",
            },
            tooltip: {
              trigger: 'axis',
              valueFormatter: (value: number) => `${value.toFixed(2)} %`,
            },
            xAxis: {
              type: 'value',
              data: histogramBins,
              show: false,
            },
            yAxis: {
              type: 'category',
              show: false
            },
            series: [
              {
                type: 'bar',
                data: histogramValues,
                showSymbol: false,
                color: "#007321",
              },
            ]
          }}
          lazyUpdate={true}
          notMerge={true}
        />
      </div>
    </div>
  );
}

export default ProfileChart;
