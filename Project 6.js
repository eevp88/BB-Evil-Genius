var b = require('bonescript');var red = "P8_13";var yellow = "P8_15";var green = "P8_17";var inputPin = "P8_10";var switchstatus =0;b.pinMode(red, b.OUTPUT);b.pinMode(yellow, b.OUTPUT);b.pinMode(green, b.OUTPUT);b.pinMode(inputPin, b.INPUT);var on = b.HIGH;var off = b.LOW;setInterval(check,200);function check(){b.digitalRead(inputPin, checkButton);}function checkButton(x) {    if (x.value == 1){        switchstatus++;        switch (switchstatus){            case 1: setTimeout (function (){b.digitalWrite(red, on);            b.digitalWrite(yellow, off); b.digitalWrite(green, off);}, 500);                break;            case 2: setTimeout (function (){b.digitalWrite(yellow, on);}, 500);                break;            case 3: setTimeout (function (){b.digitalWrite(red, off);            b.digitalWrite(yellow, off); b.digitalWrite(green, on);}, 500);                break;            case 4: setTimeout (function (){b.digitalWrite(yellow, on);            b.digitalWrite(green, on);}, 500);                break;            default: switchstatus = 0;                break;        }    }    else if (switchstatus >=5){            switchstatus = 0;        }}