void FillShapesList(){
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
}

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

void ScalePShapes(float w, float h){
  for (int i = 0; i < 256; i ++){
    scaledShapes[i] = ScaleShape(shapes[i], w, h);
  }
}

//------------------------------------------------------------------------------------------------------------------------

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
  shape.vertex(0.4568,0.6568);
  shape.vertex(0.6568,0.4568);
  
  //Rigth center
  shape.vertex(0.76335393438588,0.23935490564765);
  shape.vertex(0.76335393438588,-0.23935490564765);
  
  //Right down corner
  shape.vertex(0.6568,-0.4568);
  shape.vertex(0.4568,-0.6568);
  
  //Down center
  shape.vertex(0.23935490564765,-0.76335393438588);
  shape.vertex(-0.23935490564765,-0.76335393438588);
  
  //Left down corner
  shape.vertex(-0.4568,-0.6568);
  shape.vertex(-0.6568,-0.4568);
  
  //Left center
  shape.vertex(-0.76335393438588,-0.23935490564765);
  shape.vertex(-0.76335393438588,0.23935490564765);
  
  //Left up corner
  shape.vertex(-0.6568,0.4568);
  shape.vertex(-0.4568,0.6568);
  
  //Up
  shape.vertex(-0.23935490564765,0.76335393438588);
  shape.vertex(0.23935490564765,0.76335393438588);
  
  shape.endShape(CLOSE);
  return shape;
}
