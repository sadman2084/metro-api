/*
 * CC-0 by Sharafat Karim
 */

#include <WiFi.h>
#include <HTTPClient.h>

#define GREEN_LED 12  // Green LED pin
#define BLUE_LED 13   // Blue LED pin
#define RED_LED 14    // Red LED pin
#define buzzerPin 2

String WIFI_SSID = "সুশীল সমাজ";        // wifi - username
String WIFI_PASSWORD = "zxcvbnm6969";  // wifi - password
// String WIFI_SSID = "Sharafat";        // wifi - username
// String WIFI_PASSWORD = "88888888";  // wifi - password

String HOST_NAME = "https://metro-api-o34i.onrender.com";  // server address
String PATH_NAME = "/users/{id}";                          // server path
String rfidUID;
String balance;

void setup() {
  Serial.begin(9600);
  pinMode(GREEN_LED, OUTPUT);
  pinMode(BLUE_LED, OUTPUT);
  pinMode(RED_LED, OUTPUT);
  connectToWiFi();
}

void loop() {
  if (Serial.available()) {
    rfidUID = Serial.readStringUntil('#');
    rfidUID.trim();

    if (rfidUID[0] == '*') {
      Serial.print("Rfid -> ");
      Serial.println(rfidUID);
      rfidUID.replace("*", "");

      Serial.print("you total balance -> ");
      int num = getGetRequest(rfidUID);

      //////////////////////////
      if (num > 1000) {
        blinkLED(GREEN_LED, 3);
        Serial.println("Blinked green...");
      } else if (num > 500) {
        blinkLED(BLUE_LED, 3);
        Serial.println("Blinked blue...");
      } else {
        blinkLED(RED_LED, 3);
        Serial.println("Blinked red...");
      }
      //////////////////////////

    } else if (rfidUID[0] == '+') {

      Serial.print("Rfid -> ");
      Serial.println(rfidUID);

      int separatorIndex = rfidUID.indexOf(';');
      String val = rfidUID.substring(1, separatorIndex);
      rfidUID = rfidUID.substring(separatorIndex + 1, rfidUID.length());

      // Print the extracted values
      Serial.println("amount = " + val);
      Serial.println("rfidUID = " + rfidUID);

      Serial.print("current -> ");

      int num = getGetRequest(rfidUID);

      sendPUTRequestRecharge(rfidUID, val);

      Serial.print("updated -> ");
      num = getGetRequest(rfidUID);

      ////////////////////
      if (num > 100) {
        blinkLED(GREEN_LED, 3);
        Serial.println("Blinked green...");
      } else if (num > 50) {
        blinkLED(BLUE_LED, 3);
        Serial.println("Blinked blue...");
      } else {
        blinkLED(RED_LED, 3);
        Serial.println("Blinked red...");
      }
      ////////////////////
    }
  }
  delay(1000);
}

void connectToWiFi() {
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.println("Connecting");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  // Serial.print("Connected to WiFi network with IP Address: ");
  // Serial.println(WiFi.localIP());
  Serial.print("Connected!");
}

void dBReference() {
  int returnedValue = getGetRequest("sadman");
  Serial.print("you returned -> ");
  Serial.println(returnedValue);

  sendPUTRequestRecharge("sadman", "1");
}

int getGetRequest(String queryString) {
  HTTPClient http;

  http.begin(HOST_NAME + PATH_NAME + "?key=" + queryString);
  http.addHeader("Content-Type", "application/x-www-form-urlencoded");
  int httpCode = http.GET();

  // httpCode will be negative on error
  if (httpCode > 0) {
    // file found at server
    if (httpCode == HTTP_CODE_OK) {
      String payload = http.getString();
      Serial.println(payload);

      http.end();
      return payload.toInt();
    } else {
      // HTTP header has been send and Server response header has been handled
      Serial.printf("[HTTP] GET... code: %d\n", httpCode);
    }
  } else {
    Serial.printf("[HTTP] GET... failed, error: %s\n", http.errorToString(httpCode).c_str());
  }

  http.end();
  sleep(1);
  return (0);
}

void sendPUTRequestRecharge(String queryString, String balance) {
  HTTPClient http;

  http.begin(HOST_NAME + "/users/+/{id}?key=" + queryString + "&val=" + balance);
  http.addHeader("Content-Type", "application/x-www-form-urlencoded");

  int httpCode = http.PUT(queryString);

  // httpCode will be negative on error
  if (httpCode > 0) {
    // file found at server
    if (httpCode == HTTP_CODE_OK) {
      String payload = http.getString();
      Serial.println(payload);
    } else {
      // HTTP header has been send and Server response header has been handled
      Serial.printf("[HTTP] PUT... code: %d\n", httpCode);
    }
  } else {
    Serial.printf("[HTTP] PUT... failed, error: %s\n", http.errorToString(httpCode).c_str());
  }

  http.end();
}

void sendPUTRequestDischarge(String queryString, String balance) {
  HTTPClient http;

  http.begin(HOST_NAME + "/users/-/{id}?key=" + queryString + "&val=" + balance);
  http.addHeader("Content-Type", "application/x-www-form-urlencoded");

  int httpCode = http.PUT(queryString);

  // httpCode will be negative on error
  if (httpCode > 0) {
    // file found at server
    if (httpCode == HTTP_CODE_OK) {
      String payload = http.getString();
      Serial.println(payload);
    } else {
      // HTTP header has been send and Server response header has been handled
      Serial.printf("[HTTP] PUT... code: %d\n", httpCode);
    }
  } else {
    Serial.printf("[HTTP] PUT... failed, error: %s\n", http.errorToString(httpCode).c_str());
  }

  http.end();
}

void blinkLED(int pin, int times) {
  for (int i = 0; i < times; i++) {
    digitalWrite(pin, HIGH);
    tone(buzzerPin, 2000);
    delay(500);
    digitalWrite(pin, LOW);
    noTone(buzzerPin);
    delay(500);
  }
}
