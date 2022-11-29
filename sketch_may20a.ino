#include <Stepper.h>
#include <Servo.h> 
Servo servo; 
const int stepsPerRevolution = 1024;
int servoPin = 12;
int input_data;
Stepper myStepper(stepsPerRevolution, 11, 9, 10, 8);

int a=0;
int num=0;
void Go_Motor(int roof){
  while(num<(825*roof)){
  if(a<=500){
      a+=50;
    }
  if(a>500 and a<800){
      a+=1;
    }

    int sensorReading=a;
    int motorSpeed = map(sensorReading, 0, 1023, 0, 100);
    if (motorSpeed > 0) {
      myStepper.setSpeed(motorSpeed);
      myStepper.step(-stepsPerRevolution / 100);
    }
    num+=1;
}
  num=0;
  a=0;
}
void Back_Motor(int roof){
  while(num<(825*roof)){
  if(a<=500){
      a+=50;
    }
  if(a>500 and a<800){
      a+=1;
    }

    int sensorReading=a;
    int motorSpeed = map(sensorReading, 0, 1023, 0, 100);
    if (motorSpeed > 0) {
      myStepper.setSpeed(motorSpeed);
      myStepper.step(stepsPerRevolution / 100);
    }
    num+=1;
}
  num=0;
  a=0;
}
void Servo_Motor(){
     servo.attach(servoPin);
     servo.write(0);
     delay(500);
     servo.write(45);
     delay(2000);
     servo.write(0);
     delay(1000);
}
//------------------------------
void FeedBack_Led(int led){
  switch(led)
  {
    case 1: //green led
      digitalWrite(6,HIGH);
      delay(2500);    
      digitalWrite(6,LOW);
      break;
    case 2: //red led
      digitalWrite(7,HIGH);
      delay(2500);
      digitalWrite(7,LOW);
      break;
    case 3: // find 
        digitalWrite(6,HIGH);
        delay(100);    
        digitalWrite(6,LOW);
        delay(100);    
        digitalWrite(6,HIGH);
        delay(100);    
        digitalWrite(6,LOW);
        delay(100);  
        digitalWrite(6,HIGH);
        delay(100);    
        digitalWrite(6,LOW);
        delay(100);  
        break;
    case 4: // can not find
        digitalWrite(7,HIGH);
        delay(100);    
        digitalWrite(7,LOW);
        delay(100);    
        digitalWrite(7,HIGH);
        delay(100);    
        digitalWrite(7,LOW);
        delay(100);  
        digitalWrite(7,HIGH);
        delay(100);    
        digitalWrite(7,LOW);
        delay(100);  
        break;
  }
  
}
//----------------------------------
void setup() {
  Serial.begin(9600);
  pinMode(7,OUTPUT);
  pinMode(6,OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.available();
  input_data = Serial.read();
  switch(input_data){
    case '1': //GoTo_DarkRoom
      Back_Motor(2);
      input_data='0';
      break;

    case '2': //GoTo_can
      Go_Motor(0);
      Servo_Motor();
      Go_Motor(2);
      input_data='0';
      FeedBack_Led(1);
      break;
      
    case '3': //GoTo_glass
      Go_Motor(1);
      Servo_Motor();
      Go_Motor(1);
      input_data='0';
      FeedBack_Led(1);
      break;
      
    case '4': //GoTo_colored_PT
      Go_Motor(2);
      Servo_Motor();
      Go_Motor(0);
      input_data='0';
      FeedBack_Led(1);
      
      break;
    case '5': //GoTo_Transparent_PT
      Go_Motor(3);
      Servo_Motor();
      Back_Motor(1);
      input_data='0';
      FeedBack_Led(1);
      break;
    case '6': //GoTo_carton
      Go_Motor(4);
      Servo_Motor();
      Back_Motor(2);
      input_data='0';
      FeedBack_Led(1);
      break;
    case '7':
      input_data='0';
      FeedBack_Led(3);
      break;
    case '8':
      input_data='0';
      FeedBack_Led(4);
      break;
    case '0': //GoTo_return
      Go_Motor(2);
      input_data='0';
      FeedBack_Led(2);
      break;
  }
}
