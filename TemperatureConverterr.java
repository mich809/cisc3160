
import java.util.Scanner;

//Michael Caridad
//Lab 1
//September 13th 2020
public class TemperatureConverterr {

	public static void main(String[] args) {			
		try (Scanner input = new Scanner(System.in)) {
			System.out.print("Type either 1 or 2 and press Enter: ");
			System.out.println("\n1.Farenheit to Celsius." 
							  +"\n2.Celsius to Farenheit.");			
			
			int choice = input.nextInt();
			
			System.out.println("Enter the 7 temperatures you would like to convert: ");
			float [] temperatures = new float[7];
			
			for (int i = 0; i < temperatures.length; i++) {
				temperatures[i] = input.nextFloat();				
			}
		    
			if(choice == 1)
				farenheitToCelsius(temperatures);
			else
				celsiusToFarenheit(temperatures);
		}				
		
	}
	
	static void farenheitToCelsius(float[]tempArray) {
		for (int i = 0; i < tempArray.length; i++) {
			 float celsius =(( 5 *(tempArray[i] - 32)) / 9);
			 System.out.println(tempArray[i] + " degree Farenheit is equal to "
					 			+ celsius +" degree celsius.");					
		}
	
	}
	
	static void celsiusToFarenheit(float[]tempArray) {
		for (int i = 0; i < tempArray.length; i++) {
			 float Farenheit = tempArray[i] * (9f / 5) + 32;	
			 System.out.println(tempArray[i] + " degree Celsius is equal to " + 
					 						 Farenheit +" degree Fahrenheit.");
			
		}
		
	}	
	
	

	}


