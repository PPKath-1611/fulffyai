#include <bits/stdc++.h>

using namespace std;

const char UP ='1';
const char DOWN= '2';
const char LEFT= '3';
const char RIGHT= '4';


void printArray(int array[3][3])
{
    for(int a=0;a<3;a++)
    {
        for(int b=0;b<3;b++)
        {
      		cout<< setw(8) << array[a][b];    
        }
        cout<<endl;
    }
    cout<<endl;
}

// Calculate Manhattan distance
int manhattan_distance(int start_state[3][3], int goal_state[3][3])
{
    int manhattan_distance=0;
    for(int i=0;i<3;i++)
        {
            for(int j=0;j<3;j++)
            {
                if(start_state[i][j] > 0)
                {
                    for(int k=0;k<3;k++)
                    {
                        for(int l=0;l<3;l++)
                        {
                            if (goal_state[k][l] == start_state[i][j])
                            {
                                manhattan_distance=manhattan_distance + (abs(i-k)+abs(j-l));                           
                            }
                        }
                    }
                }
            }
        }
return manhattan_distance;

}

void makeMove(int temp[3][3],int move)
{
    int flag=0;
    for(int i=0;i<3;i++)
    {
        for(int j=0;j<3;j++)
        {
            if(temp[i][j] == 0)
            {
         
            
                if(move==1)
                {
                    temp[i][j] = temp[i-1][j];
                	temp[i-1][j] = 0;
                    flag=1;
                    break;
                }
                else if(move==2)
                {     
                    temp[i][j] = temp[i+1][j];
                	temp[i+1][j] = 0;
                    flag=1;
                    break;
                }
                else if(move==3)

                {     
                    temp[i][j] = temp[i][j-1];
                	temp[i][j-1] = 0;
                    flag=1;
                    break;
                }
                else
                {
                	temp[i][j] = temp[i][j+1];
                	temp[i][j+1] = 0;
                    flag=1;
                    break;
                }  
            }
        }
        if(flag==1){break;}
    }
}
   
//----------------------------------------------------------------------------------------------------------- 
int tile_Ordering(int current_state[3][3],int goal_state[3][3],int move) 
{
    int temp[3][3];
    for(int i=0;i<3;i++)
    {
        for(int j=0;j<3;j++)
        {
        	temp[i][j] = current_state[i][j];
        }
    }
    makeMove(temp,move);
    printArray(temp);
    int manhattan=manhattan_distance(temp,goal_state);
    cout<<"Current Manhattan number :"<<manhattan<<endl<<endl<<endl;
    return manhattan; 
}

//----------------------------------------------------------------------------------------------------------
void Hill_Climbing( int start_state[3][3], int goal_state[3][3],int former_move)
{
	int arr[4] = {100,100,100,100};
    cout<<"--------------------------------------------------------------------------------"<<endl;
    for(int i=0;i<3;i++)
    {
        for(int j=0;j<3;j++)
        {
            if (start_state[i][j] == 0)
            {
                if(i>0 && former_move!=2)  
                {
                    cout << "Checking child (moving 0 up) " << endl;
                    arr[0] = tile_Ordering(start_state,goal_state,1); 
                }
                if(i<2 && former_move!=1) 
                {
                    cout<<"Checking child (moving 0 down) "<<endl;
                    arr[1]=tile_Ordering(start_state,goal_state,2);
                }
                if(j>0 && former_move!=4)
                {
                    cout<<"Checking child (moving 0 left) "<<endl;
                    arr[2]=tile_Ordering(start_state,goal_state,3);
                }
                if(j<2 && former_move!=3)
                {
                    cout<<"Checking child (moving 0 right) "<<endl;
                    arr[3]=tile_Ordering(start_state,goal_state,4);
                }
            }
        }
        cout<<endl;
    }
    int localOptimum = 99;
    int index=0;
    for(int i=0;i<4;i++)
    {
        if(arr[i] < localOptimum)   
        {
            localOptimum=arr[i];
            index=i+1;
        }
    }
    makeMove(start_state,index);
    cout<<"Next state = minimum Manhattan number :"<<endl;
    printArray(start_state);
    if(localOptimum==0)
    {  
        cout<<"goal state reached"<<endl;

        return;
    }
    Hill_Climbing(start_state,goal_state,index);
}

int main()
{
    int initial[3][3] = {{2, 8, 3}, {1, 6, 4}, {7, 0, 5}};
    int final[3][3]= {{1, 2, 3}, {8, 0, 4}, {7, 6, 5}};
    cout<<"\n---------------------------Your initial matrix is-------------------------------\n"<<endl;	
  

    for(int i=0;i<3;i++)
    {
        for(int j=0;j<3;j++)
        {
        	cout << setw(8) << initial[i][j];	     
        }
        cout<<endl;
    }
    
    cout<<"\n---------------------------Your final matrix is--------------------------------\n"<<endl;
    for(int i=0;i<3;i++)
    {
        for(int j=0;j<3;j++)
        {
        	cout << setw(8) << final[i][j];  
        }
        cout<<endl;
    } 
	cout<<"\n--------------------------------------------------------------------------------"<<endl;
	cout<<"\n--------------------------------------------------------------------------------"<<endl;
    cout<<"\nHill Climbing Algorithm\n"<<endl;
    Hill_Climbing(initial,final,0);
    return 0;
}