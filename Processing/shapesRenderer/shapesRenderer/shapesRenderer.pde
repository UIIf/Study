PShape[] shapes = new PShape[256];
PShape[] scaledShapes = new PShape[256];
int counter = 0;
boolean toggle = false;

float w = 30, h = 30;

void setup(){
  size(1080,720);
  FillShapesList();
  ScalePShapes(w,h);
  frameRate(120);
}

void draw(){  
  //translate(width/2,height/2);
  background(255,255,255);
  
  for(int i = 0; i < height; i += 2*h){
    for(int j = 0; j < width; j += 2*w){
        shape(scaledShapes[counter], j + w, i + h);
      }
  }
  
  if(toggle){
    counter--;
  }
  else{
    counter++;
  }
  
  
  if(counter >= 255){
    toggle = true; 
  }
  else if(counter<= 0){
    toggle = false;
  }
}
