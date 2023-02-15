const score: Array<number> = []
const names: Array<string> = []
function identityOne(val: boolean | number): boolean | number {
  return val
}

function identityTwo(val: any): any {
  return val
}

function identityThree<Type>(val: Type): Type {
  return val
}

// identityThree(true)
function identityFour<T>(val: T): T {
  return val
}

interface Bottle {
  brand: string;
  type: number;
}

// identityFour<Bottle>({})

function getSearchProducts<T>(products: T[]):T {
  // do some database operations
  const myIndex = 3
  return products[myIndex]
}

const getMoreSearchProducts = <T,>(products: T[]): T => {
  // do some database operations
  const myIndex = 4
  return products[myIndex]
}

function anotherFunction<T, U>(val1: T, val2: U):object {
  return {
    val1,
    val2
  }
}

interface Quiz {
  name: string,
  type: string,
}

interface Course {
  name: string,
  author: string,
  subject: string,
}

class Sellable<Type> {
  public cart: Type[] = []

  addToCart(product: Type) {
    this.cart.push(product)
  }
}

function detectType(val: number | string) {
  if (typeof val === 'string') {
    return val.toLowerCase()
  }
  return val + 3
}