int arrowState[4] = {0, 0, 0, 0}; // up, down, left, right
int arrowStateChange[4] = {0, 0, 0, 0}; // up, down, left, right

#define Up 2     // Idle mode
#define Down 3  // Work mode
#define Left 4   // Drive mode
#define Right 5   // Drive mode

void copyArray(int source[], int destination[], int size) {
  for (int i = 0; i < size; i++) {
    destination[i] = source[i];        
  }
}

bool arraysNotEqual(int arr1[], int arr2[], int size) {
  for (int i = 0; i < size; i++) {
    if (arr1[i] != arr2[i]) {
      return true; // Arrays are not equal
    }
  }
  return false; // Arrays are equal
}

void setup() {
  Serial.begin(9600);
  pinMode(Up,INPUT_PULLUP);
  pinMode(Down,INPUT_PULLUP);
  pinMode(Left,INPUT_PULLUP);
  pinMode(Right,INPUT_PULLUP);
  digitalWrite(Up, HIGH);
  digitalWrite(Down, HIGH); 
  digitalWrite(Left, HIGH);
  digitalWrite(Right, HIGH); 
}

void loop() {
  // if (Serial.available() > 0) {
    char key = Serial.read();

    // Handle arrow key presses
    if(digitalRead(Up) == LOW){            
      arrowState[0] = 1;    
    } else {
      arrowState[0] = 0;  
    }
    
    if(digitalRead(Down) == LOW){            
      arrowState[1] = 1;    
    } else {
      arrowState[1] = 0;  
    }   

    if(digitalRead(Left) == LOW){            
      arrowState[2] = 1;    
    } else {
      arrowState[2] = 0;  
    }

    if(digitalRead(Right) == LOW                                ){            
      arrowState[3] = 1;    
    } else {
      arrowState[3] = 0;  
    } 
      
    // switch(key) {
    //   case '8': // Up
    //     arrowState[0] = 1;
    //     break;
    //   case '5': // Down
    //     arrowState[1] = 1;
    //     break;
    //   case '4': // Left
    //     arrowState[2] = 1;
    //     break;
    //   case '6': // Right
    //     arrowState[3] = 1;
    //     break;
    // }

    // Print the current state of the arrow keys
    if(arraysNotEqual(arrowState, arrowStateChange, 4)){
      Serial.print("Arrow State: ");
      for (int i = 0; i < 4; i++) {
        Serial.print(arrowState[i]);
        Serial.print(" ");
      }
    Serial.println();
    copyArray(arrowState, arrowStateChange, 4);      
    }
    // Clear arrowState
    // for (int i = 0; i < 4; i++) {
    //   arrowState[i] = 0;
    // }
  // }
}
