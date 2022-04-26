export interface Data {
  x: number[];
  min: number[];
  max: number[];
  mean: number[];
  count: number[];
}


export interface DataContainer {
  data: {[name: string]: Data}
}


export async function getDataAPI(start: number): Promise<DataContainer> {
  const url = `${window.location.protocol}//localhost:9000/data?start=${start}`;
  const response = await fetch(url, {
    method: "GET",
    headers: {
      "Authorization": "Bearer default",
      "Content-Type": "application/json",
    },
  });
  return response.json()
}
