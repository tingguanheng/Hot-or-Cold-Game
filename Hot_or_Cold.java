import java.util.*;

public class Hot_or_Cold {
    int guess;
    int prev_guess = 0;
    int no_of_guesses = 0;
    
        
    public static void main(String[] args){
        System.out.println("Welcome to Hot or Cold!\nA random number has been generated!");
        boolean playing = true;
        Hot_or_Cold attempt = new Hot_or_Cold();
        int selected_number = (int)(Math.random()*101);

        while (playing == true){
            Scanner input = new Scanner(System.in);
            System.out.println("Take a guess! Please enter a number: ");
            int guess_input=0;
            try {
                guess_input = input.nextInt();
            }catch (Exception e){
                if (input.hasNextDouble()){
                    System.out.println("No decimals allowed!");
                    continue;
                }else if(input.hasNextLine()){
                    System.out.println("No characters allowed!");
                    continue;
                }
            }
            
            if (guess_input<0 || guess_input>100){
                System.out.println("Number must be from 0 to 100!");
                continue;
            } 
            else {
                attempt.no_of_guesses+=1;
                if (attempt.no_of_guesses >1){
                    attempt.prev_guess = attempt.guess;
                }
                attempt.guess = guess_input;
                System.out.println("You have entered "+attempt.guess+"!");

                if (attempt.guess == selected_number){
                    System.out.println("You've guessed correctly!");
                    if (attempt.no_of_guesses==1){
                        System.out.println("Wow! You got it right on your first try!");
                        input.close();
                        break;
                    }else {
                        System.out.println("You've guessed "+attempt.no_of_guesses+" times before getting it right!");
                    }
                    System.out.println("Please restart the game to try again.");
                    input.close();
                    break;
                }else{
                    System.out.println("Incorrect guess!");
                    if (attempt.no_of_guesses ==1){
                        if (Math.abs(selected_number-attempt.guess)<=10){
                            System.out.println("You are hot! Nearly there!");
                        }else{
                            System.out.println("You are cold!");
                        }
                    }else{
                        if (Math.abs(selected_number-attempt.guess)<=10){
                            System.out.println("You are hot! Nearly there!");
                        }else{
                            System.out.println("You are cold!");
                        }
                        if(Math.abs(selected_number-attempt.guess)>Math.abs(selected_number-attempt.prev_guess)){
                            System.out.println("You are further from the correct number than before!");
                        }else if(Math.abs(selected_number-attempt.guess)<Math.abs(selected_number-attempt.prev_guess)){
                            System.out.println("You are closer to the correct number than before!");
                        }else if(Math.abs(selected_number-attempt.guess)==Math.abs(selected_number-attempt.prev_guess)){
                            System.out.println("You are just as far from the correct number than before!");
                        }
                    }
                }
            }
            
        }
    }
}
