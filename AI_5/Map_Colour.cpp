
#include <bits/stdc++.h>
#define V 4
using namespace std;

void printSolution(int color[])
{
    cout << "Solution Exists:" " Following are the assigned colors \n";
    for (int i = 0; i < V; i++)
        cout << "  " << color[i];
    cout << "\n";
}

bool isSafe(bool graph[V][V], int color[])
{
    for (int i = 0; i < V; i++)             // check for every edge
        for (int j = i + 1; j < V; j++)
            if(graph[i][j] && color[j] == color[i])
                return false;
    return true;
}

bool graphColoring(bool graph[V][V], int m, int i, int color[V])
{
    if (i == V)                     // if current index reached end
    {
        if(isSafe(graph, color))    // if coloring is safe
        {
            printSolution(color);   // Print the solution
            return true;
        }
        return false;
    }
    for (int j = 1; j <= m; j++)    // Assign each color from 1 to m
    {
        color[i] = j;               // Recur of the rest vertices
        if (graphColoring(graph, m, i + 1, color)) 
            return true;
        color[i] = 0;
    }
    return false;
}
 
int main()
{
    bool graph[V][V] = {
        { 1, 1, 1, 0 },
        { 1, 0, 1, 1 },
        { 1, 1, 0, 0 },
        { 0, 1, 1, 1},
    };
    int m = 3; // Number of colors
    int color[V];
    for (int i = 0; i < V; i++)
        color[i] = 0;
    if (!graphColoring(graph, m, 0, color))
        cout << "Solution does not exist";
    return 0;
}