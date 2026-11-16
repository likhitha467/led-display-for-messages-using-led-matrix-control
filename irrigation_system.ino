
int moisturePin = A0;
int motorPin = 9;
int redLED = 7;
int greenLED = 8;

int moistureValue;

void setup()
{
    pinMode(motorPin, OUTPUT);
    pinMode(redLED, OUTPUT);
    pinMode(greenLED, OUTPUT);

    Serial.begin(9600);
}

void loop()
{
    moistureValue = analogRead(moisturePin);

    Serial.print("Moisture Value: ");
    Serial.println(moistureValue);

    if (moistureValue <= 400)
    {
        Serial.println("Soil Condition: DRY");

        digitalWrite(motorPin, HIGH);
        digitalWrite(redLED, HIGH);
        digitalWrite(greenLED, LOW);
    }

    else if (moistureValue <= 700)
    {
        Serial.println("Soil Condition: MEDIUM");

        digitalWrite(motorPin, LOW);
        digitalWrite(redLED, LOW);
        digitalWrite(greenLED, LOW);
    }

    else
    {
        Serial.println("Soil Condition: WET");

        digitalWrite(motorPin, LOW);
        digitalWrite(redLED, LOW);
        digitalWrite(greenLED, HIGH);
    }

    Serial.println("--------------------");

    delay(1000);
}
