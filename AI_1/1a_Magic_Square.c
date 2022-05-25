#include <stdio.h>

void magic_square(int n)
{
    int a[n][n], i, j, count = 1, total_elements = n*n;
    
    for(i=0;i<n;i++)
        for(j=0;j<n;j++)            // Initialize all elements to 0
            a[i][j] = 0;
    
    i = 0;
    j = n / 2;
    a[i][j] = count;                // Insert element in matrix at position (0,1)
    
    while(count < total_elements)
    {
        count++;
        if((i-1) < 0 && (j-1) < 0)  // If both values cross range of matrix
        {
            i++;
        }
        else if((i-1) < 0)      // If a row value crosses range of matrix
        {
            i = n - 1;
            j--;
        }
        else if((j-1) < 0)      // If a row value crosses range of matrix
        {    
            j = n - 1;            
            i--;  
        }
        else if(a[i-1][j-1] != 0)    // check non-empty diagonal and move to next row 
            i++;
        else
        {                           
            i--;
            j--;
        }
        a[i][j] = count;
        printf("\n");
        for(int l=0;l<n;l++) {
        for(int m=0;m<n;m++)
            printf("%3d", a[l][m]);
        printf("\n");
    }
    }
    
}

int main()
{
    int n;
    printf("\nEnter Single Odd-Dimension of matrix : ");
    scanf("%d", &n);
    magic_square(n);
    int sum = n * (n * n + 1) / 2;
    printf("\nSum of rows OR columns OR diagonal : %d", sum);
    return 0;
}