#include<stdio.h>
using namespace std;
int index1;

char board[9] = {' ',' ',' ',' ',' ',' ',' ',' ',' '};
// Single array represents the board '*' means empty box in board

10. int isFull()// Board is full
11. {
12. for(int i =0;i<9;i++)
13. {
14. if(board[i]!='X')
15. {
16. if(board[i]!='O')
17. {
18. return 0;
19. }
20. }
21. }
22. return 1;
23. }
24.
25. int user_won()//Checks whether user has won
26. {
27. for(int i=0;i<9;i+=3)
28. {
29.
if((board[i]==board[i+1])&&(board[i+1]==board[i+2])&&(board[i]
=='O'))
30. return 1;
31. }
32. for(int i=0;i<3;i++)
33. {
34.
if((board[i]==board[i+3])&&(board[i+3]==board[i+6])&&(board[i]
=='O'))
35. return 1;
36. }
37.
if((board[0]==board[4])&&(board[4]==board[8])&&(board[0]=='O')
)
38. {
39. return 1;
40. }

41.
if((board[2]==board[4])&&(board[4]==board[6])&&(board[2]=='O')
)
42. {
43. return 1;
44. }
45. return 0;
46. }
47.
48. int cpu_won()// Checks whether CPU has won
49. {
50. for(int i=0;i<9;i+=3)
51. {
52.
if((board[i]==board[i+1])&&(board[i+1]==board[i+2])&&(board[i]
=='X'))
53. return 1;
54. }
55. for(int i=0;i<3;i++)
56. {
57.
if((board[i]==board[i+3])&&(board[i+3]==board[i+6])&&(board[i]
=='X'))
58. return 1;
59. }
60.
if((board[0]==board[4])&&(board[4]==board[8])&&(board[0]=='X')
)
61. {
62. return 1;
63. }
64.
if((board[2]==board[4])&&(board[4]==board[6])&&(board[2]=='X')
)
65. {
66. return 1;
67. }
68. return 0;
69. }
70.
71. void draw_board() //display tic-tac-toe board
72. {

73. cout<<endl;
74. cout<<board[0]<<"|"<<board[1]<<"|"<<board[2]<<endl;
75. cout<<"-----"<<endl;
76. cout<<board[3]<<"|"<<board[4]<<"|"<<board[5]<<endl;
77. cout<<"-----"<<endl;
78. cout<<board[6]<<"|"<<board[7]<<"|"<<board[8]<<endl;
79. }
80.
81. int minimax(bool flag)// The minimax function
82. {
83.
84. int max_val=-1000,min_val=1000;
85. int i,j,value = 1;
86. if(cpu_won() == 1)
87. {return 10;}
88. else if(user_won() == 1)
89. {return -10;}
90. else if(isFull()== 1)
91. {return 0;}
92. int score[9] = {1,1,1,1,1,1,1,1,1};//if score[i]=1
then it is empty
93.
94. for(i=0;i<9;i++)
95. {
96. if(board[i] == '*')
97. {
98. if(min_val>max_val) // reverse of
pruning condition.....
99. {
100. if(flag == true)
101. {
102. board[i] = 'X';
103. value = minimax(false);
104. }
105. else
106. {
107. board[i] = 'O';
108. value = minimax(true);
109. }
110. board[i] = '*';
111. score[i] = value;
112. }

113. }
114. }
115.
116. if(flag == true)
117. {
118. max_val = -1000;
119. for(j=0;j<9;j++)
120. {
121. if(score[j] > max_val && score[j] !=
1)
122. {
123. max_val = score[j];
124. index1 = j;
125. }
126. }
127. return max_val;
128. }
129. if(flag == false)
130. {
131. min_val = 1000;
132. for(j=0;j<9;j++)
133. {
134. if(score[j] < min_val && score[j] !=
1)
135. {
136. min_val = score[j];
137. index1 = j;
138. }
139. }
140. return min_val;
141. }
142. }
143.
144. int main() //The main function
145. {
146. int move,choice;
147. cout<<"-------------------------TIC TAC TOE-----------
------------------------------------------";
148. cout<<endl<<"USER--->(O) CPU------>(X)";
149. cout<<endl<<"SELECT : 1-> Player first 2-> CPU
first:";
150. cin>>choice;

151. if(choice == 1)
152. {
153. draw_board();
154. up:cout<<endl<<"Enter the move:";
155. cin>>move;
156. if(board[move-1]=='*')
157. {
158. board[move-1] = 'O';
159. draw_board();
160. }
161. else
162. {
163. cout<<endl<<"Invalid Move......Try different
move";
164. goto up;
165. }
166. }
167.
168. while(true)
169. {
170.
171. cout<<endl<<"CPU MOVE....";
172. minimax(true);
173. board[index1] = 'X';
174. draw_board();
175. if(cpu_won()==1)
176. {
177. cout<<endl<<"CPU WON.....";
178. break;
179. }
180. if(isFull()==1)
181. {
182. cout<<endl<<"Draw....";
183. break;
184. }
185. again: cout<<endl<<"Enter the move:";
186. cin>>move;
187. if(board[move-1]=='*')
188. {
189. board[move-1] = 'O';
190. draw_board();
191. }

192. else
193. {
194. cout<<endl<<"Invalid Move......Try different
move";
195. goto again;
196. }
197. if(user_won()==1)
198. {
199. cout<<endl<<"You Won......";
200. break;
201. }
202. if(isFull() == 1)
203. {
204. cout<<endl<<"Draw....";
205. break;
206. }
207. }
208.
209. }