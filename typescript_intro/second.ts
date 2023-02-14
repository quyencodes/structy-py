interface TakePhoto {
  cameraMode: string
  filter: string
  burst: number
}

class Story implements TakePhoto {
  cameraMode: string
  filter: string
  burst: number
  createStory(): void {
    console.log("Story was created")
  }
}

class Instagram implements TakePhoto {
  constructor(
    public cameraMode: string,
    public filter: string,
    public burst: number){}
}

class Youtube implements TakePhoto {
  constructor (
    public cameraMode: string,
    public filter: string,
    public burst: number,
    public short: string
  ) {}
}