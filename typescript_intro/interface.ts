interface User {
  readonly dbId: number,
  email: string,
  userId: number
  googleId?: string
}

const quyen: User = {dbId: 22, email: 'quyen@gmail.com', userId: 2211}
