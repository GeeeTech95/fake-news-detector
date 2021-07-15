const int inPin = A0;
const int VCC2 = 2;
const int iteration = 1000;
const float LM35_FACTOR = 0.01;

//settings for lcd
#include <LiquidCrystal_I2C.h>

const char lcd_address  = ""

//set lcd address by
LiquidCrystal_I2C lcd(lcd_address,16,2);


//adruino set up routine
void setup(){
//initialize serial comms at 9600 bits per sec

Serial.begin(9600);
Serial.println("EEE 506 Group 1");
pinMode(VCC2,OUTPUT);
digitalWrite(VCC2,HIGH);

//initialize lcd display
lcd.begin()
lcd.backlight();
lcd.print("EEE 506 Group 1");
lcd.setCursor(0,1);
lcd.print("Temp: ");

}


//repeatedly measure temperature
void loop(){
    lcdDisplay(getTemperature('C'),'C');
    delay(2000);

    lcdDisplay(getTemperature('F'),'F');
    delay(2000);

    lcdDisplay(getTemperature('K'),'K');
    delay(2000);

}



float getTemperature(char unitType){
    float value;
    float averageTemperature;
    float sumOfTemperature;
    int sensorValue = analogueRead(inPin);

    //compare sensor value to get actual voltage
    float sensorVoltage = sensorValue * (5.0 / 1023.0);
    float temperature = sensorVoltage / LM35_FACTOR;

    for (int i = 0;i < iteration;i++) {
        sumOfTemperature += temperature;
    }

    // getting the  av temp taken
    averageTemperature = sumOfTemperature / iteration;
    

    if(unitType == 'F'){
        value = (averageTemperature * 9) / 5 + 32;
    }
    else if(unitType == 'K'){
        value = averageTemperature +  273.15;
    }
    else{
        value = averageTemperature;
    }

 return value;
}

void printTemperature(char unitType)}{
    float value;
    float temperature = getTemperature(unitType);
    Serial.print(temperature);
    printDegree();
    Serial.print(string(unitType));
}

void printDegree(){
    serial.print("\xC2");
    serial.print("\xBO");
}


void lcdDisplay(float value,char symbol){

    for (int i=7;i < 16;i++){

        lcd.setCursor(i,1);
        lcd.write(254);      

    }

    lcd.setCursor(7,1)
    lcd.print(value);
    lcd.print((char)223);

    lcd.print(symbol)
}

