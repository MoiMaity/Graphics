#include<math.h>
#include<stdio.h>
#include<conio.h>
#include<graphics.h>

#define ROUND(a) ((int)(a+0.5))

void lineDDA(int xa, int xb, int ya, int yb)
{
	int dx,dy,steps,k;
	float xinc,yinc,x,y;
	dx=xb-xa;
	dy=yb-ya;
	x=xa;
	y=ya;
	
	if (abs(dx)>abs(dy))
		steps=abs(dx);
	else
		steps=abs(dy);
	xinc=dx/(float)steps;
	yinc=dy/(float)steps;
	
	setPixel(ROUND(x),ROUND(y));
	for(k=0;k<steps;k++)
	{
		x+=xinc;
		y+=yinc;
		setPixel(ROUND(x),ROUND(y));
	}
}
void main()
{
	int xa,xb,ya,yb;
	printf("Enter 1st endpoint :");
	scanf("%d%d",&xa,&ya);
	printf("\nEnter 2nd endpoint :");
	scanf("%d%d",&xb,&yb);
	printf("\nThe line :");
	lineDDA(xa,xb,ya,yb);
	getch();
}
	
	
