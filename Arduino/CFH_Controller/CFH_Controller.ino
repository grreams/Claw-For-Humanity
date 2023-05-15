String incomingByte = 0;
int choice = 0;

void setup() {
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT); 

  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    incomingString = Serial.readString();
    choice = incomingString.toInt();
  }
  
  switch(choice){
    case 0:
      // Drive off
      digitalWrite(6, HIGH);

      // All pistons off
      digitalWrite(1, LOW);
      digitalWrite(2, LOW);
      digitalWrite(3, LOW);
      digitalWrite(4, LOW);
      digitalWrite(5, LOW);
      break;
    case 1:
      // Drive on
      digitalWrite(6, LOW);

      // All pistons on
      digitalWrite(1, HIGH);
      digitalWrite(2, HIGH);
      digitalWrite(3, HIGH);
      digitalWrite(4, HIGH);
      digitalWrite(5, HIGH);
      break;
    case 2:
      // Drive off
      digitalWrite(6, HIGH);
      break;
    case 3:
      // Drive on
      digitalWrite(6, LOW);
      break;
    case 4:
      // Piston 1 on
      digitalWrite(1, HIGH);
      break;
    case 5:
      // Piston 1 off
      digitalWrite(1, LOW);
      break;
    case 6:
      // Piston 2 on
      digitalWrite(2, HIGH);
      break;
    case 7:
      // Piston 2 off
      digitalWrite(2, LOW);
      break;
    case 8:
      // Piston 3, 4 on
      digitalWrite(3, HIGH);
      digitalWrite(4, HIGH);
      break;
    case 9:
      // Piston 3, 4 off
      digitalWrite(3, LOW);
      digitalWrite(4, LOW);
      break;
    default:
      break;
  }
}
