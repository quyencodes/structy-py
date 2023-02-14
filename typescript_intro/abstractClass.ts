abstract class TakePhoto {
  constructor(
    public cameraMode: string,
    public filter: string,
  ){}

  abstract getSepia(): void
  getReelTime(): number {
    // some complex calculation
    return 8
  }
}

// const qh = new TakePhoto('test', 'test')

class Instagram extends TakePhoto {
  constructor(
    public cameraMode: string,
    public filter: string,
    public burst: number
  ) {
    super(cameraMode, filter)
  }
}

export {}