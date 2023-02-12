function addTwo(num: number): number {
  return num + 2;
  // return 'error about return type'
}

// union type stuff we'll learn later
// function getValue(myVal: number): {
//   if (myVal > 5) {
//     return true
//   }
//   return '200 OK'
// }

const getHello = (s: string): string => {
  return ""
}

var id: number = 123

function getUpper(s: string) {
  return s.toUpperCase()
}

function signUpUser(name: string, email: string, isPaid: boolean) {

}

let loginUser = (name: string, email: string, isPaid: boolean = false) => {
  if (isPaid === void 0) {isPaid = false}
}

let myValue = addTwo(5);
getUpper('four')
signUpUser('quyen', 'quyen@ts.com', false)
loginUser("h", "h&h.com")

const heros: string[] = ["thor", "spiderman", "ironman"]
// const heros = [1, 2, 3]

heros.map((hero): string => {
  return `hero is ${hero}`
})


// 1:11 video
function consoleError(errmsg:string): never {
  throw new Error(errmsg)
}

export {}