#include "sys.h"
/***********************************************
��˾����Ȥ�Ƽ�����ݸ�����޹�˾
Ʒ�ƣ�WHEELTEC
������wheeltec.net
�Ա����̣�shop114407458.taobao.com 
����ͨ: https://minibalance.aliexpress.com/store/4455017
�汾��V5.0
�޸�ʱ�䣺2021-11-05

Brand: WHEELTEC
Website: wheeltec.net
Taobao shop: shop114407458.taobao.com 
Aliexpress: https://minibalance.aliexpress.com/store/4455017
Version: V5.0
Update��2021-11-05

All rights reserved
***********************************************/
u8 Way_Angle=1;                             //��ȡ�Ƕȵ��㷨��1����Ԫ��  2��������  3�������˲� 
u8 Flag_Qian,Flag_Hou,Flag_Left,Flag_Right,Flag_Direction=0; //����ң����صı���
u8 Flag_Stop=1,Flag_Show=0;                 //ֹͣ��־λ�� ��ʾ��־λ Ĭ��ֹͣ ��ʾ��
int Encoder_A,Encoder_B,Encoder_C;             //���������������
int Encoder_A_EXTI;
int Motor_A,Motor_B,Motor_C;                   //���PWM����
int Target_A,Target_B,Target_C;                   //���Ŀ���ٶ�
int Temperature;                            //��ʾ�¶�
int Voltage;                                //��ص�ѹ������صı���
float Angle_Balance,Gyro_Balance,Gyro_Turn; //ƽ����� ƽ�������� ת��������
float Show_Data_Mb;                         //ȫ����ʾ������������ʾ��Ҫ�鿴������
u32 Distance;                               //���������
u8 delay_50,delay_flag;         //Ĭ������£����������Ϲ��ܣ������û�����2s���Ͽ��Խ������ģʽ
int Velocity=30;
u8 Usart3_Receive;
u8 rxbuf[8],Rxbuf[24];
u8 txbuf[8];
int AZ,GZ;
float Pitch,Roll,Yaw; 
u32 count,usart_count;
u8 CAN_ON_Flag;
int temp,temp2,temp3,count_temp,flag;
u8 ON_txbuf[8]={10,12,15,19,24,30,37,0} ;//У��������
u8 Velocity_txbuf[8]={11,13,16,20,25,31,38,50} ; 
u8 k;
int main(void)
{ 
	Stm32_Clock_Init(9);            //=====ϵͳʱ������
	delay_init(72);                 //=====��ʱ��ʼ��
  uart_init(72,9600);           //=====��ʼ������1
  uart2_init(36,9600);            //=====����2��ʼ��
	Timer1_Init(499,7199);
	CAN1_Mode_Init(1,2,3,6,0);  //CAN��ʼ��
	LED_Init();
  LED=1;
	while(1)
	{    	
		int i;
		
		//���͵�������ʮ���Ƶ�
		txbuf[0]=1;  //X���ٶ�
		txbuf[1]=0;  
		txbuf[2]=0;	 //Y���ٶ�
		txbuf[3]=0;		
		txbuf[4]=0;  //Z���ٶ�
		txbuf[5]=0;  
		txbuf[6]=0;  //Ԥ��λ
		txbuf[7]=0;	 //Ԥ��λ
	  CAN1_SEND(0X181,txbuf);//CAN����
		    
/***********CAN��������*********************************/
     
/***********���ڴ�ӡ��������*********************************/


//				printf("0xff\r\n");         //���ڷָ����鿴
//			  printf("%d\t",Rxbuf[0]); //֡ͷ(�̶�ֵ)
//				printf("%d\t",Rxbuf[1]); //���״̬		  
//				printf("%d\t",Rxbuf[2]); //С��x��ʵ���ٶ�	  
//				printf("%d\t",Rxbuf[3]); 
//				printf("%d\t",Rxbuf[4]); //С��y��ʵ���ٶ�
//				printf("%d\t",Rxbuf[5]); 
//				printf("%d\t",Rxbuf[6]); //С��z��ʵ���ٶ�
//				printf("%d\r\n",Rxbuf[7]); 
//			  printf("%d\t",Rxbuf[8]); //���ٶȼ�������ٶ�
//				printf("%d\t",Rxbuf[9]);			  
//				printf("%d\t",Rxbuf[10]);		  
//				printf("%d\t",Rxbuf[11]);
//				printf("%d\t",Rxbuf[12]);
//				printf("%d\t",Rxbuf[13]); 
//				printf("%d\t",Rxbuf[14]); //���ٶȼ�������ٶ�
//				printf("%d\r\n",Rxbuf[15]); 
//				printf("%d\t",Rxbuf[16]);
//				printf("%d\t",Rxbuf[17]);			  
//				printf("%d\t",Rxbuf[18]);		  
//				printf("%d\t",Rxbuf[19]);
//				printf("%d\t",Rxbuf[20]); //��ص�ѹ
//				printf("%d\t",Rxbuf[21]);
//				printf("%d\t",Rxbuf[22]);	//����У��λ���㣬ģʽ1�Ƿ�������У��	  
//				printf("%d\t",Rxbuf[23]);	//֡β���̶�ֵ��  
//			  printf("\r\noxfe\r\n");         //���ڷָ����鿴
				
				//���ͽ��յ���24λ����
				for(i=0; i<24; i++)
				{
					USART1->DR = Rxbuf[i];
				while((USART1->SR&0x40)==0);
				}	
 
		} 
}
