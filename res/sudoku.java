/*
* Creating the minimal encoding for the Sudoku solver
* The minimal encoding contains 8829 clauses
* The extended encoding will have 11,988 clauses
*/

/*
* To convert back from CNF form we would check all the values in which the value is greater than 0
* Because negative numbers in the miniSat solver means that they should be negative
*
*/

import java.util.*;


public class sudoku{

/*Naturally, the pre-assigned entries of the Sudoku grid will be represented as unit
* clauses. - Meaning they will all be printed on their own lines
* there are multiple ways that we can read in the input sudoku board
* we need to be able to parse each of them 
*/

// Parsing the contents of the given board
// and entering them as unit clauses
	public static void given_board(String s){
		// keep count of variables passed
		int count = 0;
		int i;
		int j;
		// k will be just whatever is at the index
		while(count < s.length()){

			count++;
		}
		count++;
	}


/*
* Checking to see that each cell has at least one number
*
*/
	public static void cell_atleast_one(){
		System.out.println("c every cell contains at least one number");
		// need to have the "p cnf <number of variables> <number of clauses>" here as well
		for(int i = 1; i <= 9; i++){
			for(int j = 1; j <=9; j++){
				for(int k = 1; k<=9; k++){
					System.out.print(i + "" + j + "" + k + " ");
				}
				System.out.println("0");
			}
		}		
	}


/*
* Checking to see every number appears at most once in every row
*
*/

	public static void row_most_once(){
		System.out.println("c every number appears at most once in every row");
		// need to have the "p cnf <number of variables> <number of clauses>" here as well
		for(int i = 1; i <=9; i++){
			for(int k = 1; k <=9; k++){
				for(int j = 1; j <= 8; j++){
					for(int l = j +1; l <= 9; l++){
						System.out.print("-" + i + j + k + " -" + i + l + k);
						System.out.println(" 0");	
					}
				}
			}
		}

	}


/*
* Checking to see every number appears at most once in every column
*/

	public static void col_most_once(){
		System.out.println("c every number appears at most once in every column");
		// need to have the "p cnf <number of variables> <number of clauses>" here as well
		for(int j = 1; j <=9; j++){
			for(int k = 1; k <=9; k++){
				for(int i = 1; i <= 8; i++){
					for(int l = i +1; l <= 9; l++){
						System.out.print("-" + i + j + k + " -" + l + j + k);
						System.out.println(" 0");
					}
				}
			}
		}
	}

/*
* Checking to see every number appears at most once in every 3x3 subgrid
*/	
	public static void three_square_most_once(){
		System.out.println("c each number apepars at most once in every 3x3 subgrid");
		// need to have the "p cnf <number of variables> <number of clauses>" here as well		
		// the first set of logical statements
		for(int k = 1; k <= 9; k++){
			for(int a = 0; a <= 2; a++){
				for(int b = 0; b <= 2; b++){
					for(int u = 1; u <=3; u++){
						for(int v = 1; v <= 2; v++){
							for(int w = v + 1; w <= 3; w++){
								System.out.print("-" + (3*a + u) + (3*b+v) + k + " -" +(3*a+u) + (3*b + w) + k);
								System.out.println(" 0");
							}
						}
					}
				}
			}
		}

		// the second set of logical statements
		for(int k = 1; k<=9; k++){
			for(int a = 0; a <= 2; a++){
				for(int b = 0; b <=2; b++){
					for(int u = 1; u <=2; u++){
						for(int v = 1; v <=3; v++){
							for(int w = u+1; w <=3; w++){
								for(int t = 1; t <= 3; t++){
									System.out.print("-" + (3*a + u) + (3*b + v) + k + " -" + (3*a + w) + (3*b+t) + k);
									System.out.println(" 0");
								}
							}
						}
					}
				}
			}
		}

	}

	public static void main(String [] args){
		
		/*
		* Printing out 8829 clauses for the minimal encoding
		* Hopefully they are all correct - followed the lecture slides
		* Additional 4 lines are for the comment for DIMACS FORMAT
		*/

		//cell_atleast_one();
		//row_most_once();
		//col_most_once();
		three_square_most_once();


	}
}