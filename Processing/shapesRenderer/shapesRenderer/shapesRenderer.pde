void setup(){
  size(200,200);
  translate(100,100);
  PShape shape = createShape();
  shape.beginShape();
  shape.noStroke();
  shape.fill(0,0,0);
  
  shape.endShape(CLOSE);
  frameRate(30);
}

void draw(){
  
}
