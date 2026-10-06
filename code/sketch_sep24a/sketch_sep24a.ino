#include <FspTimer.h>

class Logger {
  private:
    FspTimer& Timer1;
    static Logger* instance;

    int pin= A0;
    float dt= 10000.0f;
    unsigned long count= 0;
    int data= 0;

    bool logs= false;
    bool ready= false;

  public:
    Logger(FspTimer& t) : Timer1(t) {
      instance= this;
    }

    void innit() {
      uint8_t timerType= GPT_TIMER;
      int8_t timerIndex= FspTimer::get_available_timer(timerType);

      Timer1.begin(TIMER_MODE_PERIODIC, timerType,timerIndex,dt,0.0f,Timer1ISR_vec);
      Timer1.setup_overflow_irq();
      Timer1.open();
    }

    // interrupt function
    static void Timer1ISR_vec(timer_callback_args_t *args) {
      if (instance != nullptr) {
        instance->Timer1ISR();
      }
    }

    void Timer1ISR() {
      data= analogRead(pin);
      count++;
      ready= true;
    }
    // runtime log function
    void log() {
      if (logs) {
        if (ready) {
          ready= false;

          double volt= (data*5.0)/1023.0;
          double time= count/dt;

          noInterrupts();
          Serial.print(time);
          Serial.print(",");
          Serial.println(volt);
          interrupts();
        }
      }
    }

    // start function
    void start() {
      logs= true;
      Timer1.start();
    }

    // successful exit funtion
    static void exit_0_vec() {
      if (instance != nullptr) {
        instance->exit_0();
      }
    }
    void exit_0() {
      Timer1.stop();
      logs= false;
      Serial.println("EXIT_0");
    }

    // error exit function
    void exit_1() {
      Timer1.stop();
      Serial.println("EXIT_1");
      logs= false;
    }
};

class Stepper {
  private:
    FspTimer& Timer2;
    static Stepper* instance;

    float dt= 100.0f;
    int en_pin= 8;
    int step_pin= 9;
    int dir_pin= 10;
    int steps= 4;
    int count;

  public:
    Stepper(FspTimer& t) : Timer2(t) {
      instance= this;
    }

    void innit() {
      pinMode(en_pin,OUTPUT);
      pinMode(step_pin,OUTPUT);
      pinMode(dir_pin,OUTPUT);

      digitalWrite(en_pin,LOW);

      uint8_t timerType= GPT_TIMER;
      int8_t timerIndex= FspTimer::get_available_timer(timerType);

      Timer2.begin(TIMER_MODE_PERIODIC, timerType,timerIndex,dt,0.0f,Timer2ISR_vec);
      Timer2.setup_overflow_irq();
      Timer2.open();
    }

    static void Timer2ISR_vec(timer_callback_args_t  *args) {
      if (instance != nullptr) {
        instance->Timer2ISR();
      }
    }
    void Timer2ISR() {
      if (count < steps) {
        count++;
        if (digitalRead(step_pin) == HIGH) {
          digitalWrite(step_pin,LOW);
        }
        else {
          digitalWrite(step_pin,HIGH);
        }
      }
      else {
        Timer2.stop();
        Logger::exit_0_vec();
      }
    }

    void turn() {
      count= 0;
      Timer2.start();
    }
};

// --------------------------------------------------------

// variable and object innit
Logger* Logger::instance= nullptr;
FspTimer Timer1;
Logger logger(Timer1);

Stepper* Stepper::instance= nullptr;
FspTimer Timer2;
Stepper stepper(Timer2);

// ---------------------------------------------------------

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  logger.innit();
  stepper.innit();
}

void loop() {
  // put your main code here, to run repeatedly:
  logger.log();
  if (Serial.available() > 0) {
    char input= Serial.read();
    if (input == '0') {
      logger.start();
      stepper.turn();
    }
    else if (input == '1') {
      logger.exit_1();
    }
  }
}