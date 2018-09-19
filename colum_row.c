#include<stdio.h>
int main()
{
  int a,b,c[1000][1000],i,j,k,l,m=0;
scanf("%d%d",&a,&b);
for(i=0;i<a;i++)
{
for(j=0;j<b;j++)
{
scanf("%d",&c[i][j]);
}
}
for(i=0;i<a;i++)
{
for(j=0;j<b;j++)
{
if(c[i][j]==0)
{ 
for(l=0;l<b;l++)
{
c[i][l]=0;
}
for(k=0;k<a;k++)
{ 
c[k][j]=0; 
m=1; 
}
}
if(m==1)
break;  
}
}
for(i=0;i<a;i++)
{
if(i!=0)
{
printf("\n");
}
for(j=0;j<b;j++)
{
if(j==0)
printf("%d",c[i][j]);
else
printf(" %d",c[i][j]);      
}
}
return 0;
}
