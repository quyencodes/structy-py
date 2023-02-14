class User {
  private _courseCount = 1
  readonly city: string = "Jaipur"
  constructor (
    public email: string,
    public name: string,
  ) {}

  get getAppleEmail(): string {
    return `apple${this.email}`
  }

  get courseCount(): number {
    return this._courseCount
  }

  set courseCount(courseNumber: number) {
    if (courseNumber <= 1) {
      throw new Error("Course count should be more than 1")
    }
    this._courseCount = courseNumber
  }
}

const hitesh = new User("q@q.com", "quyen")
hitesh.city = "Jaipur"