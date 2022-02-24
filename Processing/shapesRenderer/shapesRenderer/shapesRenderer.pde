PShape[] shapes = new PShape[256];
int counter = 0;

void setup(){
  size(200,200);
  PShape[] mainShapes = new PShape[5]; 
  
  mainShapes[0] = VoidShape();
  mainShapes[1] = RectShape(0.25);
  mainShapes[2] = CrosShape();
  mainShapes[3] = CircleShape();
  mainShapes[4] = RectShape(0.9);
  
  for(int i = 0; i < 64; i++){
    shapes[i] = LerpShape(  mainShapes[0], mainShapes[1], map(i, 0, 63, 0.,1.));
  }
  for(int i = 0; i < 64; i++){
    shapes[i+64] = LerpShape(  mainShapes[1], mainShapes[2], map(i, 0, 63, 0.,1.));
  }
  
  for(int i = 0; i < 64; i++){
    shapes[i+128] = LerpShape(  mainShapes[2], mainShapes[3], map(i, 0, 63, 0.,1.));
  }
  
  for(int i = 0; i < 64; i++){
    shapes[i+192] = LerpShape(  mainShapes[3], mainShapes[4], map(i, 0, 63, 0.,1.));
  }
  
  frameRate(60);
}
//Color step = 64

PShape ScaleShape(PShape shape, float w, float h){
  PShape to_ret = VoidShape();
  PVector temp;
  
  for(int i = 0; i < 16; i++){
    temp = shape.getVertex(i);
    temp.x *= w;
    temp.y *= h;
    to_ret.setVertex(i, temp); 
  }
  
  return to_ret;
}

PShape LerpShape(PShape less, PShape more, float t){
  PShape to_ret = VoidShape();
  PVector a, b, n;
  for(int i = 0; i < 16; i++){
     a = less.getVertex(i);
     b = more.getVertex(i);
     n = new PVector(lerp(a.x,b.x,t), lerp(a.y,b.y,t));
     to_ret.setVertex(i, n);
  }
  return to_ret;
}

PShape VoidShape(){
  PShape shape = createShape();  
  shape.setFill(color(0,0,0));
  shape.beginShape();
  shape.noStroke();
  for(int i = 0; i < 16; i++){
    shape.vertex(0,0);
  }
  shape.endShape(CLOSE);
  return shape;
}

PShape RectShape(float temp){
  PShape shape = createShape();
  //shape.setFill(smth);
  
  shape.beginShape();
  shape.fill(color(255, 0, 0));
  shape.noStroke();
  
  //Right up corner
  shape.vertex(temp,temp);
  shape.vertex(temp,temp);
  
  //Rigth center
  shape.vertex(temp,0);
  shape.vertex(temp,0);
  
  //Right down corner
  shape.vertex(temp,-temp);
  shape.vertex(temp,-temp);
  
  //Down center
  shape.vertex(0,-temp);
  shape.vertex(0,-temp);
  
  //Left down corner
  shape.vertex(-temp,-temp);
  shape.vertex(-temp,-temp);
  
  //Left center
  shape.vertex(-temp,0);
  shape.vertex(-temp,0);
  
  //Left up corner
  shape.vertex(-temp,temp);
  shape.vertex(-temp,temp);
  
  //Up
  shape.vertex(0,temp);
  shape.vertex(0,temp);
  
  shape.endShape(CLOSE);
  return shape;
}

PShape CrosShape(){
  PShape shape = createShape();
  
  shape.beginShape();
  shape.fill(color(255, 0, 0));
  shape.noStroke();
  
  //Right up corner
  shape.vertex(0.5285,0.7285);
  shape.vertex(0.7285,0.5285);
  
  //Rigth center
  shape.vertex(0.2,0);
  shape.vertex(0.2,0);
  
  //Right down corner
  shape.vertex(0.7285,-0.5285);
  shape.vertex(0.5285,-0.7285);
  
  //Down center
  shape.vertex(0,-0.2);
  shape.vertex(0,-0.2);
  
  //Left down corner
  shape.vertex(-0.5285,-0.7285);
  shape.vertex(-0.7285,-0.5285);
  
  //Left center
  shape.vertex(-0.2,0);
  shape.vertex(-0.2,0);
  
  //Left up corner
  shape.vertex(-0.7285,0.5285);
  shape.vertex(-0.5285,0.7285);
  
  //Up
  shape.vertex(0,0.2);
  shape.vertex(0,0.2);
  
  shape.endShape(CLOSE);
  return shape;
}

PShape CircleShape(){
  PShape shape = createShape();
  
  shape.beginShape();
  shape.fill(color(255, 0, 0));
  shape.noStroke();
  
  //Right up corner
  shape.vertex(0.5285,0.7285);
  shape.vertex(0.7285,0.5285);
  
  //Rigth center
  shape.vertex(0.85604908870067,0.27781281060231);
  shape.vertex(0.85604908870067,-0.27781281060231);
  
  //Right down corner
  shape.vertex(0.7285,-0.5285);
  shape.vertex(0.5285,-0.7285);
  
  //Down center
  shape.vertex(0.2778128106023,-0.85604908870067);
  shape.vertex(-0.2778128106023,-0.85604908870067);
  
  //Left down corner
  shape.vertex(-0.5285,-0.7285);
  shape.vertex(-0.7285,-0.5285);
  
  //Left center
  shape.vertex(-0.85604908870067,-0.27781281060231);
  shape.vertex(-0.85604908870067,0.27781281060231);
  
  //Left up corner
  shape.vertex(-0.7285,0.5285);
  shape.vertex(-0.5285,0.7285);
  
  //Up
  shape.vertex(-0.2778128106023,0.85604908870067);
  shape.vertex(0.2778128106023,0.85604908870067);
  
  shape.endShape(CLOSE);
  return shape;
}

void draw(){
  
  translate(width/2,height/2);
  background(255,255,255);
  
  shape(ScaleShape( shapes[counter], 50, 50), 0, 0);
  //shape(ScaleShape( SmallRectShape(), 50, 50), 0, 0); 
  
  counter++;
  counter %= 256;
}
