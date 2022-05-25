#include <stdbool.h>
#include <stdio.h>
#define N 4

bool isValid(int chess[N][N], int row, int col)
{
	int i, j;
	for (i = 0; i < col; i++)
		if (chess[row][i])
			return false;
	for (i = row, j = col; i >= 0 && j >= 0; i--, j--)
		if (chess[i][j])
			return false;
	for (i = row, j = col; j >= 0 && i < N; i++, j--)
		if (chess[i][j])
			return false;

	return true;
}

bool NQueens(int chess[N][N], int col)
{
	if (col >= N)
		return true;
	for (int i = 0; i < N; i++) {
		if (isValid(chess, i, col)) {
			chess[i][col] = 1;
		 printf("\n");
         for (int i = 0; i < N; i++) {
		    for (int j = 0; j < N; j++)
			    printf(" %3d ", chess[i][j]);
		    printf("\n");
	}
			if (NQueens(chess, col + 1))
				return true;

			chess[i][col] = 0; 
		}
	}
	return false;
}

bool NQ()
{
	int chess[N][N] = { { 0, 0, 0, 0 },
						{ 0, 0, 0, 0 },
						{ 0, 0, 0, 0 },
						{ 0, 0, 0, 0 } };
	if (NQueens(chess, 0) == false) {
		printf("Solution does not exist");
		return false;
	}

   
	return true;
}

int main()
{
    printf("\n\tNQueen's Problem Solution\n\n");
	NQ();
	return 0;
}