String incomingString;
String command;
int argument;
int commandInt;

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
    incomingString = Serial.readStringUntil('\n'); // Read the command until newline character
    parseCommand(incomingString);
  }
}

void parseCommand(String commandString) {
  int separatorIndex = commandString.indexOf(':'); // Find the separator character

  if (separatorIndex != -1) { // If separator found
    command = commandString.substring(0, separatorIndex); // Extract the command
    argument = commandString.substring(separatorIndex + 1).toInt(); // Extract the argument as an integer

    executeCommand();
  } else {
    // handle error if not an int !!
    commandInt = commandString.toInt();
    if (commandInt % 2){
      turnOffDevice(commandInt / 2);
    } else {
      turnOnDevice((commandInt + 1) / 2);
    }
  }
}

void executeCommand() {
  if (command == "ON") {
    turnOnDevice(argument);
  }
  else if (command == "OFF") {
    turnOffDevice(argument);
  }
  // Add more command cases as needed
}

void turnOnDevice(int deviceNumber) {
  // Perform actions to turn on the specified device
  digitalWrite(deviceNumber + 1, HIGH);
}

void turnOffDevice(int deviceNumber) {
  // Perform actions to turn off the specified device
  digitalWrite(deviceNumber + 1, LOW);
}
  
