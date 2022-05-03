#ifndef __ADC_H
#define __ADC_H	
#include "sys.h"
#include "system.h"
#define Battery_Ch   5  //Battery voltage, ADC channel 5 //电池电压，ADC通道5
#define CAR_MODE_ADC 13 //Potentiometer, ADC channel 13 //电位器，ADC通道13
void Adc_Init(void);
u16 Get_Adc(u8 ch);
float Get_battery_volt(void) ;
u16 Get_adc_Average(u8 chn, u8 times);
extern float Voltage,Voltage_Count,Voltage_All; 	
#endif 


