let score: number | string = 33

score = 44

score = '55'

type User = {
  name: string;
  id: number;
}

type Admin = {
  username: string;
  id: number;
}

let quyen: User | Admin = {
  name: "quyen",
  id: 334
}

quyen = {username: "hc", id: 334}

// function getDbId(id: number | string) {
//   // making some api calls
//   console.log(`DB id is ${id}`)
// }
function getDbId(id: number | string) {
  // making some api calls
  if (typeof id === 'string') {
    id.toLowerCase()
  } else if (typeof id === 'number') {
    id + 2
  }
}

getDbId(3)
getDbId('3')

// array
const data: number[] = [1, 2, 3, 4]
const data2: string[] = ['1', '2', '3', '4']
const data3: (string | number)[] = ['1', '2', 3]
const data4: any[] = ['1', '2', 3] // -> bad practice

let seatAllotment: "aisle" | "middle" | "window"

seatAllotment = "aisle"
// seatAllotment = "crew"
