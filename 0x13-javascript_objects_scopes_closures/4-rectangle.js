#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let rect = '';
      for (let j = 0; j < this.width; j++) {
        rect = rect + 'X';
      }
      console.log(rect);
    }
  }

  rotate () {
    const tempHeight = this.height;
    this.height = this.width;
    this.width = tempHeight;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
};
